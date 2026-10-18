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

For real symmetric singular H positive semidefinite and delta>0, orthogonal decomposition z=z_R+z_N, b=b_R+b_N, Range(H) perpendicular ker(H) isolates the nullspace: constraint ignores z_N, so b_N!=0 gives the explicit feasible recession ray z_N=-s b_N and objective to -infinity regardless of a. For b in Range(H), reduce to positive definite restriction H_R and beta=sqrt(b^T H^dagger b). Standard conjugate-norm scalar minimization gives -infinity for a<beta; for a>beta value delta sqrt(a^2-beta^2), t=delta a/Delta and z=-(delta/Delta)H^dagger b + ker(H); when a=beta>0 the infimum 0 is unattained; a=beta=0 iff b=0 and every point is optimal. The Lorentz dual has equation H^(1/2)u=b, hence dual feasibility iff b is in range and a>=beta, with minimum-norm u=(H^dagger)^(1/2)b and dual cone coordinate nu=-sqrt(a^2-beta^2). This covers H=0, b=0, negative a, and all singular ranks. Independently for H=diag(9,0), b=(6,0), a=5,delta=5, the claimed value 5sqrt21 and unrestricted null component verify; b with nonzero null component creates an unbounded ray. This is exact reduction proof, not a numerical extrapolation.

## originality

PASS

Nguyen 2026 studies shifted ellipsoidal SOCPs and general convex-conjugacy boundary phenomena; the research package quotes a positive-definite H hypothesis for its explicit ellipsoidal formula. The submitted range-compatibility/nullspace dichotomy and complete affine minimizer classification are specific to singular H and not established by the accessible primary abstract, but the full Nguyen PDF was inaccessible, so hidden singular coverage remains a material risk. General robust ellipsoid/cylinder and CQ-free SOCP papers cover a broader framework yet their inspected statements provide criteria, not this special explicit closed-form classification. The quotient reduction is elementary and related, but the complete singular-domain classification is not the same statement as the invertible H theorem.

## value

PASS

The whole rank-deficiency boundary is a naturally needed extension of explicit elliptic SOCP primal–dual models: it distinguishes unboundedness along flat directions from finite nonunique optimal affine fibers, and identifies a nonattained zero boundary with dual attainment. This prevents invalid pseudoinverse substitution and gives closed-form decisions for degenerate structured instances. The proof is short quotient linear algebra; value is the complete, scope-motivated exact case distinction, not a claim of a general SOCP innovation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
