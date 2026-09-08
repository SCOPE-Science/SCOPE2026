# First generalized-cospectral pair of trees: exhaustive DGS census of unlabelled trees with n ≤ 12

## Context

A graph is determined by its generalized spectrum (DGS) if any graph with the
same spectrum and the same complement spectrum is isomorphic to it (Wang's
DGS program). For trees, adjacency-cospectral counts are classical
(OEIS A006610), and the all-graph adjacency census extends to n = 12
(Brouwer–Spence), but no exhaustive generalized-spectrum grouping of small
trees existed. The window n ≤ 12 is the natural first-occurrence window:
it opens at the first adjacency collisions (n = 8) and closes at the
published adjacency-census limit.

## Definitions

- Free (unlabelled) trees with 1 ≤ n ≤ 12: 987 total
  (1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235, 551 per OEIS A000055).
- Generalized spectrum of a tree T: the pair
  (Spec(T), Spec(complement(T))), i.e. the adjacency characteristic
  polynomial together with the complement's characteristic polynomial.
- Two trees are generalized-cospectral if both polynomials agree.
- DGS scope here is within trees (not against all graphs).
- Walk matrix W(T) = [e, Ae, …, A^{n−1}e], e = all-one vector;
  Smith normal form (SNF) and determinant computed in exact integer arithmetic.

## Result

Over all 987 unlabelled trees with 1 ≤ n ≤ 12:

- **Closure through n ≤ 11.** Every tree with n ≤ 11 is determined by its
  generalized spectrum within trees: all generalized classes are singletons
  (n = 8: 23 classes; n = 9: 47; n = 10: 106; n = 11: 235).
- **First collision at n = 12.** At n = 12 there are 550 generalized classes
  among 551 trees: 549 singletons and exactly one nontrivial pair,
  enumeration indices {421, 498}. This is the first (minimal-order)
  generalized-cospectral pair of non-isomorphic trees.
- **Resolution counts.** Recomputed adjacency-cospectral (non-DS) tree counts
  are n = 8: 2, n = 9: 10, n = 10: 8, n = 11: 60, n = 12: 119, matching
  OEIS A006610. Generalized spectrum resolves all of them except the single
  n = 12 pair: resolved 2, 10, 8, 60, and 117 of 119 at n = 12.
  The n = 12 adjacency class-size distribution is {1: 432, 2: 49, 3: 7};
  the generalized distribution is {1: 549, 2: 1}.

### Witness pair (n = 12)

Vertices 0..11; degree sequence (3,3,3,2,2,2,2,1,1,1,1,1), 5 leaves.

- Tree A (index 421): 0-1, 1-2, 2-3, 3-4, 3-11, 4-5, 4-10, 5-6, 6-7, 7-8, 7-9.
- Tree B (index 498): 0-1, 1-2, 2-3, 3-4, 4-5, 4-11, 5-6, 6-7, 6-10, 7-8, 7-9.

Shared adjacency characteristic polynomial (ascending coefficients):

    (0,0,-6,0,39,0,-66,0,42,0,-11,0,1)

i.e. p(λ) = λ^12 − 11λ^10 + 42λ^8 − 66λ^6 + 39λ^4 − 6λ^2
= λ^2(λ^2−2)(λ^8 − 9λ^6 + 24λ^4 − 18λ^2 + 3).

Shared complement characteristic polynomial (ascending):

    (5,36,-25,-346,-334,438,798,172,-336,-246,-55,0,1)

Both walk matrices are singular (det 0) with SNF diagonal
(1,1,1,1,1,1,2,2,2,2,686,0) up to unit signs, and both discriminants are 0
(repeated eigenvalue 0). Hence neither Wang's odd-squarefree det-W criterion
nor the Ji–Wang–Zhang odd-squarefree discriminant criterion applies to the
witness (both are sufficient-only and require nonsingular input).

Non-isomorphism certificate (AHU centre-rooted canonical forms):

- A: `((((()())))(((()))())())`
- B: `((((()())()))(((())))())`

each occurring for exactly one of the 987 trees; all-pairs distance profiles
also differ. The pair's shared adjacency class has size exactly 2 ({421, 498}).

Criterion coverage (trees satisfying the sufficient condition): Ji–Wang–Zhang
holds for 0 trees at n ≤ 9 and n = 11, 1 at n = 4, 3 at n = 10, 4 at n = 12;
Wang det-W holds for 1 at n = 1, 1 each at n = 7, 8, 9, 3 at n = 10,
6 at n = 11, 8 at n = 12 (full table in artifacts/report).

## Proof / evidence

Computational-exact classification (no new hand theorem beyond cited standard
equivalences: generalized spectrum ↔ Spec + Spec-complement; AHU correctness):

1. Enumerated unlabelled trees by rooted-tree partition recursion, then free
   trees via AHU centre-rooted forms; counts validated against OEIS A000081
   (rooted, 4766 at n = 12) and A000055 (free, 987 total).
2. Per tree, exact integer adjacency and complement characteristic polynomials
   (Faddeev–LeVerrier over Python ints, cross-checked by sympy), walk-matrix
   determinant (Bareiss), walk-matrix SNF (sympy), charpoly discriminant.
3. Grouped by (Spec, Spec-complement); intersected with adjacency groups.
4. Independent clean-room replay `output/artifacts/verify_replay.py` (own
   LeVerrier/Bareiss/AHU code, run with cwd `output/artifacts/`) reports
   `VERIFY_OK`: recomputes all 987 spec/cspec/walkdet entries, AHU uniqueness,
   A006610 adjacency counts, and the sole {421, 498} generalized class.
   The auditor re-ran the replay and independently re-derived both witness
   polynomials, walk determinants, SNF diagonals, discriminants, and
   non-isomorphism with sympy.

## Limitations

- Computational-exact, not a hand proof; completeness rests on generator
  correctness, mitigated by dual OEIS count validation and independent replay.
- Minimality means first within trees n ≤ 12 by exhaustion; no claim for
  n ≥ 13 or non-tree graphs.
- DGS scope is within trees, not against all graphs.
- Stored SNF sign differences (1 vs −1, 686 vs −686) are a sympy diagonal-sign
  convention, not a mathematical difference.

## Reproducibility

Artifacts: `output/artifacts/trees_free.json` (987 edge lists),
`output/artifacts/census.json` (per-tree spec, cspec, walkdet, disc,
SNF diagonal), `output/artifacts/witness_cert.json`,
`output/artifacts/gen_groups.json`, `output/artifacts/verify_replay.py`.
Run `python3 verify_replay.py` inside `output/artifacts/`.

## References

- OEIS A006610 (trees not determined by adjacency spectrum).
- OEIS A000055 / A000081 (free / rooted tree counts).
- Brouwer–Spence adjacency cospectral census to n = 12.
- Wang arXiv:1410.2164 (odd-squarefree det-W DGS criterion).
- Qiu–Wang–Wang–Zhang arXiv:2108.00592 (SNF strengthening).
- Ji–Wang–Zhang arXiv:2310.00846 (discriminant criterion for signed trees).
- Ji–Tang–Wang–Zhang arXiv:2411.01551 (mod-4 cospectral invariants).
