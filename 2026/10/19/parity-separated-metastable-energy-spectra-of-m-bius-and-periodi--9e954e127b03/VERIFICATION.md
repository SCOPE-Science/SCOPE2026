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

# Exact verification and boundaries

Run `python verify.py` with Python 3 and SymPy installed. The script builds both graph adjacency lists independently of the transfer polynomial, checks every labeled spin assignment for rung counts from three through nine, verifies the polynomial associated to each configuration by directly counting equally oriented graph edges, and compares the results with the closed formulas. It also constructs the transfer matrix and the row-exchange symmetry, proves their commutation by direct symbolic equality, and verifies the sector determinant identities as exact polynomial equations for arbitrary indeterminates, not by numerical sampling. The run completed successfully before packaging.

The exhaustive finite-size checks alone would not justify a theorem for all sizes. The full all-size deduction instead uses the exact symbolic block characteristic polynomials and the power-sum recurrences spelled out in `RESULT.md`. The thermodynamic moment statements use dominance of the analytic Perron root near unit fugacity; no quench measure or finite-temperature state is evaluated.
