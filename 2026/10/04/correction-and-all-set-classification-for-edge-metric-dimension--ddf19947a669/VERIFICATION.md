---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For any landmark s in a complete multipartite graph and any edge uv, d(s,uv)=0 exactly when s is an endpoint and equals 1 otherwise, because any nonendpoint is adjacent to at least one endpoint. Hence an edge code is precisely the selected endpoint set e intersect S. Injectivity of e -> e intersect S gives the complete classification: with at least three parts the complement T may contain at most one vertex; in the bipartite case a second possibility is exactly two omitted vertices, one from each part. Therefore edim=N-1 for r>=3, edim=N-2 for r=2, with N and n1*n2 bases respectively and enumerator \(z^N+N z^{N-1}+\mathbf 1_{r=2}n_1n_2z^{N-2}\). An independent brute-force distance/code replay through order eight matched this classification for every multipartite type; the actual package verifier at blob e9f2bc7c463d6608e109b7a461857364a661aa6f was also inspected and uses the same exhaustive check through order ten.

## originality

PASS

The 2022 primary paper explicitly states the conflicting value N-r and uses it in K_{2,3,5}; the foundational edge-metric literature does not supply the corrected arbitrary multipartite classification. Fresh formula/erratum searches and Resultary queries found no separate repair.

## value

PASS

This repairs an explicit infinite-family theorem and example in a paper devoted to complete multipartite resolvability. The error changes every r>=3 case, and the endpoint-intersection argument gives the full resolving-set family, basis count, and enumerator rather than a single counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
