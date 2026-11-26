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

The three degree-q sections have no common zero, so their kernel E in O³→O(q) is locally free of rank two and the incidence hypersurface is its projective bundle of lines. The relative hyperplane in this convention gives u²+c₁(E)u+c₂(E)=0, with c(E)=1−qh+q²h². The base and relative hyperplanes give the projective-bundle basis 1,u over Z[h]/(h³). Independently, multiplying by the ambient hypersurface class qh+u on P²×P² gives deg(h²u)=1 and deg(hu²)=q on X, with h³=u³=0. The integral degree-one and degree-three parts permit only a GL₂(Z) change of variables and a sign on the top form. The cubic 3ab(a+qb) has discriminant 81q², unchanged under both operations; equivalently the primitive factor determinant multiset is {1,1,q}. Hence q and, for fixed p, m are recovered. For ℓ=p all relations reduce to the same u²=0 relation since m≥1, including at p=2 or 3; elsewhere u/q is allowed and gives z²−hz+h²=0, also over Q. Over each F_{p^r} the base and fibre counts multiply to (1+p^r+p^{2r})(1+p^r), proving the zeta function. The frozen script was inspected, not run: its top-product helper encodes the expected products rather than proving them; its substitution checks are finite. A fresh count confirms 104 test matrices in its stated coefficient range.

## originality

PASS

The supported distinction is the height classification by the unmarked graded integral Chow ring together with its coefficient contrast. The exact varieties, geometric nonisomorphism, projective-bundle machinery, and additive comparisons are not claimed as new. No inspected result supplies the unmarked integral multiplicative classification or an equivalent invariant distinguishing the heights; the older uninspected reference leaves the historical conclusion qualified.

## value

PASS

For this natural family of homogeneous flag-type varieties, the cubic provides a concrete answer to which integral multiplicative information survives after forgetting the generators. It separates every height even though the rational and all prime-field rings and the zeta function cannot. That comparison is useful independently of the already known geometric classification, and goes beyond applying a projective-bundle formula in a fixed basis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
