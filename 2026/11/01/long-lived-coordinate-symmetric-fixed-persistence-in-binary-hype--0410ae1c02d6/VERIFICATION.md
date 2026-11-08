---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

PASS: For inclusive Hamming Rips on {0,1}^n, a coordinate permutation-invariant geometric point is a convex combination of complete weight-orbit barycenters; orbit supports must be a simplex. Direct support intersection gives maximum inter-weight Hamming distance D(a,b)=min(a+b,2n-a-b), including same-weight diameters. At integer r<n the eligible weights are 0..floor(r/2) and n-floor(r/2)..n, with all same-side pairs compatible and opposite-side pairs incompatible iff |i-j|<n-r. Therefore the canonical fixed triangulation is Ind(B_{m,k}) for m=floor(r/2)+1,k=n-r. On consecutive index blocks of k, the verified nested open neighborhoods allow elementary independence-complex folds of nonanchor L and H vertices; the residual graph is t=ceil(m/k) disjoint edges, whose independence complex is the boundary of a (t)-cross-polytope, S^(t-1). For adjacent scales, including parity changes in m and decrement k, the old antipodal anchor pairs map under the new contiguous fold to distinct consecutive new anchor pairs. The integral top homology map has degree ±1 when sphere dimension is unchanged; it vanishes into different-degree groups otherwise. The exact dimension threshold is d(r)>=q iff r>=ceil(2qn/(2q+1)), yielding one reduced degree-q bar between successive distinct thresholds, with final death at r=n. Independently tested 594 fold/core/threshold examples, including n=30 degree-one interval [20,24); finite tests do not replace the uniform proof.

## originality

PASS

Best-of-knowledge originality after comparing exact statements and implications; four structured comparisons and source-inspection limits are included.

## value

PASS

PASS: The full-coordinate symmetric fixed-space filtration is canonical and has an exact uniform homotopy and integral persistence classification for all Hamming dimensions. Positive-degree bar lengths unbounded in n despite ambient inclusion nullhomotopies give an informative structural contrast between fixed and ambient persistence. The fold certificates and closed threshold formula are reusable results, not a table recomputation or a random finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
