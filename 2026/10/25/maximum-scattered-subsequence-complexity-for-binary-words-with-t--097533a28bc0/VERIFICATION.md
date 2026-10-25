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

Run `python3 check.py` from the directory containing the supplied artifact. The implementation requires only Python's standard library. It tests the distinct-scattered-subsequence dynamic recurrence against the closed gap formula on **73,815** quadruples with total zero count at most 34. For 330 quadruples with at most seven zeros, it also constructs distinct subsequence sets directly. It verifies every global maximum and every maximizing quadruple in those 35 complete parameter slices, not a sample. In addition, the four algebraic difference-sign rules are checked on a finite grid with first balanced-pair parameter 0–49 and second 1–59.

Observed result: `OK; quadruples checked: 73815 direct set enumerations: 330 maximum m=34: 11780 maximizers: [(8, 9, 9, 8)]`.

The finite program is a corroborating implementation. Infinite validity depends on the recurrence identity, algebraic factorization, and explicit sign comparison in RESULT.md. The script does not establish literary priority or replace independent human mathematical validation.
