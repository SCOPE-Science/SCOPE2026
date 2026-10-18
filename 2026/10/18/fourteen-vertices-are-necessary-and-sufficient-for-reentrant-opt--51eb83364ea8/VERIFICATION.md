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

# Reproduction

Run `python verification/reentry_check.py` with a Python 3 standard-library interpreter. The script implements exact rational Sturm-sequence root counting and independently enumerates percolation states for the explicit 14-vertex example.

Observed completed output:

```
ALL TREES <=13: profile pairs = 6144 Sturm candidates = 150 0 roots = 140 1 root = 10 >=2 roots = 0
14-VERTEX WITNESS: profiles = (1, 1, 4) (1, 2, 1, 1, 1, 1) Q coefficients = [-1, 3, -1, -1, -1] Q(1/2) = 1/16 two exact roots in (0,1)
BOND ENUMERATION at 1/10 scores 57/500 121111/1000000 optimal B
BOND ENUMERATION at 1/2 scores 5/4 79/64 optimal A
BOND ENUMERATION at 9/10 scores 2313/500 5027031/1000000 optimal B
ALL EXACT CHECKS PASSED
```

The polynomial sign-change argument in `RESULT.md` establishes the 14-vertex witness for every \(p\in(0,1)\). The exhaustive profile enumeration establishes the finite size cutoff. The numerical decimal root values are for orientation only; their exact definition is via the two isolated polynomial roots. The proof does not cover graphs with cycles or vaccines administered during an active epidemic.
