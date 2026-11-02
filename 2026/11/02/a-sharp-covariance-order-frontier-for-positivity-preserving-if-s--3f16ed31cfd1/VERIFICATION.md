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
# Reproduction and verification

The independent-audit channel has not been performed. The mathematical statement has a complete proof in `RESULT.md`; the executable checks below provide reproducible finite confirmation of its formulae, boundaries and asymptotic coefficients.

Run `python3 verify.py` with Python 3.9+; no third-party packages or input files are required. The script reconstructs the original three IF-SSPRK2 matrix stages directly from the formulas, compares them with the simplified recurrence, verifies exact and discrete stationary equations, enumerates forcing correlations on both sides of the analytic frontier, and checks sign and asymptotic consequences. Its random tests are seeded and reproducible. The script emits a `PASS` line only after every check succeeds.

The strict log-concavity of the Langevin function and universal \(h>0\) and \(Q\succeq0\) quantifiers are established by the mathematical derivation, **not** by sampling. Arithmetic and transcendental evaluations are performed using ordinary floating-point functions in the checker; the theorem assumes exact arithmetic. No external expert validation is claimed.
