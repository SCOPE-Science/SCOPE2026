"""Exact and numerical checks for positivity of classical RK4 on bidirected-star Markov generators."""
from fractions import Fraction as F
from math import factorial
from itertools import product
import sympy as sp


def generator(a,b):
    n=len(a); Q=sp.zeros(n+1)
    B=sum(b)
    Q[0,0]=-B
    for i,(ai,bi) in enumerate(zip(a,b),1):
        Q[0,i]=bi; Q[i,0]=ai; Q[i,i]=-ai
    return Q


def step(Q,h):
    return sum(((h**k/sp.factorial(k))*Q**k for k in range(5)),sp.zeros(Q.rows))


def factors(a,b):
    B=sum(b); S=sum(x*y for x,y in zip(a,b)); S2=sum(x*x*y for x,y in zip(a,b))
    As=[];Cs=[];Ds=[]
    for aj in a:
        As.append(B+aj)
        Cs.append(B*B+B*aj+aj*aj+S)
        Ds.append(B**3+B*B*aj+B*aj*aj+aj**3+(2*B+aj)*S+S2)
    return B,S,S2,As,Cs,Ds

# Exhaustively sample a finite parameter box and exact step sizes; verify identities and signs.
checks=0
for n in (2,3,4):
    params=(list(product((1,2,3),repeat=2*n)) if n==2 else
            [tuple(1+(j*i+2*i*i)%5 for i in range(2*n)) for j in range(1,25)])
    for v in params:
        a=list(map(sp.Integer,v[:n])); b=list(map(sp.Integer,v[n:])); Q=generator(a,b)
        B,S,S2,A,C,D=factors(a,b)
        assert Q*sp.ones(n+1,1)==sp.zeros(n+1,1)
        for h in (sp.Rational(1,7),sp.Rational(1,2),sp.Rational(5,4)):
            P=step(Q,h)
            assert P*sp.ones(n+1,1)==sp.ones(n+1,1)
            for j in range(n):
                g=1-A[j]*h/2+C[j]*h*h/6-D[j]*h**3/24
                assert P[0,j+1] == h*b[j]*g
                assert P[j+1,0] == h*a[j]*g
                assert 9*A[j]*D[j]>4*C[j]**2
                for i in range(n):
                    if i==j: continue
                    T=B+a[i]+a[j]
                    U=B*B+B*(a[i]+a[j])+a[i]**2+a[j]**2+a[i]*a[j]+S
                    value=a[i]*b[j]*h*h*(sp.Rational(1,2)-T*h/6+U*h*h/24)
                    assert P[i+1,j+1]==value
                    assert 3*U>T*T
                    assert P[i+1,j+1]>0
            assert all(P[i,i]>0 for i in range(n+1))
            checks+=1
Q=sp.Matrix([[-3,2,1],[1,-1,0],[3,0,-3]])
P=step(Q,sp.Rational(1,2))
assert Q.eigenvals()=={sp.Integer(0):1,sp.Integer(-2):1,sp.Integer(-5):1}
assert P==sp.Matrix([[sp.Rational(17,24),sp.Rational(29,96),-sp.Rational(1,96)],
                    [sp.Rational(29,192),sp.Rational(295,384),sp.Rational(31,384)],
                    [-sp.Rational(1,32),sp.Rational(31,64),sp.Rational(35,64)]])
assert 0<sp.Rational(3,8)<1 and 0<sp.Rational(83,128)<1
print(f'PASS {checks} exact parameter-step tests and exact stable-but-negative three-state example')
