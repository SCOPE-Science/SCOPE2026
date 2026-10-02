# Independent scientific review

## Final claim

For every planar convex body of constant width \(w\), with Steiner disk \(B_S\),
\[
\frac{\pi w^2}{4}-A(K)\ge 2\pi\,d_H(K,B_S)^2.
\]
The constant \(2\pi\) is sharp; equality is attained only by the disk.

## Correctness

**PASS.** After translating the Steiner point to the origin, the constant-width support function has only odd Fourier modes beyond the constant term. The area deficit is
\[
\frac{\pi}{2}\sum_{n\ge3,\ n\text{ odd}}(n^2-1)(a_n^2+b_n^2),
\]
while the Hausdorff distance to the Steiner disk is the supremum norm of the nonconstant support part. Pointwise Cauchy--Schwarz together with
\[
\sum_{k\ge1}\frac{1}{(2k+1)^2-1}=\frac14
\]
gives the coefficient \(2\pi\). The finite Fourier family in the proof preserves positive curvature after sufficiently small scaling and has deficit-to-distance-squared ratio \(2\pi(N+1)/N\), proving sharpness. Equality in Cauchy--Schwarz would force the infinite extremal Fourier profile; its curvature measure contains a signed point-mass component, so convexity excludes it unless the perturbation vanishes.

## Originality

**PASS, to the best of the inspected literature.** Groemer's 1988 constant-width stability theorem gives existence of a nearby width-\(w\) disk with a weaker Hausdorff constant and does not identify the Steiner disk. Cufí--Gallego--Reventós give Fourier and \(L^2\)-Steiner-disk inequalities, not this sharp \(L^\infty\)/Hausdorff inequality. A later 2026-09-21 result gives a stronger angular support profile whose antipodal endpoint recovers the present estimate; its later date does not constitute prior coverage of the 2026-09-20 claim.

## Value

**PASS.** The theorem sharpens a classical constant-width stability problem, uses the canonical Steiner-centered disk rather than an existential translate, determines the optimal coefficient, and explains nonattainment away from the disk.

## Residual risks

Originality remains best-of-knowledge because an equivalent older result could be phrased in support-function or Sobolev terminology not retrieved by the searches.
