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

# Exact checks and limits

The checker `verify.py`, run alongside `certificates.json`, reconstructs all canonical rotation classes and deletion-shadow sets for binary lengths one through nine. It verifies all explicit integer codewords, disjointness of their shadows, each rational output-shadow dual inequality, and equality of integral and fractional optima through eight. For length nine it checks each of the 36 fractional-packing capacities, all 60 fractional-cover inequalities, their common exact value \(41/4\), all pairwise edges within the 19 certified conflict cliques, all 60 weighted clique-cover inequalities, and total weight \(59/6<10\). The resulting integer upper bound is nine, matching the code witness.

Executed test: `python verify.py` returned `VERIFY_OK; integral profile=1,2,2,3,3,5,6,8,9; F(9)=41/4; clique_bound=59/6`.

The proof is finite and completely enumerates the domains it asserts. The checker is not a test of larger blocklengths, historical priority, practical DNA performance or independent external audit.
