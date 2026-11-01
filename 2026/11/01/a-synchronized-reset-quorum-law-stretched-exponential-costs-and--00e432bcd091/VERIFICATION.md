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

# Reproduction and verification

Run `python3 verify.py` with Python 3.9 or later. The program requires only the Python standard library and conducts deterministic midpoint quadratures of the independent Brownian first-passage transform and the limiting Fréchet law. Checks include the exact \(N=1\) Brownian transform, equivalence of two independent integral representations of the scaled-law transform, finite-population convergence of quorum success probability and mean, and finite-population agreement of the logarithmic fixed-reset exponent.

Scientific verification is analytic: the exact finite-state-free renewal identity, Brownian reflection formula, uniform \(\operatorname{erfc}\) upper bound, fixed-clock Laplace principle, Fréchet maximum limit, and compactness barriers for rescaled global optimizers are all supplied in `RESULT.md`. Finite samples, quadrature and numerical approximations are consistency checks only and do not prove infinite-population statements. No formal proof assistant or external certification was used, and no independent audit was performed. The limiting objective's minimizer is proven to exist, but its uniqueness and numerical position are not certified.
