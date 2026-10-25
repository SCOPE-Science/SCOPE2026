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
The attached finite verifier exhaustively enumerates all graph homomorphisms for each of six small instances and builds the reconfiguration graph. It constructs explicit cycles from a short path to a two-step target rotation and repeats the path through its full rotation orbit. Tracking signed \(\pm2\) evaluation changes before and after target-color reduction verifies the predicted integer degrees and branch coefficients in cases \((m,n,k)=(4,5,2),(4,6,2),(4,5,3),(4,5,4),(6,5,2),(6,6,2)\).

The all-parameter coefficient is mathematically certified by the published cubical deck period and the evaluation commutative diagram, rather than by enumerative evidence. The classification of circle sectors uses the independent published cycle-to-cycle component theorem. The associated Smith statement is verified algebraically block by block. An independent audit was not performed.
