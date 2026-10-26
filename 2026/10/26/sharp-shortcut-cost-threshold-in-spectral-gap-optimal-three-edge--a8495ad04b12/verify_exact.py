#!/usr/bin/env python3
"""Exact rational checks of spectral factors and optimized rates."""
from fractions import Fraction
import sympy as sp


def case(m,s):
    # s is a rational square root of the shortcut-cost coefficient.
    tau=s*s;tc=sp.Rational(m*m,(m-1)**2)
    if tau<=tc:
        C=2*m+m*s+(1-m)*tau/2
        x=1/C; y=s*x/2; z=x*(1+m*(1/s-1))/2
    else:
        C=2*m+sp.Rational(m*m,2*(m-1))
        x=1/C; y=x*sp.Rational(m,2*(m-1)); z=sp.Rational(0)
    N=2+2*m;L=sp.zeros(N)
    E=[(0,1,z)]
    for i in range(m):
        a=2+2*i;b=a+1
        E.extend([(0,a,x),(a,b,y),(b,1,x)])
    for u,v,w in E:
        L[u,u]+=w;L[v,v]+=w;L[u,v]-=w;L[v,u]-=w
    t=sp.symbols('t')
    pol=sp.factor(L.charpoly(t).as_expr())
    A=sp.Matrix([[m*x+2*z,-sp.sqrt(m)*x],[-sp.sqrt(m)*x,x+2*y]])
    small=sp.factor((A[0,0]-x)*(A[1,1]-x)-A[0,1]*A[1,0])
    assert small==0,(m,s,small)
    expected=sp.factor(t*(t-(m+1)*x)*(t-x)**(m-1)*(t-(x+2*y))**(m-1)*sp.factor((t-A[0,0])*(t-A[1,1])-m*x*x))
    assert sp.expand(pol-expected)==0,(m,s)
    assert sp.simplify(sum(w*(tau if i==0 else 1) for i,(_,_,w) in enumerate(E))-1)==0
    assert sp.simplify(sp.det(A-x*sp.eye(2)))==0
    return (m,str(s),str(C),str(x),str(z))

if __name__=='__main__':
    ss=[sp.Rational(1,2),sp.Rational(1),sp.Rational(3,2),sp.Rational(2),sp.Rational(3)]
    count=0
    for m in range(2,7):
        for s in ss+[sp.Rational(m,m-1)]:
            print(*case(m,s));count+=1
    print('EXACT_POLYNOMIALS_PASS',count)
