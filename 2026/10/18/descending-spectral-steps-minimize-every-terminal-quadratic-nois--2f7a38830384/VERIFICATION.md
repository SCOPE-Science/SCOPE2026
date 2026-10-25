---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Unrolling e_{k+1}=(I−αH)e_k−αξ gives deterministic mean P(H)e0 independent of order and terminal covariance Σ_k α_k² T_k Q T_k. Neighboring α,β have identical earlier/later contributions because all updates commute; exact expansion produces covariance difference αβ(β−α)T(HQ+QH)T. Since spectral W,H,T commute, trace difference =2αβ(β−α)tr(WHT²Q), a nonnegative PSD-product trace multiplied by the swap sign. Adjacent inversion removal sorts all steps, proving simultaneous terminal-risk minimization with no stable-step restriction; strictness follows if Q,W≻0 and suffix T≠0. A complete distinct reciprocal-eigenvalue step set leaves a nonannihilated eigenspace in any inversion suffix. Loewner fails for H=diag(1,9) and Q=[[1,.8],[.8,1]], whose HQ+QH determinant −28; isotropic Q gives Loewner. Independent simulation generated 75 random SPD H,Q pairs of dimensions 2–4 and all 24 step permutations each, and verified all terminal risk inequalities and precise adjacent exchange matrices. The proof is algebraic, not from simulation.

## originality

PASS

Best-of-knowledge PASS: Zhou–Gu’s Hanoi ordering is a deterministic high-frequency-rebound strategy, not the constant-additive-oracle-noise risk optimization problem in its accessible abstract. Classical Chebyshev step-ordering studies transient numerical error or deterministically stable iteration; Fox–Parker stochastic solvers use step-dependent noise covariances to maintain a target distribution. These different objectives/hypotheses do not imply the common-covariance terminal trace exchange law from the material read. However full Zhou–Gu, Lebedev–Finogenov and Fox–Parker primary text was not read; overlapping stochastic step permutation results remain plausible.

## value

PASS

Which ordering of the SAME fixed steps gives the best terminal stochastic accuracy is a natural optimization question distinct from deterministic robustness. Uniform improvement for every Hessian-spectral quadratic risk, anisotropic noncommuting Q, and an unbounded Θ(κ) reverse-order objective penalty are meaningful rather than routine learning-rate folklore.

The dated certificate retains the supplied scientific assessment, sources and limitations.
