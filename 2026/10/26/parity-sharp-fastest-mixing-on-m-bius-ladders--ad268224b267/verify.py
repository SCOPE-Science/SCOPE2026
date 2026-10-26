"""Reproduce spectral and linear-programming checks for the Möbius-ladder result.

Run: python verify.py; requires NumPy and SciPy. Symbolic inequalities and
all-integer range arguments are provided in RESULT.md; finite checks below
are corroboration, not a substitute for those proofs.
"""
import math
import numpy as np
from scipy.optimize import linprog


def proposed(n):
    assert n >= 3
    u = 1 - math.cos(math.pi / n)
    v = 1 - math.cos(2 * math.pi / n)
    if n % 2 == 0:
        d = 2 + 2 * v - 2 * u
        a = 1 / d
        b = (v - u) / d
        t = (2 - 2 * u) / d
        jneg = n - 1
        w = 2 - u
    else:
        d = 2 + 2 * v - u
        a = 1 / d
        b = (v - u) / d
        t = (2 - u) / d
        jneg = n
        w = 2
    return a, b, t, u, v, jneg, w


def spectrum(n, a, b):
    return [1 - 2 * a * (1 - math.cos(math.pi * j / n)) - b * (1 - (-1)**j)
            for j in range(2*n)]


def matrix(n, a, b):
    n2 = 2*n
    p = np.zeros((n2, n2))
    for i in range(n2):
        p[i, i] = 1 - 2*a - b
        for j in ((i-1) % n2, (i+1) % n2):
            p[i, j] = a
        p[i, (i+n) % n2] = b
    return p


for n in range(3, 101):
    a,b,t,u,v,jneg,w = proposed(n)
    assert a>0 and b>0 and 2*a+b <= 1 + 1e-12
    vals = spectrum(n,a,b)
    assert abs(max(abs(x) for x in vals[1:]) - t) < 2e-12, n
    assert abs(vals[1]-t)<2e-12
    assert abs(vals[2]-t)<2e-12
    assert abs(vals[jneg]+t)<2e-12
    assert abs((2*v/(2+2*v-u) if n % 2 else v/(1+v-u)) - (1-t)) <2e-12
    dual = (w-u)/(2*v+w-u)
    assert abs(dual - t) < 2e-12
    # Verify claimed active dual lower bound for 1000 deterministic feasible weights.
    for k in range(10):
        at = (k + .25) / 12 / 2
        bt = ((11-k) / 12) * (1 - 2*at)
        sp = spectrum(n,at,bt)
        assert max(abs(x) for x in sp[1:]) >= dual - 1e-11
    if n <= 32:
        p=matrix(n,a,b)
        assert np.max(abs(p.sum(axis=1) - 1))<1e-12
        assert np.min(p)>=-1e-12
        ev = np.linalg.eigvalsh(p)
        assert np.max(abs(np.sort(ev) - np.sort(vals)))<3e-12
        # Independent LP over the actual mode list.
        inequalities=[];upper=[]
        for j in range(1,2*n):
            sj=1-math.cos(math.pi*j/n)
            Bj=1-(-1)**j
            inequalities.extend([[-2*sj,-Bj,-1],[2*sj,Bj,-1]])
            upper.extend([-1,1])
        inequalities.append([2,1,0]);upper.append(1)
        sol=linprog([0,0,1], A_ub=inequalities,b_ub=upper,
            bounds=[(0,None)]*3,method='highs')
        assert sol.success
        assert max(abs(sol.x[i] - [a,b,t][i]) for i in range(3))<2e-6, (n,sol.x,(a,b,t))

# Exact base cases (avoid floating-only spot check):
# n=3: u=1/2, v=3/2, (a,b,t)=(2/9,2/9,1/3).
assert all(abs(x-y)<1e-14 for x,y in zip(proposed(3)[:3], (2/9,2/9,1/3)))
# n=4: u=1-sqrt(2)/2, v=1, (a,b,t)=((2-sqrt(2))/2, (sqrt(2)-1)/2, sqrt(2)-1).
# Here a=1/(sqrt(2)+1)=sqrt(2)-1? Check explicitly against machine formula.
a,b,t,*_=proposed(4)
assert abs(a-(1-1/math.sqrt(2)))<1e-14
assert abs(b-(1/math.sqrt(2)-1/2))<1e-14
assert abs(t-(math.sqrt(2)-1))<1e-14

# Heuristic: for odd n uniform P with a=b=1/3 has -1 mode;
# even n its SLEM is 1-2u/3 (a near-antipodal odd mode).
for n in range(3,81):
    u=1-math.cos(math.pi/n)
    slem=max(abs(x) for x in spectrum(n,1/3,1/3)[1:])
    heuristic=1 if n%2 else 1-2*u/3
    assert abs(slem-heuristic)<2e-12, (n,slem,heuristic)
    if n%2:
        assert abs(spectrum(n,1/3,1/3)[n]+1)<1e-12

# The asymptotic even-order improvement factor tends to six.
for n in (100,1000,10000):
    _,_,_,u,v,_,_=proposed(n)
    ratio=3*v/(2*u*(1+v-u))
    assert 3 < ratio < 6.000001
assert abs(3*(1-math.cos(2*math.pi/10000))/(2*(1-math.cos(math.pi/10000))*(1+(1-math.cos(2*math.pi/10000))-(1-math.cos(math.pi/10000)))) - 6)<2e-6
print('VERIFY_OK: 98 sizes, 30 full matrix spectra and LP optima, 980 dual stress tests, 78 heuristic parity checks, exact n=3/n=4 and asymptotic ratio 6')
