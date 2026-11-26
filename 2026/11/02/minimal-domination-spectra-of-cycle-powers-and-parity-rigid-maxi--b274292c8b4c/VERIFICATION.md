---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In the periodic lift, consecutive centers cover their intervening positions exactly when the gap is at most 2r+1. At a center at 0 with predecessor/successor at −a,b, a private point must lie in [−r,r] intersected with [r−a+1,b−r−1]. The bounds on a,b make this intersection nonempty exactly when a+b≥2r+2; more distant centers cannot reach such a point. In the singleton case the copies of the same center do not overlap its closed interval since n≥2r+1; for k=2 the two neighbors can be distinct lifts of the same other center, as required. Rooting at a selected vertex gives exactly k roots per labeled set even for periodic gap words, yielding the n/k factor. The trace enumerates exactly these rooted words, and the formal logarithm and u derivative give 1/k and n respectively. The support inequalities are necessary by summation and sufficient by taking each gap in [r+1,2r+1]. At the upper endpoint n=k(r+1) every neighboring sum is tight, giving one constant word for odd k and 2r+1 alternating words for even k. The stated parity counts and examples follow. Independently replayed all subset-level gap conditions on 27 cases (r=1,2,3 and 2r+1≤n≤13) using private coverage multiplicities, and expanded the r=2 determinant by signed permutations; all matched.

## originality

PASS

The general-r minimal-set census and its support and parity consequences are distinct on checked evidence from ordinary domination, connected domination, a finite minimal-domination family and the known unrefined ordinary-cycle sequence. This pass excludes any priority claim for the r=1 totals or for general transfer-matrix techniques.

## value

PASS

The result fills a natural refinement of cycle-power domination: it identifies every attainable size and gives exact multiplicities of irredundant covers rather than all covers. Extremal tightness yields explicit configurations and a parity distinction invisible in the upper domination number alone. This is useful structure throughout the natural family and not just a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
