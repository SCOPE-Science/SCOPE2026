---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed r_d(U)^-1 = max_{sigma in {±1}^d}||projection_{U-perp} sigma||_2 = sqrt(d-min_sigma(sigma·U)²). Averaging squared signed sums gives m(U)<=1; equality forces only one nonzero U coordinate by positivity of 4sum_{i<j}U_i²U_j², hence exactly 2d axes maximize inradius 1/sqrt(q), q=d-1. Near an axis, signed minimum equals sqrt(1-||u||²)-||u||_1, and event reduces to ||u||_1+1-sqrt(1-||u||²)<delta_epsilon. Independently differentiated delta=q^(3/2)epsilon + 0.5q²(q+3)epsilon²+O(epsilon³). In orthant l1 polar simplex coordinates, sphere Jacobian contributes only relative O(delta²); radial endpoint is delta-0.5delta² sum t_i², with E(sum t_i²)=2/(q+1), giving local volume 2^q delta^q/q! [1-q delta/(q+1)+O(delta²)]. Multiplying by 2d / |S^(d-1)| gives exactly C_d and K_d. Checked symbolic expansion and d=2 boundary. Monte Carlo finite d tests in package only corroborate the exact signed-partition formula, not the limiting theorem.

## originality

PASS

Szarek–Wolff supplies the sharp universal upper bound on inradius and coordinate example, but not Haar probability or two-term endpoint asymptotics. Donoho–Tanner count projected face numbers, not section inradius. Published Resultary cross-polytope section diameter laws are for a different invariant and high-dimensional scaling. Qualified novelty of the specific two-term tail.

## value

PASS

Intrinsic near-optimal radius for a Haar-random central hyperplane slice of a fundamental convex body is a natural geometric probability observable. Exact leading small-event exponent d-1 and explicit next correction quantify closeness to a sharp extremal section and directional signed-partition geometry, not a restatement of the maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
