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

# Reproduction and verification

Run the included standalone scripts with a Python 3 standard-library interpreter:

```
python3 verify_grid.py
python3 verify_walks.py
```

`verify_grid.py` constructs explicit vertices and separately directed predecessor/successor adjacency lists, performs exactly \(\lceil m/2\rceil\) simultaneous refinement rounds, checks equality with coordinate-multiset classes, verifies multinomial class sizes, and checks \(\binom{m+d}{d}\) distinct colours. It covers 41 configurations and 21,546 vertices in its stated finite bounds.

`verify_walks.py` independently computes descending and ascending directed walk counts by integer-valued exponential-generating-function convolution, verifies pairwise distinct signatures of all coordinate multisets for 88 configurations with 45,731 profiles, and tests the one-dimensional lower-round collision criterion for chain lengths through \(m=29\).

The exact recorded outputs appear in `verify_grid.out.txt` and `verify_walks.out.txt`; both were generated from these packaged scripts. The general proof is in `RESULT.md`, in particular the formal power series coefficient induction. Finite numerical checks alone do not prove all quantified cases.
