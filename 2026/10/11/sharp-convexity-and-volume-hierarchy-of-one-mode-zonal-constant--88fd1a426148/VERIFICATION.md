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
# Reproducibility

`verify.py` needs Python 3 and SymPy. Run `python verify.py` from a directory containing the file. It uses exact rational arithmetic, checks the Legendre-to-cosine generating-function coefficient formula and its positivity for degrees 3, 5, 7, 9, confirms the weighted curvature bound, reconstructs the polar support radii, and symbolically integrates the support-function volume for those four degrees. It checks the exact degree-three minimum volume.

The finite test does not establish the assertions for every odd degree or prove novelty; those assertions use the all-degree Legendre generating function, the principal-radius argument and the spectral volume identity in `RESULT.md`. No external or independent audit was performed.
