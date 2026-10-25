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
# Verification of inverse-cube spectral asymptotics

The proof is analytic. The included `verify.py` independently computes the exact spectral sums and their derivatives from polylogarithms and uses Gaussian quadrature on the dominant wave-number scale. It compares critical asymptotic amplitudes for \(\delta=5/2\), \(3\), and \(4\), the near-critical collision surface, and the two-parameter critical surface. Because convergence involves inverse logarithms, moderate finite-time ratios can deviate visibly from their limits. The tests check the correct direction and quantitative scale of convergence; no finite quadrature is used as an infinite-time proof. The integration discards an exponentially small high-wave-number tail at the chosen large times. Run the standalone script using `python verify.py` with NumPy and mpmath installed. No stochastic-chain simulation and no independently audited full-current claim are included.
