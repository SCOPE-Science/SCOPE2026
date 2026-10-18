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

# Reproducibility and verification

Run the included `verify.py` using Python 3 and its standard library:

```
python3 verify.py
```

Expected output includes `VERIFY_OK dominance_certificates= 31 exact_inverse_checks= 656 family_sample_cases= 118`.

The verification program constructs the exact balanced-tail rational objective from the displayed formula, checks that all 31 omitted separations for orders three through ten have a strictly better candidate for **all** positive real gains by coefficient/discriminant sign, verifies the exact coefficients of seven decisive pair differences, and independently solves 656 rational linear systems to compare direct inverse traces with the electrical-network formula. It also tests the strict two-gain family optima at 59 sizes, giving 118 sampled comparisons. The last finite collection does **not** establish the claim for infinitely many orders; the proof in `RESULT.md` supplies the derivative sign argument and explicit rational factorizations for every integer parameter.

Finite exact arithmetic confirms the implementation but does not independently validate every written reasoning step. No independently conducted audit or third-party mathematical certification is claimed. Historical originality may require additional literature checks.
