---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Direct shore occupancy gives 2-dominance iff (a=s or b>=2) and (b=t or a>=2). Pre-existing theorem C2(K_s,t)=t+1 for 3<=s<=5 gives exact excess s-1<=4, so all possible nonsingleton block multisets are finitely enumerable. Independent complete occupancy enumeration for twelve required base (s,t) pairs returns exactly 1,2,4 templates: s3 (2,1); s4 (3,1) or ((2,0),(2,1)); s5 (4,1), ((2,0),(3,1)), ((2,1),(3,0)), ((1,2),(2,1)). For t>=2(s-1)+2 any two blocks combined cannot cover all B and >=2 B-singletons remain, so same templates stabilize; this is the nonfinite step. Falling-factorial label counts give 3t,10t,25t+15t(t-1)(t-2), with every block unlabeled and every vertex labeled. Verified finite template candidates independently; the established numeric optimum is used with credit, not claimed new.

## originality

PASS

Brešar–Henning–Samadi Theorem5.2 already solves the numerical 2-coalition number C2(K_s,t) for all bicliques and constructs witness partitions; the original scalar claim is fully covered. Its proof does not give the exhaustive optimizing occupancy profiles or labeled multiplicity counts for s=3,4,5. Jafari–Alikhani–Bakhshesh defines k-coalitions, while double-coalition literature uses different domination. A well-motivated structural/enumerative refinement remains original under inspected source coverage, with unindexed enumerator risk.

## value

PASS

A natural exact count and structural classification of all extremal partitions for three complete infinite parameter regimes of complete bipartite graphs, refining a solved scalar optimum. The linear-to-cubic optimizer multiplicity transition at s=5 and structural mixed-block reason are meaningful combinatorial phenomena; not a one-off recomputation of C2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
