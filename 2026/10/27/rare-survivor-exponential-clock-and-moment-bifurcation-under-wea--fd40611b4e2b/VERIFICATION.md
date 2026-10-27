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

## Reproduction

Use `python verify.py` with SciPy installed. The program evaluates the exact original survival expression for a bare exponentially distributed target-search time, and independently uses the elementary exact law for deterministic bare first passage. It compares two turnover magnitudes, three positive macroscopic observation times, and first, second, and third time moments in each example. All 24 comparisons passed when the supplied code was executed.

## Analytical validity and limits

The proof verifies the entire real moment-order range by a single integrable bound; the 24 numerical comparisons are only diagnostic. The exact fixed-rate survival representation, the first-moment discontinuity, and related general mean comparisons are existing results, not independently re-derived novelty. The assertions here require positive fixed birth/death scaling coefficients and a bare first-passage exponential moment. There is no independent mathematical validation or external audit.
