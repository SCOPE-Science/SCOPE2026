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
# Reproducibility and mathematical checks

Run `python3 verify_three_layer.py` under Python 3.9 or later; no network access, random seed changes, or third-party packages are needed. The program enumerates all \(2^{n(n-1)}\) directed loop-free graphs for \(1\le n\le4\) and independently calculates reflexive transitive closure. The numbers of configurations satisfying the canonical identity at world counts \(1,2,3,4\) are respectively \(1,4,64,3283\) of \(1,4,64,4096\); satisfying the stronger sufficient half-reachability premise are respectively \(1,4,64,2909\). Every sufficient-case implication was checked.

The checker also compares the exact expected numbers of zero-indegree vertices and the product of numbers of zero-indegree and zero-outdegree vertices with full-sample enumeration under edge probability \(1/2\). Seeded finite simulations at sizes \(20,40,80\), 120 trials per size, compare the canonical identity with the sufficient condition at \(p=(\log n)/n\). These are consistency checks, not the limit theorem.

The proof of the asymptotic result separately verifies the count of outgoing-closed reachable sets, the large-reachability intersection implication, overlap terms in the joint factorial moments, and a rank-bounded EF game for the model-theoretic limit. No independent audit has been performed and no external proof assistant was used.
