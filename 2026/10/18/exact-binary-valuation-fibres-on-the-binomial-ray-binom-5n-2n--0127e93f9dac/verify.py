"""Exact independent checks for binary carry distributions of binomial(5*n,2*n).

Requires Python 3 and SymPy. Run: python verify.py
"""
from itertools import product
import sympy as S

states = list(product((0, 1), repeat=3))
t, z = S.symbols('t z')
T = S.zeros(8)
w = []
for i, (a, c, d) in enumerate(states):
    for b in (0, 1):
        u = b + a + c
        h = (a + u % 2 + d) // 2
        j = states.index((b, u // 2, h))
        T[i,j] += t**h
    weight = S.Integer(1)
    for _ in range(4):
        u = a + c
        d = (a + (u % 2) + d) // 2
        c = u // 2
        a = 0
        weight *= t**d
    assert (a,c,d)==(0,0,0)
    w.append(weight)
assert w == [1,1,1,t,t,t,1,t**2]
Q = 1-z-z*z+z**3-z**4
F = ((S.eye(8)-z*T).inv()*S.Matrix(w))[0]
assert S.cancel(F.subs(t,0) - (1+z**3)/Q)==0
assert S.cancel(S.diff(F,t).subs(t,0) - z*(1-z*z)**2/Q**2)==0
# Direct digit-sum computation is independent of the transfer-matrix recurrence.
vec = [{0:1}] + [{} for _ in range(7)]
for L in range(16):
    hist = {}
    for i, poly in enumerate(vec):
        for value, count in poly.items():
            for exp in range(3):
                multiplicity = S.expand(w[i]).coeff(t,exp) if exp else S.expand(w[i]).subs(t,0)
                if multiplicity:
                    hist[value+exp] = hist.get(value+exp,0) + int(count*multiplicity)
    brute = {}
    for n in range(1<<L):
        value = n.bit_count() + (3*n).bit_count() - (5*n).bit_count()
        brute[value] = brute.get(value,0) + 1
    assert hist==brute,(L,hist,brute)
    next_vec = [{} for _ in range(8)]
    for i, (a,c,d) in enumerate(states):
        for b in (0,1):
            u=b+a+c
            h=(a+u%2+d)//2
            j=states.index((b,u//2,h))
            for val,count in vec[i].items():
                next_vec[j][val+h]=next_vec[j].get(val+h,0)+count
    vec=next_vec
print('VERIFY_OK: exact rational identities; all valuation fibres for 0<=L<=15')
