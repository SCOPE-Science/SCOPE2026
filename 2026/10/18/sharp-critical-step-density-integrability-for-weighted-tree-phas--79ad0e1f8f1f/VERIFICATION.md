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

# Reproducibility and limits

Run `python verify.py` from the folder containing this file (requires Python, NumPy and SymPy). The checker was executed and reported `PASS: 488 exact symbolic identities and finite numerical checks; dimensions 1,2,3,4,5,8.` It verifies an exact symbolic two-edge determinant identity, its Hessian coefficient and the explicit critical constant; then it tests quadratic determinant scaling across 24 differently weighted tree instances with 20 directions each and a separate anisotropic angular integral. The script is self-contained apart from the two named numerical/symbolic Python dependencies.

The theorem for arbitrary finite trees and the sharp all-dimension exponent follow from the analytical arguments in `RESULT.md`, not from this finite test. No independent audit or external validation has been performed. The priority comparison remains susceptible to unindexed mathematical literature.
