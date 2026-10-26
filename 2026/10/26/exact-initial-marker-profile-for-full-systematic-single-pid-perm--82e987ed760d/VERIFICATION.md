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

# Reproduction and limits

Execute `python3 VERIFY.py` with any Python 3 interpreter. The standard-library checker reconstructs every deletion shadow after independently ranking the remaining symbols, verifies all source messages occur exactly once in each four listed codebooks, verifies every output is unique to its parent, and tests the mathematical singleton-shadow lemma exhaustively through length seven. The output in `VERIFY.txt` is the recorded result. The two nontrivial codebooks occupy 16 distinct received words at length four and 97 at length five. The no-marker and one-marker lower bounds are separate analytic counting arguments; finite enumeration cannot establish the general lower bound on its own. The proof and witnesses cover only the declared small message lengths; no independent mathematical audit has been conducted.
