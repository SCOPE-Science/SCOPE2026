---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Convex vertex sets in trees are connected subtrees. A bipartition into two connected parts crosses exactly one edge; conversely each edge cut is convex on both sides. Three noncollinear terminals have a median outside their triple, making each singleton and complement realizable by a branch cut. If one terminal lies between two others, convexity forbids selecting endpoints but omitting middle. On four terminals compatible tree splits cannot realize all crossing 2-versus-2 labelings. Collinear triples correspond bijectively to interior vertices of each endpoint path, counted by W(T)-C(n,2). Star/path bounds follow edge-cut distance contributions. Independent exhaustive enumeration of all 1442 Prüfer-labeled trees n<=6 verified the profile and split characterization. Exhaustive small n alone does not prove arbitrary trees.

## originality

PASS

Thiessen–Gärtner prove general VCdim<=2tw+1, which for treewidth one yields upper bound 3, but do not give coefficientwise shattering profiles in the inspected 2021 article. Anthony–Ratsaby distance-prototype halfspaces are a different concept class. Published Resultary tree–Wiener simplex edge-energy result concerns different Euclidean configuration. The edge-cut and Wiener identities are classical ingredients, but their precise VC shattering-profile identity is not implied by the inspected prior assertions; possible equivalent phylogenetic compatible-split enumeration remains an originality risk.

## value

PASS

Exact shattered-support counts and VC dimensions of the natural geodesic-halfspace learning class recover the classical Wiener metric invariant and distinguish trees beyond a generic upper bound; at fixed order the entire learning profile is equivalent to a metric distance sum. This is a complete natural classification rather than a trivial restatement of VCdim<=3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
