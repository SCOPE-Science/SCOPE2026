"""Independent polynomial-coefficient census for two ternary conics over F_3.

Conics are generated from six coefficients; geometric nonsingularity is
verified by the determinant of the full polar Hessian in odd characteristic.
No 4-arc parametrization or symmetry reduction is used.
"""
from itertools import product, combinations
from collections import Counter
import json
q = 3
# Disjoint projective charts; each rational point occurs exactly once.
points = [(1,y,z) for y in range(q) for z in range(q)] + [
    (0,1,z) for z in range(q)] + [(0,0,1)]
assert len(points) == 13
line_equations = [(1,a,b) for a in range(q) for b in range(q)] + [
    (0,1,b) for b in range(q)] + [(0,0,1)]
assert len(line_equations) == 13
line_sets = [frozenset(i for i,p in enumerate(points)
            if sum(a*b for a,b in zip(L,p))%q==0) for L in line_equations]
assert len(set(line_sets)) == 13 and all(len(s)==4 for s in line_sets)

conics = []
for coeff in product(range(q),repeat=6):
    if not any(coeff):
        continue
    # One representative of each scalar-equivalence class.
    if next(a for a in coeff if a) != 1:
        continue
    a,b,c,d,e,f = coeff
    H = ((2*a,d,e),(d,2*b,f),(e,f,2*c))
    determinant = (H[0][0]*(H[1][1]*H[2][2]-H[1][2]*H[2][1])
      -H[0][1]*(H[1][0]*H[2][2]-H[1][2]*H[2][0])
      +H[0][2]*(H[1][0]*H[2][1]-H[1][1]*H[2][0]))%q
    if determinant == 0:
        continue
    zeros = frozenset(i for i,(x,y,z) in enumerate(points) if
      (a*x*x+b*y*y+c*z*z+d*x*y+e*x*z+f*y*z)%q == 0)
    assert len(zeros) == 4
    conics.append((coeff, zeros))
assert len(conics) == 234
assert len({points for _,points in conics}) == 234

C = Counter()
U = Counter()
for (f,A),(g,B) in combinations(conics,2):
    union = A|B
    if not all(union & L for L in line_sets):
        continue
    intrinsic = not any(L <= union for L in line_sets)
    C[(len(union),len(A&B),intrinsic)] += 1
    if intrinsic:
        U[union] += 1
assert C == {
 (6,2,True):702,
 (7,1,True):936,
 (7,1,False):5616,
 (8,0,False):4212,
}, C
S6 = {u for u in U if len(u)==6}
S7 = {u for u in U if len(u)==7}
assert len(S6)==len(S7)==234
assert {frozenset(range(13))-s for s in S6} == S7
assert {U[s] for s in S6} == {3}
assert {U[s] for s in S7} == {4}
assert all(all(any((s-{j}).isdisjoint(L) for L in line_sets) for j in s) for s in S6)
print(json.dumps({
 "method":"polynomial Hessian determinant and incidence",
 "smooth_conics":len(conics),
 "blocking_pair_counts":{"6_2_nontrivial":702,"7_1_nontrivial":936,
 "7_1_trivial":5616,"8_0_trivial":4212},
 "blocking_pairs":sum(C.values()),
 "nontrivial_pairs":sum(v for (m,k,n),v in C.items() if n),
 "six_unions":len(S6),"seven_unions":len(S7),
 "six_decompositions":3,"seven_decompositions":4,
 "seven_unions_are_complements":True,
},sort_keys=True,indent=2))
