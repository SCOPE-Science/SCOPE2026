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

The supplied `verify.py` uses only Python's standard library. Run `python3 verify.py` after extracting that file. The printed success line is

`VERIFY_OK hosts=8190 rational_sources=4 exact_three_way_comparisons=52 n=0..12 degenerate_boundaries=TRUE`

The script builds true distinct scattered-subsequence **sets** for every binary host of lengths \(1\) through \(12\); it then verifies the count by comparing the two halves' Parikh vectors. It independently computes the expected count for \(p=1/2,1/3,2/5,1/5\) from a pattern-first sum of geometric waiting-time tails. A third computation obtains coefficients through degree \(12\) from the algebraic square-root identity. Rational equality is exact; no approximate floating-point agreement is substituted. Both deterministic endpoint values are checked separately.

The infinite asymptotic assertions require, beyond these checks, the proof that \(S(z)=g_0(z)+g_1(z)\) has a unique positive root of \(S(r)=1\), that its derivative satisfies \(rS'(r)=2(1+t)/(1+2t)\), and that no other singularity lies on \(|z|=r\). These are established analytically in `RESULT.md`. No independent audit, external certificate, or proof-assistant check has been performed.
