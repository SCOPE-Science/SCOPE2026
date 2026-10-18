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

## Reproducible exact checks

Run `python verify.py` with SymPy installed. The checker uses exact rational arithmetic and symbolic identities only; it prints `VERIFY_OK det=625/6912 inverse_infinity_norm=164/5 rank=7` when successful. It verifies the seven polynomial Laplacians, four mutually orthonormal plane frames, all eight by seven third-mode coefficient entries via direct trigonometric power expansion, the independent complex-null-frame formula, the seven by seven determinant, the inverse, the three-plane rank deficiency, and the exact operator-norm bound.

## What is proved analytically beyond the finite checker

All-view symmetry implies the ambient degree \(0,1,3\) harmonic cutoff using the established rotation-invariant harmonic projections and forbidden equatorial modes. Every three-view configuration has a nonzero kernel because its linear third-mode data has at most six real components, and sufficiently small perturbations of the ball retain smooth strict convexity. Generic four-view success follows from analyticity and the explicit nonzero determinant. The Hausdorff bound follows from the inverse matrix and elementary sphere sup-norm estimates. These are rigorous mathematical deductions; sampling or executing the checker alone does not prove them.

## Scope and limitations

Four planes are calibrated and planar translation is the only per-shadow ambiguity. The statement does not include unknown in-plane rotations, projection brightness alone, arbitrary convex bodies, or independent validation of originality. A historical-priority assessment remains provisional.
