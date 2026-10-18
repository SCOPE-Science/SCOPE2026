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

The unrestricted mathematical argument is in RESULT.md. It derives all pinned equilibria directly from the update equations, obtains the triangular Jacobian on the locally pinned opinion region, computes the chain-of-cliques spectral radius from a positive eigenvector, and counts allowable label words by a recurrence.

`verify.py` uses only the Python 3 standard library. It checks 254 binary label words through seven cliques, verifies exact equilibrium equations on the smaller cases, compares numerically computed nonnegative-matrix Perron roots with the closed formula, and checks the full forbidden-run enumeration against its recurrence. An exact rational/radical comparison establishes the different stability regimes of two patterns with the same vaccinated fraction.

For \(\alpha=1/2\) and \(\lambda=4/25\), the test reports \(\lambda r_1=12/25<1/2<\lambda r_2=2(3+\sqrt{13})/25\). It also checks that precisely eight of the sixteen block-labeled disease-free corners on four communities satisfy the strict attracting condition.

The finite computations do not prove the all-size or all-parameter claim. Neither stability at the spectral equality nor the behavior of unmodeled stochastic trajectories was tested or asserted. Independent scientific validation has not been performed.
