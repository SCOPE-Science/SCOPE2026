---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Translate to centers 0,d and scale each nonzero coordinate to 1 by a node-metric isometry. At d=0, pairwise star overlaps share one nonloop coordinate, and no three contain a nonzero common word. For τ>2 no two stars can support d. At τ=1, the two possible singleton covers of a lone nonloop edge give the two-star union. For a unique singleton cover v, only the two-spoke loopless support admits a two-star decomposition avoiding v; each orientation of its two other endpoints adds exactly q−1 points outside V_v and these additions are disjoint. At τ=2, each oriented cover gives a q-point affine line. Coincidence of one index gives a unique intersection via the common off-star edge, while coincidence of neither requires two nonzero disjoint edges, forcing exactly the matching support. Outside that case three pairwise intersecting lines would need a common first or second index i and three distinct partner stars; their common nonzero off-star support is impossible. The matching has two disjoint groups of four lines, each with one shared point. This proves 2qc−2h+2m, including the correction to ordinary pairwise subtraction. Independently computed the ordered differences of one-ball words, tabulated multiplicities, and matched every unit-valued support for (n,q)=(4,2),(4,3),(4,4),(5,2), 35,840 cases in total, via branches/reproduction/overlap.py. The uniform result rests on the affine proof, not the finite sample. The frozen verifier was inspected, not executed.

## originality

PASS

The centered-ball volume and unshifted star geometry are prior and explicitly attributed. The supported distinct claim is the exact support-specific intersection for two different centers of radius-one balls in this looped node metric. Neither the primary centered-volume result nor the strongest indexed different-metric two-center formula supplies the two-cover incidence count or its matching correction.

## value

PASS

Two-center ball multiplicity is a natural coding-geometric invariant in a node-failure model, and distance alone provably loses information relevant to it. This is a complete uniform classification at the first nontrivial radius, with a structural reduction to two-cover incidences and an exceptional matching concurrence. It determines exact ambiguity sizes without enumerating the ambient graph words. No new packing bound is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
