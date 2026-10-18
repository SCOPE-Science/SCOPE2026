---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Set K0=Q(sqrt5), r^2=phi=(1+sqrt5)/2, L=K0(r,i). Phi has norm -1 over Q so is nonsquare in K0; [Q(r):Q]=4, [L:Q]=8. Reconstructed the four source monomial matrices modulo projective scalars, their 16-element A/mu2 orbit and the 16 distinct conic planes; exact integer quotient-ring/Pluecker Galois comparison fixes exactly eight planes under i->-i, transposes four pairs, while both r->-r and combined maps send each plane outside that collection. Thus setwise stabilizer <complex conjugation> gives Q(r) and individual stabilizers give eight Q(r) and eight Q(r,i) conics. Independently reconstructed 16 planes from monomial action with exact K0(r,i)-equivalence; output 16/16/8/0/0. The curve equations and source-quadric restrictions are separately addressed in the inspected exact source verifier; not merely assumed from old PASS.

## originality

PASS

Bonnafé–Sarti exhibit the same embedded surface, initial smooth conic, projective A-group and 16 disjoint orbit curves (arXiv v1 Remark 5.13; later source numbering may differ). The explicit coefficients being in Q(r,i) establish only an upper field bound, not the exact Galois action, minimal unordered field Q(r), or component 8+8 split. Later M20/Kummer model literature describes global structures but supplies no inspected covering marked descent statement.

## value

PASS

The exact arithmetic descent field of a singled-out 16-curve Nikulin configuration on a Kummer K3 surface, and the component-level Galois orbit profile, are intrinsic and potentially needed for arithmetic use of that explicit embedding. This is a motivated marked-configuration classification, not a claim about all abstract Nikulin configurations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
