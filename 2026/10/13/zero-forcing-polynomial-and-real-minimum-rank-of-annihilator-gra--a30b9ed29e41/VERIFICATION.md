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

The standalone `verify.py` artifact was read from its packaged path before replay.

The checker first works only with the published six-class quotient and exhaustively verifies its forcing-profile census. For \\(q=2\\) and \\(q=3\\), it then constructs the full ring \\(\\mathbb F_q^3\\), computes annihilators as literal subsets of the ring, and creates edges using Badawi's defining condition rather than the claimed class rule.

For both direct ring graphs it verifies the class sizes and every class-to-class adjacency. It exhaustively enumerates all vertex subsets to reproduce the complete zero forcing polynomial.

For \\(q=2\\), the six explicit vectors in `RESULT.md` are converted to their Gram matrix, whose complete off-diagonal pattern and exact rank \\(3\\) are verified. For every tested \\(q\\ge3\\), the triangular-prism quotient adjacency is blown up according to the two class sizes; exact rational row reduction gives rank \\(4\\), with every graph-pattern entry checked.

Exact replay output:

```text
type_profile_counts= {0: 1, 1: 6, 2: 15, 3: 20, 4: 12, 5: 0, 6: 0} size4_Aclass_distribution= (3, 6, 3)
q=2: N=6, class_sizes=[1, 1, 1, 1, 1, 1], polynomial={3: 14, 4: 15, 5: 6, 6: 1}, witness_rank=3
q=3: N=18, class_sizes=[4, 4, 4, 2, 2, 2], polynomial={14: 864, 15: 504, 16: 132, 17: 18, 18: 1}, witness_rank=4
q=4: N=36, class_sizes=[9, 9, 9, 3, 3, 3], predicted_polynomial={32: 11664, 33: 3672, 34: 513, 35: 36, 36: 1}, witness_rank=4
q=5: N=60, class_sizes=[16, 16, 16, 4, 4, 4], predicted_polynomial={56: 76800, 57: 15680, 58: 1392, 59: 60, 60: 1}, witness_rank=4
q=7: N=126, class_sizes=[36, 36, 36, 6, 6, 6], predicted_polynomial={122: 1143072, 123: 128520, 124: 5940, 125: 126, 126: 1}, witness_rank=4
VERIFY_OK
```

The direct finite tests corroborate the arbitrary-prime-power proof. The general result itself follows from the published six-class decomposition, the complete quotient peeling argument, and the standard maximum-nullity inequality.
