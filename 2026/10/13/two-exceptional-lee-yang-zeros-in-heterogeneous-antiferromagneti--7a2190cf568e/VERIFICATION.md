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
# Reproducible analytical checks and limits

Run `python3 verify.py` in the same directory. The standalone checker requires only Python's standard library. It independently constructs rational partition coefficients by direct summation over spin configurations for small stars, compares these with factorized coefficients, and tests polynomial palindromicity over many heterogeneous rational coupling choices. It locates the unique negative interior root by a monotone bisection and checks the reciprocal exterior zero, finite outlier bounds, circle-root equations, and circular arc discrepancy for deterministic pseudorandom parameter samples.

The finite computation produced:

`VERIFY_OK algebra=155 root_residual=757 outlier_bounds=102 arc_discrepancy=640`

The exact rational algebra supports the finite coefficient identities. Root and arc tests involve floating-point approximations and are not proofs of simplicity, exact root counts for all real couplings, or asymptotic convergence. These unrestricted conclusions follow from the analytic proof in `RESULT.md`, specifically the phase-curvature argument, scalar monotonicity, reciprocal symmetry, product bound and odd-level counting. No external independent audit has been performed.
