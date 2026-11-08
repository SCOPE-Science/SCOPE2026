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

Strictly positive payoff gaps ensure 0<A(x)<B(x) on [0,1]. The invariant logit(n)−logit(m)=K reduces the flow to x in (0,1), u in R with E_K(u) strictly increasing onto (0,1), unique equilibrium x*=1/(1+θ), E_K(u*)=A(x*)/B(x*). The proper separable H_K has dH/dt=Δ(x−x*)²/[B(x)B(x*)], confirmed by direct rational differentiation (A′B−AB′=d0 e1−e0 d1). For Δ<0 LaSalle gives globally selected leaf equilibrium; Δ=0 regular proper one-well levels are periodic; Δ>0 bounded energy would give invariant non-equilibrium compact omega set contradiction, so distance to boundary tends zero. Statement only interior, symmetric equal feedback. Numerical integrations are illustrations.

## originality

PASS

The actual 2024 Betz–Fu–Masuda paper derives the reduced two-environment equations and uses the determinant/cross-ratio for LOCAL stability, and shows periodic behavior for a special mirror family. The explicit logit-leaf invariant, proper global Lyapunov derivative, non-mirror critical foliation and all-initial-condition classification are not the same as those local conclusions. Literature-limited PASS.

## value

PASS

Sharp global attracting, neutral, and boundary-approaching trichotomy resolves an intrinsic dynamics question for a standard ecological game model and explains equilibrium selection from the initial environmental odds. This goes beyond reparameterizing the known Jacobian and includes a non-mirror periodic regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
