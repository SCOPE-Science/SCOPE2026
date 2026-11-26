---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and checks

Run `python3 artifacts/verify_asynchronous.py` with standard Python 3. The program uses `fractions.Fraction` and fixed-seed rational test parameters. It checks the stale and fresh covariance balance, stale covariance eigenvalue identities, two-update forcing positivity and the variance difference. The recorded run reported 6,908 exact-rational assertions.

These checks use the covariance map for independent fair selections and centered noises that are mutually independent and independent of the entire selection sequence. They test identities at finitely many parameter values, not independence in data or the general stability frontier. The analytic proof in `RESULT.md` treats the full parameter range and both sides of the frontier.
