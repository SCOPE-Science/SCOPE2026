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
# Reproducibility and boundaries

Execute `python3 verify.py` using Python 3.10 or later from the same directory as this document. The checker requires no external dependencies, network access, random seeds, or external data. It performs 25 deterministic numerical checks: nine stationary Laplace-transform recursion identities, twelve noncritical small-memory comparisons over four distinct moment orders, and four critical logarithmic-coefficient slope comparisons. All completed successfully.

The computation approximates positive Mellin integrals by Simpson quadrature after a logarithmic change of variables. It cannot independently verify the infinite product, the asymptotic uniformity, the finite-sample integrability classification, or any universal quantifier. These are established in RESULT.md by exact Gaussian transform identities, polar integration, and explicit dominated-convergence arguments. Floating-point results are not proof certificates, and the independent mathematical audit is not performed.
