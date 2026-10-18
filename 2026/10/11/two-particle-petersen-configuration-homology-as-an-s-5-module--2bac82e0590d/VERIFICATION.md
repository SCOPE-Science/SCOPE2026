---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Abrams sufficiently-subdivided model applies to Petersen girth 5 with exactly two distinct unordered points. From actual KG(5,2) edge list, independently reconstructed 45 C0,120 C1,75 C2, signed boundaries and d1*d2=0, spanning-tree 44 and 76 chord coordinates. Exact independent elimination gives rank(M mod2)=69, mod3=70, mod5=70 and 70x70 integral minor determinant -2. Hence rational rank=70, all 70-minors even but one ±2 so Smith nonzero factors 69 units and one 2. Independently checked supplied 75x5 integer H2 cycles are in ker(d2), 5x5 pivot det -1; rank ker=5. Thus H1=Z^6⊕Z/2, H2=Z^5, no higher chains. Reconstructed all 120 S5 actions on entire C2 kernel basis, verified every 75-row action, yielding H1/H2 characters by class [6,0,-2,0,0,1,0] and [5,-1,1,-1,1,0,-1], matching Specht (3,1,1) and (2,2,1). Aut(P)=S5 from five maximal K4 cliques of complement. Torsion Z/2 fixed because Aut(Z/2)=1.

## originality

PASS

Ko–Park Theorem 3.16 already gives nonequivariant H1 for triconnected nonplanar Petersen: beta1(P)=6 and one nonplanar triconnected summand gives Z^6⊕Z/2; this is explicitly NOT novel alone. An–Knudsen H2 theorem restricts to planar graphs. Inspected Resultary dodecahedral/cuboctahedral equivariant configuration findings have other graphs and symmetry representations. No primary/indexed source identified the Petersen H2=Z^5 and both precise irreducible S5 characters together; nontrivial full finite chain certificate needed.

## value

PASS

Unordered configurations of two points on the Petersen graph are a canonical nonplanar test case with torsion and a large automorphism group. Exact integral H2 and full rational S5 irreducible representations, backed by small complete exact certificates, are natural reproducible invariants that supply symmetry-sensitive information not available from general nonequivariant graph braid H1. The complete calculation has direct comparative value independent of generalizations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
