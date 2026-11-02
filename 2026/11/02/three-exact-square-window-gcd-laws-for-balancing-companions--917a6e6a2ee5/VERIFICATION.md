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

The included `balancing_square_gcd_checker.py` uses Python 3 and exact arbitrary-precision integers; run `python balancing_square_gcd_checker.py` in the directory containing this file. Its script parameter defaults check \(k=1,\ldots,300\), three sequences, and \(25\) consecutive windows each.

The observed output was:

`PASS: 300 lengths x 3 sequences x 25 windows; sum identities and difference-gcd reductions confirmed.`

The script checks the sequence recurrences, \(C_n^2-8B_n^2=1\), initial square sums, differences, and the proposed formulas. The manuscript proves all positive lengths and all nonnegative window starts by exact strong divisibility and prime valuations; the finite experiment is not used as an infinite proof.

Limitations: \(D_b(k)\), the square-window GCD of the nonhomogeneous cobalancing sequence, remains outside the theorem. The related index-GCD \(\gcd(k,B_k)\) is not further factored. Independent validation is not performed.
