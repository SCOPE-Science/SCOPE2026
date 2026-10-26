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

# Reproducibility

Execute `python3 verify.py` with a standard Python 3 installation. The verifier checks the degree-of-exactness moment identities for all four Gauss–Legendre rules and tests that all quadrature nodes and weights are positive. It independently computes weighted Gramian determinants and the pairwise-sine Cauchy–Binet expression across positive and zero damping and multiple phase values. It verifies the two- and three-node resonance formula numerically, the fourth-node root-ratio identity, continued-fraction near-resonances, the eigenvalue upper bound, and the exact undamped continuum determinant identity. The observed output is `VERIFIED 163 assertions`.

These tests use ordinary floating-point arithmetic with explicit tolerances. They are finite diagnostics; the proof of the arbitrary-step strict-positivity assertion, the infinitely many ill-conditioned steps, and the error limit is in `RESULT.md` and relies on exact algebra and continued fractions. No independent scientific audit has been performed.
