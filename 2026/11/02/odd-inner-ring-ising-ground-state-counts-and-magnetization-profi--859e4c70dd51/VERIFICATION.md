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

# Reproducibility

Run `python3 checker.py` with Python 3 and the dependencies in `requirements.txt`. The executable constructs the transfer matrix and the finite generalized Petersen graphs directly from their definitions, without importing any precomputed tables.

The following checks were actually executed successfully:

- Exact symbolic construction and comparison of the two lowest determinant coefficients over integer polynomials.
- Exact verification of the odd-part rational identity giving the Fibonacci-squared-index coefficient.
- Independent symbolic verification of the magnetization-weighted determinant and its three-term odd component.
- Exhaustive labelled-graph spin tests for circumferences \(n=6\) and \(n=8\) (the latter an adjacent parity control), matched against the transfer matrix.
- Exact min-plus transfer comparisons at each even circumference \(n=6,8,\ldots,202\), including all 50 available \(n\equiv2\pmod4\) cases.
- Exact full magnetization-resolved transfer comparisons at \(n=6,10,\ldots,50\), testing each \(0,\pm4\) multiplicity and absence of other magnetizations.

Recorded output:

```
weighted determinant odd part and magnetization support: PASS
symbolic determinant coefficients E0/E1 and odd Fibonacci identity: PASS
brute graph vs transfer, n=6: (4, 36), PASS
brute graph vs transfer, n=8: (4, 28), PASS
99 exact transfer comparisons for n=6,8,...,202: PASS
12 exact magnetization-resolved transfer comparisons n=6,10,...,50: PASS
VERIFY_OK
```

The infinite theorem follows from the proof, not from the finite test range. Independent scientific audit and independently conducted validation have not been performed.
