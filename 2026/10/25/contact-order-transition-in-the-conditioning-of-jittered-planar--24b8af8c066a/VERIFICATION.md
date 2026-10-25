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

Run `python3 verify.py` using the Python 3 standard library. The program compares two formulas for the exact observation-Gramian spectrum on 2100 seeded finite examples, checks exact two-row triangular-density tail formulas, integrates the three-row contact cone, and tests the deterministic lower bound on 4000 draws. It prints `VERIFY_OK` only if all assertions pass. No sample enumeration can establish the infinite-parameter or zero-tail limit; those depend on the local Taylor expansion, tube/coarea volume, bounded rescaling and the layer-cake argument in `RESULT.md`. Numerical quadrature checks the closed three-row cone constant, not the general family of cone volumes. The primary source and mathematical literature comparisons are not mechanized certifications. Independent audit has not been performed.
