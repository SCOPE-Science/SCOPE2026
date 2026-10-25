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

The standalone file `checker.py` requires Python 3 and NumPy. Execute it with `python checker.py`. It uses a fixed random seed and computes the complete total-degree orthogonal reproducing kernel from an independent truncated generating-product recurrence, rather than only the asymptotic leading term.

Actual execution of this script returned a successful exit code, reported `PASS: 120 exact-formula comparisons and dimension/asymptotic diagnostics`, and checked the closed quadratic kernel expression for 120 random evaluation/input configurations. Monte Carlo diagnostics covered \(m=1,2,3\), dimensions \(d=16,64,256\), and evaluation profiles at corners, half-zero points, and half-scale points (where included). The predicted quadratic coefficient was \(6/\sqrt{2\pi e}\approx1.451824347115\); the normalized corner values reported at dimensions 16, 64, and 256 were approximately 1.491360, 1.462281, and 1.455165. Results for cubic and interior evaluation profiles also agreed to the script's stated sampling tolerances.

These finite Monte Carlo values are not rigorous error bounds, and sampled points do not prove a global maximum or an infinite-dimensional limit. The correctness argument instead uses the exact product Legendre kernel, a uniform \(L^2\) estimate for omitted multi-indices, a triangular-array central limit theorem, Newton's identities, a uniform second-moment estimate, and subsequence compactness. The only calculated special-function integral is \(\mathbb E|H_2(Z)|=4e^{-1/2}/\sqrt{2\pi}\).

This verification does not establish finite-dimensional corner maximality, a quantitative rate for the full uniform little-o term, or any claim for growing polynomial degree. No independent audit has been performed.
