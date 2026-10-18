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

The frozen theorem concerns complex projective order-polytope toric varieties for P=A⊕C⊕B with a,b>=2, c>=1 and only the connected automorphism group. Facet normals are -e_u (u in A), +e_w (w in B), e_u-e_v (u in A,v in C), e_v-e_w (v in C,w in B). Applying the complete-fan Demazure criterion (one ray pairing -1, every other pairing nonnegative), exterior alternative vertices force each boundary-ray root to ± a single standard character, and eliminate any other ray-derived roots. With c=1 both signs for outside-tier coordinates survive, yielding root system A1^(a+b), connected reductive group, dimension 3(a+b)+1; with c>=2 only +eps_A and -eps_B survive, no semisimple roots, mutually commuting additive root subgroups and torus of rank a+b+c, dimension 2(a+b)+c. Independently implemented integer box enumeration m_i∈{-1,0,1} for five parameter triples and recovered exact claimed root counts 8,4,4,10,5; infinity follows from symbolic ray-case exhaustion, not bounded search. No claim on disconnected automorphisms, central isogeny, outside stated parameters.

## originality

PASS

The explicit middle-tier root-set discontinuity and connected-group classification were not given by the inspected general Demazure toric theorem or nearby Hibi singularity and Schubert-degeneration results. The general ray criterion and reductivity/dimension implication are classical prior art and are not independently novel. The family-specific nonsemisimple/reductive transition is a substantive extra calculation; possible weak-order terminology prior coverage remains a best-of-knowledge risk.

## value

PASS

For a natural three-layer order-polytope/Hibi family, varying just the middle antichain size changes the connected group from reductive to solvable with a specified additive radical; the exact root census and group dimensions are meaningful structural moduli invariants, not merely a small-case computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
