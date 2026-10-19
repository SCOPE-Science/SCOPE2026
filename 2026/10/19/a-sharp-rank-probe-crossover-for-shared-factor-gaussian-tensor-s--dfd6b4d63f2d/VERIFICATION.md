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

# Verification notes

The full proof is in `RESULT.md`. The reproducibility file `checks.py` uses SciPy for finite-dimensional one-dimensional integration against two independent chi-square densities, checks four exact isotropic constants, and confirms the closed Bessel integral for the critical two-rank case. The checker does not claim to establish convergence of asymptotic ratios or reproduce a full arbitrary-spectrum analytic proof. A deterministic SVD, Gaussian conditioning, the product small-ball lemma, and the conditional strong law prove the complete claim independently of finite numerical tests.

All calculations assume a fixed nonzero **real** matrix with exact independent standard Gaussian sampling as stated. Independent validation has not been performed.
