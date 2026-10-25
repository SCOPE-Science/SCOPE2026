# Scientific review

## Correctness — PASS

The support function on a rank-\(k\) hypersimplex is the sum of the largest \(k\) normal coordinates; complementing converts this exactly to \(r=\min(k,n-k)\). Every sorted mean-zero normal decomposes uniquely as a nonnegative sum of two-level step vectors. The width functional is linear on that chamber, so the Euclidean triangle inequality bounds width below by the minimum generator ratio. The triangle inequality is strict for combinations of two different nonparallel step vectors, proving completeness of the equality classification. Exact squared ratios reduce to the two endpoint partition sizes; a parity-aware integer calculation establishes the threshold \(\(n=4r^2-1\)\). The theorem explicitly uses intrinsic rather than ambient normals. Exact finite fraction arithmetic and random vectors corroborate the proof but are not substituted for it.

## Originality — PASS (best-knowledge assessment)

The closely related complete simplex-width proof of Har-Peled–Robson (2023) treats the rank-one case, while Martínez-Sandoval–Padrol (2019) treat hypersimplex projections and skeletons. Published research records on hypersimplex inradii, matroid independence-polytope radii and simplex plank widths were compared by **the mathematical invariants and implications**, not titles alone. The centrally symmetric case \(\(n=2k\)\) can be deduced from known inradius data and is explicitly recognized as covered; the claimed new content is the uniform formula and full direction/phase classification over the non-simplex, generally noncentrally symmetric family. No checked record states or entails that full result. Broader ordered-coordinate norm inequalities and inaccessible unindexed literature leave residual priority risk; no uniqueness or independent priority certification is claimed.

## Value — PASS

Minimum Euclidean width is a natural affine-intrinsic invariant of the uniform-matroid base polytope. The exact classification gives all minimizing directions across every integer rank and dimension, including a non-obvious structural bifurcation precisely at \(\(n=4r^2-1\)\). This connects polytope geometry to an ordered-coordinate spread functional and determines behavior even when the usual inball calculations are insufficient. It is not an arbitrary parameter slice or a known-table recomputation.

## Closest literature and limits

Har-Peled–Robson, arXiv:2301.02616 (2023): complete rank-one simplex width. Martínez-Sandoval–Padrol, arXiv:1909.01189 (2019): hypersimplex projections. Indexed connected-matroid base-polytope inradius result: implies the symmetric \(\(n=2k\)\) subcase but does not resolve general nonsymmetric minimum width. Absolute priority and independent mathematical assessment are outstanding; the exact theorem is for \(2\le k\le n-2\), with normals restricted to the affine span.

Self-review: passed. Independent audit: not yet performed.
