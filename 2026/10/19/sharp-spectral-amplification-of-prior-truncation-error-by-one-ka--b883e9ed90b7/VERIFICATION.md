---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For each test vector the conditioning quadratic form is the minimum over the observation coefficient of a nonnegative prior quadratic form plus a noise quadratic form. This proves Loewner monotonicity even for singular P_r and the bound 0≤K(P)−K(P_r)≤P. For the scalar row t e₁ᵀ+t² e_{r+1}ᵀ with R=1, the retained-coordinate posterior entries for the truncated and full priors tend to 0 and λ₁ respectively. The first diagonal difference thus proves sharpness by itself, even with eigenvalue multiplicities. The formula K(M)=M^{1/2}(I+M^{1/2}HᵀR^{-1}HM^{1/2})^{-1}M^{1/2} shows that alignment decouples the blocks even for singular M; the retained blocks cancel and the omitted block is bounded by P−P_r. The exact 2D rank-one update in RESULT.md lines 70–83 gives the stated amplification condition, including no amplification when b=0 or κ=1. At x=y=κ=100 it gives the stated rational witness. These checks concern a supremum over unbounded sensor coefficients, not finite attainment, and exact covariance conditioning only. The supplied verifier was inspected, not executed; no finite tests are needed for the universal conclusion.

## originality

PASS

The inspected prior work supplies covariance update formulas, low-rank filtering and a qualitative warning about ignoring likelihood information in prior truncation, but not the sharp norm amplification for the specified order of operations, nor the accompanying alignment and two-dimensional threshold results.

## value

PASS

The exact constant resolves how badly low-rank error can be amplified despite the posterior map being order preserving and covariance reducing. One scalar observation already causes the worst-case loss, whereas block alignment prevents it. The two-mode coefficient threshold gives a usable diagnostic beyond the qualitative warning that truncation ignores the likelihood.

The dated certificate retains the supplied scientific assessment, sources and limitations.
