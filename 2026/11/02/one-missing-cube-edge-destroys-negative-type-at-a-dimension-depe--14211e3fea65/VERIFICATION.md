---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Removing the single edge of Q_n increases only the missing endpoints Hamming distance from 1 to 3, so powered matrix is H_p+(3^p-1)(e_u e_v^T+e_v e_u^T). Walsh diagonalization and Bernstein integral show strict negative spectrum of H_p on zero-sum for 0<p<1. Even/odd character separation yields a positive rank-one obstruction with exact scalar R_n(p); root between 0 and1, one-dimensional null at equality; Li-Weston strictness propagation gives unique critical exponent and failure above. Centered Schoenberg rank yields dimensions 2^n-1 and 2^n-2. Isometric subface comparison and uniqueness give strict decrease; integral bound for Walsh modes k>=n/2 shows p_n ->0 by dominated convergence. Independent BFS/Walsh/spectrum tests for n=3..5 yielded p3≈.7474072433, p4≈.6477208242, p5≈.5946979926 and near-zero critical projected eigenvalue. Large-n claims rest on analytic proof, not numerics.

## originality

PASS

Li-Weston supplies a general negative-type strictness theorem; finite metric generalized-roundness algorithms and original Hamming-subset results are prior. Edge-deleted cube graph metric is NOT the unchanged Hamming-subset metric since the exceptional pair has distance3; exact rank-one Walsh root, strict decrease and p_n->0 are additional specialized conclusions. Qualified by possible equivalent graph embedding calculations.

## value

PASS

A single missing cube edge changes the maximal snowflake Hilbert embedding exponent from 1 to p_n<1, with quantified dimension deterioration to zero. This robustly motivates the sharp defect threshold and new rank formula in graph metric negative-type theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
