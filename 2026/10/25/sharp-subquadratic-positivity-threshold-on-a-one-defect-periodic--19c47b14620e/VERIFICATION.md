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

# Verification and scope

`python verify.py` (SymPy 1.14.0 as recorded in `requirements.txt`) was run from this package. It passed symbolic determinant, all 20 directed off-diagonal and five diagonal identities, exact polynomial endpoint and asymptotic checks, and 30 exact-rational matrix-sign comparisons across six mesh ratios. `verify_output.txt` contains the output. The matrix is non-symmetric after multiplying the inverse by the consistent mass; the program checks *directed* entries, not only unordered pairs. The sign proof in `RESULT.md` establishes all real parameters in scope.

Reproducibility command: `python -m pip install -r requirements.txt` followed by `python verify.py`. The polynomial checks use SymPy exact rational/domain arithmetic. No finite parameter sweep is offered as an infinite-family proof. Formal independent validation has not been conducted.
