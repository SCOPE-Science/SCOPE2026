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

# Finite integral verification

From a directory containing `verify_grid_fixed.py`, run:

```sh
python3 verify_grid_fixed.py
```

The script requires Python 3 and SymPy (tested with 1.14), constructs all admissible orbit vertices and compatibility edges directly, generates every simplex of the fixed-space orbit complex, and checks the face-vector formula. It forms sparse integral simplicial boundary matrices, computes independent mod-two ranks, and independently recomputes full Smith normal forms over \(\mathbb Z\). Its assertions check rank consistency and unit nonzero invariant factors for every case \(3\le n\le8\), with exact highlighted ranks and torsion-free homology at \(n=8\). Expected final line: `PASS complete`.

The uniform face-vector, Euler and connectivity statements have elementary proofs in RESULT.md. The computer calculation has a finite domain only and does not certify claims for larger \(n\). Independent validation has not been performed.
