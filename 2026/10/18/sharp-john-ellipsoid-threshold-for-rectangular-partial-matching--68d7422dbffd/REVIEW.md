# Scientific review: sharp rectangular John-ellipsoid threshold

## Correctness — PASS

The row-product John certificate is explicit: for each row, the \(b+1\) contact normals \(-e_j\) and \(\mathbf1\), normalized with the inverse shape, have zero weighted first moment and identity weighted second moment when every weight equals \(b/(b+1)\). The contact criterion establishes global uniqueness in the full \(ab\)-dimensional product, not merely optimality among symmetric ellipsoids. The exact support of a column-cap normal is \((a+\sqrt a)/(b+1)\). This yields a necessary and sufficient survival inequality. Below the threshold, permutation invariance and a convex interpolation of centers and positive-definite square-root shapes show that simultaneous column slack would contradict log-determinant optimality. Spectral decomposition and determinant give the volume. All assumptions include \(2\le a\le b\); subcritical shape/volume are expressly unclaimed. The standalone exact-rational checker passes 132 parameter instances; finite tests are corroboration only.

## Originality — PASS, subject to priority risk

Heuer–Striker, arXiv:2012.09901, Section 3, prove/review the complete partial-permutation polytope facet structure and study face and enumeration questions; the full inspected manuscript has no John-ellipsoid result. Torres, arXiv:2306.11910, Theorems 2.4 and 3.1, treats fractional matchings, fixed-cardinality matching polytopes and normality; the full inspected manuscript has no maximum-volume-ellipsoid formula. The square-parameter family \(a=b\) lies strictly on the non-survival side of the rectangular inequality, so its analysis cannot cover this new survival regime. Results about fixed-cardinality matching-polytope slices have different affine dimensions and do not imply ellipsoids of the entire polytope. The Cao–Chen faces study was not fully accessible, so equivalent terminology or a broader optimal-design theorem remains a nonzero literature-priority risk; published-search nonmatches alone are not treated as proof of novelty.

## Value — PASS

This establishes a sharp, all-parameter geometric phase boundary for an infinite family of classical matching polytopes: genuine column facets can be *invisible to the unique John ellipsoid* even though deleting them properly enlarges the convex body. The threshold gap grows like the square root of the row count; exact contacts and volume are obtained without enumerating matchings or solving a growing semidefinite program. The boundary also distinguishes noncontact, onset-of-contact, and necessarily-active regimes. The result is motivated by the geometry of a fundamental integral matching relaxation, rather than by an arbitrary parameter slice.

## Bibliographic limitations

No independent priority certification is claimed. One plausible square-doubly-substochastic faces article could only be compared by its abstract; no claim is made that its full paper was inspected. In the non-survival regime, the actual John ellipsoid is not explicitly classified here.

Self-review: passed. Independent audit: not yet performed.
