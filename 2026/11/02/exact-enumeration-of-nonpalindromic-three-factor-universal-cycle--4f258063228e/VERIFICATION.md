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

The de Bruijn overlap graph has q² ordered pair vertices and q²(q-1) distinct allowed 3-gram edges, indegree=outdegree=q-1. On q-by-q matrices adjacency is A(F)=1(F1)^T-F^T. Decompose into the all-ones line (eigenvalue q-1), centered symmetric (eigenvalue -1, mult q(q-1)/2), centered skew (eigenvalue +1, mult (q-1)(q-2)/2), and q-1 two-dimensional blocks with characteristic λ²+q-1. This proves entire characteristic polynomial over complex numbers. Simple degree eigenvalue q-1 plus balance gives common positive directed Laplacian cofactors equal product of nonzero Laplacian eigenvalues /q²; use directed matrix-tree to guarantee connectivity, then BEST theorem with fixed initial *unique edge* so no accidental division by rotation length. q2 single directed 4-cycle. Independent exact determinant/spectrum/cofactor checks q=2,3,4 (rooted trees 1,108,3538944) matched closed formula; actual infinite proof is symbolic.

## originality

PASS

Best-of-knowledge originality attaches to evaluated full all-q spectrum and Euler tour product, not BEST/matrix-tree or the de Bruijn construction.

## value

PASS

Exact all-alphabet enumeration of a simple natural restricted universal-cycle language, plus full graph spectral data, by an explicit decomposition linking nonbacktracking overlap dynamics to spanning trees. Not merely Euler-cycle existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
