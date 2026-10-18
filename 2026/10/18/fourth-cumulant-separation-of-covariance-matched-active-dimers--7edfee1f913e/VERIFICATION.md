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

# Verification record

The public standalone executable is `checks/verify.py`, requiring `numpy`, `scipy`, and `sympy`. Execute `python checks/verify.py` after extracting this finding's embedded files. The checker independently reconstructs the four-time Gaussian Wick and telegraph Markov products, enumerates all 24 chronological orderings for a symbolic time integral, computes the finite-time fourth cumulant by analytic two-dimensional quadrature, and compares against independently discretized conditional-Gaussian variance mixtures (matrix traces for Gaussian drivers and four-time sign correlations for telegraph drivers).

The standalone checker yielded **61 passed assertions** across the parameter examples \((\mu,\nu,P,Q)=(1.3,0.7,1.5,0.8)\), \((0.6,2.4,4,0.5)\), and \((3,1.9,0.7,2)\). The direct exact fourth-cumulant growth-rate ratios were \(2.9053254437869818\), \(29\), and \(3.301111111111111\), respectively. These agree with the formula \(1+3\nu/\mu+(\nu/\mu)^2\).

Finite-grid checks support the identities but do not prove the infinite-parameter theorem. The proof's all-parameter content comes from exact Wick/Markov four-time laws, positive kernel decomposition, integration over chronological permutations, and dominated convergence. Limitations include the stationary harmonic independent-driver setup, positive finite rates, source-defined entropy-production convention, and lack of empirical finite-sample calibration. Independent audit has not been performed.
