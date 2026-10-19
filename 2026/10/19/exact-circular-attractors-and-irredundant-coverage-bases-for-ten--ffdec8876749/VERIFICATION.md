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

# Verification of the finite paperfolding circular-attractor certificate

Running `python3 verify_paperfolding.py` beside `paperfolding_certificates.json` reconstructs all factor occurrences and cyclic coverage masks literally from the original sequence rule. It verifies each of the ten upper witnesses, the full rational-weight inequality at every position, and the exact irredundant coverage-basis size. `verification_output.txt` records a completed run of this same code.

The largest stage contains \(868{,}847\) distinct circular factors and uses \(21\) nonzero dual-factor weights summing to \(51/8\) with positional load at most \(1\). Every listed finite result is certified by an exhaustive deterministic check, not by probabilistic hashing, sampled substrings, or extrapolation.

No formula for larger dyadic stages or exhaustive classification of all optimal position sets is established. Independent scientific audit has not been performed.
