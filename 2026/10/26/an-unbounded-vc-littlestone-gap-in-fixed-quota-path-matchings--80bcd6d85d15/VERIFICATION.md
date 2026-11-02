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

For one P8, selecting three nonadjacent edges among seven yields exactly ten edge sets. A direct trace calculation finds a shattered pair but no shattered triple, so VC=2; an independent recursive version-space game finds Ldim=3, with ten hypotheses ruling out depth four. For all paths of at most six edges, an exhaustive exact all-ranks check finds no Ldim >=3. For product classes on disjoint ground sets, VC and Littlestone dimensions add: a shattered set restricts to shattered sets in each coordinate, and adaptive trees can be combined; for the upper bound on sequential depth the standard finite game rank has additivity under product of independent label domains. Thus disjoint s-fold products have 2s and 3s, with precise per-component quotas. Independently reconstructed every source tree and tested the finite base/marginal path cases. No claim about a *single global* fixed quota across components or arbitrary graphs.

## originality

PASS

The finite ten-matching P8 witness, its sharp small-path minimality, and its graph-specific VC/Littlestone gap are not stated by the materially inspected learning-theory sources. The general inequality Ldim <= log2|C| and direct-product additivity are standard and must not be presented as new. The infinite gap s is a consequence of the finite base gap; originality is restricted to the particular matching incidence witness and its minimal path threshold. Priority remains qualified because a prior equivalent finite concept class might have appeared under online matching prediction or shattering-tree terminology.

## value

PASS

The exact disparity on a natural finite combinatorial family demonstrates a structural separation of static and adaptive prediction for *fixed-rank matchings*, with the smallest possible path size for adaptive depth three and a parametrized sequence whose gap grows linearly. The product extension is elementary, but the minimal graph-constrained witness and its full static/adaptive certificate are motivated by complexity of learning matching hypotheses, not an arbitrary unmotivated slice. The result does not claim a new general VC/Littlestone inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
