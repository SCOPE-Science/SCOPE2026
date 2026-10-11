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

# Exact verification

Run the standalone standard-library checker with `python verify.py`. It expands and compares every polynomial coefficient of the analytic squared-defect identity, including both diagonal-square and off-diagonal-square contributions. It also independently checks the positive-definite \(2\times2\) square-root formula via Cayley–Hamilton and the exact rational witness with squared norms \(803/34\) and \(233/10\), giving difference \(27/85\).

The analytic proof in `RESULT.md` establishes the entire parameter interval and all endpoints. A successful checker is an algebra replay of a proved identity, not independent validation, a survey of all possible matrices, or a replacement for checking the mathematical hypotheses.
