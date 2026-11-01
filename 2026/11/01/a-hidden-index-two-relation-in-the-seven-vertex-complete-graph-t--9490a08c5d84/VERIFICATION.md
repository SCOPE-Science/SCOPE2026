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

Exact verification is supplied by `verify.py` and `verification_output.txt`. The checker builds all 105 cubical square generators, all 105 edge–vertex generators, the 70 triangle-product columns, the 35 local columns, and the ten-term column from their stated combinatorial rules. It tests all chain identities, determines the boundary rank by elimination modulo 3, then obtains actual integer Hermite and Smith normal forms; full homology follows by the rank-and-primitivity proof in RESULT.md. The checker requires Python 3 and SymPy. No external data files, stored matrix files, unbounded searches, or floating-point arguments are required. Independent mathematical audit has not been performed.
