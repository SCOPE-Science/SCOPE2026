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

The general claim is analytic; it does not rely on a finite test or external proof certificate. `RESULT.md` defines the graph, exact SIS recurrence, community sums, all parameter ranges, and the proof of the strict \(m^2/8\) lower bound. The algebraic eigenvector identities used as critical lemmas are \((\Lambda-m+1)V_A=v_{b_1}\) and \((\Lambda-m+1)V_C=mV_B\); they follow by summing the adjacency eigenvalue equation over the first and third cliques. The spectral bounds follow by a two-block Rayleigh test and maximum-degree estimate. Existence, uniqueness and normalized critical convergence are proved without numerical approximation.

Execute `python checker.py` from the extracted package using Python 3.10+, NumPy and SciPy. In the observed run, ten nonlinear fixed-point solves for \(m\in\{4,6,10,20,40\}\) and \(\varepsilon\in\{0.02,0.005\}\) passed, with fixed-point residuals below \(10^{-8}\). The checker verifies the matrix construction, local spectral ordering, block-sum identities, upper/lower spectral bounds, all-community isolated subcriticality and the positive equilibrium's ratio inequality. Its numerical eigenvalues and optimizer output are not certificates of an infinite theorem.

This is a deterministic mean-field product map, not the exact finite-state Markov chain. It is not asserted that the quadratic bound is optimal, or that it persists under arbitrarily weak inter-community mixing. Publication priority has not been independently assessed.
