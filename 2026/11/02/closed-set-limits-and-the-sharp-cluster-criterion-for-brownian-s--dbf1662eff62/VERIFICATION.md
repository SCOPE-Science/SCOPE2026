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

Use Python with SymPy installed. In this directory execute `python verify.py`, and compare stdout to `verify_output.txt`. The checker exhausts subsets of the constraint edges for grids of lengths \(2\) through \(8\) for partition and endpoint controls; on small grids it evaluates exact rational Schur complements at the nodes, and on grids up to length \(6\) checks all half-grid pairs including Brownian bridge covariance residuals. It also tests complete and empty constraint configurations.

The recorded output comprises 6422 exact arithmetic assertions, not simulation. The infinite-dimensional conclusions rely separately on the proof in `RESULT.md`: Gaussian block projection, Brownian bridge tail bounds, continuity of affine interpolation under Hausdorff convergence, the compactness converse and the closed-set approximation construction.

The theorem does not provide an independent external review or a general noisy-conditioning result. Historical-priority uncertainty regarding broad Gaussian conditional interpolation results remains.
