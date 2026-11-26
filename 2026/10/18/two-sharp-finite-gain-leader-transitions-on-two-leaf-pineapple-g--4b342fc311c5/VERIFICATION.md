---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Connectivity plus positive diagonal anchors makes the matrix positive definite. With one unit injected at z, split the two ground currents as a and 1−a. Polarizing the L⁺ quadratic form for the net injection gives aR_zx+(1−a)R_zy−a(1−a)R_xy; adding the two ground-leg energies and minimizing over real a gives the stated per-vertex Green diagonal and hence the two-ground trace formula. The core resistances are h=2/(r+1); dangling leaves add their series resistances. For LC the squared resistance-difference sum is 2(1+h)²+2(1−h)²+(r−1), recovering the less immediate table entry. The other four entries follow from the symmetry orbits with T=n for HL, 4h² for HC, 8 for LL and 2h² for CC. Substitution gives the stated five differences. LL and CC are strictly dominated, including r=2 where one coefficient of the LL comparison vanishes. The HC–LC crossing polynomial strictly decreases for positive gain, and HL–LC has one positive root; at κ=r+1 the first relevant numerator is negative and the second positive, giving α_r<r+1<β_r. These signs yield both ties and exclude the third orbit at either tie. Separately rebuilt the laplacians and directly inverted the anchored matrices with exact fractions at r=2,3,5 and gains 1/8,1,10, checking global minima over all pairs. Those finite comparisons supplement rather than prove the all-order and real-gain classification.

## originality

PASS

The objective and general gain-dependent pair centrality are known. The distinct part supported by the comparison is an explicit all-r ordering of the pair orbits for a clique with two leaves at the same hub, including two different thresholds and exact ties. The closest same-day statements and the later reentrance result differ in graph or mechanism, not merely notation; none gives this ordering for this family. The checks do not certify historical priority.

## value

PASS

This canonical clique-with-pendants family provides an all-order unweighted example in which the optimum passes through three distinct leader placements as finite equal gain increases. The exact middle interval and ties resolve behavior that a single fixed-gain, small-graph, or infinite-gain analysis cannot reveal. The reason to study this family is its minimal structural contrast between clique and pendant locations, not a chosen isolated parameter value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
