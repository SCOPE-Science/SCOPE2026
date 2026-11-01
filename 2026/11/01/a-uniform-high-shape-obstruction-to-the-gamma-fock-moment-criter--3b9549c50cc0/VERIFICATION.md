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

# Verification

The proof is analytic for the entire real range \(\kappa\ge144\). It reduces the impossible moments to two inequalities for the moment-generating function, proves a pointwise exponential inequality, and concludes with a strictly positive rational gap. The proof explicitly justifies exchanging the nonnegative exponential power series and expectation via monotone convergence.

Run `python verify_bounds.py` with Python 3 and no third-party packages. This reproduces the exact Taylor-remainder majorant \(6767/1862\), verifies it is smaller than \(15/4\), and confirms that the positive final gap is \(6887/29360128\). The code is an arithmetic check of particular finite steps, not a substitute for the all-shape analytical argument.

The result is **only** a negative statement about a specific sufficient moment criterion. It gives neither a pair of functions violating exterior domination nor an upper or lower estimate for the actual Korenblum radius beyond existing results. External/independent audit is not performed.
