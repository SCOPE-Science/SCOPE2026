# Self-review

## Correctness — PASS

The domain includes every nondegenerate convex trapezoid with positive bases; affine normalization reduces all of them to a one-parameter strip with linear half-width. The proof computes the unsigned first area moment by conditional integration of three independent uniform horizontal coordinates and ordered heights, computes the squared moment via an independently derived determinant/covariance identity, and exactly factors the derivative of the normalized variance. All coefficients, boundary values and asymptotic constants are checked symbolically by `verify.py`; sampling checks do not replace the infinite-parameter proof. The inverse Hölder bound follows from a positive continuous derivative multiplier and an explicit integral inequality.

## Originality — PASS, provisional

The older general formulas for expected random convex-hull area (Buchta, 1984) and the general determinant second-moment identity already supply the individual moment ingredients. Those ingredients are **not** claimed as original. The finding instead establishes strict global shape ordering of their dimensionless dispersion ratio on all trapezoids, exact endpoint rigidity, the full inverse classification and optimal quadratic endpoint conditioning. These assertions are neither the classical extrema for four-point convex-position probability nor the published Gaussian-position or regular-polygon moment results. The compared indexed research records on random circumradius laws and vertex-sampled polygon triangles concern different sampling objects/invariants. The original 1984 German article could not be accessed in full and remains an explicit priority risk; an unindexed equivalent theorem could exist.

## Value — PASS

For affine shape reconstruction, individual triangle areas change under overall scaling; normalized dispersion is directly measurable without a Euclidean calibration and is invariant under shear. A complete, sharp and strictly ordered one-parameter law between the limiting triangle and parallelogram class supplies a natural inverse geometric statistic, while quadratic endpoint behavior precisely identifies the unavoidable ill-conditioning. This is a whole-family classification, not a single evaluation or a numerical table.

## Scope and remaining risks

The theorem does not reconstruct an arbitrary quadrilateral, provide sampling confidence bounds, or establish a stronger-than-Hölder endpoint inverse. General first-moment formulas and prior square/triangle constants are correctly treated as earlier work. The accessible literature review supports provisional priority only.

Self-review: passed. Independent audit: not yet performed.
