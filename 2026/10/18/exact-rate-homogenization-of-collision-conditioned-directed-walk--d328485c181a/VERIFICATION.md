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

The accompanying `verify.py` is a finite numerical and exact-state-space diagnostic for the independently proved identities. Run `python verify.py` with Python 3 and NumPy installed. It reconstructs the killed Markov generators from their definitions, checks both left and right principal eigenvector equations, and evaluates every legal jump of the transformed process. The state spaces exhaust all cyclically ordered labeled configurations in the tested dimensions, but only finitely many dimensions and rate profiles are tested. The script additionally confirms the rate-independent stationary distribution and rate-dependent quasi-stationary normalization in the two-particle case. All infinite and arbitrary-parameter claims are supported by the analytical determinant and similarity proof, not by extrapolation from the tests. No independent audit has been performed.
