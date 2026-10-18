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

Run `python3 verify_dual_records.py` with standard Python 3. The script enumerates all permutations with sizes one through eight and constructs both record arrays from each permutation and its explicitly constructed inverse. It compares each joint probability to its closed expression using `fractions.Fraction`, checks each entry of the cross-covariance matrix, verifies off-diagonal Bernoulli independence, and verifies the total-count covariance. Four additional numerical tests check the stated second-order asymptotic within a cubic error envelope.

Observed result: `PASS: 656 exact-rational assertions and 4 numerical comparisons; exhaustive permutations through n=8`.

Limits: exhaustive enumeration through eight cannot certify arbitrary \(n\), and the asymptotic numerical checks do not constitute a limit proof. Both general statements follow instead from the independent conditional-prefix proof and uniform binomial bounds in `RESULT.md`. Scientific priority was compared against identified sources but not independently audited.
