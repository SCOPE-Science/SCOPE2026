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

# Reproducibility and proof checks

Execute `python3 verify.py` using the standalone standard-library script. The actual run returned `PASS: 199 local unit-root counts; 22 exact mean/variance checks`. The local tests include both negative and positive discriminants and the reducible quadratic \((U+V)(U+2V)\).

The mathematical proof separately establishes the exact root count at every eligible odd prime, CRT independence, centered mean and variance formulas, bounded exceptional primes, the fixed-modulus prime equidistribution step, and the growth balance that makes representations with an early shift negligible. Only these arguments prove the infinite statement. Computation cannot certify global source priority, asymptotic prime equidistribution, or independent validation.

No claims are made beyond the stated fixed \(r\), coercive nondegenerate \(F\), divisibility chain, reciprocal-divisor divergence, and growth hypotheses. In particular, the borderline exponent is not asserted optimal.
