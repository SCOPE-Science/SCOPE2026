# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/09/014`  
**Audited source tree:** `e289605779fc4f3409af189df4a586c460a83bad`  
**Date:** 2026-09-26 UTC  
**Disposition:** PASSED, rank-one scope

## Correctness

PASS within the explicitly defined rank-one Bloch projectors. Independently enumerated all 64 deterministic assignments for the stated Collins–Gisin coefficients: local maximum 0, achieved by 20 assignments. Werner singles are 1/2, coincidence (1−v ai·bj)/4 and coefficient sum 4, so I=−1+vS/4. The listed planar angles give S=5. For any three unit Alice vectors, optimizing Bob gives |a1+a2+a3|+|a1+a2−a3|+|a1−a2|; with t=|a1+a2| this is at most 2√(1+t²)+√(4−t²)≤5, the final squared difference being (t²−3)²≥0. Equality is attained at t=√3. Thus v*=4/5 and the claimed gap above 1/√2 holds. The scope excludes degenerate projectors 0,I; Collins–Gisin show these can embed CHSH, so the word 'projective' alone must be read with the record's rank-one definition.

## Originality

PASS, but the source comparison requires correction. Collins and Gisin's open original paper supplies the same singlet settings and numerical pure-state I3322 maximum 0.25 (its Eq. 19 and nearby text), and states a Werner violation only for p>3/4 on p. 5. For their own white-noise mixture the random-state value is −1, making the 0.25 endpoint imply 4/5 under rank-one measurements; their 3/4 sentence is inconsistent with that arithmetic. The present exact global vector upper bound, rather than the known settings or numerical optimum, resolves the rank-one visibility precisely. Pal–Vértesi's higher-dimensional optimum addresses a different domain. No claim is made that the full projective/POVM Werner threshold is 4/5.

## Scientific value

PASS, scoped. An exact global optimization and clean separation from CHSH for nondegenerate qubit projectors clarifies a canonical Bell-test slice and a contradictory threshold statement in the original paper. It is useful as a small analytic benchmark, while degenerate local projectors and unrestricted measurements fall outside this theorem.

## Prior work

- https://arxiv.org/pdf/quant-ph/0306129
- https://arxiv.org/pdf/1006.3032

## Scope

The conclusion is for three rank-one qubit projectors per side. The original Collins–Gisin paper's p>3/4 sentence conflicts with its own p=0 and p=1 values under this scope; this audit derives the exact upper bound directly.
