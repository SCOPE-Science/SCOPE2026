# Same-model review

## Correctness

PASS. The source-proved volume and mean-width laws have densities proportional to
\[
\kappa^{1/(d+1)}
\quad\text{and}\quad
\kappa^{d/(d+1)}.
\]
Their exponents sum to \(1\), so the Hellinger affinity is exactly
\[
I_{1/2}/\sqrt{I_aI_b}.
\]
Cauchy--Schwarz gives equality only for constant curvature. Differentiation of
\[
F(t)=\log I_t
\]
gives
\[
F''(t)=\operatorname{Var}_{\mu_t}(\log\kappa),
\]
and a direct midpoint second-difference identity gives the integral kernel with the stated factor \(1/2\). The similarity-scaling exponents cancel exactly. No numerical experiment is used as proof.

## Originality

PASS. The closest source gives both optimal laws and proves rigidity from their equality, but the inspected full text contains no Hellinger or Bhattacharyya distance and no curvature-variance representation of their mismatch. The earlier intrinsic-volume approximation article was also checked for these equivalent formulations and did not reveal a covering statement. Exact-source, exponent, and probability-distance searches located no stronger result.

Residual risk: because the metric calculation becomes short after the two densities are juxtaposed, an unindexed observation could exist under normalized-moment or Jensen-gap terminology.

## Value

PASS. The recent theorem makes incompatibility of two canonical limiting laws the mechanism of its spherical rigidity. The exact Hellinger gap is therefore a natural quantitative invariant of that mechanism, and the variance formula identifies the precise log-curvature fluctuation contributing to it. The quantity is similarity invariant and applies to every \(C^2_+\) convex body, while the claim deliberately stops short of unproved geometric stability.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest source is Steven Hoehner, arXiv:2602.18547v1. Besau--Hoehner--Kur, arXiv:1905.08862 and IMRN 2021, supplies the earlier intrinsic-volume approximation framework.

No bound from this Hellinger gap to Hausdorff, Banach--Mazur, or affine distance from a ball is asserted. The formula requires strictly positive continuous Gauss curvature.
