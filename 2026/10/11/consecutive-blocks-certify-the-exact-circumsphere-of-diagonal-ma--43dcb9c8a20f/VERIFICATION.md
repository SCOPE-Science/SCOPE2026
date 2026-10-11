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
The proof in `RESULT.md` is symbolic for every \(2\le k<n\).

Critical checks:
- diagonal matching-field vertices are \(e_{1,j_1}+\cdots+e_{k,j_k}\) for \(j_1<\cdots<j_k\);
- row \(i\) is supported exactly inside the possible band \(i\le j\le i+n-k\);
- the active-band row-sum affine space has dimension \(k(n-k)\), equal to the polytope dimension;
- the orthogonal row-uniform point has squared norm \(k/(n-k+1)\);
- every vertex has squared distance \(k(n-k)/(n-k+1)\) from that point;
- the \(n-k+1\) consecutive-block vertices cover each active coordinate exactly once and hence average to the center;
- their barycentric identity proves no displaced center can have equal or smaller enclosing radius.

`verify.py` enumerates all diagonal matching-field vertices for \(2\le k<n\le10\), computes the exact affine rank by rational row reduction, checks the common squared radius, and verifies the consecutive-block barycentric certificate. Finite computation is corroborative only and does not assess originality.
