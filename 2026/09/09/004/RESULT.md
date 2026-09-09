# Refutation of the involution equidistribution conjecture for Class-69 length-2 mesh patterns

## Context

Length-2 mesh patterns are nearly classified: Fang–Fu–Kitaev–Li–Su–Sun
(arXiv:2606.14367, June 2026) prove the number of distribution-equivalence
classes satisfies 105 ≤ dist ≤ 106 and Wilf-classes 46 ≤ wilf ≤ 47, with both
gaps hinging on a single 2019-conjectured 4-way equidistribution (Class 69 in
Remark 1.3 / Su–Kitaev–Zhang Table 5). That paper further conjectures
(Conjecture 1, concluding remarks) that this 4-way equidistribution also holds
when restricted to involutions. The first two and last two patterns are
trivially equivalent by reverse-complementation; the 4-way claim is new.

## Definitions

A mesh pattern is a pair p = (π, R) with π ∈ S_m and
R ⊆ [0,m] × [0,m] (Brandén–Claesson). Dots are drawn at (i, π_i); the unit
square with bottom-left corner in R is shaded. Values a < b at positions
i1 < i2 in σ ∈ S_n form an occurrence of p when π = 12 and no other point of
σ lies in any shaded position-zone × value-band rectangle, with zones
x = 0 (left of i1), 1 (between), 2 (right of i2) and bands y = 0 (below a),
1 (between a, b), 2 (above b).

Class 69 (all with π = 12, dots (1,1),(2,2)):

- A = {(1,2),(1,1),(2,1),(0,0)}
- B = {(2,2),(0,1),(1,1),(1,0)}
- C = {(0,2),(1,1),(2,1),(1,0)}
- D = {(1,2),(0,1),(1,1),(2,0)}

Let s_{n,k}(p) count σ ∈ S_n with exactly k occurrences of p, and
s^{inv}_{n,k}(p) the same restricted to involutions (σ = σ^{-1}).

## Result

**Theorem.** The four Class-69 patterns are not equidistributed on
involutions. They split into exactly two involution-distribution classes
{A, B} and {C, D} at every 3 ≤ n ≤ 9 checked; in particular at n = 3:

- s^{inv}_{3,k}(A) = s^{inv}_{3,k}(B): {k=0: 2, k=1: 1, k=2: 1};
- s^{inv}_{3,k}(C) = s^{inv}_{3,k}(D): {k=0: 1, k=1: 2, k=2: 1}.

Hence Conjecture 1 of Fang et al. (involution equidistribution of all four
Class-69 patterns) is false, with minimal counterexample at n = 3. The
proposed involution analogue should be replaced by the two-class refinement
{A,B} vs {C,D}.

## Proof / evidence

*Proof of the refutation (hand-checkable).* The four involutions of length 3
give, by direct inspection of the shaded regions:

| σ   | A | B | C | D |
|-----|---|---|---|---|
| 123 | 1 | 1 | 2 | 2 |
| 132 | 0 | 2 | 1 | 1 |
| 213 | 2 | 0 | 1 | 1 |
| 321 | 0 | 0 | 0 | 0 |

Example: σ = 132, pattern A. Candidate (a,b) = (1,3) (positions 1,2) is killed
by (pos 3, val 2) in shaded cell (2,1); candidate (1,2) (positions 1,3) is
killed by (pos 2, val 3) in shaded cell (1,2): count 0. For pattern C,
(1,2) survives since (pos 2, val 3) sits in band y = 2 of the middle zone
while C shades only (1,1),(1,0) there: count 1. Avoidance counts differ (2
involutions avoid A/B, only 1 avoids C/D), so the 4-way involution
equidistribution fails. The machine re-verifies every entry with two
independent counters. ∎

*Computed evidence (not claimed as proof).* Exhaustive enumeration over all
of S_n for n = 7, 8, 9 shows all four patterns with identical occurrence
distributions — consistent with but not proving the open full-group 2019
conjecture:

- n = 7 (5040): {0: 1956, 1: 1690, 2: 887, 3: 365, 4: 120, 5: 21, 6: 1}
- n = 8 (40320): {0: 16482, 1: 13453, 2: 6689, 3: 2595, 4: 855, 5: 217, 6: 28, 7: 1}
- n = 9 (362880): {0: 155739, 1: 120534, 2: 56782, 3: 20987, 4: 6624, 5: 1813, 6: 364, 7: 36, 8: 1}

Involution census (232/764/2620 objects at n = 7/8/9) confirms the split
persists, e.g. avoidance at n = 9: 1407 (A/B) vs 735 (C/D):

- n = 7: A/B {0: 116, 1: 38, 2: 45, 3: 17, 4: 12, 5: 3, 6: 1}, C/D {0: 58, 1: 64, 2: 49, 3: 35, 4: 19, 5: 6, 6: 1}
- n = 8: A/B {0: 390, 1: 127, 2: 137, 3: 57, 4: 33, 5: 15, 6: 4, 7: 1}, C/D {0: 203, 1: 212, 2: 156, 3: 100, 4: 59, 5: 26, 6: 7, 7: 1}
- n = 9: A/B {0: 1407, 1: 396, 2: 482, 3: 155, 4: 116, 5: 39, 6: 20, 7: 4, 8: 1}, C/D {0: 735, 1: 738, 2: 516, 3: 316, 4: 181, 5: 91, 6: 34, 7: 8, 8: 1}

## Limitations

- The refutation is a complete finite proof (n = 3, hand-checkable).
- Full-group 4-way agreement to n = 9 is computed evidence only and does not
  decide the unrestricted 2019 conjecture; the 106-vs-105 / 47-vs-46
  full-group classification is unaffected.
- Mesh semantics follow the Brandén–Claesson / paper-macro convention
  (dots at (i,π_i), shading by bottom-left corner); alternative conventions
  could shift counts.

## Reproducibility

`output/artifacts/enumerate.py` (stdlib + numpy) regenerates every table and
writes `output/artifacts/tables/dist_S{7,8,9}.json`,
`dist_inv{7,8,9}.json`, and `LOG.txt`. Two independent counters (position-pair
loops with per-cell scans; value-pair loops with numpy segment tests; plus a
joint 4-pattern single-pass classifier for the S_9 run) agree on 1500 random
permutations at each of n = 7, 8, 9 and on all involutions with n ≤ 7; the
n = 9 avoidance column was replayed with the reference counter. The auditor
independently re-enumerated S_7 and all n = 7 involutions from scratch with
matching results.

## References

- Q. Fang, S. Fu, S. Kitaev, H. Li, X. Su, Z. Sun, On mesh patterns of short
  length: Equidistribution and enumeration, arXiv:2606.14367 (2026). Class 69
  (Remark 1.3); involution Conjecture 1 (concluding remarks).
- X. Su, S. Kitaev, J. Zhang, Equidistribution of mesh patterns of short
  length, arXiv:2605.19429 (2026). Prior bounds and classification tables.
- P. Brändén, A. Claesson, Mesh patterns and the expansion of (coloured)
  permutation statistics as functions of permutation patterns, Electron. J.
  Combin. 18(2) (2011). Mesh-occurrence definition.
