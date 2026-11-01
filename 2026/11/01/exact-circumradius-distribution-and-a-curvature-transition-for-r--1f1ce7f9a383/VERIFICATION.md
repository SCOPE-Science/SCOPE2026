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

# Reproducibility and mathematical limits

Run `python3 verify.py` from the directory containing this file. It needs only Python 3's standard library and prints `ALL_CUBE_SHADOW_CIRCUMRADIUS_CHECKS_PASSED` when all checks succeed. Tests reconstruct 800 cube shadows from projected vertex coordinates, compare them with the ordered-normal formula, check 200 monotonicity grid points, compare the quadrature with independent spherical integration, check the two endpoint and the interior transition asymptotics, and draw 120,000 independently seeded Haar orientations to compare empirical events with the exact integrals.

The derivation in `RESULT.md` is the proof for the continuum of orientations. Quadrature truncation and finite Monte Carlo trials are diagnostic, not exhaustive validation, not proofs of the asymptotic formulas, and not historical-priority certification. The exact probability measure is normalized spherical area on \(S^2\); the sign-and-order sector contributes a factor \(48/(4\pi)=12/\pi\). The CDF is derived for the cube shadow circumradius, and no analogous cube section or octahedron projection distribution is asserted. Independent mathematical audit has not been performed.
