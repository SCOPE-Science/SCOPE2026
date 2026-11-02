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

# Reproducible checks and their scope

Run `python3 verify.py` with a standard Python 3 installation. No third-party packages or external data are needed. The program implements the exact two-stage construction (path/cycle extrema, then implication strongly connected blocks) and independently enumerates every binary assignment for small verification instances.

Successful outputs from the included program:

```
exhaustive path/cycle constraint systems: 10843
random feasible-incidence systems: 1150
sharp degree-three counterexample: four sites, three residents, sizes {1,3}
large construction: 10000 candidate sites; feasible requested count verified
```

Each small case compares the attainable cardinality spectrum, minimum and maximum, and all requested cardinality witnesses with brute-force truth. Random instances may contain unary and pair constraints. The seven-vertex degree-three obstruction is checked by exhaustive solutions of its three displayed equations. The 10,000-site test checks the constructed witness against every local constraint. The exact general complexity and no-gap assertions rely on the mathematical proof; finite tests neither establish asymptotic bounds nor exhaust all finite networks.

No independent audit or independent validation has been performed.
