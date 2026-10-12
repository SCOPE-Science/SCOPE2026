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
# Exact-rational verification

Run `python3 verify.py` using a standard Python 3 interpreter from the directory containing the embedded files. The checker computes the two iterates with `fractions.Fraction` and tests every smaller reduced numerator, rather than merely comparing a formula against a second copy of the same formula. It also tests very large prime powers at their predicted minimizers and checks the complete quotient-exclusion inequality for bounded ranges.

Observed output in `VERIFY.stdout` is:

`VERIFY_OK exhaustive_prime_powers=43 rejected_smaller_coprime_numerators=583945 large_power_candidate_checks=377`

The analytic proof in `RESULT.md` establishes the theorem for all primes and exponents. These finite tests are neither a complete enumeration of arbitrary parameters nor an independent audit. The existing denominator-two case is acknowledged as previously known.
