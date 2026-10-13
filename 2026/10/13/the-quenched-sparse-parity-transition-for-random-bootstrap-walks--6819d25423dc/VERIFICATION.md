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
# Verification of finite identities

The included `verify.py` uses only the Python standard library and exact fractions. Invoke `python verify.py` in a directory containing that file. It rederives the Bernoulli parity mean through an even/odd recurrence rather than by assuming the closed formula, directly enumerates all active coefficient configurations in small cases, enumerates the input-sign paths to confirm the exact binomial mixture of parity means, and verifies the conditional one-step cross covariance. The packaged checker produced `VERIFY_OK: 684 exact rational parity / covariance assertions`.

The checker has no bearing on the asserted infinite-time almost-sure statements unless accompanied by the analytical arguments in `RESULT.md`. The subcritical limit uses conditional row concentration and a martingale functional central limit theorem, the supercritical claim uses conditional Borel--Cantelli, and the critical claim uses local-time strip estimates, occupation-time convergence, and Lévy's arcsine law. No deterministic coefficient-environment certificate, convergence rate or full critical joint law is claimed.
