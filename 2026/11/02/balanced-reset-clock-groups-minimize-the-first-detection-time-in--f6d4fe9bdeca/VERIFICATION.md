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

# Reproduction and proof limits

Run `python3 verify.py` from the package directory. The check script uses only Python standard-library modules. It verifies 42 exact rational moment-transfer identities across three two-point clock-survival laws, then computes Brownian moment renewal equations with trapezoidal convolution and tests 28 strict ordering assertions at four observation times. The measured strict inequalities support numerical consistency with the theorem.

Analytic correctness is instead based on: conditional independent excursions; positivity of exact symmetrized transfer and splitting kernels for all \(t\ge0\); the finite balancing algorithm; and strict nondegeneracy of the Brownian–Poisson conditional survival for every \(t>0\). The numerical grid does not quantify global discretization error or prove all-time strictness. No independent audit or physical-data validation has been performed.
