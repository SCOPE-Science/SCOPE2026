# Self-review

## Correctness — PASS

The exact estimator, interpolation template, common versus independent shift coupling, and all probability distributions are specified in RESULT.md. Uniform second-order interpolation remainder gives a centered bounded triangular array with limiting conditional variance \(J_f V(\Xi)/8\); conditional Lindeberg implies the mixed-normal law. Exact uniform-shift polynomial integrals yield \(\mathbb E V=1/80\) and the non-Gaussian standardized fourth moment \(101/27\). Zero conditional cell means imply identical finite-size variances under the two shift schemes, while independent shifts give an ordinary Lindeberg CLT. Pair differences give the exactly conditionally unbiased variance estimator, and its triangular-array law of large numbers supports studentization. The packaged verifier checks 137 polynomial, finite-moment, and numerical identities. Boundary restrictions: \(f\in C^2([0,1])\), \(J_f>0\), and the specified uniform template and two residual draws. No numerical experiment is used to justify infinite convergence.

## Originality — PASS, with bounded priority risk

Kunsch, *Linear Monte Carlo quadrature with optimal confidence intervals* (arXiv:2309.09059), defines shared interpolation shifts in his stratified-control-variate construction but proves error/confidence-width rates, not this common-shift Gaussian-mixture limit, universal kurtosis, exact shared/independent-shift variance equivalence, or feasible conditional pivot. Chopin–Gerber (arXiv:2210.01554), full-text Theorem 2, derive a CLT for different locally controlled cubic stratification, not the same randomized interpolation scheme. Nakayama–Tuffin (DOI:10.1145/3643847), author-preprint sections 1–4, develop normal calibration conditions for randomized quasi-Monte Carlo and discuss fixed-randomization normality failure, without deriving this explicit interpolation-based coefficient or pivot. Glynn–Szechtman (2002) study general control variates and iid sampling; their broad methods do not specify the SCV model. Actual semantic searches of the research-record database for both algorithm and formulas did not return an implication-complete equivalent. The general common-environment mixture mechanism is classical and is not claimed as independently new. Undiscovered specialized literature is a residual publication-priority risk.

## Value — PASS

A shared randomization phase is an actual structural feature of the motivating estimator, not an arbitrary mathematical slice. Two algorithms with **exactly equal finite-sample mean squared error** can have fundamentally different limiting confidence calibration; the explicit non-Gaussian constant \(101/27\) and accessible two-residual studentization quantify the difference at no added function-evaluation cost. This is a specific reproducible test case for confidence-interval design in smooth stratified quadrature. The result does not claim broader optimality or universal superiority of independent shifts.

## Verification and limitations

Run `python verify.py` with `requirements.txt`. The checker establishes symbolic equalities and numerical sanity checks; the infinitely many-cell convergence follows from the written analytic argument. The 95% unstudentized coverage of approximately 0.9446368 is a numerical integral of the proved limit, not an exact finite-sample guarantee. Publication priority and all analytic steps have not undergone independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
