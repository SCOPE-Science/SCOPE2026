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

# Verification evidence

Execute `python3 verify_rounding.py` using Python 3 with no external dependencies. The script enumerates exact rational probabilities of all four row patterns using multinomial weights for seven choices of rounding probability, several feasible within-row couplings, and each dimension from 2 to 8. All 210 cases match the inclusion-exclusion expression exactly. It also confirms the exact success probabilities for the rank-optimal and conditioning-optimal schemes and the independent-entry comparison. Output is stored in `verification_output.txt`. The sharp optimization for all real probabilities and the almost-sure singular-value limits are proved mathematically in `RESULT.md`; the script cannot certify those infinite claims by finite checking. No independent audit has been performed.
