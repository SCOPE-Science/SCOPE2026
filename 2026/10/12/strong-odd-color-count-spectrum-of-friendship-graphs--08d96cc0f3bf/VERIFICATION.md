---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

In any proper coloring center c is fresh and each outer edge has two distinct endpoint colors. Each outer vertex automatically meets odd neighborhood counts because it sees distinct center and partner colors. At c, each outer color has positive odd multiplicity <=k. There must be an even number q of outer colors; q=2 forces both sizes k and is possible iff k odd. For even 4<=q<=2k, choose positive odd class sizes d_i<=k summing to 2k by distributing k-q/2 units among q capacities floor((k-1)/2); capacity is sufficient. A complete multipartite graph with these classes has a perfect matching because largest part <=k, placing distinct colors at each edge. This proves all allowed counts for every k>=2. Independent canonical partition enumeration gave F2:{5}, F3:{3,5,7}, F4:{5,7,9}.

## originality

PASS

The block-graph optimization result encompasses minimum-color computability on F_k, but does not itself determine the feasible spectrum, its missing counts or parity threshold. The inspected cycle-join/one-point-union paper does not furnish the matching spectrum classification. Full block-graph paper unavailable this run, explicitly a residual risk, not automatic originality failure.

## value

PASS

A complete spectrum for a natural block-graph family reveals a sharp parity transition of the minimum and proves gaplessness above that bound in odd steps; useful structural benchmark for the recent general algorithm. The full attainable-count classification is more than computing one easy optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
