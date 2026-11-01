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

Run the standalone program from the same directory as the mathematical statement:

```sh
python3 verify_odd_polygon_diameter.py
```

The program executed successfully with output:

```text
VERIFY_OK 194 deterministic and seeded checks
```

The executable uses only the Python standard library. Its checks include direct Cartesian vertex projection calculations for regular odd polygons with 3, 5, 7, 9, 11, and 13 sides; exact polygon clipping to measure small projection caps against the theoretical Weibull parameter; independent quadrature for the bivariate Poisson-cone intersection-area identity in multiple branches; positivity, symmetry and marginal-survival bounds; algebraic checks of the small-tail coefficient; finite-domain Poisson simulations and area-uniform finite-sample simulations; and rough cross-comparisons between the latter two Monte Carlo implementations.

The Poisson simulation restricts the quadrant to a square large enough to capture all points relevant to a chosen positive threshold. Finite point clouds are sampled exactly by area-weighted triangulation and barycentric coordinates. Random generators use a fixed seed, making results reproducible. None of the finite experiments certifies the universal \(N\to\infty\) limit, a rate of convergence, or historical priority; those conclusions require the analytical argument and an external literature comparison respectively.

The essential analytical checks are: (1) positive directional derivatives at every diametral vertex pair, (2) cone Jacobian-to-area normalization \(2/m\), (3) joint convergence of all vertex-local empirical point processes, (4) localization and the vanishing quadratic distance remainder, (5) the union-of-triangles Poisson void calculation, and (6) the finite inclusion–exclusion argument showing that collisions between different diametral-pair events first enter at order \(t^6\). All six are provided in the proof.

Independent mathematical validation has not been performed.
