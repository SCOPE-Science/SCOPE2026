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

# Verification record
The analytic proof uses the unnormalized graph Laplacian, a complete three-sector decomposition of the powered resistance distance form, and a strictly convex scalar threshold equation. The independent standalone program `verify_resistance.py` reconstructs resistance values from reduced integer Laplacians by exact rational inversion and checks the full centered powered-distance matrices for thirteen small instances, three exponent regions each, plus exact algebraic identities and finite asymptotic diagnostics.

Run `python verify_resistance.py` with SymPy, NumPy and SciPy installed. The output ends with `ALL_RESISTANCE_NEGATIVE_TYPE_CHECKS_OK` on success. These tests are finite and do not certify every integer size or real exponent; the all-parameter conclusion is established by the detailed proof in `RESULT.md`. Near-critical eigenvalues are subject to numerical tolerance; exact rational checks are used where applicable.

Self-review: passed. Independent audit: not yet performed.
