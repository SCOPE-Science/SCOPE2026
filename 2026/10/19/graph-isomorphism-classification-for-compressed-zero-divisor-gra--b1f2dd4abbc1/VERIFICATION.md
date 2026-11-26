---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The Gorenstein condition and m^3=0!=m^2 give Soc(R)=m^2, so the pairing on m/m^2 is well-defined over the residue field even without a coefficient field. A radical vector would lift to the socle and hence vanish in m/m^2. The annihilator of a nonsocle element is the inverse image of its orthogonal hyperplane, and nonsingularity identifies equal hyperplanes exactly with equal projective directions. Thus the compressed graph has one universal socle vertex and all projective points; product-zero pairs are precisely orthogonal pairs after excluding loops. The hyperplane has Q points, so each isotropic point has full degree Q, each other point Q+1, and summing gives N+(NQ-I)/2 edges. In characteristic two B(v,v) is the square of a linear functional, giving either N or Q projective zeros. In odd characteristic the Gauss-sum average for a diagonal form has zero nontrivial-character contribution in odd dimension (sum of the quadratic character is zero); in even dimension G^2=chi(-1)q gives the stated signed correction, after removing the vector zero and dividing by q-1. The socle is unique since N-Q=q^(d-1)>1. With two nonsocle degrees their minimum is Q and q=(N-1)/Q. With a single degree the only cases are binary dimension alternating or anisotropic (degrees 1 or 2, then q=N-1), or higher even dimension alternating (degree Q). For odd q and even d>=4 the signed correction has magnitude strictly smaller than both Q and N-Q, so there are no hidden regular cases. These data recover d from N and the form's similarity type from I, with determinant class needed only for odd q and even d and alternating status for even q. Conversely a linear equivalence up to scalar preserves adjacency. In d=2 the orthogonal-complement involution gives fixed points and transposed pairs, hence pendant edges and triangles at the socle; one-vertex gluing multiplies the Tutte polynomials and tree counts. Both explicit rings have two radical generators with zero squares and cross-product generating m^2, through xy and 2t respectively; their characteristics differ. Bounded independent projective enumerations checked q=2 and 3 in d=2 for both form types and q=3,d=3 for the identity form (I=4, |E|=37). Replay by normalizing nonzero vectors to first nonzero coordinate 1 and testing the Gram product on distinct pairs. The uploaded checker was inspected but not executed; the proof does not rely on finite tests.

## originality

PASS

Best-of-knowledge pass for recovering q, d and the multiplication similarity class from the unlabelled loop-free compressed graph over the entire finite short Gorenstein family. The bilinear/annihilator model and the isotropy counts are established ingredients. There is very close catalogue coverage of ordinary graphs in the standard graded family and effectively a dimension-two compressed slice via the ordinary-graph fiber description. Neither supplies the compressed reconstruction across unknown field sizes and dimensions.

## value

PASS

The graph loses multiplicities of elements in annihilator classes, and in particular can lose ring characteristic. A complete answer to which multiplication data survive that loss is a natural graph-isomorphism classification. Recovering the field and form even when the two expected nonsocle degrees collapse, and delineating failure of ring reconstruction by an explicit mixed-characteristic example, gives value beyond the classical isotropic table and the routine bouquet invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
