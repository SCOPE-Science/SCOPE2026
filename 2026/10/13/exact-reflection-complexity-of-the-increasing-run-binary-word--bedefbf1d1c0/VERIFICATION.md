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

## Reproducibility
Run `python3 verify_run_reflection.py` using Python 3 without external libraries. The expected output is `VERIFY_OK n=1..140 exact-factors/reversal-orbits n=1..85 right-special-sets n=1..1000 arithmetic-identity`. The code generates progressively increasing 0- and 1-runs and enumerates exact factors/reversal classes; checks predicted right-special factors and arithmetic-pair formulas. The finite enumeration does not establish the theorem for unbounded n; the proof in RESULT.md is the all-length certificate.

## Scientific and priority limits
The word is nonrecurrent, aperiodic and not reversal-closed. The unqualified original conjecture was already refuted by a periodic example in the 2026 paper, so this is an aperiodic strengthening and exact formula, not the first literal disproof. No outside independent audit or proof certification has taken place.
