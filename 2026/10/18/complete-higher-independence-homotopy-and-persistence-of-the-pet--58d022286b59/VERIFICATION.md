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

# Finite verification

From the directory containing these files, run:

```sh
python3 verify_petersen.py
python3 crosscheck_petersen.py
```

Both programs use only Python 3's standard library. `verify_petersen.py` reconstructs the graph from the ten lexicographically ordered two-subsets of a five-point set, visits every one of its 1024 vertex masks, constructs and checks the acyclic matchings at each of nine stages, and verifies the exceptional integral four-cell attaching matrix has a determinant-one maximal minor. It also executes a complete reduced \(\mathbb F_2\) persistence reduction on 1024 augmented chain columns. A valid run ends with `ALL CHECKS PASSED`.

`crosscheck_petersen.py` uses independent graph-traversal and modular boundary-rank implementations. It checks homology in characteristics \(2,3,5,7\) at all ten stages and independently computes the nonzero inclusion rank in degree three from parameter \(2\) to parameter \(4\). A valid run ends with `ALL INDEPENDENT CHECKS PASSED`.

The source code is the finite reproducible certificate: a saved console log alone would not establish the result. The checks prove only the exhaustive ten-vertex finite classification and the stated field-specific persistence. They are not an external audit and do not establish a general theorem for arbitrary graphs.
