# No Johnson-stable rank-5 paving matroid on >=12 points is U_{2,5}-free

## Context
The admitted target claimed infinitely many orders n (including all large primes
n == 1 mod 20) admitting a rank-5 sparse paving matroid M_n whose nonbasis
family H is Johnson-stable (|H1 cap H2| <= 3) and which is U_{2,5}-free
(3-connected, cyclic, with >= n(n-1)/20 circuit-hyperplanes). This sits on the
Geelen excluded-uniform-minor program and the Pendavingh-van der Pol
cover-complexity/counting benchmark for Ex(U_{2,5}).

## Definitions
- Paving matroid of rank 5: every set of size <= 4 is independent; a 5-set is
  either a basis or a nonbasis (dependent hyperplane / circuit-hyperplane).
- Johnson-stable: distinct nonbases H1, H2 satisfy |H1 cap H2| <= 3
  (nonbases form a stable set in the Johnson graph J(E,5)).
- U_{2,5}: rank-2 uniform matroid on 5 points (5-point line); M has a U_{2,5}
  minor if some contraction-restriction is isomorphic to it.
- Sparse paving implies paving; the theorem needs only paving.

## Result (Theorem)
Let M be a rank-5 paving matroid on ground set E with |E| = n >= 12, and
suppose its family H of nonbases (dependent 5-sets) is Johnson-stable, i.e.
|H1 cap H2| <= 3 for all distinct H1, H2 in H. Then M has a U_{2,5} minor.
In particular no such matroid is U_{2,5}-free.

Corollary: the target's infinite family cannot exist — every order it claims
(all large primes n == 1 mod 20, all exceeding 12) is ruled out, since the
Johnson-stability and U_{2,5}-freeness clauses already contradict each other
at n >= 12. Cyclic symmetry, 3-connectivity, duality, and density are moot.

## Proof / Evidence
Unconditional proof (DRAFT.md), verified line by line:
1. Fix an arbitrary 3-set C. Since all <=4-sets are independent, r(C)=3 and
   M/C has rank 5-3=2 on E\C, loopless since r(C+{x})=4.
2. For distinct x,y in E\C, r_{M/C}({x,y}) = r(C+{x,y})-3, which is 1 iff
   C+{x,y} in H and 2 otherwise. So x,y are parallel in M/C iff C+{x,y} in H.
3. The pair-graph G_C on E\C (edge xy iff C+{x,y} in H) is a matching:
   if x were adjacent to distinct y1,y2, then C+{x,y1}, C+{x,y2} would be
   distinct members of H intersecting in >= C+{x} (size >=4), contradicting
   Johnson-stability. This covers the empty-H case too.
4. A matching on N=n-3 vertices has independence number >= ceil(N/2); for
   n>=12, N>=9 so alpha(G_C)>=5. Any independent 5-set I has all 10 pairs
   outside H (bases); with looplessness, (M/C)|I is simple rank-2 on 5 points
   with every pair a basis, i.e. U_{2,5}, obtained by contracting C and
   deleting E\(C cup I). Sharp: N>=9 iff n>=12.

Computational companion (illustration only, not the proof):
`output/artifacts/verify_disproof.py` (stdlib only, exit 0) checks the cyclic
orbit of (0,1,2,4,9): at n=17 (680 triples) and n=41 (smallest prime ==1 mod 20,
10660 triples), the orbit is Johnson-stable and every G_C is a matching with an
explicit independent 5-set witness. Independently replayed: VERIFY_DISPROOF PASS.

## Limitations
Refutes the infinite tail (all n>=12); says nothing about hypothetical
small-order (n<=11) Johnson-stable U_{2,5}-free examples, which the target does
not claim. No statement about non-paving or non-Johnson-stable families.
Cyclic symmetry and density play no role.

## Reproducibility
- Read DRAFT.md for the self-contained proof (no dependencies).
- Run `python3 output/artifacts/verify_disproof.py` (stdlib only) — expect
  exit 0 and `VERIFY_DISPROOF: PASS`.

## References
- J. Geelen, Some open problems on excluding a uniform matroid.
  https://www.math.uwaterloo.ca/~jfgeelen/Publications/uniform.pdf
- R. Pendavingh, J. van der Pol, On the number of matroids compared to the
  number of sparse paving matroids, arXiv:1411.0935.
  https://arxiv.org/html/1411.0935v2
- R. Pendavingh, J. van der Pol, Counting matroids in minor-closed classes,
  JCTB 2014.
  https://www.sciencedirect.com/science/article/pii/S009589561400118X
- D. Mayhew, G. Royle, Matroids with nine elements, arXiv:math/0702316
  (census complete only to 9 points; orders >=12 lie beyond).
