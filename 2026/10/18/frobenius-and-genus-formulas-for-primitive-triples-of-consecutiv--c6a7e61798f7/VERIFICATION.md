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

# Computational checks and limits

Run `python3 verify.py` with Python 3 standard library. It reconstructs every normalized triple independently from exact binomial coefficients and verifies the six-case gcd and gluing decompositions for all indices from \(2\) through \(300\). It separately computes each Apéry set via shortest paths for \(2\le n\le160\) and checks exact Frobenius and genus against the claimed formula. `VERIFY_OK` indicates all these finite checks passed. The theorem for all \(n\ge2\) is proved in `RESULT.md`; these computations are diagnostic and do not independently certify infinite quantifiers.
