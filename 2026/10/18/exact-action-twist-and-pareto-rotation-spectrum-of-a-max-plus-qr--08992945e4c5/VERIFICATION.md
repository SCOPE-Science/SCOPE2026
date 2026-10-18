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

The explicit polygon-area, normalized density, and twist formulas were verified as exact SymPy identities by running `python verify.py` in the package directory. Its output was `VERIFY_OK`.

The checker also evaluated the conserved max-plus integral on a finite rational grid and independently computed exact returns and clockwise geometric windings on five rational invariant levels. These are diagnostic controls, not proofs for all real parameters. The all-level rotation calculation is proved from the rigid return map and return-time distribution; the cutoff and Pareto results are algebraic and weak-convergence deductions in `RESULT.md`.

No independent or external validation is claimed. The full claim is limited to the unperturbed integrable map and the stated planar-area sampling law.
