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

# Reproducibility and verification

The self-contained `verify.py` uses the Python standard library. Run `python verify.py` and check its final `VERIFY_OK` line. Its search covers all gluing parameter tuples that could beat the explicit construction for \(2\le s\le6\); the search bounds follow from the Frobenius formula and inequality in the proof. It also computes Frobenius numbers by an independent numerical-semigroup closure procedure. These tests are finite cross-checks, not a proof for all \(s\). The general proof is the direct two-case inequality argument in `RESULT.md`. External independent validation has not been performed.
