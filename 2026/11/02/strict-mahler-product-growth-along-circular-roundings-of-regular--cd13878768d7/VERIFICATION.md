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

The full mathematical proof is in `RESULT.md`. A reproducible standard-library checker is `checker.py`; run `python3 checker.py` in the artifact directory. It performs 560 finite checks: exact-rational derivative-identity substitutions, independent angular polar-area quadratures using direct vertex maxima, derivative comparisons, and endpoint/asymptotic tests. The verification checks were executed successfully on the bundled source before packaging and again from the package after embedding.

The universal derivative-sign argument does **not** depend on the finite grid: it follows from the positive derivative lower bound and the analytic variance estimate in the proof. Numerical quadrature does not certify infinitely many parameter values. Neither independent mathematical auditing nor externally certified computation is asserted. The small-parameter and large-parameter limiting statements include their explicitly stated fixed-parameter restrictions.
