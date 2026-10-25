---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For F_m=K1 join P_m, m>=1, maximal graphical-arrangement chambers index acyclic orientations, and facets of their cones correspond to Hasse covers; thus the zonotope vertex degree is the cover count. Spoke A/B labels force each between-run edge A→B and forbid it from being a cover due to the hub alternative. Internal edges are covers; an A-run contributes its sinks' spokes, a B-run its sources' spokes. For run length L, adjoin a plus and minus to an orientation word: s sinks correspond to 2s-1 sign flips, giving binom(L,2s-1). Hence T(z,u)=z/((1-z)^2-u z²), and summing compositions with either initial spoke direction yields 2T/(1-T)=2z/(1-3z+(1-u)z²). The m-degree coefficient and δ>=0 follow; m covers form a spanning tree whose primitive lattice incidence vectors are unimodular, so δ=0 is sufficient as well as necessary for smooth toric fixed points in any characteristic. Coefficient extraction yields 2Fib_{2m}, total 2*3^{m-1}, mean and variance for m>=3 and max floor((m-1)/2). A fresh independent enumeration over all orientations for m=1..7 computed Hasse covers by edge deletion/reachability and recovered Q7(u)=754+600u+102u²+2u³ and all preceding coefficients. This is corroboration, not the proof for every m.

## originality

PASS

Exact fan chamber cover-count distribution could appear as an orientation-descent polynomial or face-incidence refinement; the general arrangement dictionary is covered, the specialized run-decomposition local spectrum was not found in read source material.

A stronger general degree-refined theorem could dominate this claim, but the inspected general theorems have different outputs. In particular a global face polynomial cannot by itself determine the vertex-degree multiset.

Known total counts are dominated parameters of degree sums, not a table of the exact local degree distribution. The Fibonacci smooth-point interpretation is treated as a consequence of the full polynomial, not standalone novelty.

Neither global criterion for smooth zonotopes nor global face enumeration implies the per-vertex fan excess spectrum without additional dedicated calculation. The actual claim is a family-specific refinement of established graphic-arrangement theory.

## value

PASS

Fan graphs are a canonical family of graphical zonotopes, generally nonsimple; a complete distribution by excess number of invariant curves is more informative than the previously tabulated total vertices or a global simplicity criterion. It supplies a characteristic-free toric smooth fixed-point count, all local edge degrees, moments and extremal excess via a concise natural run statistic. The invariant is motivated by toric singularity detection and polytope graph structure; no local class-group rank or entire singular-locus classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
