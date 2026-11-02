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

Execute `python3 verification.py` using Python 3 standard-library modules only. At initial inspection, the source checker passed 71,058 assertions. The checker integrates each degree-three Dirichlet monomial exactly using factorial moments and independently compares it with the closed harmonic formula for every rank in dimensions two through nine. Additional exact rational sign/threshold-profile checks cover sizes two through 350; numerical comparisons report rank fractions at larger sizes.

The rigorous steps required for arbitrary dimension are the ranked-gap simplex change of variables, explicit Dirichlet moments, harmonic-tail algebra, adjacent-rank sign argument, and harmonic asymptotic. The code does not certify the infinite theorem, historical originality, or an independent audit. Scientific limitations are stated in `RESULT.md`.
