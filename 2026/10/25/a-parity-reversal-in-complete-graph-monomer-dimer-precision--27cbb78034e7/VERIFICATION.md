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

## Reproducible checks
Execute `python3 check.py` using Python 3.9 or later with no third-party packages. The script independently enumerates weighted matchings for graph orders four through eight, verifies exact first and second moments, compares explicit edge covariance and precision matrices using rational arithmetic, tests the three representation-mode formulas, and checks selected activity asymptotics. Observed output: `PASS: 5039 exact rational assertions`.

## Analytical versus finite evidence
Finite enumeration provides independent checks of formulas at finitely many sizes and activities only. The unrestricted theorem follows from the exact partition-polynomial identities, spectral projectors, and low-/high-activity asymptotic expansions given in RESULT.md. No computer-aided proof of a universally quantified polynomial inequality is claimed. The checker uses only the Python standard library; no external computational services or unpublished data are required.
