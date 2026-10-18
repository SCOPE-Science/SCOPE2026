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

# Reproduction and limits

Run `python3 verify.py` from the same directory as this file; Python 3 standard library is sufficient. The script computes coefficients of \(A(x)^{t^2}\) and \(A(x^t)^t\) using exact logarithmic-derivative recurrences and compares selected coefficients with a second, direct finite-Euler-product algorithm. Since \(A(x)\) has constant term \(1\) and integral formal inverse, the content and first obstruction indices of these numerator coefficients equal those for \(F_{t^2}-C_t\).

The test instances comprise 16 distinct prime powers and 26 integers with more than one distinct prime factor. For prime powers the script checks full divisibility by \(p^{a+1}\), the first failure residue modulo \(p^{a+2}\), and the resulting gcd of computed coefficients. For composite multi-prime parameters it checks the first failure modulo each prime divisor, as well as the gcd of the finite prefix. The second method compares 460 directly expanded numerator-product coefficients. The saved `certificate_output.txt` records all tested parameters and a PASS summary.

The certificate is finite, not a proof of coefficientwise congruence for all \(n\). The infinite theorem is proved in `RESULT.md` through formal Frobenius, exact binomial valuation, coefficient isolation, and invertibility of the Euler product. The novelty assessment has not been independently audited.
