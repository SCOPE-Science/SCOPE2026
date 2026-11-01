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

# Verification performed

The included `check.py` was run with Python 3 and completed with:

`PASS 220411 assertion groups/weighted enumerated moments`

It independently enumerates all balanced domain-wall subsets for cycle orders 4, 8, 12, and 16; compares their exact two-point moments against the rational recurrence; checks the hypergeometric moments, Fourier spectrum, frequency ordering and sharp extrema through order 128; and compares the exact Fourier values against numerical quadrature of the beta-integral representation. Some counters count individual moment comparisons, not independent trials. Analytic positivity, spectral ordering, and the asymptotic estimate are proved in RESULT.md for every permitted order. No external mathematical validation has been performed.
