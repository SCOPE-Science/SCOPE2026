# Connectedness of the Hurwitz space H(PSL(2,7),(2A,3A,7A,7A)): one braid orbit

## Context
Connected components of Hurwitz spaces — braid orbits on Nielsen classes — are the
Fried–Voelklein moduli input to the regular inverse Galois problem and to current
component-counting programs (asymptotics as branch points grow; Coleman–Oort
applications). Single (2,3,7)-triple existence/multiplicity for PSL(2,7) is
classical, but the 4-point braid-orbit decomposition for the class
(2A,3A,7A,7A) is a distinct global dynamical invariant not settled by
single-triple integers.

## Definitions
- Fixed model: `G = PSL(2,7) = SL(2,7)/{±I}`, elements as F7-matrix pairs
  `(a,b,c,d)`, canonical representative = lexicographic minimum of `m, -m`.
  Computed classes: `1A(1), 2A(21), 3A(56), 4A(42), 7A(24), 7B(24)`;
  `7A` is the class of `[[1,1],[0,1]]`.
- Nielsen class `N`: ordered product-one generating 4-tuples `(g1..g4)` with
  `g1*g2*g3*g4 = 1`, `<gi> = G`, class multiset `{2A,3A,7A,7A}`.
- Braid generators: `si: (..,a,b,..) -> (..,aba^{-1},a,..)`,
  `si^{-1}: (..,a,b,..) -> (..,b,b^{-1}ab,..)`.
- Reduced classes: `N` modulo simultaneous `G`-conjugation (canonical rep =
  lex-minimum of the 168 conjugates); braid action descends. The outer
  automorphism (conjugation by `diag(1,3)`, det 3 nonsquare) swaps `7A<->7B`
  and fixes `2A,3A` setwise, so for multiset `{2A,3A,7A,7A}` the
  class-preserving subgroup of `Aut(G)` is `Inn(G)`.

## Result
- `|N| = 48384` ordered tuples: exactly `4032` in each of the 12 position
  patterns of the multiset.
- Generation is automatic: 0 non-generating product-one tuples in every pattern.
- Full braid action: 1 orbit of size 48384.
- Reduced quotient: `|N/G| = 288 = 48384/168` (simultaneous conjugation acts
  freely; every stabilizer is trivial), forming 1 braid orbit of size 288.
- Hence the (reduced) Hurwitz space `H(PSL(2,7),(2A,3A,7A,7A))` is connected
  (exactly one component).
- Cover genus (degree-7 coset action of an order-24 subgroup): cycle structures
  `2A: 2^2.1^3`, `3A: 3^2.1`, `7A: 7`; Riemann–Hurwitz
  `2(7+g-1) = 2+4+6+6 = 18`, so `g = 3`.
- Negative lift observation: the section-dependent `SL(2,7)`-lift product sign
  (`+1`: 24120, `-1`: 24264) is not braid-invariant (both signs occur inside
  the single orbit), so no Schur-lift separation exists here — consistent with
  connectedness.

## Explicit braid-word witness
- `A = ((0,1,6,0),(0,1,6,1),(1,4,0,1),(1,4,0,1))`, classes `(2A,3A,7A,7A)`.
- `B = ((0,1,6,0),(0,1,6,2),(0,3,2,5),(2,0,2,4))`, classes `(2A,7A,7A,3A)`.
- Word (11 moves): `s1, s2^-1, s3, s2^-1, s1, s2^-1, s2^-1, s2^-1, s3^-1, s2, s1`.
- Class trace: `2377 -> 3277 -> 3727 -> 3772 -> 3772 -> 7372 -> 7732 -> 7372
  -> 7732 -> 7723 -> 7273 -> 2773`; product-one and generation hold at every
  step; endpoint equals `B` exactly.

## Proof / evidence
Machine-verified exhaustive enumeration (stdlib-only Python):
- Raw bound `21*56*24*24 = 677376`; per-pattern product-one plus generation scan.
- Full-braid BFS over `N` with `sigma_i^{±1}` (closure in `N` asserted at every
  move): 1 component of size 48384.
- Independent union-find recount over canonical reps: 1 component of size 288;
  closure/coverage: orbit sizes sum to class counts at both levels.
- Witness replayed move-by-move with class/product/generation checks.
- Audit independently reran the script (all counts reproduced), replayed the
  11-move word with an independent implementation, recounted all 12 patterns
  without the generation filter (0 non-generating), took a global stabilizer
  census (trivial everywhere), and recomputed the degree-7 coset cycle types.

## Limitations
- Single Nielsen class (plus `(2A,3A,7B,7B)` by outer-automorphism symmetry as
  corollary).
- Computational proof: replayable in minutes but not hand-checkable.
- Conventions: ordered tuples; reduced = Inn-quotient (= full
  class-preserving Aut-quotient here).
- `g = 3` is the genus of the degree-7 cover, not of the Hurwitz space itself.

## Reproducibility
- Run: `python3 output/artifacts/census.py` (stdlib only; minutes-scale).
- Outputs: `output/artifacts/results.json` (counts, orbit sizes, lift data,
  witness word, representatives).
- Note: the script's final write path is hardcoded to the research lane; rerun
  writes must be redirected or the path edited (all computation precedes it).

## References
- M. D. Fried, Introduction to moduli, l-adic representations and the Regular
  Version of the Inverse Galois Problem, arXiv:1803.10728.
- B. Seguin, Counting Components of Hurwitz Spaces, arXiv:2409.18246.
- H. M. M. Salih, Connected Components of Affine Primitive Permutation Groups,
  arXiv:2001.02295.
- LMFDB, Abstract group 168.42: PSL(2,7),
  https://www.lmfdb.org/Groups/Abstract/168.42
