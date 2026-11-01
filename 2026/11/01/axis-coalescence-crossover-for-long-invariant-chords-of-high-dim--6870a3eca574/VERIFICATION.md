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

# Verification and scope

Run `python checker.py` in an environment with NumPy and SciPy, as listed in `requirements.txt`. The checker is self-contained and uses fixed local random seeds. It assesses the exact quadratic chord formula against explicitly intersected lines, the spherical endpoint law, 3D and 4D spheroid quadratures, multiaxis fixed-shape endpoint limits, and the dimension-four/five one-axis coalescence profile. Its direct intersection and quadrature calculations provide independent numerical routes to the same finite formulas. All checks have numerical tolerances in the script; neither simulation nor numerical integration proves an infinite or asymptotic theorem.

The mathematical proof is in `RESULT.md`, including a separate argument for zero transverse dimensions, exact normalization, dominated convergence and local uniformity in the crossover parameter. Algebraic matching of neighboring endpoint coefficients uses the standard beta–gamma identity. The strongest published coverage comprises general ellipsoid chord-power moments (Heinrich 2014) and known low-dimensional chord laws (Kellerer 1984). No independent mathematical audit has yet been performed.
