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

# Reproducible exact computations

`verify.py` is a standalone Python 3 program using only the standard library. Run `python verify.py` and compare its complete stdout bytes with `certificate.json`. The certificate records 155 exact, exhaustive labeled-subset enumerations agreeing with independently coded hypergeometric covariance calculations; 43,608 strict monotonicity checks on a finite parameter grid; exact rational negative/zero/positive examples; and numerical approximations to the limiting roots.

The certified checks depend only on the included program and not on external data, network services, or random seeds. They verify sample cases and implementations. Proof for arbitrary parameter values, uniqueness of the sign transition and limiting asymptotics is the analytic argument in `RESULT.md`, which must be evaluated separately; exhaustive checks on a bounded grid cannot certify these universal statements.
