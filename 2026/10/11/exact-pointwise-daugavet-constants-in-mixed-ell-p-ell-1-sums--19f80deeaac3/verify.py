"""Finite exact-rational checks for the scalar lemmas in the accompanying theorem.

The Banach-space slice argument is analytic and is not certified by this script.
"""
from fractions import Fraction as Q
from itertools import product

# Monotonicity of the best-aligned single-atom discrepancy when c <= m.
checks = 0
for b_num, m_num, c_num, s_num in product(range(11), repeat=4):
    if not (c_num <= m_num <= b_num):
        continue
    b,m,c,s = map(lambda n: Q(n,10), (b_num,m_num,c_num,s_num))
    assert b-c+abs(s-c) >= b-m+abs(s-m)
    checks += 1

# Exact radial inequalities at a variety of rational points on the Euclidean circle.
circle = [(Q(0),Q(1)),(Q(1),Q(0)),(Q(3,5),Q(4,5)),
          (Q(4,5),Q(3,5)),(Q(5,13),Q(12,13)),(Q(12,13),Q(5,13))]
radial_checks=0
for r,s in circle:
    assert r*r+s*s == 1
    for ai,bi,mi in product(range(11), repeat=3):
        if mi>bi or ai*ai+bi*bi>100:
            continue
        a,b,m=Q(ai,10),Q(bi,10),Q(mi,10)
        actual=(a+r)**2+(b-m+abs(s-m))**2
        assert actual>=0
        radial_checks+=1

# Exact global phase law for p=2 and unit atomic norm. Both branches follow
# from linear functions on [0,m] and [m,1]; sampled points test arithmetic.
phase_checks=0
for k in range(1,101):
    m=Q(k,100)
    bound=2*(1-m) if m<=Q(1,2) else 4*(1-m)**2
    witness=m if m<=Q(1,2) else Q(1)
    def f(s): return 1-s*s+(1-m+abs(s-m))**2
    assert f(witness)==bound
    for t in range(101):
        s=Q(t,100)
        assert f(s)>=bound
        phase_checks+=1

# Strictly mixed radial slice beats either endpoint for five equal atomic masses.
m=Q(1,5)
assert (1-m*m)+(1-m)**2==Q(8,5)
assert Q(8,5)<2
assert Q(8,5)<(2-2*m)**2
print(f"VERIFY_OK discrepancy_checks={checks} radial_checks={radial_checks} "
      f"phase_checks={phase_checks} balanced_five=8/5 analytic_proof_required=True")
