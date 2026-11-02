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

# Verification of the pinned damped-Jordan timing result

Run `python3 verify.py` with Python 3.10 or later. No third-party packages or external files are needed. The checker performs 1,404 exact rational Cauchy--Binet identities, a finite collection of stationary-root and boundary diagnostics for \(b\) below, at and above one, high- and near-critical asymptotic checks, and equal-replication invariance checks. It reports 20,714 assertions.

The symbolic part establishes event-pair identities for tested rational inputs; the mathematical proof in `RESULT.md`, not the finite computation, establishes the full continuum of horizons and equality cases. Numerical root tests do not prove the existence, uniqueness or asymptotic expansion of arbitrary real roots. No independent audit has been performed.
