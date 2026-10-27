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

# Verification scope

The artifact `VERIFY.py` is a self-contained Python 3 script requiring only standard-library modules (`fractions` and `math`). Run `python3 VERIFY.py` from this package directory. It was executed successfully and printed `VERIFIED: 132051 exact rational/integer comparisons`.

The test suite confirms for finite triangular matrices the difference-matrix inverse identity, an exact rank-\((j-1)\) approximation with a residual block bounded by \(\lceil N/j\rceil\), and the direct rational identity for \(S^{*m}CS^m-C\) at sampled finite indices and shift orders. It checks dyadic slab reconstruction exactly. The matrix inequalities apply in all dimensions by the analytic construction in RESULT.md. The finite checks are not an exhaustive enumeration of parameters or a computer proof of Schatten membership at infinite dimension.

The analytic proof covers every real \(\alpha>1\), all admissible complex coefficient phases, and all real exponents \(p>0\). Its reliance on the standard Schatten quasi-ideal power triangle inequality for \(p\le1\), singular-value approximation bounds, and tail continuity for \(\mathcal S_p\) is explicit. Publication priority and independent audit are separate unresolved matters.
