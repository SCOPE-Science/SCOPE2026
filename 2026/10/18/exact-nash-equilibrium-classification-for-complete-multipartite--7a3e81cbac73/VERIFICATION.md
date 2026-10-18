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

# Reproducible checks

Run `python3 verify.py` with the Python standard library. The program uses `fractions.Fraction` and an exact Gauss-Jordan solver. It directly optimizes the opinion for both actions and compares full payoffs, calculates the unique candidate opinion vector for every binary action configuration, tests every unilateral Nash inequality, and independently evaluates the predicted balanced-part conditions. It checks 1,416 action profiles on ten part-size patterns with four rational parameter families (only admissible multipliers are used). The example on a four-vertex complete bipartite graph yields exactly six Nash equilibria, four of them mixed with opinions \(5/12\) and \(11/12\).

These finite computations verify concrete formulas and detect elementary errors; no finite enumeration establishes the all-orders theorem. That theorem is proved by spectral inertia, weighted covariance, the equality case of the eigenvalue expansion, and exact multipartite counting in `RESULT.md`. Third-party validation and independent audit have not been carried out.
