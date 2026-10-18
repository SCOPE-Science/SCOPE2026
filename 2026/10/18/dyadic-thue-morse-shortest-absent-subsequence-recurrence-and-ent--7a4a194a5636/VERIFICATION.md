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

# Verification notes
Run `python3 verify.py`. Its direct matrix multiplication checks \(m=1\) through \(9\). Its independent direct membership enumeration checks \(m=1\) through \(5\), and its distinct-subsequence dynamic programming checks \(m=1\) through \(9\), against the recurrence. Every source word in the checked range is generated from parity of binary digit sum, not from a precomputed data table. The enumerations are finite confirmations only; the infinite statement is justified in the proof in `RESULT.md`. No independent mathematical audit has been performed.
