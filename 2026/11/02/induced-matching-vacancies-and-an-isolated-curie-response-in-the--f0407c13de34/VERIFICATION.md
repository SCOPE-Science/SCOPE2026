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

The complete finite certificate is `check_icosahedron.py`, requiring only the Python standard library. Execute:

```
python3 check_icosahedron.py
```

The checker constructs the twelve vertices, thirty edges, and twenty triangle faces and exhausts all \(3^{12}=531441\) allowed ternary spins by two independent representations. One computes physical pair products directly; the other enumerates occupied and positive bit masks and evaluates the exact induced-edge formula. The two enumeration tables agree; the strict inequalities, occupancy regimes, critical degeneracies, geometric vacancy rules and Curie coefficient are asserted without floating-point arithmetic.

Observed output from the checker:

```
PASS: 531441 ternary configurations; 531441 mask partitions; 30 edges, 20 faces.
PASS: occupancy minima and multiplicities, sharp inequalities, critical sectors.
PASS: intermediate vacancy sets are exactly 75 induced 2K2 patterns, each with 2 signs.
PASS: first-boundary 462, second-boundary 351, Curie coefficient 40/117.
```

The certificate proves a finite exact result, not an infinite family. The outcome is self-reviewed; an independent audit has not been performed. It does not certify historical uniqueness, finite-temperature response beyond the stated limit, or generalization to other graphs.
