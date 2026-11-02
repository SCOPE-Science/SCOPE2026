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
# Reproducibility

Run `python3 verify.py` with Python 3 standard library. The script computes first-zero ranks directly modulo each prime power and checks the exact theoretical frequencies. It ran successfully for 21 prime/exponent combinations with 7,129 fully enumerated coefficients: primes \(5,7,11,13,17,19,23,29\); maximum exponents respectively \(4,3,3,3,2,2,2,2\). Every observed frequency and the characterization of the maximum-rank locus agreed.

The all-level proof is symbolic and does not depend on extrapolating finite computations. Its indispensable steps are: integer-polynomial composition; valuation increase for \(s\equiv\pm2\pmod p\); cyclicity and cardinality of split/non-split norm-one groups for \(p\ge5\); and Hensel uniqueness for distinct roots. The verifier does not constitute independent mathematical validation.
