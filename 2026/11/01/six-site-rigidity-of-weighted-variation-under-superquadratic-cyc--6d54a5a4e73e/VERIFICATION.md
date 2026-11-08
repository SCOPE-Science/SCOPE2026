---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Edge increments x_i=u_{i+1}-u_i are zero-sum and satisfy dot x_i=Phi(x_{i-1})+Phi(x_{i+1})-2Phi(x_i). The monotonicity of the sign and Phi gives contraction for uniform weights. For n>=6 disjoint sparse dipoles at j and j+3 impose d_j+d_{j+3}<=0 for d_j=w_{j-1}+w_{j+1}-2w_j, whose cyclic sum forces paired equality; perturbing the dipole with epsilon, q=p-1>1, yields a positive first-order term if any d_j≠0, hence each d_j=0 and all weights equal. For n<=5, strict negativity of uniform gradient TV on nonzero zero-sum gradients follows graph diameter<=2 and gives openness by compactness. Independent exact sign-chamber rational calculation found maximum -1/4 for p=3 weighted C5, zero for p=2 alternating C6, +1/2 for p=3 alternating C6. The claim does not cover 1<p<2 or arbitrary conductances.

## originality

PASS

Best-of-knowledge source-comparison judgement: claim is not shown to be a restatement or corollary of the actual inspected antecedents. A new sparse-dipole first-order perturbation argument and the short-cycle sign gap are needed for the claimed threshold.

## value

PASS

The sharp six-site threshold and contrast with linear heat expose a structural change in a basic nonlinear graph diffusion’s anisotropic variation stability; the complete if-and-only-if for all n>=6 and motivating finite exceptional cases are mathematically meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
