"""Independent cross-checks for the n=24 target-triple computation.
1. Character orthonormality at n=24 for the exact partitions involved.
2. Tensor-dimension identity sum_nu g(A,B,nu)*dim(nu) = dim(A)*dim(B).
3. S3 permutation invariance of g.
4. Recompute g with cleared caches and reversed class order (independent traversal).
"""
import sys, math
from fractions import Fraction
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-638/output/artifacts")
import kronecker as K

A = (9,7,5,3); B = (8,7,5,4); C = (7,6,6,5)
n = 24
assert sum(A)==n and sum(B)==n and sum(C)==n

parts = list(K.partitions_of(n))
print("num classes:", len(parts))
assert len(parts) == 1575, len(parts)

# 1. orthonormality of the three irreps
for X, Y in [("A","A"),("B","B"),("C","C"),("A","B"),("A","C"),("B","C")]:
    XX = {"A":A,"B":B,"C":C}[X]; YY = {"A":A,"B":B,"C":C}[Y]
    s = sum(Fraction(K.chi(XX,mu)*K.chi(YY,mu), K.z_of(mu)) for mu in parts)
    print(f"<{X},{Y}> =", s)
    assert s == (1 if X==Y else 0), (X,Y,s)

# hook-length dimensions
def dim(lam):
    nn = sum(lam)
    h = 1
    for i,r in enumerate(lam):
        for j in range(r):
            leg = sum(1 for rr in lam[i+1:] if rr > j)
            arm = r - j - 1
            h *= (leg + arm + 1)
    return math.factorial(nn)//h
dA,dB,dC = dim(A),dim(B),dim(C)
print("dims:", dA, dB, dC)

# 2. full row: g(A,B,nu) for all nu of 24; check sum g*dim = dA*dB and g(A,B,C) value
tot = Fraction(0); gABC = None
for nu in parts:
    t,_ = K.kronecker_exact(A,B,nu)
    assert t.denominator == 1 and t >= 0, (nu,t)
    tot += t * dim(nu)
    if nu == C: gABC = t
print("sum g*dim =", tot, " dA*dB =", dA*dB)
assert tot == dA*dB
print("g(A,B,C) via full row =", gABC)
assert gABC == 134682

# 3. S3 permutations
import itertools
vals = set()
for X,Y,Z in itertools.permutations([A,B,C]):
    t,_ = K.kronecker_exact(X,Y,Z)
    vals.add(t); print(X,Y,Z,t)
assert vals == {134682}, vals

# 4. reversed traversal recompute
K._rim_cache.clear(); K._chi_cache.clear()
parts_rev = list(reversed(parts))
t = Fraction(0)
for mu in parts_rev:
    z = K.z_of(mu)
    a=K.chi(A,mu)
    if not a: continue
    b=K.chi(B,mu)
    if not b: continue
    c=K.chi(C,mu)
    if not c: continue
    t += Fraction(a*b*c, z)
print("reversed-order recompute:", t)
assert t == 134682
print("ALL CROSS-CHECKS OK")
