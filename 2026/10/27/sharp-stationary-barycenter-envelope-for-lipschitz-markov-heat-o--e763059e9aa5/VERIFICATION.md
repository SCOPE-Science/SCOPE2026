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

The argument is an analytic finite-state theorem. Its crucial identities and boundaries were separately checked as follows:

- Exact rational arithmetic: 1,105 stationary block-averaging kernels, their exact invariant laws, transport seminorms, and cut-barycenter equalities; unit-edge uniform-law checks for dimensions 3 through 29; one four-state nonmonotone stationary permutation counterexample.
- Numerical cross-checks: 720 random continuous-time reversible path semigroups across nine dimensions, comparing an independent one-dimensional Wasserstein cumulative-sum calculation against the coordinate-potential difference and checking the equilibrium ceiling.
- Singular-limit diagnostics: 42 fast-inside/slow-cut conductance families checked against their predicted two-block barycentric limits.

All tests passed upon execution of the standalone `check_stationary_barycentric.py`. The Python script uses NumPy and SciPy for matrix exponentials; exact arithmetic in the block checks uses the standard library. Numerical tolerances do not certify infinite parameter ranges. The proof covers all dimensions and parameters stated in `RESULT.md`.

The cited literature was compared for mathematical implications, but no independent audit has been carried out; the full Pflug--Schachermayer article could not be inspected and residual priority uncertainty remains.
