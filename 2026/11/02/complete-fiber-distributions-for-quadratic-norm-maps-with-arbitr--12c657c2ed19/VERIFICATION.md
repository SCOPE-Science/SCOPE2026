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

# Verification of the finite-field norm-perturbation classification

Run `python3 verify.py` with Python 3 only. The checker implements \(\mathbb F_{p^2}\) as ordered pairs over \(\mathbb F_p\), using irreducible quadratic relations. For each \(p=2,3,5,7\) it enumerates all \(p^4\) matrices representing \(\mathbb F_p\)-linear maps, computes norm values by exponentiation, and tabulates every output multiplicity. The predicted two possible profiles are compared by direct assertions. The number of checked linear maps is \(3123\). This is finite verification only; the universal proof is given in `RESULT.md`. The source and assertion paths are wholly contained in this package.

No external or independent audit has been performed.
