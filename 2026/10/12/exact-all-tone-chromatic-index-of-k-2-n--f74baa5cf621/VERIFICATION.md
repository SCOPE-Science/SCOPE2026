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

The theorem is proved symbolically in `RESULT.md`. The critical lower-bound facts are: the \(n\) labels on one degree-\(n\) star are pairwise disjoint; a label on the other star is disjoint from its matched label and can meet each of the other \(n-1\) labels in at most one color; and the labels on the second star are themselves pairwise disjoint. These facts force \(n\max\{0,t-n+1\}\) colors outside the first-star palette.

The construction in `verify.py` uses the same modular labels as the proof and checks all relevant pairwise intersections. It was run over \(1\le n,t\le80\). This is a finite consistency check, not a substitute for the universal proof.

Expected replay output:
`ALL CHECKS PASSED; construction_cases=6400; n_range=1..80; t_range=1..80; boundary_star_cases=80; boundary_C4_cases=80; t1_t2_cases=158`

No claim is made for complete bipartite graphs with first shore larger than two.
