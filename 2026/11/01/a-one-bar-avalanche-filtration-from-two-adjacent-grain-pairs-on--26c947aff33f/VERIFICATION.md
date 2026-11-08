---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

At every parallel update, four distinct binary grains shift one position to the right and exit at the sink, giving F_t={t,t+1,t+k+2,t+k+3} truncated to [0,n-1]. Intersect each new full simplex with the earlier union: a simplex for 1<=t<=k, two disjoint nonempty contractible simplices at t=k+1, a connected contractible 1-dimensional tree for k+2<=t<=n-2, and an already present vertex at t=n-1. These exhaustive cases hold even as the rightmost grains fall into the sink (n>=k+4). Cofibration homotopy pushouts give inclusion equivalences except the single 2-component attaching locus which creates S1; integral homology transition isomorphisms follow. Independent reconstruction checked all attachment intersections for 72 (k,n) pairs. Finite tests corroborate, not replace, the proof.

## originality

PASS

The exact 4-grain persistent one-bar statement is not the three-grain final-homology theorem of Riihimäki–Smith. The additional adjacent grain destroys a growing family of cycles in the published 3-grain comparator and fixes a single birth time. Full-text comparison of adjacent directed-path and cycle statements found no implication; best-of-knowledge PASS subject to unindexed work.

## value

PASS

Natural minimal perturbation of the published two-left-one-right 3-grain directed-path avalanche, producing unexpectedly n-independent first Betti one in place of n-k-2. The full all-parameter persistence barcode and exact birth k+1 are motivated topological dynamics, not a one-off finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
