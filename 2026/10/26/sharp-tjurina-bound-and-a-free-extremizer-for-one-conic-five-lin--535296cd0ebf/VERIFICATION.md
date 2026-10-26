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
# Reproduction and scope

Run `python3 verify.py` using standard Python 3, without external packages. The script performs exact integer polynomial multiplication, differentiation, and comparison; confirms the two cubic Jacobian syzygies and \(\det=-147f\), conic smoothness by a nonzero Hessian determinant, tangent gradients at the listed points, and numerical incidence and Tjurina totals.

A successful run emits `VERIFY_OK`. The script does not prove the external published nonexistence result for maximizing degree-seven conic-line arrangements. That premise is Merta–Zieliński (2026), Proposition 3.2, arXiv:2610.16658v1; the local exhaustive intersection argument and all quantifiers for the new statement appear in RESULT.md. Numerical statements are exact identities over the integers, not floating-point experiments. Independently adjudicated priority and validity remain unperformed.
