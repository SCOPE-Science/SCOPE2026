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

Run `python CHECK.py` with standard Python 3. The exact-arithmetic checker independently enumerates every casting subset for every voter and profile and separately evaluates the nonrepeating-delegation-path formula. It enumerates every unilateral deviation and welfare outcome for 83 rational parameter pairs including all three algebraic thresholds and adjoining intervals. Replayed output from the packaged files:

`VERIFY_OK exact_parameter_cases= 83 event_level_payoffs= 6723 profile_deviation_checks= 13446`

This verifier is an algebraic consistency and boundary test, not a proof for all real participation probabilities and tolerances. The real-parameter proof is the symbolic 15-class analysis in RESULT.md. Public status records self-review only. No independent audit has been performed.
