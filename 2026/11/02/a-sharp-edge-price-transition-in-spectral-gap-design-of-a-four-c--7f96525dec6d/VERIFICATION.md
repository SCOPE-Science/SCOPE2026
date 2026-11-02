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

# Reproducibility checks

Run `python3 verify.py` with Python 3 standard library. The executed program returned:

```text
VERIFY_OK exact_rational_sqrt_cost_cases=135 boundary_family_cases=11 independent_spectra=120 arbitrary_feasible_comparisons=4200
Scope: numerical comparisons are finite; global optimality follows from the two-block proof and AM-GM or Rayleigh bounds.
```

Exact rational checks verify the budget, even/odd spectral equalities, semidefinite determinant equality and the transition family at rational parameters. Jacobi diagonalization independently checks weighted graph spectra for randomized parameters, including budgets and transition crossings; asymmetric allocations are sampled as corroboration. Globality, full quantification, and uniqueness come from the analytical argument in `RESULT.md`. Finite calculations cannot eliminate untested allocations or substitute for the proof.
