---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS. For B_r=K_{1,r}□K_2, r≥2, the two adjacent spine vertices and r opposite page pairs form all vertices. Every paired dominating set falls into exactly one of no-spine, one-spine, or both-spine cases. With both hubs, a perfect matching forces either whole selected pages or two opposite singleton pages on distinct pages; with exactly one hub, domination forces its full side and matching permits exactly one omission on the other; with neither hub, all 2r page vertices must be selected. This yields P_r(z)=z²(1+z²)^r+r(r−1)z⁴(1+z²)^{r−2}+(2r+1)z^{2r}. To identify inclusion-minimal sets, test all strict paired-dominating subsets (not just one-vertex deletions): exactly the spine pair and 2r+1 sets of size 2r are minimal. Independent brute-force from original graph definition and recursive exact matching checked all subsets for r=2..6 and coefficients/membership, e.g. r=6 total 557 and 14 minimal; bundled script checks through r=8 and 349,504 subsets. Finite checks substantiate the case proof, not replace it.

## originality

PASS

PASS best-of-knowledge for an exact quadrilateral-book PDS vertex-set polynomial and full inclusion-minimal classification, excluding general paired-domination definitions. The 2021 Alizadeh–Gözüpek primary result classifies equality of upper paired domination and upper domination under bipartite/unicyclic/girth hypotheses, not polynomial coefficients on K1,r□K2. Resultary returned a paired-domination polynomial of CHAIN graphs and a power-domination polynomial of book graphs; neither is this combination of predicate and graph. No direct stronger implication or table covering the B_r polynomial was established. Unindexed book/prism variants remain a residual originality risk.

## value

PASS

PASS. Exact enumeration of a natural family of planar, bipartite, 2-vertex-connected quadrilateral books determines every feasible cardinality and all inclusion-minimal PDS. The contrast between all even sizes in unrestricted solutions and only sizes 2 and 2r among inclusion-minimal solutions gives an arbitrarily long, mathematically motivated gap; it is not a textbook substitution into a generic count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
