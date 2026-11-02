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

# Verification and limits

Run `python3 verify.py` with Python 3 and no extra packages. The script compares the exact formula with independent direct order and modular-exponent computations, as well as with additional prime-support exponent tests and power-threshold checks.

The verified output in the preparation environment was:

```
VERIFY_OK direct_cross_checks= 3422 support_exponent_checks= 549 general_bases=2,3,5,7 power_thresholds=PASS
```

The proof uses the odd-prime valuation identity for \(\nu_p(b^{d_pu}-1)\), the prime-power order formula and the Chinese remainder theorem. These are sufficient to prove the infinite statement without reliance on the finite tests. The modular test using \(n^2\) recovers the quotient modulo \(n\) exactly; no huge exponential integer need be stored. The verifier does not test moduli with an even prime factor or bases not coprime to the modulus. No independent audit has been performed.
