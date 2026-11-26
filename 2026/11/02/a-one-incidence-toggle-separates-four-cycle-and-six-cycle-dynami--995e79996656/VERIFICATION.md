---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In characteristic two the design identity BB^T=(k-lambda)I+lambda J gives BB^T=I, so the unedited adjacency update squares to I. After conjugating the block state by B, the off-diagonal blocks are U=I+u a^T and V=I+a u^T, with u=e_i, a=Be_j, u^T u=a^T a=1 and independent u,a by k>=3. For insertion u^T a=0, so the nondegenerate span of u,a splits off and the complementary update is a swap. On the affected four coordinates the diagonal blocks of T^2 have characteristic polynomial x^2+x+1, annihilate under the third power minus identity, and have no fixed vector even when the polynomial splits. T^3 there is an off-diagonal involution, hence its fixed dimension is two. Adding the complement gives fixed dimensions v-2, 2v-4, v, 2v at powers 1,2,3,6. For deletion u^T a=1, U,V are rank-(v-1) idempotents with images ker(a^T), ker(u^T) and kernels spanned by u,a respectively. Each block maps the other's image isomorphically, so the image of T has dimension 2v-2 and is invariant with invertible restriction. On im U one has UV p=p+(u+a)(u^T p); on im V the symmetric transvection uses a^T. In either case the added map has rank one and square zero: u+a is nonzero, u and a give independent forms, and u+a is orthogonal to both. Thus the square of T restricts to a nonidentity involution with fixed dimension 2v-4 on the image, and T to an order-four map there: T^5=T, T^3!=T. A T-fixed vector is determined by p fixed by UV with z=Vp, giving dimension v-2. All periodic points are on the image and every point outside it enters in one step. Using q to the fixed dimensions and subtracting proper divisor periods gives exactly the stated positive primitive-period counts (v>=4, q>=2); the orbit counts divide by d. Every fiber over an image point is a coset of the two-dimensional kernel, so a d-cycle has basin d q^2.

## originality

PASS

The design orthogonality identity and rank/fixed-space counting of linear finite maps are standard inputs. The checked works do not give the bit-dependent four-versus-six period classification with basin and exact-period populations for the stated design parity over finite characteristic-two fields. Closest directly comparable is the same-day projective-plane toggle result; its lambda=1 does not permit BB^T=I in characteristic two and its spectra are genuinely different.

## value

PASS

A single graph edit of an initially involutory update is a natural perturbation. The algebra identifies a structural split: insertion preserves invertibility but produces exact order six, while deletion collapses two dimensions yet creates genuine order four on a stable image and forces a uniform transient/fiber structure. The complete q-dependent period and basin census makes the distinction stronger than witnessing individual orbits, and is not a finite-design example or a catalogue of existing designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
