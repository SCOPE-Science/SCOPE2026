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

# Verification

Run `python3 verify.py` with Python 3 and the standard library. The program enumerates every eligible positive pair for all integers below \(9^k\) for \(k=1,2,3,4\) and compares the resulting full representation function against the independently encoded base-nine pointwise identity. For \(k=5,6\), it checks the analytic digit-formula counts without brute-force enumeration of pairs. Output is preserved verbatim in `verification-output.txt` with final `CERTIFICATE_OK`.

This is exact finite computational corroboration. The unlimited-\(k\) theorem, the carry-state count and sharp exponent rely on the proof in RESULT.md, not on extrapolation. No separate external audit or independent validation has been performed.
