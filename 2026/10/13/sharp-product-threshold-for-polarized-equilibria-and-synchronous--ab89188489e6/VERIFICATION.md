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

Run `python3 verify.py` using Python 3's standard library. The script checks the sampling cubic by exact rational substitution, the two-step composition algebra, derivative conditions and several rational parameter profiles. It also performs finite illustrative orbit iterates in four invariant sign regions and verifies the specified heterogeneous witness. Successful local output: `VERIFY_OK: exact triad reduction, 36 composition certificates and four basins`.

The finite checker does not enumerate a continuum or prove uniqueness by iteration. The full-domain classification, global convergence and critical asymptotic rates follow instead from the strict monotonicity, strict concavity and normal-form proof in `RESULT.md`. The outcome has not undergone independent review.
