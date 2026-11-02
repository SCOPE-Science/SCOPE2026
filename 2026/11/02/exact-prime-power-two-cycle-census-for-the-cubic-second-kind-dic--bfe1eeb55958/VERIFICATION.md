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

# Reproduction

Run `python3 verify.py` using Python 3. The script has no third-party dependencies. It constructs and compares integer polynomial coefficients for the exact identity underlying the proof and enumerates every class modulo prime powers for the selected primes \(2,3,5,7,11,13,17,19\). The script checks agreement for each individual residue class with the theorem's disjoint-set description and confirms the predicted point counts, rather than merely comparing totals. The exact packaged verifier was executed successfully and returned `VERIFY_OK prime_power_levels=50 residue_classes=271821 identity=exact`.

# Limits

These finite checks cannot prove a universal all-prime-power statement; that statement is proved by the integer factorization and valuation analysis in RESULT.md. No independent audit has been performed.
