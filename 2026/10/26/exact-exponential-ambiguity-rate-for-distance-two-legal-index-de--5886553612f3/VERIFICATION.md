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

Execute `python3 verify.py` in the directory containing this file. The script uses only the Python standard library. It independently builds terms by the defining least-missing-positive rule through index \(16\); enumerates admissible index subsets through index \(17\); compares Fibonacci-product counts; verifies \(\sum_{i=1}^{n-3}a_i=a_n-4\); and checks exact mean-count cutoffs. The expected console output begins with `VERIFIED:`.

# Proof status and limits

The unbounded conclusion is established by the written parity-path counting argument, the recurrence-derived prefix identity, and a normalized-root convex-combination inequality. Enumeration through index \(17\) is a finite consistency check only. The sequence recurrence is a published premise from arXiv:2210.10577, Proposition 2.3. No independent external mathematical validation has been performed.
