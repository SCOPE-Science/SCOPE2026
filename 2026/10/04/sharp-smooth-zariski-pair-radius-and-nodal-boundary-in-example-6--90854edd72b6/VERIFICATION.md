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
# Verification

The embedded checker reconstructs the two cubics from Example 6.2, recomputes the singular-parameter elimination factors over the rationals, verifies the fixed-parameter singular points and Hessian determinants, checks the line and conic discriminants used for conditions (b) and (c), and verifies exact constant-term Rouché bounds on the circle of radius \(1/20\).

Run:

`python artifacts/verify.py`

Expected terminal line: `VERIFY_OK`.

The computation is finite exact algebra. It does not certify any claim about arrangement topology outside the stated centered disk or about literature completeness.
