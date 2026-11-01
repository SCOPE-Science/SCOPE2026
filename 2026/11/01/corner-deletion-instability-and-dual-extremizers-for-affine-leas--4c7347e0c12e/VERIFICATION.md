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

# Reproducible exact checks

Execute `python3 verify.py` from this directory using a standard Python 3 installation. The program uses only the standard library. It constructs the exact rational hat-kernel rows from the analytic Gram-inverse formula for dimensions \(2\) through \(10\), tests 1,394,017 kernel entries for nonnegative sign products and checks all row sums, then evaluates every Hamming orbit through dimension \(100\) and confirms that the stated closed form is the exact maximum. In dimensions \(2\) through \(10\), 63 endpoint rows also attain the exact constant.

Separate exact symbolic linear-algebra calculations in dimensions \(2\) through \(6\) directly compared the hat matrix \(F(F^{\mathsf T}F)^{-1}F^{\mathsf T}\) against the formula and checked idempotence; all passed. The expected exact values for dimensions \(2,3,4\) are \(1\), \(7/4\), and \(21/11\). The attached checker reproduces the principal combinatorial and row-norm checks.

Finite tests do not prove the all-dimensional theorem. The universal sign argument, binomial sign identity, zero-shell bound, and endpoint localization are established in RESULT.md. No independent scientific validation has been performed.
