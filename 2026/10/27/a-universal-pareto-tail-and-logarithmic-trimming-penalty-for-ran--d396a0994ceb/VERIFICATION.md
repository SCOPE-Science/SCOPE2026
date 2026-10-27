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

# Reproducibility checks and limits

`verify.py` uses only the Python standard library. Execute `python3 verify.py`. Its verified output is:

`VERIFY_OK rank-one residual rational identities=672, sharp-tail asymptotics and coarea constants=25, normalized core truncation=8`

The checks include exact-rational determinant and trace identities for \(2\times2\) matrices \(\operatorname{diag}(a,-b)\), numerical confirmation of explicit distributional tails, comparison of equivalent zero-level area formulas across dimensions, and independent angular quadrature for the exact trimming example. The proof of the universal asymptotics rests on the spherical coarea calculation in `RESULT.md`, not simulation. This verification does not cover generalized/singular matrices or independent scientific auditing.
