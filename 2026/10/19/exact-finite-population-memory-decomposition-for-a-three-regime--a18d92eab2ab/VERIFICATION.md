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

# Verification record

Run `python verification/check.py` with Python 3 using the standard library only. The program constructs the precise joint count/environment continuous-time generator and solves each finite stationary system over exact rational numbers, then checks the theorem's environment cross covariance, stationary variance, positive correction coefficient, and first seven lag derivatives of the two-time covariance by generator powers. Thirty generators, 210 exact covariance-derivative identities, and all positivity tests passed when executed against the packaged code. The explicit finite tests are not exhaustive over parameters or \(N\); the all-size proof is in RESULT.md.

The three-state transition rates and voter rates were matched to the model definitions in Caligiuri and Galla, arXiv:2305.19096. The mathematical assessment is a self-review; independent audit has not been performed.
