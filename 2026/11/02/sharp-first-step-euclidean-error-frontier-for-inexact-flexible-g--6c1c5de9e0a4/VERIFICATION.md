---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

With initial residual unit v, the first FGMRES LS step chooses α=(v·w)/||w||² for w=Az, ||v-w||≤µ, and residual q=v-αw=t u, t≤µ, u unit, v·u=t. Conversely every such pair u,v is realized by w=v-tu,z=A^-1w, so this constrained geometry is exact, not a relaxation. Errors are Bv and tBu for B=A^-1; compressing B² onto span{u,v} with SPD eigenvalue ratio≤κ reduces to the sharp norm ||diag(γ,1) R_t diag(γ^-1,1)||, γ≤κ. Its determinant is one, squared Frobenius norm 2+(γ-γ^-1)²(1-t²); the top singular value equals [√(4+δ²(1-t²))+δ√(1-t²)]/2 with δ=κ-κ^-1. Multiplying by t gives exact envelope gκ(t), achieved by two-dimensional right singular vector construction for arbitrary t. Optimizing over t≤µ yields t*=√[(4+δ²)/(4+2δ²)] and Gκ(µ)=gκ(min{µ,t*}); saturation (κ+κ^-1)/2. Solving gκ(t)=1 gives exact nonexpansion iff µ≤[1+δ²]^-1/2 for κ>1; for κ=1 G=µ. Independently constructed 2D SPD singular-vector witnesses for κ=1,2,10,100 across t=.05,.2,.7,.94 and matched computed LS error ratio to envelope including κ=10,µ=.2 giving≈1.9603998767. The determinant/singular-value proof, not finite tests, carries all dimensions.

## originality

PASS

Güttel–Nyman (2026) use the same inner action norm criterion but prove sharp outer residual contraction, not this Euclidean solution-error minimax frontier. Published Resultary symmetric GMRES(1) theorem treats *unpreconditioned* symmetric (often indefinite) actions and is not the flexible inexact preconditioning model; its SPD monotonicity does not imply monotonicity under adversarial flexible actions.

## value

PASS

The complete sharp tolerance/conditioning frontier is directly actionable for assessing when a nominally accurate inner preconditioner can worsen solution error, with exact two-dimensional adversarial witnesses and saturation. This is a natural numerical reliability invariant, not just the classical qualitative residual-error distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
