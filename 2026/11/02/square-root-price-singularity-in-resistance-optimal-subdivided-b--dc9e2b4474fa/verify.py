"""Independent numerical/symbolic tests for a two-price graph-subdivision resistance theorem.

Requires numpy, scipy and sympy. Run: python verify.py
"""
import math
import random
import numpy as np
import sympy as sp
from scipy.optimize import brentq


def coefficients(p, q):
    assert p >= 2 and q >= 2
    n = p + q + p*q
    a = (p-1)/q + (q-1)*(p+1)/p + (p+1)/n
    b = (p-1)*(q+1)/q + (q-1)/p + (q+1)/n
    c = (p-1)*(q-1)
    return a, b, c


def full_trace(p, q, x, y):
    n = p+q+p*q
    lap = np.zeros((n,n), dtype=float)
    for i in range(p):
        for j in range(q):
            z = p+q+i*q+j
            for v,cond in [(i,x),(p+j,y)]:
                lap[v,v] += cond
                lap[z,z] += cond
                lap[v,z] -= cond
                lap[z,v] -= cond
    spectrum=np.linalg.eigvalsh(lap)
    assert abs(spectrum[0]) < 1e-10 and spectrum[1]>1e-9
    return sum(1/z for z in spectrum[1:])


def optimum_ratio(p,q,P,Q):
    a,b,c=coefficients(p,q)
    # y/x=t, x=B/(p*q*(P+Q*t)); all constrained optima interior
    def deriv(t):
        return Q*a-P*b/t**2+c*(Q-P)/(1+t)**2
    return brentq(deriv,1e-7,1e7,xtol=1e-13,rtol=1e-13)


def tests():
    checks=0
    for p,q in [(2,2),(2,3),(3,4),(4,4),(3,6),(7,7)]:
        for x,y in [(1.,1.),(1.31,.73),(.53,2.4)]:
            a,b,c=coefficients(p,q)
            got=full_trace(p,q,x,y)
            expected=a/x+b/y+c/(x+y)
            assert math.isclose(got,expected,rel_tol=5e-12,abs_tol=5e-12),(p,q,got,expected)
            checks+=1
    p,q,x,y=sp.symbols('p q x y',positive=True)
    N=p+q+p*q
    A=(p-1)/q+(q-1)*(p+1)/p+(p+1)/N
    BB=(p-1)*(q+1)/q+(q-1)/p+(q+1)/N
    C=(p-1)*(q-1)
    assert sp.simplify((p-1)*((q+1)/(q*y)+1/(q*x))+(q-1)*((p+1)/(p*x)+1/(p*y))+(q+1)/(N*y)+(p+1)/(N*x)+C/(x+y)-A/x-BB/y-C/(x+y))==0
    checks+=1
    t=sp.symbols('t',positive=True)
    phi=(1-t)*(1+t)**3/t**2
    assert sp.factor(sp.diff(phi,t))==-2*(t+1)**2*(t*t-t+1)/t**3
    checks+=1
    for p,q in [(2,2),(2,7),(3,3),(3,8),(6,9),(10,10)]:
        for P,Q in [(1,1),(1,2),(3,1),(1.7,1.2),(.2,4)]:
            tstar=optimum_ratio(p,q,P,Q)
            a,b,c=coefficients(p,q)
            f=lambda t:(P+Q*t)*(a+b/t+c/(1+t))
            assert f(tstar) < min(f(tstar*.995),f(tstar*1.005))
            assert tstar>0
            checks+=1
    for m in [100,400,1600,6400]:
        tstar=optimum_ratio(m,m,1,2)
        assert abs(tstar*math.sqrt(m)-1)<5/math.sqrt(m)
        checks+=1
        tstar=optimum_ratio(m,m,2,1)
        assert abs(math.sqrt(m)/tstar-1)<5/math.sqrt(m)
        checks+=1
    for delta in [-4,-1,0,1,4]:
        t_inf=brentq(lambda t:phi_numeric(t)-delta,1e-5,1e5)
        t_m=optimum_ratio(2500,2500,1,1+delta/2500)
        assert abs(t_m-t_inf)<.02,(delta,t_m,t_inf)
        checks+=1
    print('ALL_OK:',checks,'test groups; complete Laplacian checks, root minimizers, symbolic derivatives and asymptotics')

def phi_numeric(t):
    return (1-t)*(1+t)**3/t**2

if __name__=='__main__':
    tests()
