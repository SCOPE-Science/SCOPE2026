---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The independent-cascade live-edge formulation on a path gives each exterior vertex probability p^j and each interior vertex p^j+p^(b-j)-p^b (two disjoint routes); summation proves the stated influence polynomial for every n>=2 and 0<p<1. Exchanging one tail vertex strictly improves an unbalanced split, yielding the only optimum at each gap. The exact adjacent-gap increment is p^b[1+b(1-p)]-p^ceil((n-1-b)/2). The ratio R_(b+1)/R_b is at most p(2-p)<1, proving strict unimodality over all integer gaps; g_b=(b-h_b)log p+log[1+b(1-p)] is strictly concave, negative near zero and positive immediately left of one, so its unique interior zero yields precisely one threshold for b>=ceil((n+1)/3). Their strict ordering and n=4 p=1/2 follow. Checked direct independent exact adjacent differences and tail balancing in 140 cases; finite checks do not justify universal quantifiers.

## originality

PASS

The novel candidate is the exact all-sizes p-monotone gap phase diagram with strictly increasing roots, not the live-edge model or a path optimization algorithm. Primary general works do not imply it. A plausible exact-object thesis remained inaccessible in full; this is a genuine historical priority risk but no decisive evidence of coverage was found. Best-of-knowledge PASS with this explicit qualification.

## value

PASS

Optimal two-seed placement versus transmission is a canonical influence-optimization question. Exact all-n phase thresholds and successive increasing optimal distance are nontrivial structural information beyond an algorithm or influence submodularity: the four-vertex first transition, ties and every intermediate gap are fully classified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
