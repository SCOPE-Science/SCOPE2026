---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For K_{a,b} with a,b>=3 and t deleted independent cross edges, enumerated shortest paths by pair class: ab-t intact cross pairs contribute one; each removed x_i y_i has exactly (b-1)(a-1)-(t-1) length-three geodesics (choices of two middle indices except the t-1 blocked ones); left-internal pairs contribute b*C(a,2)-t(a-1), right-internal a*C(b,2)-t(b-1), and a+b vertex-length-zero paths are included by definition. Summation simplifies to a+b+ab(a+b)/2+t(ab-2a-2b+3)-t², for the whole connected family. Concavity of t(C-t) proves integer argmax nearest C/2 clipped to permitted interval. For a=b=n, direct substitution yields n=3 maximum t=0, n=4 tie t=1,2, n=5 t=4, and t=n for n>=6. The crown difference n(n²-5n+3) is positive n>=5. Independent BFS path-multiplicity computations corroborated 130 parameter cases (3<=a,b<=7), not used in place of the pairwise proof.

## originality

PASS

The 2026 introducing paper defines geodesic subpath number, observes that deleting perfect matchings can improve it, and poses a broader bipartite extremal problem. The assessed all-a,b,t exact matching-deletion polynomial and maximizers resolve that motivated family, while a nearby diameter-two extremum excludes the t>0 diameter-three cases. No earlier covering identity found in published database queries.

## value

PASS

The geodesic subpath number is a newly studied invariant with an explicit proposed matching-removal phenomenon. This resolves the entire natural one-parameter deletion family, discovers a clean concave optimization and sharp balanced-order phase transitions, addressing a concrete structural question rather than a tiny arbitrary instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
