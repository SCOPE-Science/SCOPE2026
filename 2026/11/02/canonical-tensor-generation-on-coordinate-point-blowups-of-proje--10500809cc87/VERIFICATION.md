---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS: Given Ito-Zeng-Zeng's toric restriction bigness criterion, reconstruct orbit closures as exceptional coordinate subspaces or strict transforms of coordinate P^q. -K=(n+1)H-(n-1)sum E, positive on exceptional orbit closures. On a selected coordinate line its degree is n+1-m(n-1), zero only when n=3,m=2. On a strict q>=2 coordinate plane with m selected vertices, -K section exponent simplex has sum a_j=n+1 and cap a_j<=2 on m selected vertices; full dimension iff m<q+1 or n+1<2(q+1). K has no sections due negative degree after pushing exceptional positive terms to P^q. This yields n=2 or 4 arbitrary t, n=3 t<=1, n>=5 t<=2. Intersections K.ell=n-3>0 and K.f=-(n-1)<0 prove neither nef nor anti-nef for stated cases. Source checker source read for n=2..8, finite checks separate from all-n argument.

## originality

PASS

PASS, qualified: Ito-Zeng-Zeng 2026 establishes the GENERAL toric orbit-closure tensor-generation criterion; source here explicitly specializes it to canonical bundles of all coordinate-point blowups and proves an exact n,t classification with an n=4 exception. Ito-Olander broader derived criterion is also prior and does not directly print this classification. Newness is this natural complete family classification, not the toric criterion itself; latest Ito-Zeng-Zeng full text could not be inspected, so possibility it already lists it remains a significant priority risk.

## value

PASS

PASS: Full classification over every n,t of a canonical line bundle's tensor-generation, including counterintuitive n=4 exception and examples neither nef nor anti-nef, is a naturally motivated complete classification which could guide derived generation questions. Finite n2..8 census alone would not suffice; uniform polytope argument supplied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
