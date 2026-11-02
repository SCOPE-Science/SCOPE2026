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

The standalone `verify_wiman7.py` was executed with exact symbolic arithmetic in \(\mathbb F_7[t]\). It reconstructed the full Cartier coefficient matrix, preserved the nodal-adjoint subspace, checked \(\det K=D^3\), the twelve simple roots, the exact rank-at-root off-diagonal certificate, and the parameter exclusions via exact discriminants/resultants. Execution ended with `VERIFY_OK`.

The geometric identification of the normalization, irreducibility via distinct Kummer-square classes, and Cartier-formula interpretation are justified in RESULT.md rather than being asserted on the strength of program output alone. Nothing here is an independent audit.
