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

# Verification details

Run `python3 check_energy.py` with the Python standard library; expected output begins with `CHECK_OK`.

This script recomputes all spherical Wick pairings through total degree six using exact rational polynomial arithmetic, compares coefficients of the invariant formula, verifies the shift to the barycentric deficit, and independently evaluates the equilateral spinor beta integral. Successful execution was observed on the packaged script before delivery.

The analytic inequalities \(Q\le6t-t^2\) and \(|abc|\le Q/2\) hold for every triple of unit vectors and are proved in RESULT.md. The script is a check of the algebraic identities, not a substitute for the infinite-family argument and not an independent mathematical audit.

Relevant primary literature: Hedenmalm–Xie, arXiv:2610.15004v1, Sections 6.2–6.5 and Problem 6.23. Historical-priority uncertainty remains for inaccessible or unindexed literature.
