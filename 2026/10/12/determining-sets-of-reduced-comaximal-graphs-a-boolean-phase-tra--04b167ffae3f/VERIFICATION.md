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

The standalone `verify.py` artifact uses only the Python standard library and was replayed from its packaged path.

It constructs the reduced comaximal graph directly from the tuple of field orders. For \((2,3)\), \((3,3)\), \((2,2,2)\), and \((2,2,3)\), it exhaustively enumerates graph automorphisms and then checks every vertex subset until the first determining size is reached. The resulting determining numbers and counts of minimum sets agree with the theorem in all four cases.

It also verifies the closed non-Boolean formulas on \((2,3,3)\), \((3,4,5)\), and \((2,2,5,3)\), and constructs optimal Boolean separating families for \(2\le r\le8\).

Exact replay output:

```text
CASE (2, 3) vertices 3 automorphisms 2 determining 1 minimum_sets 2
CASE (3, 3) vertices 4 automorphisms 8 determining 2 minimum_sets 4
CASE (2, 2, 2) vertices 6 automorphisms 6 determining 2 minimum_sets 12
CASE (2, 2, 3) vertices 9 automorphisms 16 determining 3 minimum_sets 8
FORMULA (2, 3, 3) determining 7 minimum_sets 64
FORMULA (3, 4, 5) determining 29 minimum_sets 13824
FORMULA (2, 2, 5, 3) determining 37 minimum_sets 2097152
BOOLEAN 2 determining 1
BOOLEAN 3 determining 2
BOOLEAN 4 determining 2
BOOLEAN 5 determining 3
BOOLEAN 6 determining 3
BOOLEAN 7 determining 3
BOOLEAN 8 determining 3
VERIFY_OK
```

The exhaustive computations validate finite boundary cases. The general theorem is proved by the support-fiber and coordinate-stabilizer argument; no finite experiment is used as an infinite proof.
