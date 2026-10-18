---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Over any algebraically closed k of characteristic 2, F=Y^4+XZ^3 is integral, with unique geometric singular point [1:0:0] and unique common tangent point [0:1:0]; geometric stabilizers must fix both. Over the scheme-theoretic stabilizer coordinate ring, entries off the triangular geometric form are nilpotent (finite-type algebra with all geometric values zero). Coefficient comparison in F(M(X,Y,Z))=λF, with bottom right normalized to 1, yields g(a+dg)=0, ah+cg=0 and c+dh=0, so unit a+dg forces g=h=c=0. Remaining constraints are a=b^4, d=v^4 and u^4=0, with b unit. Conversely these matrices preserve F up to b^4 and determinant b^5. Matrix multiplication gives b"=bb', u"=u(b')^4+bu', v"=v+bv'+u(v')^4. The representing group scheme has coordinate ring free of rank four over k[b,b^-1,v], reduced affine group dim2 and Lie dim3, with subgroup α4 at b=1,v=0. Pinned verify.py checks symbolic char-2 polynomial relations and finite GL3(F2) projective count, but universal statement depends on the coefficient proof. No gap found in all k-algebra functoriality.

## originality

PASS

The published Hilario–Stöhr source exhibits the exact quartic family and its singular/tangent geometry, while Hilario–Schröer studies nonreduced automorphism-group schemes on a different rational cuspidal hierarchy. Neither inspected source gives the full plane-embedded stabilizer group scheme Spec k[b,b^-1,v,u]/u^4 of this c=0 quartic. The nilpotent α4 direction is undetectable from geometric automorphisms and is the substantive new determination.

## value

PASS

The exact rank-four infinitesimal thickening over a two-dimensional reduced affine stabilizer is a structurally meaningful characteristic-two phenomenon. The α4 subgroup and extra tangent direction are invisible to rational-point symmetry counts, so this is a motivated natural invariant of a previously studied rational plane quartic and a concrete guide to non-smooth group-scheme actions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
