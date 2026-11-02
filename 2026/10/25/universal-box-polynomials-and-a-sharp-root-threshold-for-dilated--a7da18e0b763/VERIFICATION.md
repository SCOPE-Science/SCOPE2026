---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For any empty lattice tetrahedron with normalized m>=2, its ordinary h*(S)=1+(m-1)z^2 by lattice-point count, reciprocity and normalized volume. In rS, all scaled facets are r Delta2 (Pick, unimodular induced facets), all edges r Delta1 (primitive edges). The Boolean face identity ell*=h*(rS)-4h*(r Delta2)+6h*(r Delta1)-3 gives a=mr(r^2-1)/6-(r-1)^2 and b=mr(2r^2+1)/3-2r^2+2r-1 in (0,a,b,a). Independent symbolic extraction and r=2 factorization verified. For r>=2, a>0 and c=b-2a>0, giving a simple zero and two distinct strictly negative roots; r=1 instead has multiple zero. h*(2S)=(1+6z+z^2)(1+(m-1)z), roots distinct for all integer m>=2, r>=3 uses Jochemko Veronese strict-root result for degree-two h*. Finite checker only corroborates r<=4/m<=10, not theorem proof.

## originality

PASS

The sharp r=2 simultaneous root onset and the m-only local-box coefficient identity go beyond classical Reeve h*, Jochemko ordinary Veronese real-root threshold and general large-width existence bounds. The HNF literature has related exact coefficient parametrizations, so narrower historical equivalence is an acknowledged priority risk; actual prior implications, not title matching, were assessed.

## value

PASS

All empty three-dimensional lattice simplices, not one illustrative shape, receive an explicit shape-independent local polynomial, strict gamma-positivity and sharp smallest integer dilation for both polynomial root properties. This is a natural exact Ehrhart invariant classification with a genuine threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
