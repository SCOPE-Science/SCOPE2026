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

# Verification and limits

Run `python3 verification.py` in this directory. No nonstandard Python modules are needed. Expected final output: `VERIFY_OK`.

The script exactly reduces Fejér character sums modulo integer cyclotomic relations for rotation orders 2, 3, 4 and 5. It verifies all three finite-group irreducible-character multiplicities, isogeny dimension totals, cyclic quotient genera, Riemann--Hurwitz defects, and single-orbit branch cardinalities. Its computations concern the finite character tables, not a finite census of smooth curve parameters.

The universal mathematical argument uses invariant equations, equivariant adjunction and Koszul cohomology, spherical harmonic decomposition, rational group algebra, and the tame inertia/quotient formula. Geometry and these standard theorems are not mechanically formalized by this script. No independent mathematical audit has been performed.
