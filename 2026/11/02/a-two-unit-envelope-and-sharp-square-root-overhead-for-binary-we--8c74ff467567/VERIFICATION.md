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

# Reproducible finite checks

Run `python3 verify.py` in a directory containing the embedded standalone `verify.py`. Python 3.8 or later and only its standard library are required.

On the packaged source, the observed completion line is:

```
VERIFY_OK exact BFS k=2..12; direct/mark equivalence n<=11; constructed bounds and full coverage k<=100,150,200,300,500
```

The breadth-first product-automaton search is exhaustive for each claimed exact finite case; it is not extrapolated to greater lengths. A second implementation of target membership directly scans letters and compares with the zero-marker criterion for every word of length at most eleven. The construction tests cover all target pairs for each stated value of \(k\), but checking finitely many instances cannot prove an all-length claim. The infinite assertions follow instead from the interval-incidence inequality and two-residue construction documented in `RESULT.md`.
