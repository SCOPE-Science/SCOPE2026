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

# Verification of the volume-spline claim

The self-contained `verification/volume_spline_verifier.py` script uses exact `fractions.Fraction` arithmetic and standard-library combinatorics; no downloads, solver, or floating-point tolerances are required.

From the packaged source, run:

```
python3 verification/volume_spline_verifier.py
```

Successful replay before packaging printed:

```
PASS {'exact_slice_integrals': 594, 'nonnegative': 594, 'threshold': 198, 'point_membership': 5404, 'knot_jumps': 115} TOTAL 6905
```

The 594 exact slice-integral checks reconstruct each positive-part affine integral independently of the closed spline expression for dimensions 2–12 at rational test parameters. The 5,404 membership checks compute distances to every signed coordinate vertex directly on rational grids. The remaining exact checks cover nonnegativity, vanishing, last-chamber coefficients, and nonzero stated jump coefficients.

Universal validity is supplied by the analytic inclusion-exclusion proof and polynomial cancellation in `RESULT.md`, not by finitely many tests. The code does not establish historical priority, independent mathematical certification, or results for other convex bodies.
