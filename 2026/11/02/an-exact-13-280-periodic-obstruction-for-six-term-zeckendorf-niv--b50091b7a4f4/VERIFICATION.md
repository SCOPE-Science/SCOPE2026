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

The exact standalone checker `verify.py` reproduces the local congruence results. It verifies Fibonacci modulo-p period invariance over two consecutive full index periods, then tests three prime cutoffs. Its expected terminal message is:

```
VERIFY_OK period=1680 counts=210,112,78 final_density=13/280 local_sieve_only=YES
```

All computations use standard Python integer arithmetic. The mathematical argument that a residue classification modulo 1680 proves a statement for all indices is supplied in RESULT.md. The published two-shape structural premise is not independently re-proven by the program. Local admissibility is strictly weaker than existence of a six-term Zeckendorf–Niven progression.
