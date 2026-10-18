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

## Mathematical checks
The explicit saturated-equality proof handles the real nonconstant boundary case, constants, disconnected tight components, signed boundary marks, integer distance spans and completeness of the canonical walk representation. A finite midpoint decomposition cannot move the magnitude parameters because one mixed tight run fixes their ratio together with the unit-sphere sum. The recurrence tracks boundary-touching for the current run and mixed-run occurrence for all completed runs, with flat transitions admitted only when the previous run has been anchored. Its final-state criterion is exactly the walk condition.

## Reproducible computations
`verify_path.py` implements the recurrence using arbitrary-precision integers. It performs 36 direct brute-force walk-enumeration comparisons for all pairs \(2\le n\le9\), \(1\le d<n\); all passed. An additional numerical half-space intersection of the **original auxiliary-variable polytope** gives the same vertex number for dimensions \(2\le n\le6\); all five cases passed. This numerical check is not a proof. The recurrence is proved for all positive integer dimensions in RESULT.md. Run with `python verify_path.py`; optional numerical comparison requires NumPy/SciPy. No external validation has been performed.

## Limits
The result says nothing about irregularly spaced paths, infinite metric spaces, complex-valued functions, Fortet–Mourier norm balls, or a closed expression for the vertex sequence. Prior mathematical literature can contain unnoticed equivalents. No independent scientific audit was conducted.
