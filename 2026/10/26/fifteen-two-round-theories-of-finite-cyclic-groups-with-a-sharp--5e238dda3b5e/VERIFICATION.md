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

# Reproducibility and limits

Execute `python3 verify.py` using the standard Python library. The program independently enumerates every atomic ternary-addition diagram and the mathematically reduced eight-bit diagrams for orders through 64, computes exact two-round EF invariants for all orders through 128, checks the 15 predicted classes and the seven explicit distinguishing formulas, and compares ten larger sampled cyclic groups against their proposed representatives.

Recorded output appears in `VERIFY_OUTPUT.txt`. A zero exit status and `VERIFY_OK` verify these **finite** assertions only. The theorem for arbitrary positive group orders additionally requires the uniform profile lemma and its all-orders case analysis in `RESULT.md`. The scripts do not establish originality or independent certification. Human rechecking of the lemma and literature comparisons remains appropriate.
