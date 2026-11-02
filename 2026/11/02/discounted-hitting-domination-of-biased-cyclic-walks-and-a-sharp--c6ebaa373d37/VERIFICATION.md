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

# Reproducibility and checks

The provided `verify_biased_cycles.py` is self-contained and uses only the Python standard library. Invoke `python3 verify_biased_cycles.py` from the directory containing the file. It independently forms and solves exact rational full-cycle first-hitting systems rather than assuming the gap characterization, and separately solves finite Dirichlet interval systems. It checks 4,036 nonempty cycle source subsets, 196 threshold combinations, all feasible-set polynomial coefficients in those cases, numerical substitution of the closed characteristic-root formula, and high-precision checks at the algebraic bias optimum.

Verification completed successfully with outputs:

`VERIFY_OK rational_grid_instances= 196 independent_exact_cycle_subsets= 4036 feasible_cardinality_checks= 1176`

`DRIFT_OPTIMUM_OK p= 0.78077640640441513745535246399351925628679980634340510859965839328 H4= 0.17980589839889621563616188400162018592830004841414872285008540168 H5_interior_upper= 0.081282631917854258336877018559212675969483440877505513543575417149`

The infinite and continuous-parameter statements follow from the analytic proof in `RESULT.md`; finite checks alone cannot establish them. The high-precision numerical drift checks are not a replacement for exact algebraic inequalities shown in the proof. No independent audit has been performed.
