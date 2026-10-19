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
# Reproduction and limits

Install dependencies from `requirements.txt`; execute `python verify.py` in a directory containing both files. The program builds each weighted-wheel Laplacian by adding conductances to its edges, diagonalizes it numerically and performs independently computed eigenspace restriction rank tests. It compares every two-vertex choice on rim orders four through eighteen at multiple generic weight ratios and all Fourier/radial collision ratios. It also checks exact SymPy Kalman ranks on selected four-, six-, and eight-rim weighted wheels and every triple of vertices at all resonance indices for prime rim orders five, seven and eleven.

Successful execution prints `VERIFY_OK 12705 checks`. The exact count is an execution result of this specific program. Float comparisons in the finite eigenspace checks use explicit rank tolerances; exact rational Kalman checks protect against selected numerical aliasing errors. The spectral decomposition, determinant arguments and counting proof in `RESULT.md`, rather than this finite experiment, establish the infinite family. The conclusion has received self-review only; no independent audit has been performed.
