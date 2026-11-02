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

The edge-labeled overlap graph has every weight-one vertex of degree two and every zero/two vertex degree one. Forced-path contraction gives a balanced two-arc directed graph on m=n-2 vertices with arcs i->i-1 mod m and i->m-1-i (loops and parallel arcs distinct). Euler cycles anchored by the unique 0^(n-2)1 edge are counted by in-arborescences via BEST, since all outdegrees two. The Fourier blocks of 2I-P-R have paired determinants 2(1-zeta^k)(1-zeta^-k) and exceptional eigenvalue four for even m; directed tree cofactor equals 2^floor(m/2). Independently constructed all contracted integer cofactors for m=1..15 and directly enumerated binary rotation classes for n=3..6: 1,2,2,4. Rotational anchoring is essential.

## originality

PASS

Fresh best-of-knowledge statement-level comparison with relevant published Resultary findings and primary articles, acknowledging known general methods and narrower ancestors; no inspected stronger theorem implies the exact final result. Priority is qualified by explicit residual risks.

## value

PASS

Universal cycles for all two-subsets in shorthand representation form a natural constrained de Bruijn population-count problem; determining how many such cyclic orderings exist is independent of constructing one, and an exact all-length exponential count is a usable combinatorial invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
