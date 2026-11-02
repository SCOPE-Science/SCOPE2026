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

# Reproducible checks

Run `python3 check_rook_old.py` using Python 3.8 or later. No external packages are required. The program constructs the exact open neighborhoods of the \(m\)-by-\(n\) rook graph, enumerates every candidate subset, checks that selected cells each have precisely one selected neighbor, and checks that all selected-neighbor signatures over **every** cell are nonempty and pairwise different. It compares this direct implementation with the proposed exact count.

The seventeen checked board sizes are \((1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)\), totaling 1,501,038 subsets. The direct counts include \(C_{2,4}=6\), \(C_{2,5}=30\), \(C_{3,3}=9\), \(C_{3,6}=90\), and \(C_{4,5}=180\), with zero values for all other tested boards with both dimensions at least two. All seventeen cases passed in a direct run.

The proof covers all \(m,n\ge2\) by disjoint-path structure and signature injectivity; the finite enumeration is an independent diagnostic, not an infinite certificate. The code-size polynomial follows from the proved classification. Priority against unindexed results is not established by computation. Independent mathematical audit has not been performed.
