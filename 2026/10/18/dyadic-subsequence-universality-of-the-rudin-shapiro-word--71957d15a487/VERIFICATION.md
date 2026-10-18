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

Run `python3 verify.py` with Python 3.10 or newer. The program generates the binary Rudin–Shapiro word by two independent mechanisms, compares small scattered-subsequence languages directly with the greedy arch algorithm, checks all three incoming states of every substitution-block transfer at levels four through eleven, and compares the formula and global discrepancy bound with direct prefix scans.

Expected terminal signal: `VERIFY_OK`. The checker is finite, while the infinite statements are proved by transfer induction and binary prefix decomposition in `RESULT.md`. No independent scientific audit or machine-checked infinite proof is asserted.
