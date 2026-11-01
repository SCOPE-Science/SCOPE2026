"""Reproducible small-grid checks for the seven-point triangular-torus Turan theorem.

Run with Python 3; NumPy and SciPy are optional (used for extra LP checks).
The analytic proof, not finite enumeration, establishes every-order assertions.
"""
from math import cos, sin, pi, floor, isclose
from itertools import product


def predicted_minimum(n):
    q, r = divmod(n, 3)
    if r == 0:
        return -1.5, 2
    a = cos(2*pi*q/n)
    b = cos(2*pi*(q+1)/n)
    return ((2*a+b) if r == 1 else (a+2*b)), 6


def min_modes(n, tol=4e-12):
    freq = [cos(2*pi*j/n) for j in range(n)]
    values = [(freq[u]+freq[v]+freq[(u-v)%n],u,v)
              for u in range(n) for v in range(n)]
    minimum = min(x[0] for x in values)
    pts = [(u,v) for value,u,v in values if abs(value-minimum)<tol]
    return minimum, pts


def expected_modes(n):
    q, r = divmod(n,3)
    if r == 0:
        a = (q,2*q)
        return {a,(-a[0]%n,-a[1]%n)}
    if r == 1:
        positive = {(q,2*q),(q,2*q+1),(q+1,2*q+1)}
    else:
        positive = {(q,2*q+1),(q+1,2*q+1),(q+1,2*q+2)}
    return positive | {(-u%n,-v%n) for u,v in positive}


def complex_fourier(a,b,n,u,v):
    phases = (u, v, (u-v)%n)
    # For f(positive vector)=a_j + i b_j, and f(negative)=conjugate.
    return 1 + 2*sum(aa*cos(2*pi*k/n)+bb*sin(2*pi*k/n)
                     for aa,bb,k in zip(a,b,phases))


number_grid_tests = 0
number_fourier_tests = 0
number_dual_tests = 0
for n in range(5,91):
    v, modes = min_modes(n)
    expected, multiplicity = predicted_minimum(n)
    assert isclose(v,expected,abs_tol=6e-13)
    assert len(modes)==multiplicity
    assert set(modes)==expected_modes(n), (n,modes,expected_modes(n))
    q,r=divmod(n,3)
    if r:
        assert v>-1.5
    else:
        assert isclose(v,-1.5,abs_tol=1e-14)
    # The predicted invariant optimizer has nonnegative Fourier values,
    # with zeros precisely at the predicted modes.
    a_star=-1/(2*v)
    for u in range(n):
        for w in range(n):
            F=complex_fourier((a_star,)*3,(0.,)*3,n,u,w)
            assert F>-6e-12, (n,u,w,F)
            if (u,w) in set(modes):
                assert abs(F)<1e-11
            else:
                assert F>0
            number_fourier_tests+=1
    number_grid_tests+=1

# Direct separate linear algebra on active Fourier modes.
try:
    import numpy as np
    from scipy.optimize import linprog
    for n in range(5,22):
        freq=[]
        for u,w in product(range(n),repeat=2):
            angles=(2*pi*u/n, 2*pi*w/n, 2*pi*(u-w)/n)
            cosrow=[2*cos(t) for t in angles]
            sinrow=[2*sin(t) for t in angles]
            freq.append(cosrow+sinrow)
        # f(v_j)=a_j+i b_j. Max mass = 1+2 sum a_j
        r=linprog([-2,-2,-2,0,0,0],A_ub=-np.array(freq),
                 b_ub=np.ones(n*n),bounds=[(None,None)]*6,method='highs')
        assert r.success,(n,r.message)
        S,_=predicted_minimum(n)
        assert abs((1-r.fun)-(1-3/S))<1e-7,(n,r.fun,S)
        aopt=np.array(r.x[:3]); bopt=np.array(r.x[3:])
        if n%3:
            # Unique optimizer, even without averaging/symmetrization.
            assert np.linalg.norm(aopt-np.array([-1/(2*S)]*3),np.inf)<1e-7
            assert np.linalg.norm(bopt,np.inf)<1e-7
        else:
            assert abs(sum(aopt)-1)<1e-7
            assert abs(bopt[0]-bopt[1]-bopt[2])<1e-7
        number_dual_tests+=1
except ImportError:
    print('OPTIONAL scipy or numpy unavailable: LP cross-check omitted')

# Asymptotics cross-check for both nonzero residue classes.
from math import sqrt
for n in (1000,1001,1003,1004):
    if n%3==0: continue
    s,_=predicted_minimum(n)
    T=1-3/s
    sign=1 if n%3==1 else -1
    approx=3+8*pi*pi/(9*n*n)+sign*16*sqrt(3)*pi**3/(81*n**3)
    assert abs(T-approx)<4e-11

print('CHECK_PASS', 'orders=5..90', 'grid_modes=',number_grid_tests,
      'Fourier_inequalities=',number_fourier_tests,'LP_instances=',number_dual_tests)
