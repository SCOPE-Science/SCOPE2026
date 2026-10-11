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

# Reproducibility and limits
Run `python verify_octahedron.py` with Python 3, NumPy, SciPy, and SymPy in the same directory as the source script. A representative successful complete output appears in `verification_output.txt`.

The checker symbolically factors the derivative numerator as \((2-\sqrt2)(u^2-(\sqrt2-1)^2)(u^2+3+2\sqrt2)\). It compares the independently accumulated finite cone formula against the axial expression for eleven aspect ratios, returning maximum absolute discrepancy \(3.33\times10^{-16}\). For eight invertible matrices it uses 2500 independently sampled directions per matrix to compare random orientation frequencies with the exact cone probability. It independently constructs two-dimensional convex hulls from all six projected vertices on 960 randomly selected directions, with no disagreement between hull vertex count and algebraic dominance classification. All test code and seed are present.

This is a finite diagnostic, not an exhaustive test over directions or matrices. The proof for all positive axial scales relies instead on the analytic cone partition and sign-factorized derivative in `RESULT.md`. Numerical Monte Carlo tolerances were set conservatively and do not provide a scientific certificate of novelty or independent audit.
