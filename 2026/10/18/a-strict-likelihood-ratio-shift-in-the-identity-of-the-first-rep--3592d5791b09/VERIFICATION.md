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

# Verification scope

The analytic argument counts first-repeat paths and invokes Newton's strict elementary-symmetric inequalities for a positive alphabet. `verify_first_repeat.py` independently enumerates all length-bounded sample words for 16 exact-rational vectors of lengths two through five, checking each conditioned joint mass, both endpoint posteriors, all pairwise odds, and the conditional mean direction. Running `python verify_first_repeat.py` produced a PASS report for 84,056 enumerated sample words.

Finite enumeration is not exhaustive over arbitrary probabilities or arbitrary alphabet sizes. No external independent mathematical audit has been performed. The theorem's infinite-parameter generality rests on the written proof, not on this script.
