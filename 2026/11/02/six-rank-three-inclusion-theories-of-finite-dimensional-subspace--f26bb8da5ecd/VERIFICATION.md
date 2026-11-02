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

# Computational verification

Run `python3 verify_pair_extensions.py` and `python3 verify_full_types.py` from this directory; both use only Python 3 standard libraries. The recorded outputs `pair_checks.txt` and `full_types_checks.txt` were obtained by actual execution. The former checks symbolic pair-extension signatures against explicit subspaces for binary ambient dimensions 1–7 and ternary dimensions 1–5, checks analytic truncation of root profiles through dimension 40, and computes the 2825-subspace representative. The latter independently builds subspace sets by closure and computes nested rank-three first-order types, for binary dimensions 1–5 and ternary dimensions 1–4. Both end in a `VERIFY_*_PASS` line. Enumeration is finite and cannot itself establish the all-field, all-dimension theorem; the infinite deduction is in RESULT.md.
