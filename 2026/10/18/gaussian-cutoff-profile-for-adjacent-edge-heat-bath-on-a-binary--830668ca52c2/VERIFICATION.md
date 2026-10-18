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

The exact finite-dimensional checker `verify.py` can be run with Python 3 and the standard library only:

```
python verify.py
```

Its executed output terminated with `VERIFY_OK 2097`. It reconstructs the full exact-rational transition laws for cycle lengths \(3\) through \(8\) for the first four steps; compares every Walsh eigenvalue with the direct distribution; enumerates all subsets to confirm the cyclic-run formula; checks the chi-square regrouping; and reports illustrative \(L^2\) distances at four larger lengths. No simulation, pseudorandom seed, external mathematical package or hidden data file is required. The exact finite checks do **not** prove the large-\(n\) limits; those follow from the geometric-series Fourier-tail inequalities in `RESULT.md`. No separate independent audit has been performed.
