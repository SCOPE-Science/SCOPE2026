---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Orthogonal coordinates make E_α a rank≤2 block [[0,-H^-1 b],[-α b^T,1-αd]]. The two singular values are those of T_α=[[0,-c],[-αp,1-αd]]. Positive-semidefinite test for zI−T^TT and a concave determinant quadratic give the stated minimax and uniqueness, including b=0 and transition dc=p. The SPD Schur complement of 2I−B^{1/2}AB^{1/2} gives spectral interval. Exact witness H=diag(1,4), b=(1/2,2), d=27/20 has ||E_opt||²=2550/2429>1 although spectral radius<1. Independent check: Independently reconstructed operator T and its spectral norm for 100 random SPD block systems with dimensions m∈{1,2,3,5}; checked each analytic minimum against seven other α values. For the exact 3×3 witness computed α=810/2429 and norm²=2550/2429 independently. Tests supplement PSD determinant proof.

## originality

PASS

Fan–Hu–Zhang define exactly the Type-II additive preconditioner in Section 3.1 but their Section 3.4 Richardson estimates concern Type I under projection-error hypotheses; Theorem 3.6 establishes nonsingularity, not Euclidean minimax. General block-Jacobi/Richardson results involve different scaling family or spectral/condition-number objectives. This exact codimension-one one-step Euclidean frontier and robust noncontraction witness are not implied by examined theorems.

## value

PASS

A stationary iteration can converge asymptotically while no α produces a uniformly contracting first Euclidean step. A closed optimizer and exact obstruction inform choice of regularization for a natural preconditioner, rather than merely tabulating a small case. The result does not claim performance of dynamic FGMRES.

The dated certificate retains the supplied scientific assessment, sources and limitations.
