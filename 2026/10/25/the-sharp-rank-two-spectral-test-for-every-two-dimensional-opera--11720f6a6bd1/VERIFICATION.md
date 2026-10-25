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

# Verification notes

The analytic compression argument proves the infinite-dimensional statement in both scalar fields. The finite-rank trace and nonzero-spectrum factorization are standard, and the nonscalar-compression lemma is proved directly in RESULT.md.

The reproducibility file `support/check_rank2.py` uses Python 3 and SymPy exact arithmetic. Running `python support/check_rank2.py` from the extracted package reports `exact_cases= 309 assertions= 9888 status=PASS`. This checks exact ranks, involution identities, trace normalization and nonnilpotence for finitely many matrix pencils, including sparse and complex tests. The finite tests do not establish the universal theorem or independent review.

Verification state: self-reviewed. Independent audit: not performed.
