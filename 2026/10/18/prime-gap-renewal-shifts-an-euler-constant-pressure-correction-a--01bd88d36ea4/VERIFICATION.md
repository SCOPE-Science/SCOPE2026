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
# Reproducibility and limitations

Run `python3 verify.py` with Python 3.9 or later (standard library only). The verifier sieves primes through two million, independently evaluates the prime-gap partition root by bisection, checks three pressure and gap-mean comparisons, checks nine corrected Palm distribution values, and enumerates small marker words independently of their renewal-composition recurrence. A successful run prints `VERIFY_OK`.

All finite-prime truncations are numerical checks. They neither constitute an exact prime-number-theorem certificate nor prove infinite-point-process convergence. The proof's universal steps use the established effective prime number theorem, Kac and Abramov induction, relative entropy, and stationary renewal convergence. The output is analytical and self-reviewed; independent mathematical audit has not been performed.
