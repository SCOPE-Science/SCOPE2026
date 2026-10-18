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

# Reproduction and limits

Run `python check_24cell.py` with Python 3 standard libraries. It constructs exact rational kernels using the degree-by-degree Chebyshev recurrence and prints PASS after exact row-reduction, characteristic-root polynomial, moment, inverse, and flat-eigenvector checks. The script does not sample positive weights; global weighted optimality and uniqueness follow from the proved two Rayleigh-quotient inequalities for arbitrary strictly positive normalized weights.

The resulting claims are not extended to other point sets, dimensions, or to independently audited publication status.
