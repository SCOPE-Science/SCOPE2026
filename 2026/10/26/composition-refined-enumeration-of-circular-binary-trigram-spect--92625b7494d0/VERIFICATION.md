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

Run `python3 verify.py` beside `RESULT.md` using Python 3 standard library. The program constructs cyclic triples with wraparound, independently enumerates every word of length one through eighteen in composition classes, tests the explicit vector parametrization for each class, and compares with the fixed-composition sum. It then computes coefficients of the displayed univariate rational function using a completely separate integer denominator recurrence through degree 120 and checks against the structural sum.

Expected final output: `VERIFY_OK: 18 word lengths, all fixed compositions; 120 rational coefficients`.

The argument for *every* length relies on the mathematical proof's Eulerian equivalence and finite geometric-series identity. These computations test rather than replace that argument. This is a mathematical reproducibility check, not an external or independent audit.
