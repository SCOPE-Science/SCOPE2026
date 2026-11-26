# Independent mathematical audit

## correctness

PASS

For the exact simplex minimizer, test its variational inequality at e_i to obtain g_i·v ≥ ||v||²−ρ(λ_i−||λ||²). Independently, λ_i−||λ||² = 1/4−||λ−e_i/2||²; the projection of e_i/2 onto the sum-one hyperplane adds 1/(2m) to every entry, is strictly feasible, and gives the deficit (m−1)/(4m). In the two-dimensional family of RESULT.md the given weights sum to one, weighted transverse components and weighted horizontal perturbations cancel, and Gᵀv+ρλ is constant, certifying the unique optimum. The determinant is −2msδ/(m−1), so the gradient segment excludes zero; with s² below, at, or above the cutoff, the worst component respectively ascends, is flat to first order, or descends. At m=2 the explicit quadratic example has changes 3/8 and −13/8 and an alternative direction with both derivatives −1. The strict cutoff is universal and sufficient, not necessary for descent in every instance. This is a pointwise exact unconstrained theorem; it does not extend the certificate to finite step lengths, projections or inexact multipliers. Read RESULT.md §§Proof–Verification, VERIFICATION.md and verify.py statically; the listed 27/196 increase is a different supplementary witness, not a conflict or a fresh run.

## originality

PASS

The rule and the variational-inequality method are known. The distinct result supported by the comparison is the jointly attainable best constant and necessary boundary for a universal strict-descent certificate in the stated exact unconstrained regime, including failure despite common descent being possible.

## value

PASS

Ridge is used to stabilize the multiplier, but that can undermine common descent before Pareto stationarity. A fourfold tightening of the prior unconstrained norm-squared certificate, sharp at every objective count, tells exactly when the norm alone is a safe first-order diagnostic. The matching ascent of a strongly convex objective despite an alternative common descent direction demonstrates a real failure mode rather than only sharpening an inequality on paper.

The dated certificate retains the supplied scientific assessment, sources and limitations.
