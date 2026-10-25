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

The transient subgenerator \(Q\), target-rate vector \(r\), and four rational test times are fully specified in `RESULT.md`. The included script recomputes the order-400 Taylor sums with exact rational arithmetic and asserts the four enclosing intervals. Since \(Q\) is symmetric, \(\|Q\|_2\leq224\); the stated exponential-series tail bound makes the derivative-sign margins rigorous. The state-minimality proof uses the real spectral decomposition of a reversible killed generator and the zero-count bound for real exponential sums.

Limitations: the calculation is a finite exact witness, not a classification of multimodal first-passage laws. The full text of Kijima (1987) was inaccessible; only its abstract was compared, so this remains a residual literature risk. Independent audit and independent validation have not been performed.
