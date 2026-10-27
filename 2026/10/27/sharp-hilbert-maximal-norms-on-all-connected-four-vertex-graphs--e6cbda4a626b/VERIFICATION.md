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
# Reproduction and limitations

Run `python3 verify.py` in the same directory as this document. It requires only Python 3's standard library. It enumerates all 385 distinct normalized graph-ball matrix selections arising from the six labeled connected four-vertex graph types. For each nonwinning matrix it proves \(qI-A^\mathsf{T}A\) positive definite using exact rational leading-principal-minor checks; for each winning matrix it verifies the exact characteristic polynomial and its position above the separating barrier. No randomness, floating-point matrix eigensolver or external file is required.

The proof in `RESULT.md` gives the nonlinear-to-finite-matrix reduction, analytic root identification, Perron eigenvectors, and uniqueness of selected radii. The checker certifies a genuinely finite sublemma and does not purport to establish priority in the mathematical literature or validation independent of the accompanying review. Independent audit has not been performed.
