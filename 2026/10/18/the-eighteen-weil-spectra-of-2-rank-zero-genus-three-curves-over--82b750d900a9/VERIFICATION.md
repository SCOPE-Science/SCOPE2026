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

# Computational verification

The scripts require Python 3 standard library only. Execute them in the directory containing `classification.csv`:

```
python verify_classification.py
python independent_check.py
```

`verify_classification.py` checks all 128 reduced models, all translation group laws, all 32 isomorphism-orbit representatives and their trace counts through the third extension. It rewrites `classification.csv`. The independent script enumerates the roots of \(y^2+y=f(x)\) directly using alternate irreducible polynomials, verifies all 32 rows and computes the fourth-extension point counts over \(\mathbf F_{256}\), checking the genus-three functional equation. Outputs captured in `verification_primary.txt` and `verification_independent.txt` record successful runs. These finite calculations are exhaustive only because the separately proved normal-form reduction confines the theorem to exactly 32 models; they do not alone prove the reduction or global literature novelty.

The Newton-polygon assertion uses the computed coefficient divisibilities plus standard Newton-polygon algebra. The only external review is self-review; independent audit has not been performed.
