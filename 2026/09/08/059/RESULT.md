# Exact maximum rainbow Schur-triple counts R(n) for 3-colorings of [1,n], n <= 12

## Context

Graham-Rodl-Rucinski posed the minimum number of monochromatic Schur triples in
2-colorings of [1,n]; resolved by Datskovsky / Schoen / Robertson-Zeilberger
(formula floor((n^2-4n+6)/11), OEIS A321195). Parczyk-Spiegel (arXiv:2410.22024,
v2 Apr 2026) proposed the natural anti-Ramsey variant: the maximum number of
rainbow Schur triples over 3-colorings of [1,n], motivated also by the
Erdos-Sos rainbow-triangle problem (settled by Balogh et al.). They prove the
asymptotic max rainbow fraction lies in [0.4, 0.66364], conjecture 0.4 is tight
via an explicit construction c0, and publish no exact small-n table. This
record supplies the missing exact small-n benchmark. Scope n <= 12 sits just
below the Schur number S(3) = 14.

## Definitions

- [n] = {1, ..., n}.
- A Schur triple is an ORDERED triple (x,y,z) in [n]^3 with x + y = z;
  (x,y,z) and (y,x,z) count as distinct when x != y (Parczyk-Spiegel
  convention). Total T(n) = n(n-1)/2.
- A triple is rainbow under c:[n] -> {0,1,2} if c(x), c(y), c(z) are pairwise
  distinct.
- R(n) = max over all 3-colorings of the number of rainbow Schur triples.
- S3 classes: colorings modulo global permutation of the 3 color labels.
- Template c0 (Parczyk-Spiegel lower-bound construction, labels mapped to
  {0,1,2}): even i -> 2; odd i <= 2n/5 -> 0; odd i > 2n/5 -> 1.

## Result

Exhaustive enumeration over all 3^n colorings gives:

| n | T(n) | R(n) | R/T | labeled optima | S3 classes |
|---|------|------|-----|----------------|------------|
| 1 | 0 | 0 | -- | 3 | 1 |
| 2 | 1 | 0 | 0.0000 | 9 | 2 |
| 3 | 3 | 2 | 0.6667 | 6 | 1 |
| 4 | 6 | 4 | 0.6667 | 6 | 1 |
| 5 | 10 | 6 | 0.6000 | 12 | 2 |
| 6 | 15 | 8 | 0.5333 | 12 | 2 |
| 7 | 21 | 12 | 0.5714 | 6 | 1 |
| 8 | 28 | 14 | 0.5000 | 24 | 4 |
| 9 | 36 | 18 | 0.5000 | 30 | 5 |
| 10 | 45 | 22 | 0.4889 | 6 | 1 |
| 11 | 55 | 28 | 0.5091 | 6 | 1 |
| 12 | 66 | 30 | 0.4545 | 66 | 11 |

So R(1,...,12) = 0, 0, 2, 4, 6, 8, 12, 14, 18, 22, 28, 30.

One optimal coloring per n (colors {0,1,2}):

- 1: [0]; 2: [0,0]; 3: [0,2,1]; 4: [0,1,2,1]; 5: [0,1,2,1,0];
  6: [0,1,2,1,2,1]; 7: [0,1,2,1,2,1,0]; 8: [0,1,2,0,1,2,1,0];
  9: [0,1,2,1,0,1,2,1,0]; 10: [0,1,0,1,2,1,2,1,2,1];
  11: [0,1,0,1,2,1,2,1,2,1,0]; 12: [0,0,1,2,2,1,1,2,2,1,0,0].

All 11 S3-class representatives at n = 12 (each attains 30):

- [0,0,1,2,2,1,1,2,2,1,0,0], [0,1,0,1,0,1,2,1,2,1,2,1],
  [0,1,0,1,2,1,0,1,2,1,2,1], [0,1,0,1,2,1,2,1,2,1,0,1],
  [0,1,0,1,2,1,2,1,2,1,2,1], [0,1,2,1,0,1,2,1,0,1,2,1],
  [0,1,2,1,2,0,0,2,1,2,1,0], [0,1,2,1,2,0,1,2,1,2,1,0],
  [0,1,2,1,2,1,0,0,0,1,2,1], [0,1,2,1,2,1,0,1,0,1,2,1],
  [0,1,2,1,2,1,0,2,0,1,2,1].

(Full per-n class representatives are stored in artifacts/results.json.)

Comparison with the c0 template: recounting c0 on [1,n] gives
0, 0, 2, 4, 6, 8, 10, 14, 18, 22, 26, 30 for n = 1..12.
Hence c0 is optimal at every n <= 12 EXCEPT n = 7 (10 < 12) and n = 11
(26 < 28) -- a concrete small-n caveat to its asymptotic tightness
conjecture.

## Proof / Evidence

Computational exactness by exhaustive search plus independent replay
(stdlib Python only):

- Generation (artifacts/enumerate.py): enumerates 3^(n-1) colorings per n with
  c(1) = 0 fixed. Fixing is exact for the maximum because a global color
  permutation is a symmetry of the rainbow count; labeled counts are lifted by
  x3. Tracks the maximum, labeled-optimum counts, and canonical S3 classes
  (minimum over the 6 color permutations). Runtime ~0.8 s total.
- Independent audit (artifacts/verify.py, separate code path): full 3^n
  labeled product with set-based rainbow predicate; rechecks T(n),
  recomputes each R(n), replays each witness, recounts labeled optima, and
  verifies class representatives are pairwise S3-inequivalent and cover all
  optima. Output: VERIFY_OK on all 12 values and class counts.
- The auditor additionally re-ran a from-scratch full labeled brute force and
  S3-canonical recheck: all R(n), labeled counts, class counts, witness
  replays, and the c0 recount reproduced exactly.

## Limitations

- Ordered-triple convention (T(n) = n(n-1)/2); unordered conventions differ by
  roughly 2x off-diagonal -- convert before comparing.
- Exactness is computational (exhaustive enumeration + independent replay),
  not a structural closed form; no formula for R(n) is claimed.
- Only 3 colors, only intervals [1,n], n <= 12.
- No claim on the asymptotic 0.4-tightness conjecture; classification is up to
  S3 color permutation only.

## Reproducibility

In output/artifacts/ run:

    python3 enumerate.py && python3 verify.py

stdlib only; enumerate.py regenerates results.json (~1 s), verify.py prints
VERIFY_OK.

## References

- O. Parczyk, C. Spiegel, An Unsure Note on an Un-Schur Problem,
  arXiv:2410.22024 (v2, Apr 2026). Asymptotic bounds 0.4-0.66364, 0.4-tightness
  conjecture, c0 construction; no exact small-n table.
- M. Budden, B. Landman, Rainbow Numbers for the Generalized Schur Equation,
  arXiv:2401.07357. Different invariant (minimum colors forcing rainbow).
- Y. Cheng et al., Integer colorings with forbidden rainbow sums,
  arXiv:2005.14384. Different objective (counting rainbow-free colorings).
- C. Koutschan, E. Wong, Exact Lower Bounds for Monochromatic Schur Triples
  and Generalizations, arXiv:1904.01925. 2-color monochromatic case only.
- OEIS A321195 (minimum monochromatic Schur triples, 2 colors);
  OEIS live searches for 'rainbow Schur', 'maximum rainbow triples', and the
  candidate prefix returned No results.
