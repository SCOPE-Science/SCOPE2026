---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The edge-symmetric and antisymmetric vectors give a 2x2 block with diagonal difference 2 and off-diagonal epsilon(U−V)/2; the isolate is unrotated. The upper eigenvalue is at least 2, whereas both lower branches lie in [0,epsilon], including at a tie of those lower branches. The lower block projector has antisymmetric weight (1−1/sqrt(1+epsilon²T²/4))/2, which the squared original-system norm multiplies by 2. Given T=t the edge midpoint is uniform on [t/2,1−t/2]. Subtracting s(t)<t/2 for t>0 keeps that midpoint in [0,1], so the folded-uniform first moment gives q(t). Its curvature is strictly positive, with endpoint slopes −1/6 and 2s(1)s'(1)>0; monotonicity of r carries the reversal over to conditioning on R. For F=E q(T), the bounds F≤7/24+epsilon²/960<1/3=q(0) and F−q(1)≥1/24−14s(1)²/15>0 give one strict crossing; multiplying q−F by r minus its value at the crossing gives a strictly negative integral. Direct integration against 2(1−t) gives E[T²]=1/6, Var(T²)=7/180 and Cov(q_0(T),T²)=−1/240. The scaled gap has limiting second moment Var(W)+Var((U+V)/2)=1/8 and variance 23/576. Uniform expansions give Cov(G,R)=−epsilon³/1920+O(epsilon⁵), the two mean orders and, after normalization, −3/sqrt(805). These are analytic checks, not inferences from an amplitude grid.

## originality

PASS

The supported distinct result is the finite-amplitude joint gap and squared-residual law, particularly its nonmonotone conditional mean, strict negative covariance, and weak-noise correlation in this model. No equivalent coverage was identified in the statement-level comparisons, subject to the unidentified marginal-law reference.

## value

PASS

The edge and isolate give a minimal nullspace with both a mixing direction and an unaffected coordinate. The exact calculation supplies a counterexample to a monotone interpretation of conditioned separation, even though the covariance is strictly negative across the full isolated-branch regime. This is a usable joint benchmark for diagonal splitting analyses that otherwise treat gap and nullspace residual separately.

The dated certificate retains the supplied scientific assessment, sources and limitations.
