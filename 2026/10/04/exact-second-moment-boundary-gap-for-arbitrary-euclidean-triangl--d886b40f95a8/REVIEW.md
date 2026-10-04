# Review

## Correctness
**PASS.** The claim follows from the identity \(\mathbb E\|Z-Z'\|^2=2(\mathbb E\|Z\|^2-\|\mathbb EZ\|^2)\), exact Dirichlet moments for area-uniform barycentric coordinates, and exact one-dimensional segment moments for the arclength mixture on the three sides. The resulting side-length formulas were algebraically replayed in `verify.py`. Strict positivity is proved symbolically after the semitangent substitution \(x=s-a\), \(y=s-b\), \(z=s-c\), with every term positive for a nondegenerate triangle.

## Originality
**PASS.** Lotnikov's arXiv:2608.14848v1 states the all-moments conjecture, gives arbitrary planar results only for sufficiently high moments, and treats triangles at the first moment. Tokmachev's arXiv:2607.08869v1 gives all moments under centroid coincidence; for a triangle this covers only the equilateral case. Searches for the exact second-moment formulas, equivalent moment-of-inertia formulations, and published-database records returned no covering arbitrary-triangle statement. Older polygon distance-distribution papers inspected in scope concern area-uniform point pairs or regular polygons, not this boundary-versus-interior gap.

## Value
**PASS.** The result fills a natural low-order hole in a current geometric-probability comparison: \(p=2\) is the first nontrivial power moment after the mean and is structurally special because it reduces to covariance, yet generic triangles fall outside the centroid-based all-moment theorem. The exact gap in classical triangle invariants gives a reusable quantitative statement rather than a one-off numerical check.

## Closest literature and limitations
The closest sources are arXiv:2608.14848v1 and arXiv:2607.08869v1. The result does not extend their first-moment or centroid-based theorems to arbitrary powers; it establishes only the exact squared-distance comparison for triangles. A residual bibliographic risk remains that an equivalent classical moment-of-inertia formula may exist under different terminology.

Same-model review: passed. Independent audit: not yet performed.
