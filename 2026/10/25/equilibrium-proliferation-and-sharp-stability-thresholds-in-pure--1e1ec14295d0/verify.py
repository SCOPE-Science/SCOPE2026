"""Reproduce algebraic and numerical checks for pure-triad SIS on friendship graphs.

Requires Python 3.10+ and SymPy.  All finite tests supplement the proof.
"""
from fractions import Fraction as Q
from math import comb
import sympy as sp


def symbolic_checks():
    k, lam, y = sp.symbols('k lam y', positive=True)
    h = 1 / (lam * (1-y))
    eq = k * lam * y**2 * (lam * (1-y) - 1) - 1
    J = sp.Matrix([
        [-1-k*lam*y**2, 2*k*lam*(1-h)*y],
        [lam*y*(1-y), -y/(1-y)],
    ])
    # The determinant reduces to k*lam**2*y**3-2 exactly on eq=0.
    assert sp.simplify((J.det() - (k*lam**2*y**3-2)) / eq - (y-2)/(1-y)) == 0
    assert sp.simplify(J.trace() + 1+k*lam*y**2+y/(1-y)) == 0
    # The nonzero branches cross zero determinant at the cubic maximum.
    assert sp.simplify((k*lam**2*y**3-2).subs(k,1/(lam*y**2*(lam*(1-y)-1)))
                      - (3*lam*y-2*(lam-1))/(lam*(1-y)-1)) == 0
    assert sp.simplify(sp.diff(y*y*(lam*(1-y)-1),y) - y * (2*(lam-1)-3*lam*y)) == 0
    assert sp.simplify(sp.diff((lam-1)**3/lam,lam) - (lam-1)**2*(2*lam+1)/lam**2)==0
    return 5


def threshold(k):
    lo, hi = 1.0, 2.0
    while 4*k*(hi-1)**3 < 27*hi:
        hi *= 2
    for _ in range(100):
        mid = (lo+hi)/2
        if 4*k*(mid-1)**3 < 27*mid:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def branches(k, lam):
    t=threshold(k)
    if lam < t-1e-10: return []
    peak = 2*(lam-1)/(3*lam)
    if abs(lam-t)<1e-10: return [peak]
    max_y = 1-1/lam
    def f(y): return k*lam*y*y*(lam*(1-y)-1)-1
    if f(peak) <= 0:
        raise AssertionError('expected two roots')
    results=[]
    for a,b in ((0.0,peak),(peak,max_y)):
        fa=f(a)
        for _ in range(100):
            c=(a+b)/2
            if f(c)*fa<=0:
                b=c
            else:
                a=c;fa=f(c)
        results.append((a+b)/2)
    return results


def evaluate(m, lam, active, y):
    h=1/(lam*(1-y))
    xs=[h]
    for j in range(m):
        xs.extend([y,y] if j<active else [0.0,0.0])
    deriv=[-h + lam*(1-h)*sum(xs[1+2*j]*xs[2+2*j] for j in range(m))]
    for j in range(m):
        u,v=xs[1+2*j:3+2*j]
        deriv.extend([-u+lam*(1-u)*h*v, -v+lam*(1-v)*h*u])
    assert all(-1e-12<=x<=1+1e-12 for x in xs)
    assert max(map(abs, deriv)) < 2e-11
    return h


def numeric_checks():
    cases=0;nonzero=0
    for m in range(1,9):
        for lam in (1.5,2.0,2.75,3.1,3.5,3.8,4.0,4.1,5.0,8.0,12.0):
            count=1
            for k in range(1,m+1):
                bs=branches(k,lam)
                count+=comb(m,k)*len(bs)
                for idx,y in enumerate(bs):
                    h=evaluate(m,lam,k,y)
                    nonzero+=1
                    peak=2*(lam-1)/(3*lam)
                    det=k*lam*lam*y**3-2
                    tr=-1-k*lam*y*y-y/(1-y)
                    assert tr < 0
                    assert (abs(det)<1e-8 if len(bs)==1 else (det<0 if idx==0 else det>0))
                    if k<m:
                        assert lam*h-1>0
                    else:
                        assert (abs(det)<1e-8 if len(bs)==1 else (y<peak if idx==0 else y>peak))
            independently=1+sum(comb(m,k)*(0 if lam<threshold(k)-1e-10 else
                            1 if abs(lam-threshold(k))<=1e-10 else 2)
                               for k in range(1,m+1))
            assert count==independently
            if lam>4:
                assert count==2**(m+1)-1
            if lam==4:
                assert count==2**(m+1)-m-1
            cases+=1
    return cases, nonzero


def exact_checks():
    # A lower full-activity endemic equilibrium at m=2, lambda=4.
    lam=Q(4);m=2;k=2;y=Q(1,4);h=1/(lam*(1-y))
    assert (h,y)==(Q(1,3),Q(1,4))
    assert -h+lam*(1-h)*k*y*y==0
    assert -y+lam*(1-y)*h*y==0
    assert k*lam*lam*y**3-2 < 0
    # At m=1, lambda=4 the two positive branches coalesce.
    m=k=1;y=Q(1,2);h=Q(1,2)
    assert -h+lam*(1-h)*k*y*y==0
    assert -y+lam*(1-y)*h*y==0
    assert k*lam*lam*y**3-2==0
    # Differential identity ensures equal coordinates in each live petal.
    for h in (Q(0),Q(1,3),Q(7,9)):
        for u in (Q(0),Q(1,5),Q(1)):
            for v in (Q(0),Q(2,7),Q(1)):
                du=-u+lam*(1-u)*h*v
                dv=-v+lam*(1-v)*h*u
                assert du-dv == -(1+lam*h)*(u-v)
    return 34


if __name__=='__main__':
    a=symbolic_checks()
    b,n=numeric_checks()
    c=exact_checks()
    print(f'PASS: {a} symbolic identities, {b} parameter cases, '
          f'{n} evaluated nonzero endemic configurations, '
          f'{c} exact-rational cases/identities.')
