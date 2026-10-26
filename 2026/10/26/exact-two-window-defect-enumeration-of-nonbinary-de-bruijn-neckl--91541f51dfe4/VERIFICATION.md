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

# Finite arithmetic checks

Run the standalone `verify.py` with Python 3 and no third-party packages:

```
python3 verify.py
```

The code constructs the directed de Bruijn graph of order \(n-1\) with arbitrary integer alphabet size \(q\), removes the two specified windows, computes the grounded out-Laplacian arborescence determinant by exact fraction-free Bareiss elimination, and applies the BEST factorial product. It compares these values with the exact derived loop/alternation count for nine cases: \((2,2),(2,3),(2,4),(2,5),(2,6),(3,2),(3,3),(4,2),(4,3)\). It additionally exhaustively enumerates necklaces (independent of the graph cofactor implementation) at \((2,2),(2,3),(2,4),(3,2)\) and checks all cyclic factor frequencies. The observed terminal message was:

```
VERIFY_OK tree_cases=9 exhaustive_cases=4 total_checks=13
```

Representative exact totals: \(T_{2,4}=20\), \(T_{2,5}=2816\), \(T_{3,2}=24\), \(T_{3,3}=435456\), \(T_{4,2}=20736\). These tests do not establish the result at untested sizes and do not constitute an independent audit. Infinite correctness rests on the supplied combinatorial proof, the BEST theorem, and the directed matrix-tree identity. The published binary case is prior coverage, not a new result.
