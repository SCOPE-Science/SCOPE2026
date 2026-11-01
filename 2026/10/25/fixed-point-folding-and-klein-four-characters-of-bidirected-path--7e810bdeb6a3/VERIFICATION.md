---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Each forbidden pair of arrows in the path is either an opposite pair on one edge or a double-incoming/outgoing pair on adjacent edges. Alternating lane labels identify this incompatibility graph with ladder P_n box K_2; independent sets are the multipaths. Fixed geometric points are unions of permitted vertex orbits with constant barycentric coordinates. Reflection across ladder columns yields precise smaller ladders: R to length floor((n-1)/2), RT to ceil(n/2); T orbit is always an incompatible rung, so its fixed space is empty. Signed fixed-face Lefschetz equals reduced Euler characteristic of the orbit ladder. Using Caputi–Collari–Smith X_n~S^floor((n-1)/2) gives R-degree (-1)^floor((n+3)/4), T-degree (-1)^(d+1), integral because rank one, and quotient top homology iff n=0,7 mod8. Independent orbit graphs checked all 27 (n=2..10,g in {R,T,RT}), signed Lefschetz 21 cases (n=2..8). No infinite conclusion is based on the finite checks.

## originality

PASS

Caputi–Collari–Smith Proposition 2.2 supplies ordinary sphere homotopy only. The published Resultary circular ladder has extra wrap-around conflicts and sometimes 3-dimensional homology; its D_n×C2 character is not the open ladder representation. The similarly named strong Morse path-reversal paper has distinct incidence faces/forbidden patterns, so its mod-eight sign is not the multipath result. This separates precise objects and homology, not titles.

## value

PASS

All three natural involution fixed spaces and the full integral V4 character are meaningful equivariant refinements of a known sphere, with sharp mod-eight quotient consequence; explicit PL folding is usable for further fixed-point or quotient computations. Not a routine relabeling of circular ladder or strong Morse results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
