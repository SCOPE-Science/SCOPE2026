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

# Reproduction and mathematical limits

Run `python3 verify.py` with Python 3.9 or later; no external packages are needed. The script applies the positive-definite diagonal-resolvent ball step using scalar bisection and checks the bandwise decrement estimate, active-ball norm, accumulated full-path bounds, rational two-coordinate resolvent identities, and geometric-spectrum gradient-flow lengths. A successful run produced `PASS: 80671 finite checks`.

The script uses a fixed pseudorandom seed, finite floating-point arithmetic, and a finite set of examples. It neither enumerates all dimensions and radii nor certifies the limiting assertion. The analytic spectral telescoping and compact-subarc backward-Euler convergence arguments in `RESULT.md` establish the universal and asymptotic conclusions. The lower-bound transfer requires taking the radius to zero **after fixing the matrix dimension**, not a simultaneous limit with growing dimension.
