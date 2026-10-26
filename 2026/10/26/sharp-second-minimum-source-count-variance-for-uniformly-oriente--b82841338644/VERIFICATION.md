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
# Finite exact verification

Execute `python verify.py` using the Python 3 standard library. The program tests every labeled tree with \(4\le n\le7\) produced by all Prüfer codes. For orders at most six, it compares the variance formula to exhaustive orientation enumeration, using exact `fractions.Fraction` arithmetic. It also verifies the sharp lower bound and equality structure and checks the degree inequalities over a finite consistency range; the unrestricted degree bounds appear in the written proof.

Observed checks:

```
PRUFER_EXHAUSTIVE_PASS 4 min_nonpath_gap 15/64 labeled_minimizers 4
PRUFER_EXHAUSTIVE_PASS 5 min_nonpath_gap 11/64 labeled_minimizers 60
PRUFER_EXHAUSTIVE_PASS 6 min_nonpath_gap 7/64 labeled_minimizers 360
PRUFER_EXHAUSTIVE_PASS 7 min_nonpath_gap 3/64 labeled_minimizers 840
LOCAL_DEGREE_BOUNDS_PASS d=3..1000 (finite consistency only)
VERIFY_OK
```

The unrestricted theorem follows analytically from the proof, not finite enumeration. No external audit was performed.
