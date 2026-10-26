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

# Reproducibility of the exact second-moment identity

The mathematical derivation in `RESULT.md` is the decisive proof. The standalone `CHECK.py` runs numerical second-moment evolution independently of the hypergeometric solution and checks all three asymptotic regimes, the critical Euler-integral formula, and the nonreset OU limit. It returned 233 passing deterministic assertions using Python, NumPy and SciPy.

The jump process has a continuous integral observable despite jumps in the position. Its generator yields precisely two moment equations, which are solved by a Laplace transform valid because the integrated variance is bounded by a quadratic function. A separate approximate Euler simulation with 40,000 realizations over duration six yielded variance ratios 1.013, 1.013 and 1.038 for rate ratios 0.5, 1, 2.5, consistent with discretization error. These stochastic observations are not proofs. The published model source concerns marginal relaxation rather than this path average.

No claim of a central limit theorem, almost-sure convergence, independent review or external certification is made.
