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

# Reproducibility and limits

The proof is mathematical and applies to every finite field \(\mathbb F_q\); the code provides independent finite checks, not a substitute for the projective-line argument.

From the directory containing `verification/`, run:

```
python3 verification/check_all_fields.py
python3 verification/check_graph_spectrum.py
```

Both programs use only Python's standard library. Compare their exact standard output against `verification/check_all_fields.out` and `verification/check_graph_spectrum.out`, respectively. They construct finite fields, symmetric Gram matrices, nonzero square generators, and every ordered natural basis, then recompute the numbers and graph distributions from the definitions. The first checker exhausts all eligible Gram matrices and nonzero generator vectors over fields of orders \(2,3,4,5\); it samples further Gram forms over \(7,8,9,16\), always exhaustively evaluating all nonzero generator vectors for each chosen form. The second checker exhausts odd-prime forms of orders \(3,5,7\), and uses representative forms at \(11,13\). The field extensions are implemented explicitly via irreducible polynomials; these choices and all loops appear in the included source files.

`VERIFY_OK` indicates that every finite enumerated case matched the formulas, not that a higher-dimensional or otherwise extended theorem has been checked. The general proof depends only on finite-field perfection in characteristic two and elementary two-dimensional nondegenerate quadratic forms in odd characteristic.
