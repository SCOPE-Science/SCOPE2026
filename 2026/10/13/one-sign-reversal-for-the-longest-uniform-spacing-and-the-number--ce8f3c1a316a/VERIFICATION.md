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

Run `python3 verify.py`. It uses only the Python standard library, exact rational arithmetic, and 1,089 pairs of independent finite covariance evaluations. It checks the low- and high-threshold sign regions and the special two-spacing case. The verification script does not test or prove the asymptotic at infinity, nor can a finite scan prove universal uniqueness. These conclusions require the analytic derivation in `RESULT.md`.

Independent scientific audit is not performed.
