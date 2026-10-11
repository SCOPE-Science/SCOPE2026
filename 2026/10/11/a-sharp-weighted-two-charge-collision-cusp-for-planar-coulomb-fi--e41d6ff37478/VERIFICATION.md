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

# Verification and reproducibility

The rigorous checks are the exact one-pole area normalization, the triangle-deficit scaling identity, the integrable \(O(|w|^{-3})\) tail, almost-everywhere convergence of the moving disks, the focal-coordinate Jacobian, and two beta integrals producing a positive convergent series. All are proved in `RESULT.md` with explicit hypotheses. `check_collision.py` is a Python 3 standard-library diagnostic:

```sh
python3 check_collision.py
```

The script independently evaluates the series numerically and a two-dimensional positive quadrature; it also checks finite rational binomial-coefficient identities and weight-swap symmetry. It is not an infinite proof, an exhaustive literature check, or an external audit. Numeric approximations are explicitly separated from the exact integral and convergent-series identities. No larger class, finite-angle formula, or multi-pole collision assertion has been established.
