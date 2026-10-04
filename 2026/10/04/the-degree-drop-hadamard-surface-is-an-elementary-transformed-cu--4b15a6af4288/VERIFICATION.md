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

Run `python verify_example42.py` with SymPy available. The script checks the three polynomial identities from the source parametrization, the unique projective base point on the four standard source charts, projective smoothness by Gröbner tests for the Jacobian-rank-drop ideal on all five target coordinate charts, the affine birational normal form, the local blow-up sections, the contracted fiber, and the directrix source divisor. A successful replay prints `VERIFY_OK`.

The computation proves the exact coordinate claims used in the proof. The identification of the determinantal surface with the standard rational normal cubic scroll uses the classical theory of \(2\times3\) determinantal scrolls. No independent external audit has been performed.
