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

# Reproducible checks

Execute `python3 verify.py` using the Python standard library. The program checks the direct two-by-two generalized Nyström residual against the orthogonal-residual/left-Gaussian factorization for seeded independent Gaussian samples. It also verifies exact \(q=2\) moment factors using gamma functions and numerical angular integration, and compares the \(q=1\) logarithmic leading law at a small parameter.

The finite executable tests do not demonstrate infinite-moment divergence, almost-sure behavior, or the asymptotic regimes for arbitrary real exponents. Those claims rely on the analytical normal-ratio density, elementary beta integrals, and dominated-convergence/boundary-layer arguments detailed in RESULT.md. The identity \(\mathbb ET_h^2=((k-1)/(k-2))h\) is proved symbolically by angular integration, not inferred from Monte Carlo data. No independent scientific audit is represented as having occurred.
