"""Exact checks for an endpoint-atom perturbation of a metric-star spline projector.

Run with Python 3.10+ and SymPy >= 1.12. This checks symbolic identities
for all formal parameters and independently tests rational Gram inversions.
The accompanying mathematical proof specifies the quantifiers and sharpness.
"""
from fractions import Fraction as F
import sympy as sp


def check_symbolic():
    m,w=sp.symbols('m w',positive=True)
    q=w/(m+(3*m+1)*w)
    # Sherman--Morrison inverse rows at the center and each type of leaf.
    J=lambda a,b: sp.factor((a*a+b*b)/(2*(a+b)))
    a=2*(1-q)/m
    b_atom=(1-(3*m+1)*q)/m
    b_ordinary=3+(1-q)/m
    b_other=(1-q)/m
    L=sp.factor(J(a,b_atom)+J(a,b_ordinary)+(m-2)*J(a,b_other)+q)
    C=sp.factor(J(4*(1-q)/m,2*(1-(3*m+1)*q)/m)
                 +(m-1)*J(4*(1-q)/m,2*(1-q)/m)+2*q)
    T=1+(sp.Rational(7,3)-4/(3*(m+1))-1)*m/(m+(3*m+1)*w)
    den=3*(m+(3*m+1)*w)*(1+2*w)*(m+1+(3*m+4)*w)
    num=(7*m*m+3*m+(56*m*m+38*m+3)*w
         +(147*m*m+137*m+26)*w*w+(126*m*m+150*m+48)*w**3)
    assert sp.factor(L-num/den)==0
    assert sp.factor(C-(5*m+(25*m+5)*w+(30*m+18)*w*w)/
                     (3*(1+2*w)*(m+(3*m+1)*w)))==0
    assert sp.factor(T-(7*m*m+3*m+(9*m*m+12*m+3)*w)/
                     (3*(m+1)*(m+(3*m+1)*w)))==0
    A=(m*m-m+(8*m*m-6*m-1)*w+(21*m*m-13*m-6)*w*w
       +(18*m*m-12*m-12)*w**3)
    B=(3*m**3+4*m*m+2*m+(15*m**3+24*m*m+13*m+2)*w
       +(18*m**3+33*m*m+21*m+6)*w*w)
    assert sp.factor((L-C)-2*A/den)==0
    assert sp.factor((L-T)-4*w*B/((m+1)*den))==0
    E=(m*m+(2*m**3+14*m*m+4*m)*w
       +(17*m**3+76*m*m+37*m+2)*w*w
       +(48*m**3+184*m*m+118*m+12)*w**3
       +(45*m**3+165*m*m+128*m+20)*w**4)
    derivative=4*E/(3*(1+2*w)**2*(m+(3*m+1)*w)**2
                    *(m+1+(3*m+4)*w)**2)
    assert sp.factor(sp.diff(L,w)-derivative)==0
    k=sp.symbols('k',nonnegative=True)
    # Exact coefficient nonnegativity is certified by displaying every
    # coefficient after m=k+2 and checking against their explicit forms.
    assert sp.expand(A.subs(m,k+2)-(k*k+3*k+2
               +(8*k*k+26*k+19)*w+(21*k*k+71*k+52)*w*w
               +(18*k*k+60*k+36)*w**3))==0
    # B and E have strictly positive coefficient lists in m,w.
    assert all(c>0 for c in sp.Poly(B,m,w).coeffs())
    assert all(c>0 for c in sp.Poly(E,m,w).coeffs())
    L0=(7*m+3)/(3*(m+1))
    Linf=(21*m*m+25*m+8)/((3*m+1)*(3*m+4))
    assert sp.factor(L.subs(w,0)-L0)==0
    assert sp.factor(sp.limit(L,w,sp.oo)-Linf)==0
    assert sp.factor(sp.limit(L,m,sp.oo)-sp.Rational(7,3))==0
    print('EXACT_SYMBOLIC_NORM_DOMINANCE_DERIVATIVE_LIMIT_IDENTITIES_OK')


def inverse(A):
    n=len(A)
    V=[[F(x) for x in row]+[F(int(i==j)) for j in range(n)]
       for i,row in enumerate(A)]
    for i in range(n):
        k=next(j for j in range(i,n) if V[j][i])
        V[i],V[k]=V[k],V[i]
        s=V[i][i];V[i]=[x/s for x in V[i]]
        for k in range(n):
            if k!=i:
                c=V[k][i];V[k]=[x-c*y for x,y in zip(V[k],V[i])]
    return [row[n:] for row in V]


def integral_abs_line(v0,v1):
    if v0*v1>=0: return (abs(v0)+abs(v1))/2
    return (v0*v0+v1*v1)/(2*(abs(v0)+abs(v1)))


def check_rational():
    for m in range(2,11):
        for w in [F(0),F(1,100),F(1,3),F(1),F(7,2),F(10),F(100)]:
            mass=[[F(0) for _ in range(m+1)] for _ in range(m+1)]
            mass[0][0]=F(m,3)
            for j in range(1,m+1):
                mass[0][j]=mass[j][0]=F(1,6)
                mass[j][j]=F(1,3)
            mass[1][1]+=w
            I=inverse(mass)
            L=[]
            for i in range(m+1):
                v=sum(integral_abs_line(I[i][0],I[i][j]) for j in range(1,m+1))+w*abs(I[i][1])
                L.append(v)
                assert sum((I[i][0]+I[i][j])/2 for j in range(1,m+1))+w*I[i][1]==1
            num=(7*m*m+3*m+(56*m*m+38*m+3)*w
                 +(147*m*m+137*m+26)*w*w+(126*m*m+150*m+48)*w**3)
            den=3*(m+(3*m+1)*w)*(1+2*w)*(m+1+(3*m+4)*w)
            formula=num/den
            assert L[2]==formula,(m,w,L,formula)
            assert max(L)==formula
            assert all(v<formula for v in [L[0],L[1]] if w>0)
            assert all(v==formula for v in L[2:])
    print('INDEPENDENT_RATIONAL_GRAM_AND_KERNEL_INTEGRALS_OK',9*7,'CASES')
    print('ALL_LEAF_ATOM_SPLINE_CHECKS_PASSED')

if __name__=='__main__':
    check_symbolic()
    check_rational()
