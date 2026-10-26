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

The standalone standard-library script `check_ewens_sparse_runs.py` was executed from its actual package source with Python 3 and returned the exact line `EWENS_SPARSE_FINITE_OK 100724 36 12 214`. Its 100,724 weighted finite colourings, 36 distinct-run expectation comparisons, 12 normalizations and 214 two-marker local neighbourhood checks passed.

The asymptotic proof is independent of this finite enumeration. It rests on explicit Ewens factorial moments, elementary fixed-window overlap estimates, canonical mark-cluster factorial moments, bounded-degree Hanf locality, and a first-order run-existence detection family. No verification beyond these checks or independent scientific audit is claimed.
