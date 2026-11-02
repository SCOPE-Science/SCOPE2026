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

# Reproducibility

Run `python3 verify.py` with Python 3 and its standard library. The program exhaustively traverses the finite ternary support-last-letter state space and independently enumerates every ternary input word of length at most ten. It verifies the entire 328-set census, 315 persistent supports at length ten, exact first realization lengths, and the four-symbol obstruction. Its recorded output appears in `verification_output.txt`. These checks verify finite assertions; infinite exact-length persistence and the universal ternary Euler-trail theorem require the graph arguments in RESULT.md. No independent audit has been performed.
