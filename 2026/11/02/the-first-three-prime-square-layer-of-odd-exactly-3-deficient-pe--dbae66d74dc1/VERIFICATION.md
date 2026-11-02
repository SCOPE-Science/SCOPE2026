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

# Reproducible checks
Run `python3 VERIFY.py` with Python 3.8 or later. It performs exact rational bounding inequalities, full 26-signature quadratic enumeration for each of nine permitted smaller primes, trial-division primality checks, direct divisor-sum verification of the four witness triples, and exhaustive testing of the remaining \(5^2 7^2 11^2\) case.

Observed result:

`VERIFY_OK signatures=23400 positive_K=22620 square_discriminants=57 integral_roots=9 witness_triples=4 integers=3 excluded_p5_case=148225`

The proof's infinite exclusions are algebraic. The finite certificate covers every residual case because the polynomial equation has a unique positive root whenever its leading coefficient is positive. The script is ordinary reproducibility code, not a formal proof or an independent audit.
