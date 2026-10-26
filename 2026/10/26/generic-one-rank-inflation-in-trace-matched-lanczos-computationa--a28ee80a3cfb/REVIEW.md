# Scientific review

## Correctness

PASS. The universal rank identity follows by splitting the covariance into its boundary two-plane and a positive scalar bulk. Strict Cauchy--Schwarz gives a positive boundary determinant whenever the next Lanczos coefficient is nonzero; the exact conditional Gaussian has rank \(d-m\). The minimal example has exact rational determinant \(1/100\), an exact zero-variance observation under the true covariance, and approximate variance \(4/25\). The one-parameter positive-definite family proves persistent support mismatch despite vanishing matrix-norm error. `CHECK.py` independently reconstructs the rational example.

## Originality

PASS on inspected published and indexed results, with priority uncertainty beyond them. The source paper's exact and approximate covariances and its rank claim for the exact posterior were compared directly; no inspected theorem asserts the generic rank inflation of the approximate posterior or mutual singularity under vanishing matrix error. Classical Gaussian-conditioning work gives the exact nullspace but not this specific approximation's changed rank. Focused record searches for equivalent Lanczos covariance rank and observed-direction variance found no covering statement. A general covariance-approximation principle could be used to derive aspects once this rank obstruction is known; older specialized literature may contain related support-mismatch observations.

## Mathematical value

PASS. A generic extra positive eigenvalue means an uncertainty distribution intended to quantify information left after exact linear observations assigns positive uncertainty to an observed direction. This changes the support dimension of the posterior and makes strict information divergence infinite, despite arbitrarily small operator error. This is a structural calibration boundary for a natural matrix-free covariance construction, not a numerical tolerance artifact or a single isolated counterexample.

## Scientific limitations

Exact arithmetic and the exact-trace analytic approximation only. No assertion about actual finite-probe numerical implementations, full-rank inverse-covariance KL metrics, or a generic remedy. Independent priority and proof confirmation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
