"""Exact finite tests for a finite-interval resetting theorem; not an infinite proof."""
from fractions import Fraction as F
from sympy import Symbol, Poly, expand, Rational, Matrix

x=Symbol('x')

def poly(m,odd):
    if m==0: return Poly(1,x,domain='ZZ')
    p0=Poly(1,x,domain='ZZ')
    p1=Poly(2*x-1 if odd else x,x,domain='ZZ')
    for _ in range(1,m):
        p0,p1=p1,Poly(2*x*p1.as_expr()-p0.as_expr(),x,domain='ZZ')
    return p1

def setup(N,i):
    odd=N%2
    A=poly(N//2,odd)
    B=poly(abs(N-2*i)//2,odd)
    return A,B

def rational_reset(N,i,q):
    # Reset before normal walk with probability 1-q, including from the starting site.
    size=N-1
    P=Matrix(size,size,lambda r,c:0)
    for j in range(size):
        for k in range(size):
            P[j,k]=(1-q if k==i-1 else 0)
            if abs(j-k)==1: P[j,k]+=q*F(1,2)
    ones=Matrix([1]*size)
    return (Matrix.eye(size)-P).inv().multiply(ones)[i-1]

count=0
for N in range(2,61):
    for i in range(1,N):
        A,B=setup(N,i)
        expr=Poly(expand((x*A.as_expr()-x*B.as_expr()-i*(N-i)*(x-1)*B.as_expr())/(x-1)),x) if False else None
        # Work in t=x-1, so this polynomial's zero constant and the remaining coefficients encode benefit.
        t=Symbol('t')
        aa=Poly(A.as_expr().subs(x,t+1),t)
        bb=Poly(B.as_expr().subs(x,t+1),t)
        hh=Poly((t+1)*(aa-bb).exquo(Poly(t,t)).as_expr()-i*(N-i)*bb.as_expr(),t)
        c=hh.all_coeffs()[::-1]
        assert c[0]==0,(N,i,c)
        crit=(N*N-F(5)*(N-2*i)**2+20) # four times threshold N²/4-5(N/2-i)²+5
        if crit>=0:
            assert all(v>=0 for v in c),(N,i,'negative Taylor coefficient')
        else:
            assert c[1]<0,(N,i,'wrong linear sign')
        for q in (F(1,2),F(2,3),F(4,5)) if N<=10 else ():
            y=F(1,q)
            expected=Rational(y)* (A.eval(y)-B.eval(y))/((Rational(y)-1)*B.eval(y))
            actual=rational_reset(N,i,q)
            assert expected==actual,(N,i,q,expected,actual)
            count+=1
        count+=1
print('PASS:',count,'exact Chebyshev/finite-Markov checks; N=2..60')
