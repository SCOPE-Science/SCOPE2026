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

# Verification and boundaries
Run `python3 verify.py` using Python 3 and NumPy. The script constructs exact-rational transition matrices, checks detailed balance and eigenspace eigenvalue identities, verifies the four-phase SLEM on finite test cases, compares against symmetric scalar candidates, then stress-tests asymmetric reversible matrices. A separate exact check tests the single Metropolis-optimal mass in sampled dimensions. The universal proof relies on spectral convexity, direct-sum eigenspaces and one-dimensional minimax monotonicity, not the tests. Independent audit has not been performed.
