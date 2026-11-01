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

# Reproducible verification

Execute `python3 verify_crown_cca3.py`; no external modules are needed. The checker computes the exact transition from each of 19,683 saturated paired-color profiles and tracks representatives of every initially occupied pair type. Assertions establish the full period/preperiod count arrays, exceptional profiles' exact multiplicities and immediate recurrence, as well as repetitively realizable witness signatures for all larger sizes. Independently, the checker implements literal graph neighbors (excluding each deleted matched partner) and enumerates all 597,870 labelled states for shore sizes 1 through 6, asserting agreement of exact preperiod and least period for each state. The recording is in `verification_output.txt` and should end `CROWN_CCA3_VERIFY_OK`.

The finite enumeration rigorously suffices for arbitrary graph sizes only together with the mathematical proof that the nine-entry saturation and the transported initial type representatives constitute an exact deterministic factor. Direct enumeration of graphs through size six alone would not prove the infinite classification. Independent audit: not performed.
