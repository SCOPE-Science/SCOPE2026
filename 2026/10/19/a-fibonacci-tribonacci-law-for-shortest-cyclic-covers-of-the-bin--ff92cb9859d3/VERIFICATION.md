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

# Reproduction and scope

Run `python3 verify.py` from the extracted package directory. Only Python's standard library is required for the constructive exact-integer verification; installing NetworkX additionally permits independent constrained and **unrestricted** minimum-cost-flow calculations, both covering all window lengths \(3\le k\le10\).

The actual verification run, with NetworkX available, printed:

```
VERIFY_OK constructed_exact_cycles_k=3..16 independent_constrained_and_unrestricted_mincost_k=3..10
```

The code generated all required binary factors, checked the source/target bijection, generated optimal Eulerian cycles and exhaustively verified their cyclic windows through \(k=16\). It also compared every finite count with the rational generating function and found the independently optimized costs identical through \(k=10\). The mathematical proof, not these finite experiments, establishes the all-length theorem. No independent scientific audit or external validation is claimed.
