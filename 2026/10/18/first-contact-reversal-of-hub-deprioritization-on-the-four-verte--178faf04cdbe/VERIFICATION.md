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

Run `python3 verify.py` using Python 3 standard library only. The program exactly constructs and inverts the substochastic six-pair neutral dual matrix on the connected four-vertex path and computes the periodic resolvent for each of six schedules. It independently reconstructs the complete neutral voter transition on all fourteen transient strategy configurations, calculates the selection-gradient per active edge directly and compares the two methods. The program asserts the six exact benefit and cost coefficients, all three rational thresholds, the signed derivatives at \(b=4,c=1\), and the endpoint-degree averages. The run terminated successfully with the final line `PASS: six exact periodic schedules, independent 6-pair and 14-state calculations`.

Finite exact matrix inversion is a complete certificate for this four-node transition problem once the stochastic-model reduction given in the proof is established; numerical simulation alone would not certify the derivative of infinite-time fixation. The program does not check arbitrary graph sizes, phase-randomized mutant introductions, nonperiodic schedules, or other updating rules. External independent validation has not been performed.
