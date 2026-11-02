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

Run `python check_inverse_extremal.py` with Python 3.9 or later. There are no third-party dependencies.

The script enumerates all weakly increasing maps in dimensions one through six. For each ordered pair it evaluates both semigroup inverse identities by direct function composition; it then reconstructs the independent block-gap degree formula and compares their integer values for every input map. For every rank in those dimensions it also compares exact ordered-inverse-pair totals with the claimed squared binomial formula. It checks the global maximum and the count of elements attaining it.

Independently of direct pair enumeration, it evaluates the balanced-composition rank bound and the closed global maximum and extremizer-count formulas in every dimension from two through five hundred, including the predicted maximizing ranks. Expected end marker: `VERIFY_OK`.

The direct enumeration is exhaustive only in dimensions at most six; the 500-dimension loop verifies an integer formula against an independent finite maximization, not all transformations. Neither numerical test independently verifies the infinite-family theorem. The symbolic argument in `RESULT.md` supplies the proof, and the historical originality assessment remains qualified.
