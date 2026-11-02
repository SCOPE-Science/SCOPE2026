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

Run `python3 verify_involution_rank.py` using Python 3.8 or newer; it uses only the standard library. The program enumerates every three-level strict radical matrix for the listed small field sizes, checks \(X^2=0\) directly, computes the ordinary matrix rank independently, and compares its rank histogram with the formula. It reports `THREE_LEVEL_INCIDENCE_INVOLUTION_RANK_OK 12` if all twelve configurations pass. All values in the explicit tested examples are exact integers; the code enumerates prime fields only. The algebraic argument in `RESULT.md`, not a finite computational extrapolation, covers arbitrary finite fields of characteristic two and proves the max-rank boundary. No independent audit has been performed.
