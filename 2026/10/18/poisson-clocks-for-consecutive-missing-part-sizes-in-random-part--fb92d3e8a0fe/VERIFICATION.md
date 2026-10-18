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

Run `python3 verify.py` from the folder containing the supplied file. The script uses only Python's standard library. Actual execution passed 754 exact comparisons of forbidden-block partition counts against inclusion-exclusion coefficients for \(0\le N\le28\), checking run lengths 2 and 3, overlapping and nonoverlapping pairs, and cumulative marked-start counts. It also confirmed decreasing mean-approximation errors and overlapping-pair terms for run lengths 2, 3, 4 in the independent geometric model at parameters \(N=10^8\) and \(N=10^{12}\).

The exact finite identity derives from multiplying the generating series for unrestricted partitions by \(\prod_{j\in S}(1-z^j)\). The asymptotic conclusion instead requires DeSalvo--Menz Theorem 4.14 and the factorial-moment cluster proof; the program cannot check those infinite statements. No automated formal proof or independent external audit is claimed.
