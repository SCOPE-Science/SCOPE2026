---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For any char-2 field and A=k[x,y]/(x²,y²), all derivations form A∂x⊕A∂y, alternating biderivations are A(∂x∧∂y), and alternating triderivations vanish. The bracket g=a+bx+cy+dxy has δ0(h)=g(h_y∂x+h_x∂y), δ1(X,Y)=g(X_x+Y_y)+Xg_x+Yg_y. Direct column rank by a,b,c,d strata gives (rank δ0,rank δ1)=(0,0),(2,2),(3,3), hence Betti triples (4,8,4),(2,4,2),(1,2,1). For g=dxy, the four linear vector fields have only two nonzero wedge products ps=qr=xyη; off the socle, normal forms 1+dxy and x+dxy each admit degree-1 generators whose product is nonzero xyη, yielding Λ(P,Q). Finite-field bracket multiplicities 1,q-1,q^4-q follow from parameter count. Independently built F2 cochain maps for all 16 g, checking ranks and δ1δ0=0; independently inspected verify_ring.py code also ranges GF2/4/8. The arbitrary-field proof is explicit rank/product algebra.

## originality

PASS

The closest Launois–Richard primary work computes Poisson cohomology for truncated polynomial algebras over C under {X,Y}=XY, not square-zero characteristic 2 where d(x²)=0 and derivations are A-free. Even for the common monomial bracket g=xy, the characteristic-2 Betti vector (2,4,2) differs from the complex characteristic-zero structure. This audited claim classifies all g and all alternating cup products, not older bracket-isomorphism counts.

## value

PASS

A complete three-ring classification for the canonical 4-dimensional square-zero plane reveals pronounced characteristic-2 effects and exactly which Poisson bracket strata can be distinguished by cohomology rings. This is a natural modular Poisson cohomology invariant, with explicit cup structure rather than just small dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
