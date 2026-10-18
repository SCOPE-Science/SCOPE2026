---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Direct differentiation of the seven-parameter model at (x*,y*)=(1,1) gives instantaneous [[-3/2,-6],[7/20,0]] and only delayed entry B22=-1, so Δ=P(λ)+Q(λ)e^{-λτ}, P=λ²+3λ/2+21/10, Q=λ+3/2. An independent Sympy derivation gave F(X)=|P(i√X)|²-|Q(i√X)|²=(X-27/20)(X-8/5), so precisely two possible positive crossing frequencies; Δ(0,τ)=18/5 rules out zero. Phases from -P/Q are cos θ-=-7/8 and cos θ+=-9/11 with positive sine, giving all crossings τ±(j). Independently computed first delays τ+0=1.9993800252788, τ-0=2.26890737505765, τ+1=6.96667415817688, τ-1≈7.67661228. Re[(dλ/dτ)^(-1)] is F'(ω²)/|P(iω)|²: numerically at ω- it is -0.0694444444444, at ω+ +0.0649350649351, with nonzero crossing slopes -0.00865738555 and +0.01115082176; opposite directions confirmed, not inferred from numerical roots alone. Zero-delay λ²+5λ/2+18/5 Hurwitz. For Re λ>=0, |e^{-λτ}|<=1 gives a uniform quadratic modulus bound for unstable roots; continuity/argument principle and the two simple transversals establish initial stable, two-right-root unstable, stable again, then unstable sequence. Standard retarded-equation linearization applies away from crossing delays. Smooth equilibrium via nonzero Jacobian determinant and strict inequalities gives open-neighborhood robustness. No assertion at critical delays.

## originality

PASS

The exact same predator-self-regulation delay model appears as eq.(1.2) in Ou et al. 2023/2024. Its Theorem 3.1 uses assumption (A2) selecting a one-positive-frequency regime and analyzes first Hopf delay; the present F has two positive roots and positive constant, outside (A2), so the full reentrant stable-unstable-stable sequence and exact positive parameter vector are not logical corollaries. Sui--Du's 2023 theorem already gives delay-induced stability recovery in a predator-prey setting, but its delayed fear response enters prey reproduction, with diffusion and distinct spectrum; source of the general phenomenon is credited. General Beretta--Kuang crossing theory supplies methods but does not construct this model-specific feasible witness. No cross-model broad significance is claimed. Resultary unavailable; only bounded priority conclusion.

## value

PASS

The nontrivial motivated distinction is a completely explicit biologically admissible parameter witness for repeated loss and recovery of stability in the very model whose original analysis only addresses a sufficient first-Hopf regime. Verifying both crossing branches and all right-half-plane root counts rules out a misleading finite-numerical switch diagram; open-set persistence shows it is not a one-point algebraic accident. This is useful for bifurcation structure and delayed-control interpretation without asserting global attractors or a new general delay-equation theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
