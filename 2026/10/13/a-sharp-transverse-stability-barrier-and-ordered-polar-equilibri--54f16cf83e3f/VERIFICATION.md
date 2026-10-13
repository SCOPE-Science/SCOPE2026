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

Run `python verify.py` from the directory containing the source files. SymPy is required. A successful run prints `VERIFY_OK`.

The checker uses exact symbolic expansion and simplification to compare the original mean-field equations with the shifted cubic field, verifies all branch and eigenvalue identities, checks the quadratic center-manifold coefficient and destabilizing cubic term at the critical parameter, and compares two explicit rational parameter points. The stable and saddle conclusions for arbitrary parameters follow from the displayed algebraic signs and strict inequalities in RESULT.md; the checker alone does not prove the universal claim.

The one-sided confidence boundary, the absence of further interacting equilibria, and the distinction between local and global dynamics are argued analytically in RESULT.md. No computation is treated as an exhaustive survey of all real parameters. External independent scientific verification has not been performed.
