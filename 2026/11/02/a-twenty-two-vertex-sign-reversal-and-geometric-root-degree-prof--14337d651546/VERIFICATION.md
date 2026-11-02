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

The exact Markov-recurrence calculation is derived from the uniform-parent growth rule and proved in `RESULT.md`. Run `python3 verify.py` (Python 3.9+ standard library); the observed run passed 637 exact assertions including independent enumeration of all parent arrays with at most nine vertices, coefficient comparisons, and checks at the integer sign boundary.

A finite run cannot establish an infinite-size theorem. The infinite fixed-degree limits follow from the probability generating function, coefficient bounds, and a deterministic Cesàro recurrence, not extrapolation. Historical priority has not been independently certified. No external expert or independent audit was carried out.
