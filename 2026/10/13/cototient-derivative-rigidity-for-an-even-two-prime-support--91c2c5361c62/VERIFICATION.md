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

The source file `verify.py` was run with standard Python. It independently constructs least-prime-factor tables, factors each integer, computes Euler's totient and the arithmetic derivative, compares the direct equation to the proposed two-branch characterization, and checks the auxiliary equations for odd inputs.

```text
VERIFY_OK complete_n=200000 two_support_checked=21172 two_support_hits=[12, 44, 332]
ODD_U_CHECK_OK u_le=50000 half_port=[1, 3, 21, 903, 23529] primary_odd=[1]
```

Run using `python3 verify.py` from the directory containing that file; no third-party packages are needed. The two finite bounds are precisely as displayed, and no absence statement beyond either bound is inferred. The unrestricted theorem follows from the symbolic argument in `RESULT.md`. Auxiliary-squarefreeness is likewise proven symbolically, not inferred from these counts. No independent review or external certification is claimed.
