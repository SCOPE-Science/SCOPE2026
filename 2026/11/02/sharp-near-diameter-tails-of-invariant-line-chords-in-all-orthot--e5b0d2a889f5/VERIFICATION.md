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

# Numerical and analytic verification

The proof in `RESULT.md` is analytic. Its key reproducible identities are the exact indicator-protected projection-of-overlap formula, the invariant-line normalization, the compact Dirichlet simplex integral and the cube extremality argument. An independent Python script numerically tests the first two dimensions through deterministic quadrature and dimensions four and five through seeded, scrambled Sobol low-discrepancy integration. The reported ratio \(\Pr(L>2A-\varepsilon)/(C_d(a)\varepsilon^{2d-2})\) approaches one under decreasing \(\varepsilon\) for tested examples; for the four-cube the ratios at \(0.1,0.05,0.025\) are approximately \(1.141246,1.067258,1.032864\). For a five-cube they are approximately \(1.164315,1.077643,1.038094\). Quasi-Monte Carlo is neither exact enumeration nor a certificate of an infinite limit; no uniform numerical error claim is made.

Execute `python verify_chords.py` with NumPy and SciPy installed. The verifier uses the same explicitly stated line-sampling convention and checks positivity constraints for all coordinate overlaps.
