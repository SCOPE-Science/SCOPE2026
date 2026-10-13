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

# Computational verification and mathematical limits

The accompanying `verify.py` requires Python 3.9 or later and `mpmath` as declared in `requirements.txt`; run it using `python verify.py`. At 75 decimal digits it checks 15 symmetric beta shape values, independent numerical differentiation of the special-function KL expression, Gaussian projections at off-target parameter choices, four trigamma-bound sample points, three large-shape diagnostics and six odd-sample median identities. The script prints a `PASS` line and two representative numerical values when successful.

Critical universal steps do not rely on finite sampling: differentiating the beta entropy establishes equation (2) of `RESULT.md`, the integral formula with strict AM–GM yields the decisive bound \(\psi_1(a)-\psi_1(a+1/2)<2/(2a-1/2)^2\), and the algebraic difference equals \(9/4\). The limit is derived from Stirling and trigamma asymptotic series, not extrapolated from the numerical diagnostic. None of the finite tests proves originality or establishes behavior outside the stated symmetric beta family.

An updated journal treatment of the motivating order-statistics entropy problem has only been examined at the abstract level; the accessible preprint has been inspected in full. The priority comparison remains subject to independent review.
