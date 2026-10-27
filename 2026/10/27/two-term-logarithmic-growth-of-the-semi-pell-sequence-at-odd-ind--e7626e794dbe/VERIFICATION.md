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

# Reproduction of mathematical checks

The published defining recurrence is \(s(0)=0\), \(s(1)=1\), \(s(2t)=s(t)\), and \(s(2t+1)=2s(2t)+s(2t-1)\) for \(t\ge1\). The separate routine `overpartition_table` computes the coefficient count of marked odd-multiplicity binary partitions without invoking this recurrence. The executable compares all 513 coefficients at weights 0 through 512 and checks odd-index monotonicity over this range. For \(8\le k\le19\), it evaluates the explicit injection count and verifies it is at most \(s(2^k-1)\), and it verifies a coarse bound on the opposite side.

Run `python3 semi_pell_growth_verify.py` under Python 3.8+ with no third-party dependencies. The observed run completed without assertion failures and printed the endpoint statistics for all twelve exponents.

These tests do not prove the existence of a logarithmic asymptotic or certify any untested infinite range. The unrestricted estimates are established by the direct counting, elementary generating-function inequalities, and monotonicity argument in `RESULT.md`. The absolute implied constant in \(O(\log n)\) is not explicitly optimized. No independent audit was conducted.
