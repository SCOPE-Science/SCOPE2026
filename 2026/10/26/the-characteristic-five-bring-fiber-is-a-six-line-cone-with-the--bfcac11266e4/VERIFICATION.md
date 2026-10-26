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

# Reproducible finite checks
Execute `python3 verify.py` from the directory containing the enclosed verification program; it requires only Python's standard library. The completed execution returned:

```
F_5: points=31 (expected 31)
F_25: points=151 (expected 151)
directions [(1, 2, 3), (1, 2, 4), (1, 3, 2), (1, 3, 4), (1, 4, 2), (1, 4, 3)] PGL2-action 120 delta 9
VERIFY_OK
```

The checker enumerates the six distinct \(\mathbf F_5\)-rational conic/cubic intersection points, tests the Jacobian-minor transversality criterion, checks both transformed equations at each affine four-tuple, enumerates the full six-point \(S_5\)-action, counts all points of \(\mathbf P^3(\mathbf F_5)\) and \(\mathbf P^3(\mathbf F_{25})\) lying on the curve, and evaluates the Hilbert polynomial of a \((2,3)\) complete intersection. Field extensions beyond \(\mathbf F_{25}\) and all geometric assertions are proved by the symbolic and scheme-theoretic arguments in `RESULT.md`, not extrapolation from finite checks. There is no independent audit or external certification.
