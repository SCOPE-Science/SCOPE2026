# Scientific review

## Correctness — PASS
The single-probe Gaussian projector moment is reduced to a two-dimensional angular integral and proved exactly. Applying the positive-definite \(2\times2\) square-root identity produces the stated risk. The exact isotropic-risk factorization, derivative and quadratic discriminant establish all strict and equality cases. The risk decreases strictly with certified angular alignment, and the derivative has at most one interior maximum, yielding the robust endpoint-or-limit theorem. Exact arithmetic and independent numerical angular quadrature support the formulas but do not replace proof.

## Originality — PASS, with publication-priority uncertainty
The motivating covariance-aware RSVD treatment of Boullé--Townsend (arXiv:2105.13052, notably its covariance-quality bounds) and the general Gaussian/sketch error bounds of Diouane et al. (arXiv:2206.08793) were compared by hypothesis and conclusion; they do not identify the exact one-probe planar angle-vs-strength risk order or the certified-alignment minimax switch. Targeted searches of published mathematical records did not identify a covering statement. Classical planar Gaussian angular projector identities could potentially imply parts of the derivation, and uncatalogued exact comparisons cannot be excluded; these are residual publication-priority risks.

## Mathematical value — PASS
The result addresses the natural design question raised by covariance-informed randomized range finding: how strong should an imperfect prior be when only its guaranteed alignment is known? A sharp, dimensionless quality threshold produces a robust choice between isotropic probing and concentrating all effort along the prior. The explicit example demonstrates a nonmonotone, counterintuitive reversal: increasing the same prior strength first raises and then lowers expected error. The entire classification uses exactly one matrix--vector product and a natural squared Frobenius loss, not an arbitrary isolated numerical slice.

## Scope and risks
The guarantee is planar, exact-arithmetic, one probe and rank-one Gaussian covariance tilt; it does not compare against all conceivable sampling strategies. Nonattainment of the strong-prior infimum at finite covariance strength is explicit. The literature review cannot establish publication uniqueness and no independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
