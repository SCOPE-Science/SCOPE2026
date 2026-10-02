# Independent mathematical audit — SCOPE-20260914-032

Disposition: **passed**.

## Correctness
**PASS** — At a=2/5, the sup-norm perturbation is at most 4/5. The even/odd periodic and antiperiodic free spectra isolate the relevant eigenvalues. Exact Ritz expectations and residual variances give the stated one-sided Kato-Temple lower bounds: even-periodic 5917/1425>83/20 and even-antiperiodic 19/20, while the odd-sector Ritz upper bounds are 19/5 and 4/5. The surrounding clusters are separated, so these are the first two finite gaps and the second has width at least 7/20>1/5.

## Originality
**PASS** — Targeted searches found extensive two-term Hill/Whittaker-Hill gap asymptotics but no theorem or table giving this finite-amplitude a=2/5 second-gap lower bound or the threshold disproof.

### Equivalent formulations
The threshold disproof is equivalent to one certified point with w2>=0.2 below a=0.5; no such prior point was found.

### Broader coverage
These broader results do not provide the concrete finite-amplitude certified lower bound that implies the requested threshold is false.

### Exact database or table
Search failure is only supplementary; statement-level non-implication is the main evidence.

### Claim versus prior implication
The record supplies a separate finite-dimensional variational certificate.

### Source inspections
- **Asymptotics of instability zones of the Hill operator with a two term potential** (https://arxiv.org/abs/math-ph/0509034): not covering the finite-amplitude certificate. Results are asymptotic in small coupling or high gap index.

## Scientific value
**PASS** — A single rigorously certified counterexample is mathematically sufficient to invalidate the stated threshold interval. The result supplies a reusable exact variational/Temple certificate rather than only a floating-point observation, so its value is the sharp logical disproof of the target, not a claim to determine the full gap function.

## Residual risks
- The literature search may miss a numerical spectral table for this exact normalization, but no stronger implication was found.

## Checked sources
- record artifacts/verify_disproof.py
- Resultary
- arXiv:math-ph/0509034
- J. Approx. Theory 135 (2005) 70-104
