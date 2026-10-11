---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The arbitrary-\(n\) proof is given in `RESULT.md`.

Critical checks:
- bisubsets are exactly the valid pairs \(S\mid T\) with \(S,T\ne\varnothing\), \(S\cup T=[n]\), and not both equal to \([n]\);
- the published facet offset becomes \(n^2-(u-v)^2\) in complement-size coordinates;
- the intrinsic projected-normal squared length is \([u(n-u)+v(n-v)]/n\);
- all facet types with \(|u-v|\le n-2\) are strictly farther than the claimed radius for \(n\ge3\);
- the only minimizing types are \((u,v)=(n-1,0)\) and \((0,n-1)\);
- simultaneous permutation averaging fixes only the origin in \(M_n\times M_n\), so the minimum origin-to-facet distance is the global inradius;
- the tangent families force \(x_j\ge0\) and \(y_j\ge0\) for every coordinate at an optimal radius, and zero-sum then forces the unique center \(0\);
- for \(n=2\), the six facets reduce to \(|a|\le3\), \(|b|\le3\), and \(|a-b|\le4\), giving the stated incenter segment.

`verify.py` exhaustively enumerates all \(3^n-3\) bisubsets for \(2\le n\le8\), computes every origin-to-facet squared distance exactly as a rational number, checks the tangent-facet counts, and verifies the exceptional \(n=2\) constraints. Finite computation is corroborative only and does not assess originality.
