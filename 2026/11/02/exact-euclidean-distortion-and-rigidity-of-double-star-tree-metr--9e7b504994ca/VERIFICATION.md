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

Run `python verify_double_star.py` with Python 3.10 or newer. It uses only the standard library, 75-digit Decimal arithmetic, and explicit regular-simplex coordinates. The observed result was `CHECK_OK parameter_cases= 173 explicit_vertex_pairs= 28223`. Among its cases are every pair \(2\le m,n\le14\) and four large parameter choices. Every unordered pair of vertices in each tested double star is checked against the graph metric and the predicted squared Hilbert-distance bounds. Balanced closed forms and the asymptotic constant are also compared to the defining equation.

The computation samples finitely many integer sizes and uses an explicitly specified decimal tolerance; it neither certifies symbolic uniqueness of roots nor proves the theorem for all sizes. The full all-parameter proof, including root uniqueness, sharpness, the nontrivial opposite-center distance bound, and equality rigidity, is given in `RESULT.md`. References in `RESULT.md` delimit the comparison with previous results. This is a self-review, not an independent audit.
