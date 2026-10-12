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

# Exact verification

Execute `python3 verify_pd_variance.py` with a current Python 3 installation. Only `fractions` and `collections` from the standard library are needed. On this package the program prints `VERIFY_OK` with the parameter interval, derivative tests, and survivor-state totals.

The checker reproduces the variance polynomial and its derivative, verifies positivity of **all three** sign-adjusted degree-two Bernstein coefficients at each of four rational extinction probabilities, proves positive lengths and root-to-tip height one on the complete 18-edge binary tree, and checks the four strict binary derivative rational margins. As an independent numerical/algebraic route, it sums the rooted-PD distribution over all 1024 possible sets of survivors for each of four rational extinction probabilities on two tree profiles (8192 contributions), matching the covariance-formula variance exactly.

**Mathematical scope.** The analytic Bernstein/Descartes argument, not the finite enumeration, proves the interval-wide exactly-three-critical-points theorem. The fully resolved example has at least three critical points and at least two local maxima; no exact critical-point census for that tree is asserted. The verification is a same-model, reproducible arithmetic check, **not** independent validation or a formal theorem prover certification.
