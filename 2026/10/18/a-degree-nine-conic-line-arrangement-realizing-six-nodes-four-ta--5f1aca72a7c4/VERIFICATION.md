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

The smooth conic XZ−Y² and the three triangle secants intersect transversely at the three distinct triangle vertices. For the four parameters t=±1±√2 the distinct extra lines are t²X−2tY+Z=0; restricting one to [1:s:s²] gives (s−t)². Pairing roots of t²−2a t−1 with a=±1 gives the quartic in the finding. Two tangents with distinct parameters s,t meet at [1:(s+t)/2:st], off the conic; this point lies on a secant precisely when s+t=0, s+t=2, or 2st=s+t respectively. These tests give the four listed off-conic triples and no other tangent pair plus secant incidences. No three tangents concur because the corresponding equation in t would be a nonzero quadratic with three roots. No tangent contains a triangle vertex. All 21 line pairs and all 14 conic–line multiplicity units are accounted for, yielding six transverse double points, four simple tangencies, and seven ordinary triples. Their local forms A1, A3 and D4 contribute 1, 3, and 4 respectively, hence τ=46. Independent arithmetic in integer pairs representing Q(√2) confirmed the incidence signatures; sparse Jacobian coefficient columns yielded rank 45/45 modulo 101 in degree four and rank 59/63 over Q in degree five, without relying on the frozen selected minor. These ranks give mdr=5 over C, since ranks over Q and C agree and any lower-degree syzygy could be multiplied to degree four. The sharp du Plessis–Wall expression at (9,5) is 64−15−3=46.

## originality

PASS

The numerical maximal-Tjurina type (9,5) is known and a distinct Resultary record realizes the same weak basket. The supported distinct finding is this explicit, projectively inequivalent conic–seven-line realization with its verified Jacobian degree. Neither the invariants alone nor first realization of the basket across the catalogue is credited as new.

## value

PASS

This is a concrete sharp example in a specified restricted singularity and component class, not a recomputation of the already known numerical bound. Its three secants and four tangents give a different incidence configuration from known same-basket extensions and a reproducible sharpness witness with verified mdr. The realizability question was motivated in the primary literature before this computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
