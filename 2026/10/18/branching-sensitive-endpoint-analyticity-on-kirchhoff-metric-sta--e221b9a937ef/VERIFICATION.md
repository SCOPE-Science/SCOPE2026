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
Run `python3 verify_star.py` using Python 3 and its standard library. The included finite numerical checker passed 71 deterministic assertions, checking the Gaussian constant, the one-dimensional norm representation, degree monotonicity at multiple spatial points, the operator-kernel heat-scaling identity at several times, and approximations to the limiting degree behavior. Its quadrature and scalar maximization are exploratory, not certified enclosures.

The analytical verification is in `RESULT.md`: the kernel comes from the Neumann/Dirichlet decomposition, exact endpoint norms from absolute Gaussian row integrals, strict monotonicity from the sign-change interval, and the first-order asymptotic from a dominated-convergence argument along spatial maximizers. No independent audit has been performed.
