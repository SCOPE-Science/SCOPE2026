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

# Reproducibility and proof scope

Execute `python3 verify.py` with Python 3 and no nonstandard packages. The script constructs prime-supported squarefree examples in integer bases \(2,3,5,8,10\), at fixed prime-factor counts \(7,6,6,5,5\). It verifies the primality of the selected factors, generates all \(2^r-1\) nonunit divisors, converts each divisor into its actual base-\(b\) digit string, verifies all pairwise prefix inequalities, and checks that a common initial-digit length separates all divisors. The output terminates in `VERIFY_OK` after all assertions pass.

## Noncomputational checks

The proof uses the rational-exponent valuation argument to exclude cylinder boundaries, continuity to obtain a uniform perturbation radius for finitely many subset products, unique factorization to count distinct integer products, and the prime number theorem in finitely many fixed intervals. The computer script tests examples only. It neither verifies the prime number theorem nor proves that the construction works for unbounded \(r\) or all integers \(b\); these universal claims rely on the fully written proof in `RESULT.md`.

## Limits

The theorem is for each *fixed* \(b\) and \(r\) as \(X\to\infty\); implied constants vary with them. It does not identify least examples, optimal density, or an asymptotic equivalent. Scientific priority remains subject to stronger unlocated literature. Independent audit has not been performed.
