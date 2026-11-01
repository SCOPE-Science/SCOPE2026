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

The accompanying `CHECK.py` uses SymPy 1.14.0 for exact symbolic arithmetic and assertions; the package declares this dependency in `requirements.txt`. It checks the quartic strict-dissipation identity, quartic radial drift, fourfold rotation, the perfect-square identity yielding the sharp threshold, the explicit high-coupling positivity witness, and the nondegenerate Hessian of the exhibited smooth Lyapunov function.

The proof separately establishes global existence and attraction from the proper strict quartic Lyapunov function. General necessity is proved by scaling a local Morse Hessian for the homogeneous vector field, and sufficiency adds a globally strict smooth converse Lyapunov function to a weak positive quadratic form. The external smooth converse GAS theorem is invoked, not independently reproved. Analytical arguments, rather than a finite checker run, quantify over all real couplings, states, and candidate smooth Morse Lyapunov functions.

No independent audit or formal external certification has been performed. Historical-priority coverage remains subject to expert comparison.
