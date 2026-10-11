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
# Reproducibility and verification

The companion `verify.py` is a standalone SymPy script. Invoke `python verify.py` in a Python environment with SymPy installed; successful execution prints `VERIFY_OK`. Its assertions check harmonicity of the cubic polynomial, exact principal-radius expressions and endpoint factors, all polynomial candidates for the curvature maximum, the threefold planar Fourier decomposition, the full angular support-area integral, the determinant-based surface and volume integrals, the distribution-function derivative, endpoint normalization, and consistency with mean projected area, exact projection-body volume polynomial, and its sharp monotonicity derivative.

The decisive all-parameter arguments are written in RESULT.md: a derivative with precisely two interior stationary points proves the support radius bound, Minkowski's planar support-function identity determines each projection area, the spatial support-function volume identity determines the projection-body volume, and uniformity of the cosine of a random direction gives the law. The verifier checks the closed forms symbolically, not by numerical sampling; neither program output nor partial enumeration is asserted to independently establish the geometric theorem.

The first public manuscript was read in full for comparison. Other relevant published full result texts were compared statement-by-statement. A relevant 2026 paper about random brightness in polytopes was inspected at abstract level only, and an earlier equivalent statement under different notation cannot be ruled out solely by search.
