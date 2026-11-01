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
# Reproduction and limits

Run `python verify.py` using only Python's standard library. The 428 assertions compare direct binomial averages with Fourier-multiplier evaluations at sampled points, test the real-exponential norm comparison, and exercise selected convergent-denominator and near-resonant inequalities. These are finite checks, not a computer proof of any infinite-dimensional or all-parameter statement.

The analytic proof's core identity is the exact geometric-mean update of unilateral positive shift weights. It gives the Fourier multiplier \((1+e^{2\pi im\theta})/2\). Fourier polynomial approximation proves uniform convergence. Splitting the analytic Fourier series near \(k^{1/3}\) proves the bounded-type upper rate; convergent denominators supply the matching lower barrier. The nested Liouville construction enforces retention of selected Fourier coefficients at arbitrarily late times while maintaining a common analytic strip.

The primary 2026 composition-operator paper and 2022 Birkhoff-weight paper were inspected for scope. A closely related historical weighted-shift paper was accessible only through its public abstract and journal listing. Publication-priority uncertainty therefore remains, and no independent audit has been performed.
