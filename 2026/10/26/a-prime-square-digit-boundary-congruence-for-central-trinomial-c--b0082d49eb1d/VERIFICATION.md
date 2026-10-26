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
# Verification of the prime-square digit-boundary congruence

The analytic argument starts from the integral quotient of cubic cyclotomic polynomials and uses no numerical step. The formal support bound prevents nonzero multiples of the prime from entering the constant-term coefficient. It is valid for every prime at least five and all positive multipliers.

The accompanying Python 3 file `verify.py` uses an exact integer recurrence for central trinomial coefficients and verifies both forms of the theorem for 12 primes and 31 multipliers per prime (372 parameter pairs). It additionally verifies the stated prime-power specialization whenever the index lies within the computed range. Reproduce by executing `python3 verify.py` in the same directory; the expected output is `VERIFY_OK`.

These computations are finite consistency checks, not proofs for every prime and multiplier. The explicit formula relies on the established Cao–Sun congruence for the base index. No independent mathematical audit or independent validation has been performed.
