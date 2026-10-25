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
# Reproducibility and verification

The attached `verify.py` is standalone and uses exact rational arithmetic in the Python standard library. Executing `python3 verify.py` independently obtains the alternating cotangent sums through two polynomial Newton-sum recurrences, then checks the reduced denominator and normalized numerator congruence for each \(p\in\{5,7,11,13,17\}\).

Expected terminal certificate: `CERTIFICATE_OK prime_cases=5 exact_newton_methods=2`.

The proof in `RESULT.md` supplies the all-prime argument through cyclotomic root polynomials and the maximal logarithmic coefficient. This computation samples five primes only, cannot establish an infinite theorem, and is not an independent mathematical audit.
