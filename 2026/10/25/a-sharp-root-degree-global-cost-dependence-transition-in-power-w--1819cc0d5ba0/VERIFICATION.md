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

The exact-rational verifier `verify.py` completed 259 tests, covering five integer power-weight exponents and all tree sizes from 2 through 7 by exhaustive independent-parent enumeration, finite telescoping identities, and finite Bernoulli root-degree identities. Run with `python3 verify.py`; no third-party package is needed. The expected stdout is in `verification_output.txt`.

The analytical statements beyond the enumerated sizes require the martingale innovation identity, the Bernoulli triangular-array central limit theorem, finite-sigma-field approximation for joint independence, and absolute convergence of the displayed covariance series. Finite checks corroborate the finite formula but do not prove infinite-size convergence. No independent audit has been performed.
