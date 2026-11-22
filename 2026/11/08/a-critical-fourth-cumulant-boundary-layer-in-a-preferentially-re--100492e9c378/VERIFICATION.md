---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The exact Taylor coefficient identities for the Kummer characteristic function can be checked symbolically in `checker.py`. Direct finite-time Fourier-moment and moment-equation calculations corroborate the fourth cumulant and root position. The proof of a unique finite-time threshold on the compact rate interval instead uses the uniform complex-parameter Kummer remainder and its first rate derivative, as given in RESULT.md. Numerical tests and symbolic checks do not establish this uniform asymptotic theorem by themselves. The fixed-rate critical cumulant constant predates the present finite-time threshold statement.
