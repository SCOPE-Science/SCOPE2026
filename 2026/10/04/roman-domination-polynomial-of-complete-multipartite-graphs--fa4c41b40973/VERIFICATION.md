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

The proof is complete: with no label 2 only the all-one assignment works; with 2s in at least two parts every zero sees a 2 outside its part; with a unique 2-containing part, feasibility is exactly absence of zeros in that part. The generating-function terms are precisely these disjoint cases. The minimum weights/counts follow by exhausting weights 2, 3 and 4. The packaged exhaustive checker verifies every complete multipartite isomorphism type through order ten, but the universal claim rests on the symbolic partition.

## originality

PASS

Originality passes for the full all-function weight enumerator. Classical sources define Roman domination and study the minimum/forcing parameter; recent Roman-domination-polynomial work found in the searches concerns other graph families. Resultary returned related Roman variants on complete multipartite graphs but no earlier ordinary all-function formula.

## value

PASS

A complete weight enumerator is a natural strengthening of the classical minimum Roman domination parameter and gives every feasible-labeling count for arbitrary multipartite part sizes, together with exact minimum-function counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
