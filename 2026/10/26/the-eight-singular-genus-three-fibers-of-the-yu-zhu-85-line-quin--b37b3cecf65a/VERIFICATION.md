---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The unchanged `verify_genus3_fibers.py` is an optional exact replay in Python 3 with SymPy. It checks the coefficient identities for the binary quartic, its discriminant, the square identity used at the primitive cube roots, the specializations at zero, infinity, and one, and the Euler-characteristic arithmetic. It uses `c = r*(1-t*r**3)`, consistent with the coordinate `r=a/b`; the finite line-star parameters are obtained by solving `c=0` and are `r=0` and `r**3=1/t`. The script is not by itself a classification of quartic singularities. The uniform argument in `RESULT.md` derives the zero sets, verifies exhaustiveness and reducedness, and identifies the analytic types at all singular points.
