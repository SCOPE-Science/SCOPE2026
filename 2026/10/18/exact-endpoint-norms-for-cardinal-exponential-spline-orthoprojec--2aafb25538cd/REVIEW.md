# Review of the exact cardinal exponential-spline endpoint norm

## Correctness — PASS
The proof obtains the full kernel from the positive tridiagonal Gram symbol and its geometrically decaying inverse; strict cellwise convexity forces all maxima to be knots. A unique sign crossing gives an exactly integrated nodal row. The weak-tension coefficient follows by differentiation of the signed integral at the limiting zero, and the large-tension limit follows from explicit Gram asymptotics. All quantifiers and parameter boundaries are stated. A standard-library finite-section implementation passed 34 auxiliary assertions, but finite checks were not treated as an infinite proof.

## Originality — PASS, conditional on documented source-access risk
Closest material is Kayumov (2004), with a sharp uniform-over-meshes constant 3, and Unser–Blu (2005), with a generic orthogonal projection/filter representation. Neither accessible statement identifies the exact full-line tension curve, all maximizing knots, or the quadratic weak-tension bump. General Chebyshev-spline boundedness and classical cardinal L-spline interpolation do not settle this orthoprojector norm. Full historical primary texts were only partly accessible, so independent priority verification is needed before publication.

## Value — PASS
A sharp uniform-grid least-squares stability constant is a natural object. The theorem proves that small hyperbolic tension strictly worsens the sharp bound, strong tension restores the polynomial baseline, and the maximal response occurs at a finite intermediate value. Its full exact parameter formula and maximizer rigidity are more informative than a generic uniform bound.

## Limitations
The result is limited to the bi-infinite uniform mesh and the symmetric second-order exponential equation. No optimal-tension uniqueness or exact maximum value is asserted. Incomplete historical full-text access leaves a material priority risk; numerical consistency checks do not replace proof.

Self-review: passed. Independent audit: not yet performed.
