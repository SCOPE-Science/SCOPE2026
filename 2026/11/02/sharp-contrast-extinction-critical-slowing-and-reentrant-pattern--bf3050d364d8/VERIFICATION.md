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

The executable `verify.py` uses Python 3, numpy, scipy, and sympy. From the directory containing it, execute `python verify.py`. It confirms the identities \(\ell(z)+\ell(-z)=1\), \(2\ell(z)-1=\tanh(z/2)\), and the critical Taylor coefficient \(\lim_{v\to0}(\tanh v-v)/v^3=-1/3\) symbolically. Four hundred randomized stochastic-network configurations test the diameter inequality. Twenty two-node cases verify exact equilibria and both Jacobian eigenvalues; four coupling contrasts check the secondary stability threshold, and long-time integration checks the critical constant numerically.

The analytical theorem does not rely on random tests to establish universal quantification, and numerical integration does not certify an infinite-time limit. The proof supplies the comparison principle, finite-zero convergence argument, exact invariant line and spectra. For parameter precision, all claimed sharp constants are given by exact equations rather than numeric sampling. No independent audit or external validation is represented.
