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
# Verification of the dyadic Delannoy shift theorem

Run `python3 delannoy_period_verifier.py` using a standard Python installation. This is a finite independent reconstruction of the sequence via its integer three-term recurrence, not a replacement for the symbolic proof. The expected successful diagnostic is:

```
VERIFY_OK independent_binomial_crosschecks= 161 dyadic_phase_checks= 197504 sharp_valuation_checks= 98688 period_entries= 1027 shorter_period_exclusions= 1016 highest_modulus= 2048
```

The script checks the first 161 binomial identities, 197504 shift congruences with all shifts divisible by four through 512 and all eligible indices below 1801, 98688 cases with exact valuation, and all least-period claims modulo powers of two through 2048, excluding every smaller candidate shift on a complete interval for each tested modulus. The unrestricted conclusion rests on the finite-term Vandermonde expansion, its valuation bounds, the exceptional two-term cancellation modulo 32, and the period-gcd argument. The independent mathematical audit remains unperformed.
