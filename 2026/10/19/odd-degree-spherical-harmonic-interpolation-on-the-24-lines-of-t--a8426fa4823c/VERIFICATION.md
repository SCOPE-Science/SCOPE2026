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

Run `python verify.py` with SymPy installed. The program constructs the 24 exact coordinates and verifies all 12-by-12 root-sign relations, four- and eight-dimensional eigenspace multiplicities, full Gram eigenvalues in 21 distinct odd degrees through degree 41, several direct spherical Chebyshev kernels, low-degree interpolation ranks, and the tight arithmetic progression when represented among sampled degrees. All comparisons are exact symbolic integer/rational/algebraic equalities.

The general theorem for every odd degree is analytically proved from the signed-matrix identities and the closed Chebyshev values. Finite tests do not prove the infinite quantifier and no independent audit is represented.
