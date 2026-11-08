---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For f(x)=λ||x||²/2, scaled random orthogonal frame P with PᵀP=(d/ℓ)I, E[PPᵀ]=I and E[P1]=0, and fresh centered finite-variance oracle errors, exact forward differences give G=λPPᵀX+(λhd/(2ℓ))P1+Pζ/h. The shared-baseline noise covariance is σ²(I+11ᵀ). Conditional first/second moments, (PPᵀ)²=(d/ℓ)PPᵀ and ||P1||²=d give r=1−2ηλ+η²λ²d/ℓ and b=η²[λ²d³h²/(4ℓ²)+2dσ²/h²]. Induction yields the exact all-horizon squared iterate norm. r∈[0,1) exactly for 0<η<2ℓ/(λd); AM–GM gives the unique h*, η*=ℓ/(λd) minimizes r, and the floor sqrt(2)dσ/λ (not globally minimized over η). Replacing a shared baseline with independent baselines retains the trace-based squared risk despite changing full law. Independently computed 4 exhaustive finite signed-frame/Rademacher second-moment cases using exact arithmetic.

## originality

PASS

Best-of-knowledge PASS for exact all-time mean-square law, shared-vs-separate baseline equivalence, and direction-count invariant fastest-step floor under independently redrawn query noise. General structured S-SZD paper uses a common stochastic sample instead, so its noise cancels in differences; exact-oracle orthogonal-direction paper lacks the inverse-h² term. Finite-difference bias/variance calculus and projector identities are classical and not claimed new.

## value

PASS

The exact finite-time risk and shared-baseline economy answer a natural oracle-design question, with a sharp dimension/direction cancellation at fastest mean-square contraction; useful beyond a routine one-step textbook error calculation because it distinguishes true independent query redraw from common-sample schemes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
