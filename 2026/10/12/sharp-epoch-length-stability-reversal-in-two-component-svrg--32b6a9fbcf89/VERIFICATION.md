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

# Verification

The reproducible standard-library program `verify_svrg.py` independently enumerates every Bernoulli curvature-sign branch at epoch lengths two and three for rational test data. It matches both closed-form squared-moment factors, checks the exact degree-six Bernstein polynomial, two opposing exact rational stability witnesses, and tight rational sign brackets for the crossover roots.

Execute `python verify_svrg.py`; the actual execution returned `VERIFY_OK: exact random-branch moments, Bernstein identity, two rational stability reversals, root brackets`.

The proof in `RESULT.md` is analytic for all positive unequal curvatures and all positive stepsizes. Finite enumeration cannot independently certify global uniqueness or novelty. Independent audit status is `not_performed`.
