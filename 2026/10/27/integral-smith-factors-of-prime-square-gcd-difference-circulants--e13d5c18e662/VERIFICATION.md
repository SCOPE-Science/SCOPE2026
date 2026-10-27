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
# Exact reproducibility and limits

Run `python3 verify.py` from the extracted package. The checker uses no external packages and reports:

```text
VERIFY_OK exhaustive_full_SNF p=2,3; exact_core_SNF 10 primes; factor_chains_and_determinants 10 primes
```

It enumerates integer determinantal divisors for the complete gcd-difference matrices at \(p=2\) and \(p=3\), and checks exact determinantal divisors for the two-by-two and four-by-four universal blocks at ten prime arguments. It also tests invariant-factor divisibility and products against known Fourier-determinant factors. These experiments do not prove the universal classification; the proof is the explicit integral-equivalence reduction and three-by-three minor argument in `RESULT.md`. No numerical extrapolation is used to assert the theorem. Independent mathematical audit has not been performed.
