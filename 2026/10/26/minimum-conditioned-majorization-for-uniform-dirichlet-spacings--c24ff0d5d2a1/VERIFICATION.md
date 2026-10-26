---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible verification

The elementary change-of-variables and majorization proof in RESULT.md establishes the theorem for every integer \(n\ge2\); the computations below are independent finite corroboration, not an infinite or external certificate.

Run `python3 verify.py` with Python 3's standard library. It asserts equality of the conditional-moment and independent exponential-order-statistic covariance forms for each \(2\le n\le29\), checks strict negativity, and compares the analytic conditional-maximum CDF with minus the derivative in the minimum of an independently derived constrained-volume formula at 71 rational test points with \(3\le n\le8\). The run produced three `PASS` lines and no assertion failure.

The direct conditional-volume identity is
\[
\Pr(m\ge a,M\le b)=\sum_{j=0}^n(-1)^j\binom nj\bigl(1-na-j(b-a)\bigr)_+^{n-1},\qquad 0\le a<1/n,\ b\ge a,
\]
with derivative evaluated away from piecewise-polynomial breakpoints. Its exact derivative must equal \(f_m(a)\Pr(M\le b\mid m=a)\). All tested fractions use exact integers and rational arithmetic.

No stochastic simulations, unstated external data, package dependencies, external certification, or independent audit are asserted.
