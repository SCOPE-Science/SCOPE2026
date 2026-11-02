---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

With A_ij=c_i>0, y_i=c_i and uniform independent row I_t/coordinate J_t, the residual p_t=1−1^T x_t and centered nullspace z_t=x_t−(1−p_t)1/m obey p_{t+1}=(1−eta_t lambda_{I_t})p_t and z_{t+1}=z_t+eta_t lambda_{I_t}p_t(e_{J_t}−1/m). Independence and E(e_J−1/m)=0 eliminate cross terms; E p_t²=Q_t=prod(1−2a eta_s+b eta_s²), E||z_k||²=(1−1/m)b sum eta_t² Q_t. Orthogonality gives exact solution-error and residual formulas. The bound eta_t lambda_i<1 and sum eta_t infinite ensure p_t→0 pathwise; nonnegative coordinate increments with total mass ≤1 give a.s. bounded convergence, hence mean-square convergence. The variance series has positive t=0 term, so a nonzero limit for every admissible schedule. Independent exact rational branch enumeration k=0,...,6 and matrix 2×2 rational constant-step formula match. Scope excludes arbitrary rank-deficient operators and coordinate-dependent samplings.

## originality

PASS

Known randomized coordinate descent theory can converge to random solutions and distinguishes residual from parameter error; those qualitative statements do not supply this particular doubly sampled all-schedule exact finite-time variance law. Initiating October 2026 DSBGD article's full text was inaccessible, so any direct stronger coverage is a named residual priority risk; a permissible qualified best-of-knowledge positive originality decision does not assert whole-paper noncoverage.

## value

PASS

Exact all-step and all-admissible-stepsize nullspace variance law sharply distinguishes residual convergence from minimum-norm selection in a natural genuinely two-row/two-coordinate randomized inverse-problem algorithm. The explicit positive asymptotic variance despite exact data fit identifies a mathematically consequential gap in a claimed selection principle, not just numerical instability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
