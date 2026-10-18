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

# Reproducibility and evidence limits

Run `python3 verify.py` from the directory containing this document. The program uses only the Python standard library and reports 84 exact-formula comparisons computed in floating point, 36 sign checks at the two neutral endpoints, six numerical exponential escapes, and three asymptotic drift checks of 600,000 iterates each. All these completed successfully in the supplied package environment. Check counts describe finite diagnostics, **not** an exhaustive computer proof.

The quantified infinite-time statements rest on the proof in `RESULT.md`: a global nonlinear bound, sign reversal of the tail, a strict contraction on the mean coordinate in the outer region, and a telescoped asymptotic drift. The material reviewed for prior coverage consists of the publicly available complete 2023 primary article (DOI:10.3390/math11061517), closely related public summaries, and statement-level comparison with existing published mathematical results. No external independent validation has been performed.
