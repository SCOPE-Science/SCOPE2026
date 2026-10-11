"""Reproduce symbolic certificates and finite checks for a three-node Fourier Riesz problem.

Requires Python 3, SymPy, and NumPy. Execute: python checker.py
The finite tests corroborate, but do not substitute for, the all-order proof.
"""
from itertools import combinations
from math import cos, pi, sqrt
import sympy as sp

v = sp.symbols('v', real=True)
r = sp.sqrt(3)

def trig_multiple(k):
    z = ((1 + sp.I*v)/(1-sp.I*v))**k
    re, im = sp.expand_complex(z).as_real_imag()
    return sp.factor(re), sp.factor(im)

c1, s1 = trig_multiple(1)
c2, s2 = trig_multiple(2)
c4, s4 = trig_multiple(4)

# N = 3q + 1: qx = 2pi/3-2u, (q+1)x = 2pi/3+4u.
a1 = 1-c1+r*s1
b1 = 1-c2-r*s2
factor1 = 2*v*(v+r)*(v-(2-r))*(v+2+r)/(1+v*v)**2
assert sp.simplify(a1+b1-factor1)==0

# N = 3q + 2: qx = 2pi/3-4u, (q+1)x=2pi/3+2u.
a2 = 1-c2+r*s2
b2 = 1-c1-r*s1
factor2 = 2*v*(v-r)*(v-2-r)*(v+2-r)/(1+v*v)**2
assert sp.simplify(a2+b2-factor2)==0

# Unbalanced (q,q,q+2) triples have the third off-diagonal -t.
t = -1+c4+r*s4
P = v**8-8*v**6-56*r*v**5-22*v**4+80*r*v**3+112*v**2+8*r*v-3
cert = -4*v**2*(v-r)**2*P/(1+v*v)**6
assert sp.simplify(a2*(t-a2)-b2*b2-cert)==0

# Each of these small cases has only two possible spacing types.
for N in range(3,71):
    z = lambda j: 1 + 2*cos(2*pi*j/N)
    B = sorted(set([0, N//3, (2*N)//3]))
    if len(B)<3: continue
    import numpy as np
    def cond(trip):
        G = np.array([[3 if i==j else z((trip[i]-trip[j])%N)
                       for j in range(3)] for i in range(3)])
        w = np.linalg.eigvalsh(G)
        return float(w[-1]/w[0])
    val = cond(B)
    allvals = [(cond(trip),trip) for trip in combinations(range(N),3)]
    best = min(x for x,_ in allvals)
    assert abs(val-best)<1.e-9, (N,val,best)
    balanced = [trip for x,trip in allvals if abs(x-best)<1.e-8]
    expected = N//3 if N%3==0 else N
    assert len(balanced)==expected,(N,len(balanced),expected)
    q=N//3
    assert all(max((t2-t1)%N for t1,t2 in zip(trip,trip[1:]+(trip[0],)))-
               min((t2-t1)%N for t1,t2 in zip(trip,trip[1:]+(trip[0],)))<=1
               for trip in balanced)

# Exact small-case inequalities and eigenvalue identities.
s5 = sp.sqrt(5)
assert sp.simplify((5/( (5-s5)/2 )) - ((5+s5)/2))==0
assert 13 < float((5 / ((3-s5)/2))) < 14
assert float((7+sp.sqrt(25-16*sp.sqrt(2)))/4) < 3
print('CHECK_PASS exact_symbolic_identites=3 cyclic_orders=3..70',flush=True)
