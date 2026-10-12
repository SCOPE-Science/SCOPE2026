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

Run `python verify.py` after installing `sympy` from `requirements.txt`. The script recomputes the specified integer matrix determinant and row Gram matrix, derives all three hard-row projected norm weights and correlations, and constructs the two rank-one residual projectors independently as rational \(3\times3\) matrices. It checks their idempotence and composition identities, forms the exact expectation operators for one and two independent sampled steps, checks characteristic traces and determinants, verifies the Perron equations, and proves disjoint rational enclosures for the nine reported positive algebraic quantities. A successful execution prints `VERIFY_OK`.

The code is exact on this integer example. The universal two-row formulas, asymptotic Perron limit, dimension minimality, and perturbative openness are proved in `RESULT.md`, rather than inferred from a finite test. No external independent audit has been performed.
