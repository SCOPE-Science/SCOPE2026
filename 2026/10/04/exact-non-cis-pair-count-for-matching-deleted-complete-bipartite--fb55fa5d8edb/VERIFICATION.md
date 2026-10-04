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
The analytic proof classifies all maximal cliques and maximal stable sets of \(K_{a,b}-M_t\). The only mixed maximal stable sets are the \(t\) deleted matching pairs, and for each such pair exactly \((a-1)(b-1)-(t-1)\) surviving edges avoid it. This gives the claimed formula directly.

`verify.py` supplies a separate finite stress test. It constructs the graph from the edge relation, enumerates every nonempty vertex subset, tests clique/stable-set maximality by direct adjacency checks, and counts disjoint maximal-clique/maximal-stable-set pairs. It checks all \(1\le a,b\le5\) and \(0\le t\le\min\{a,b\}\), plus crowns through \(n=6\). Its finalized replay is:

`ALL CHECKS PASSED; parameter_cases=80; subset_candidates_per_family_sum=17672; a,b_range=1..5; crown_n_range=2..6`

The enumeration is finite and does not certify the theorem beyond its tested range. The universal claim rests on the analytic proof. The full text of the 2026 recognition preprint was not available through the accessible primary/OA retrieval path during literature comparison, so originality retains that explicit access risk.
