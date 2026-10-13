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

The proof is symbolic. The checker evaluates the exact exponent-vector discrepancy
\[
\sum_i\left(\gcd(k,\alpha_i)-\log_2(\alpha_i+1)\right)
\]
on bounded samples only as regression evidence.

For \(k=1\), it checks every exponent tuple of lengths \(1\) through \(4\) with each exponent from \(1\) through \(10\), verifying nonpositivity and verifying that equality occurs exactly when all exponents are \(1\).

For each \(2\le k\le40\), it chooses a prime divisor \(r\mid k\) and checks the positive witness coefficient \(r-\log_2(r+1)>0\) through \(t=30\), and checks the negative prime-power witness
\[
1-\log_2(kt+2)<0
\]
through the same range.

These finite checks do not prove unboundedness. The infinite proof is the explicit symbolic construction in RESULT.md.
