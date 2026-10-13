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

The analytic proof is the primary verification. For a set \(S\) in \(K_{n_1,\ldots,n_r}\), every outside vertex in part \(i\) has exactly \(|S|-|S\cap V_i|\) neighbors in \(S\). The proof classifies all proper \(1\)-fair dominating sets from these exact equations and then derives every partition case.

`verify.py` supplies an independent finite check from the definitions. It enumerates every nondecreasing multipartite profile of total order \(2\) through \(7\), every set partition of the vertex set, tests whether each block is an allowed singleton or has a valid coalition partner, and compares the maximum block count or nonexistence with the theorem.

The exhaustive calculation is not used as evidence for orders above \(7\). No computational certificate is needed for the infinite step because the occupancy proof is symbolic.
