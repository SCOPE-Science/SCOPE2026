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
# Verification of the terminal law

The embedded file `verify_adsorption.py` runs using only Python 3.10+ standard-library packages. Command: `python3 verify_adsorption.py`. It passed 622 grouped exact-rational and gamma-product assertions. A separate direct enumeration of all labeled triple choices confirms the reduced two-class chain at initial class sizes one through seven; grid checks confirm its conditional rates at 289 two-class states, and gamma products are independently recomputed.

These calculations corroborate the finite transition algebra, not the weak convergence theorem. The latter depends on the explicit normalization, martingale central limit estimate, uniform boundary-layer control, and terminal hitting identity in RESULT.md. No computer experiment was used as an infinite proof. The theorem covers balanced classes and equal allowed-trimer attempt rates only. Independent validation has not been performed.
