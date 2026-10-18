---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Schur orthogonality on standard S_n matrix coefficients gives sample Gram ((n−1)/n!)(2I+B^TB+(n−5)J). The three products of edge-transpositions give exactly n−1, n−4, n−5. Complete K_n incidence BB^T=(n−2)I+J yields positive eigenlevels n(n−3)^2/2, n and 2 for n≥4; arbitrary edge masks are positive-definite principal submatrices. Unsigned-incidence kernel has dimension m−n+b; for r-regular graphs BB^T=rI+A gives all spectral levels and exact condition number at n≥6,r≥3. Complete-class restriction kernel consists exactly of skew-symmetric coefficient matrices.

## originality

PASS

Qualified best-of-knowledge originality based on mathematical statement and implication comparisons, not title matches. PASS under best-of-knowledge, with possible older frame-theoretic formulation as risk. Search self-hit 2026/10/11/SCOPE-graph-spectral-transfer-for-transposition-sampling-in-the-standa--75af0a9770e8 identifies the assigned candidate itself, not prior independent coverage.

## value

PASS

Canonical graph-indexed sampling of the standard noncommutative Fourier block admits exact spectral interpolation for every edge subset. The bipartite-component bottom eigenspace and precise regular graph spectral transfer/condition number are useful structural links, not a relabeling of the complete Johnson spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
