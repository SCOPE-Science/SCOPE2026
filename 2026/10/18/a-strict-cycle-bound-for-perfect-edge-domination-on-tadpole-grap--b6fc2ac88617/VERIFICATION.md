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

Run `python3 verify.py` from the directory containing this document. The program requires only the Python standard library and needs no network access or external input. It checks the full six-state transfer matrix, its exact polynomial identity, the nine initial counts and deficits, two recurrence regimes, and exhaustive edge-subset counts in explicitly limited cases. A successful run prints `VERIFIED: matrix identity, 9 exact seeds, edge-subset replay, recurrences, strict inequalities.`

The script's finite enumerations are **not** claimed to prove the infinite result. The proof of all parameters uses the exact matrix identity, the local-color bijection, a reversible pendant-extension decomposition and double induction, as given in `RESULT.md`. No independent review, formal proof assistant, or external certification was performed.
