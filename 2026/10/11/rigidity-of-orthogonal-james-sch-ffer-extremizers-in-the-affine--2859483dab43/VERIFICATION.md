---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For the affine-regular hexagonal norm max(|u|,|v|,|u-v|), the explicit isometries R(u,v)=(u-v,u), S(u,v)=(v,u) act transitively on vertices and open edges. At open x=(1,t), 0<t<1, its sole norming functional f=u forces Birkhoff unit y=(0,+/-1); chords are 1+t and 2-t. At vertex x=(1,0), the full norming segment f_a(u,v)=u-av, a in [0,1], forces after sign y=(a,1); chords 1+a and 2-a. Both min<=3/2 and max>=3/2 are sharp only at parameter 1/2. Open-edge and vertex equality pairs are related by S and order reversal (hexagonal Radon orthogonality symmetry), hence one orbit; all such pairs have both chords 3/2. Endpoint and nonsmooth vertex cases are included; bounded substitutions at t=0,0.1,0.5,0.9,1 corroborate formula but are not proof.

## originality

PASS

The known orthogonal constants J_perp=g_perp=3/2 do not classify all Birkhoff-orthogonal equality pairs. A complete unique dihedral orbit with simultaneous isosceles equality is a stronger statement, checked against same-object 2022 original article.

## value

PASS

This is the natural equality-locus completion of Baronti--Papini’s canonical Radon-hexagon example for two orthogonality-constrained constants. The result proves their two extremizer sets coincide as one isometry orbit with equal chord lengths, rather than merely finding the already-known 3/2 values. The vertex/edge distinction is substantive due to nonsmooth BJ orthogonality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
