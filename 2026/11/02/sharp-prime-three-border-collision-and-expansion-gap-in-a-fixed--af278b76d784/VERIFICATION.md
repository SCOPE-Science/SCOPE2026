---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

With strict branch endpoints including F(0)=-s, a 3-cycle avoiding boundaries must have two sign-switching inner visits and one sign-preserving outer visit. Solving one positive-outer itinerary gives X=r(s²-s+1)/(rs²-1), Y=s(X-1), Z=s(Y+1); strict 0<X<1, -1<Y<0, 1<Z<s iff r(s-1)>1. Its odd symmetric partner is distinct; at equality exactly boundary cycle 0 -> -s -> -1 -> 0, and below no cycle. Return derivative rs²>4 because s>2, r>1/(s-1); inf 4 approached as s down to 2 and r up to 1, not achieved. Independent rational branch test at r=4/5,s=5 gives (84/95,-11/19,40/19) as asserted. Inspected script checking 64 itinerary words for 12 rational parameter pairs.

## originality

PASS

The map and qualitative chaos/numerical bifurcations are published in the 2021 and 2023 García-Grimaldo–Campos-Cantón works. The exact all-(r,s) least-period-three census, border discontinuity, and sharp >4 expansion gap were not found in accessible source text. Original 2021 complete paper remains inaccessible, so the originality PASS is qualified.

## value

PASS

A complete explicit period-three birth and repeller classification at a discontinuous border is a natural dynamical invariant, distinguishing the unique equality orbit from two strict off-boundary cycles; the sharp expansion barrier is mathematically significant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
