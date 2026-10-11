---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Any resolving set for a balanced spider must place a noncentral landmark on at least \(q-1\) arms, and one arbitrary noncentral landmark on each of \(q-1\) arms already resolves the tree. For \(\lceil L/2\rceil\le k\le L\), every size-\(q-1\) resolving set leaves one arm whose leaf is at distance at least \(L+1>k\), while one depth-\(L-k\) landmark per arm (and depth one at \(k=L\)) gives a resolving dominating set of size \(q\). For \(k\ge L+1\), depth-one landmarks on any \(q-1\) arms attain the metric dimension. For an arbitrary minimum basis the omitted leaf is at distance \(L+\min d_i\), giving the exact depth criterion and the stated count. The inspected verifier directly checks definitions for \(3\le q\le5\), \(2\le L\le5\), including all smaller candidate sizes and all minimum-set counts; the finite computation corroborates the symbolic proof.

## originality

PASS

The complete 2021 distance-k resolving-domination paper was inspected. It proves the general stabilization \(\gamma_k^r(G)=\dim(G)\) once \(k\) reaches the graph diameter and gives path/cycle formulas, but no spider or subdivided-star treatment was located. The submitted balanced-spider theorem sharpens stabilization from diameter \(2L\) to the exact threshold \(L+1\) and classifies/counts every minimum set thereafter. Resultary search for balanced spiders and distance-k resolving domination returned no earlier equivalent theorem.

## value

PASS

Balanced spiders are a canonical tree family and give a clean example where the general diameter stabilization bound is far from sharp. The exact transition, complete metric-basis compatibility criterion, and minimum-set enumeration provide a natural structural benchmark for the combined domination/resolvability invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
