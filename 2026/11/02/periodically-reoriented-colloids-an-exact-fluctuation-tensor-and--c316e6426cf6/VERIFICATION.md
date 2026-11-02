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

# Computational and analytic verification

The source code `verify_transport.py` computes the analytic \(v_\tau\) and \(\Gamma_\tau\), checks the trace identity and the specialization to an isotropic translational mobility matrix on a finite grid, verifies positive-definite covariance and the scalar optimizer, and compares the exact finite-cycle quantities with Monte Carlo sampling of the independent-noise representation. It ran successfully using NumPy and SciPy, with 56 deterministic algebraic or tolerance-controlled checks and 90,000 simulated cycles in the benchmark.

Run: `python verify_transport.py` with dependencies in `requirements.txt`. The analytic benchmark covariance is approximately \(\left(\begin{smallmatrix}0.47658030&0.01640636\\0.01640636&0.43986696\end{smallmatrix}\right)\); the simulated estimate was \(\left(\begin{smallmatrix}0.47415604&0.01624391\\0.01624391&0.44015039\end{smallmatrix}\right)\). The analytic drift was approximately \((0.01064268,-0.00706460)\), and the simulated drift \((0.01732237,-0.00739521)\), consistent with its finite-sample standard deviation and the script's predefined tolerant test.

The formal proof of the infinite-time central limit theorem, the exact tensor and the unique optimum is mathematical (Itô formula, Fourier harmonic average, iid LLN/CLT, scalar convexity). The code does not certify these infinite statements or independent priority. The Monte Carlo computation is reproducible but depends on sampling variability.
