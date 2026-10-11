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

The theorem concerns *all* real \(s\geq0\). Its proof uses exact slicing of coordinate three-faces, the coarea formula for uniform sums, algebraic substitutions and explicit derivative inequalities. No exhaustive computational sampling of an interval is claimed.

The accompanying dependency-free `verify.py` uses only Python's standard library and exact rational arithmetic. At each of eighteen rational parameter values, including \(s=0,2,4\), it enumerates the intersections of every 5-cube three-face with the hyperplane, constructs each rational polygon hull by orientation tests, computes its projected shoelace area, and verifies that the coefficients of \(\sqrt{s^2+2}\) and \(\sqrt3\) match the closed formula. It also tests the endpoint coefficient table. Run: `python3 verify.py`; expected output:

```
EXACT_RIDGE_FACE_SLICES_OK 18
EXACT_ENDPOINTS_OK
```

The analytic proof is required for correctness for all real parameters; the script is only a finite reproducibility and transcription check. Prior work already determines the endpoint \(s=0\) via an octahedral skeletal polynomial. The older Burton 1980 paper was not fully available for comparison, and independent audit has not been performed.
