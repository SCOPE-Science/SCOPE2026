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

# Verification

Run `python3 VERIFY.py` from the directory containing the standalone checker. It uses only the Python standard library and performs a direct formal-context/Galois derivation count, independently of the short-cycle formula. Successful checks produce:

```
VERIFY_OK: exhaustive n=1..4; qualifying context counts [1, 5, 91, 5005]
VERIFY_OK: five isolated four-cycle mark cases z=0..4
```

Exactly 5,005 qualifying incidence graphs with shores of size four satisfy the deterministic structural hypotheses, and the checker examines all of them. It also tests a four-cycle with precisely 0, 1, 2, 3, or 4 vertices of graph degree two. These checks establish finite consistency only. The limiting marked-Poisson law comes from a graph-subcount factorial-moment argument, and the linear coefficient from degree/isolated-edge variance estimates; neither is certified by finite enumeration. No independent audit was performed.
