---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

A fixed point of a simplicial involution has equal barycentric weights on the two vertices of each exchanged orbit; the admissible-orbit complex is a genuine triangulation of the geometric fixed locus. For the torus l1 metric, singleton fixed orbits are diagonal D_i; a two-point (i,j)/(j,i) orbit has diameter 2δ_n(i,j), so at r=2 only adjacent pairs E_i appear. Direct cross-orbit distances yield exactly D_i~D_(i±1), E_i~E_(i±1), D_i~E_i and D_i~E_(i−1). The flag-complex triangles are precisely {D_i,D_(i+1),E_i}, {D_(i+1),E_i,E_(i+1)}; no four-clique exists for n>=7. These form two cyclic boundary rings joined by a triangulated annular strip, giving S1×[0,1], integral H0=H1=Z and no higher homology. At r<2 no pair orbit or diagonal edge survives, giving n discrete points. Scale interval is only [0,2], no claims above r=2.

## originality

PASS

No stronger or equivalent covering result was established in the actual comparisons of statements/implications; this is a best-of-knowledge assessment with the precise unread-primary-source and alias risks separately documented.

## value

PASS

The scale-two ambient torus-grid complex has known torus homotopy, but coordinate-transposition fixed points form an annulus with boundary; computing the complete geometric fixed locus rather than just diagonal vertices is a nontrivial natural symmetry refinement. Its sharp change from n points at r<2 to an integral H1 class at r=2 is a meaningful equivariant persistence threshold for a standard metric family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
