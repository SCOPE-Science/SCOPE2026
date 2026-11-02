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

To reproduce finite checks, save the complete adjacent `check.py` file and run:

```sh
python3 check.py
```

The tested interpreter uses only Python standard-library modules. The actual replay prints `VERIFY_OK assertions= 387`, preceded by the numerical scalar root and constant checks. It compares direct enumeration of all binary strings for selected \(k\), \(n\) and rational \(q\) against exact rational killed-chain recursion. It also compares exact characteristic determinants, tests numerical Perron eigenvalues against the scalar optimum for selected instances, and tracks the limiting constants over increasing spell lengths. These tests are not an exhaustive proof of the continuum or the limit; the proof of the unique optimizer and asymptotic scaling is given in `RESULT.md`. No independent audit or external theorem certification has been performed.
