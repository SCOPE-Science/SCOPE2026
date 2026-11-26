# Independent mathematical audit

## correctness

PASS

Any sufficiently large positive common multiple of cycle lengths gives the same idempotent for a map; a positive power shares it. Thus no edge crosses its classes, and every class is connected via the idempotent. For a fixed idempotent e a map with eventual power e commutes with e, permutes its roots by σ, sends each fiber i into fiber σ(i), and has no nonroot cycle. Conversely those conditions send every point to a root, which must be the root of its original fiber at any sufficiently large multiple of the root permutation order. For a fixed σ, sum each row of the forest matrix over choices of its outgoing arrow x→y: use the row unit vector at x minus that at y for a nonroot target, and just the row unit vector at x for a root. An assignment with a nonroot cycle gives a row dependence, including a zero row for a loop; an acyclic assignment gives determinant one by ordering vertices by distance to roots. Factoring the resulting L=D−PQ reduces to I−QD⁻¹P, with the sole possible entry in row i at σ(i) equal to b_{σ(i)}/m_{σ²(i)}. Thus per cycle the reduced factor is 1−∏ b_i/m_i, including singleton cycles. Empty nonroot set gives one per permutation; the rank-one factor gives n^{n−2} at n≥2 and one at n=1. At n=5 the two rank-two contributions are 16+1 and 3+8, with 20 and 60 root/fiber assignments. The only unequal profiles at equal rank for n<5 are (3,1) and (2,2) at rank two for n=4; both give size 4. Independent replay /workspace/branches/review_replay_2.py checked through n=5 using first-repeat orbit phases, not the supplied common-exponent code; it confirms the first split and multiplicities, not the all-n theorem.

## originality

PASS

The qualitative indexing and some low- or high-rank cases are prior background. The supported distinct contribution is the explicit closed sum over root permutations with a cycle factor for every fiber profile, and the first rank-only obstruction. No exact equivalent or mechanically dominating formula was established in the inspected material.

## value

PASS

The size of each component is a natural missing invariant beyond knowing its idempotent. The formula replaces enumeration of n^n maps by a computation on the root-permutation and fiber data. The first 17-versus-11 split shows exactly where rank stops determining component order, and the formula explains the split without any assumption about internal graph isomorphism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
