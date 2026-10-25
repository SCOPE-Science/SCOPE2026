---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For H(d,q), q>=2,d>=1,1<=t<=d, root-normalize to a=0^d,b=1^t0^(d-t). Four type counts alpha,beta,gamma on t changed coordinates and delta on remaining coordinates are exactly orbits of obvious coordinate/symbol permutations preserving both roots. Their distances are u=beta+gamma+delta, v=alpha+gamma+delta, while the number f of neighbors with both distances decreased by one equals delta (only one replacement per selected nonzero unchanged-coordinate symbol). Thus alpha=t+f-u,beta=t+f-v,gamma=u+v-t-2f. Equitability of the stabilized individualization partition implies distance-pair and local f are constant on each stable cell, proving orbit equality; automorphisms forbid a finer partition. Distance-pair cells determine delta without refinement iff q=2 or t=1 or t=d, otherwise explicit feasible tuples (t-2,0,2,0),(t-1,1,0,1) share distances but have different f, and one round fixes it. Orbit sizes and class counts follow from multinomial/binomial counts. Independently constructed 1-WL and checked five q,d,t instances, including H(3,3) with t=2.

## originality

PASS

Known Hamming full automorphism wreath product and perfect/equitable coloring theory establish root-orbit context, but do not establish ordinary two-root 1-WL equals those orbits. A current general Tinhofer hierarchy theorem relates such refinements to group-orbit behavior but does not give the exact all-q,d,t rooted Hamming classification. The necessary-and-sufficient two-root distance-pair equitability condition and one-round recovery for the deficient cases are not stated in the inspected sources. Specialized association-scheme/Terwilliger literature remains a priority risk.

## value

PASS

Hamming graphs are foundational in coding and association schemes. An all-parameter exact description of two-root coarsest equitable partitions, the precise non-equitability frontier, and one-round correction is a meaningful structural and logical invariant, stronger than recording a few orbits or a generic automorphism classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
