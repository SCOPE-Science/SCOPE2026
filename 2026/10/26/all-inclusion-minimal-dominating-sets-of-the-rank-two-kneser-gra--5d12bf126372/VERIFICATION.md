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

# Verification of the rank-two Kneser classification

Run the included programs with standard Python 3 without additional packages:

```
python3 check_exhaustive.py
python3 check_structural.py
```

The exhaustive script checks all subsets of the \(\binom n2\) Kneser vertices at \(n=5,6,7\), with the correct closed-neighborhood domination predicate and deletion minimality. Its final line is `EXHAUSTIVE_CHECK_OK`. The structural script constructs all five combinatorial templates, confirms no duplicates, checks domination and each deletion directly for \(n=5,6,7,8,9\), and ends `STRUCTURAL_CHECK_OK`. Their captured full standard output is included in `exhaustive_output.txt` and `structural_output.txt`.

Observed total numbers are \(27,203,1029\) in the exhaustive range and \(27,203,1029,3676,10425\) in the structural range. The general theorem relies on the vertex-cover criterion and graph-theoretic argument stated in `RESULT.md`, not on extrapolating finite computations. Exact originality cannot be machine-certified by code; independent external review has not been performed.
