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
# Reproduction and proof boundary

Run `python verify.py` with dependencies from `requirements.txt`. The included `verification_output.txt` is a recorded output from the same checked script; reproducibility does not depend on an external log. The script calculates gamma expectations by adaptive quadrature, checks the finite integration-by-parts and spectral-bias identities, compares the strict inequalities, tests the asymptotic constants, and reconstructs the estimator through dense matrix linear solves. It also performs seeded Gaussian experiments to cross-check finite expectations.

The proof is analytic: Sherman–Morrison and Gaussian rotational invariance give exact signal and nullspace means, gamma integration by parts and strict Cauchy–Schwarz give the all-parameter impossibility result, and dominated convergence gives the leading asymptotic coefficients. No finite collection of checks certifies the quantified infinite families. The present record carries no independent audit evidence.
