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

# Reproducibility and boundaries

Run `python3 artifacts/verify.py` with Python 3 standard libraries; the script is standalone and uses no downloaded input. Independently re-evaluated the Selberg integral \(1/30\), the unit-disk sixth-chord power and leading tail constant, the square's sixth-chord side-versus-diagonal ratio, and a seeded experiment of 750,000 random disk triangles.

Expected diagnostic markers include `EXACT_GAP_INTEGRAL_1_OVER_30_OK`, `DISK_SIXTH_CHORD_INTEGRAL_AND_TAIL_COEFFICIENT_OK`, `INDEPENDENT_SQUARE_CHORD_DIRECTION_MARGINALS_OK`, `DIRECT_RANDOM_TRIANGLES_CIRCUMRADIUS_CONDITIONAL_GEOMETRY_OK` and `ALL_MARKED_RARE_TRIANGLE_DIAGNOSTICS_OK`.

The proof is analytic: a bounded rescaled transverse coordinate allows dominated convergence and exact integral normalization; finite simulations cannot prove infinite limits. Historical priority is provisional because the full Kendall 1985 paper was not accessible. Independent mathematical audit remains not performed.
