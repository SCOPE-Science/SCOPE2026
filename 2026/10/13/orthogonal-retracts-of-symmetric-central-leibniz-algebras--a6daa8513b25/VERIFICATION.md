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

The derived line is preserved, so write an endomorphism as (v,t) -> (Av, phi(v)+lambda*t). Bracket preservation is B(Av,Aw)=lambda B(v,w). Idempotence gives A^2=A, lambda^2=lambda and phi A+lambda phi=phi. For lambda=1, nondegeneracy makes A invertible; hence A=1 and phi=0. For lambda=0 the image of A is totally isotropic and phi is uniquely a functional on that image composed with A. Conversely these conditions suffice. The projection is an arbitrary linear projection onto an isotropic subspace, not an orthogonal projection. For image dimension k, there are q^{k(n-k)} complements and q^k graph functionals; the graph recovers the subspace and functional, and the zero and identity maps are counted separately. Incidence with isotropic (k-1)-planes gives the recurrence via W^perp/W. The orthogonal point counts follow by splitting off hyperbolic planes: if Z_d counts zero vectors, then Z_d=q Z_{d-2}+(q-1)q^{d-2}, with bases Z_0=Z_1=1 and Z_2=2q-1 or 1. This gives the claimed Witt-type formulas, including the anisotropic-plane boundary. Hand checks at q=3 give 7130 and 812 for the split and nonsplit four-dimensional forms. Frozen VERIFICATION.md and verify.py were inspected, not executed; those finite checks are not the proof or a formal certification.

## originality

PASS

Best of checked knowledge, the distinct contribution is the all-dimensional classification and labeled map/image enumeration for the nondegenerate symmetric central bracket. The projection method has close analogues and the orthogonal Grassmannian counts themselves are standard. No order of priority is inferred between same-day records.

## value

PASS

The result gives a natural all-ranks invariant of a standard class of central algebras, distinguishes labeled image counts from map counts and gives their common fiber size. It makes the dependence on the orthogonal Witt type explicit, including the existence obstruction. The useful contribution is this census and parametrization for the symmetric bracket, not a new formula for classical isotropic subspaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
