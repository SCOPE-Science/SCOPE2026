---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: Brownian generator D ∂xx with independent A→I α, I→A β, Poisson reset x→x0 at rate r, and target at 0 transparent when inactive, absorbing when active. The coupled backward ODE on two half-lines has reset value u=F(x0), one-sided active Dirichlet data F_A(0+)=0,F_A(0−)=1, and continuity of F_I,F_I′ at the transparent interface. Decomposition of gate generator into constant vector and (α,−β) eigenvector yields modes exp(−√(r/D)x),exp(−√((r+λ)/D)x), with c=(z−1)/(2λ) and matching constraints. Solving source-value fixed point gives p_-^A=α(1−z)(1−h)/(2λ), p_-^I=(1−z)[α+(r+β)h]/(2λ), stationary mixture p_-=α(1−z)(1+rh/λ)/(2λ), h=e^(−x0√((r+λ)/D)), z=√(r/(r+λ)). Derivative analysis gives strict reduction with reset rate r and x0 and strict increase with λ at fixed α/λ. Boundary r→0, r→∞ fixed x0, λ→∞ and x0√(r/D)→ell limits follow directly; almost-sure eventual capture establishes uniqueness of bounded Dirichlet solution. Independently checked generator/interface residuals in three parameter regimes and simulated exact Brownian-bridge crossings between jump times in 30,000 independent paths per rate, matching p_- within sampling error. The independent check does not prove the general PDE theorem.

## originality

PASS

PASS best of knowledge with substantial numerical-prior conflict: Żbik–Dybiec–Capała–Palmowski–Sokolov 2025/2026 treats the same transparent blinking target with position resetting and solves first-passage-time Laplace transforms and mean time. Its section III.3 plots and discusses a numerical probability of capture from the initially occupied side, rather than supplying a closed analytic side-approach formula. Crucially, that numerical trend versus resetting rate is different from the exact backward-equation derivative found here; this is identified as unresolved scientific reconciliation and not erased. First-passage-time marginal laws cannot determine side marking. Reflective gated half-line analyses of Bressloff and Mercado-Vásquez–Boyer use different boundary conditions; Bressloff 2026 spatial-endpoint splitting differs from two sides of one transparent target. General matrix backward-ODE techniques are prior knowledge, not the specific result.

## value

PASS

PASS: side-resolved capture probability at a semipermeable blinking trap with nonrenewed gate is an independently meaningful first-passage observable. Its exact conditional law, strict monotonicities and singular fast-gating limit reveal pathwise information not present in marginal first-passage-time laws, with a nontrivial strong-reset spatial boundary layer. The possible discrepancy with published numerics increases the need for follow-up rather than making the theorem scientifically trivial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
