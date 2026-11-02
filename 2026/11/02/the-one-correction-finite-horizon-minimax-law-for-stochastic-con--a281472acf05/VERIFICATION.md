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

# Reproducible mathematical checks

Run `python3 verify.py` using Python 3.9 or later and no third-party dependencies. The expected terminal result is `ALL_CHECKS_PASSED 326741`.

The verifier uses exact `fractions.Fraction` arithmetic to reconstruct Laplacian characteristic polynomials for the six-cycle, three-cube, \(K_{3,3}\), and four-by-four crown graph; to check the claimed stochastic matrices and rational contraction values; and to test the strict compression identity for all rational parameter pairs on a fixed grid. It also tests spectral families of Boolean hypercubes, complete balanced bicliques as the boundary case, and crown graphs across several finite horizons. Finite verification is not a proof of the infinite-dimensional or all-graph quantifiers, which are established by the analytic compression and spectral argument in RESULT.md.

The uniqueness conclusion assumes \(0<\mu<d\) and \(r\ge3\). The exact-consensus boundary \(\mu=d\) is tested only as a consistency check and is excluded from the novelty claim. No independent audit is claimed.
