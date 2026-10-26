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

# Verification notes

The mathematical proof verifies the claim for every allowed mesh size and timestep. The accompanying `verify.py` script constructs the scaled matrices with `fractions.Fraction`, inverts them by exact Gaussian elimination, and checks 48 finite instances. It confirms constant preservation in every checked instance, entrywise nonnegativity at the claimed safe timesteps, the strict negative displacement-two coefficient at selected rational timesteps below the threshold for mesh sizes four through ten, and nonnegativity for the three-node case. The script is a finite reproducibility check, not an exhaustive proof over all parameters.

No independent audit or external validation is claimed.
