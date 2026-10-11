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

The complete argument is the five-step algebraic proof in `RESULT.md`. Independently, `verify_john_biclique.py` reproduces direct facet tangencies, positivity, John first/second moments, and spectra on a finite grid. Executing `python3 verify_john_biclique.py` with NumPy installed reports: `OK: 169 numeric dimension pairs, 10647 facet contacts, 12 rational star instances, 168 exact rational contacts`. The rational instances use exact fractions and Gaussian elimination. Finite checks cannot certify the entire family or literature priority. The maximum-volume and uniqueness assertions are proved by John's contact criterion; an independent audit has not been performed.
