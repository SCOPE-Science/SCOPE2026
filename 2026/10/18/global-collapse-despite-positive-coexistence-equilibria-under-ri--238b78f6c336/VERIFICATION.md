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

For 3D exact specified flow on (x,r,c), N>=3,2≤M≤N−1, positive rates and 0<β<α, define Δ=θ1μ2−θ2μ1−θ4(μ1+μ2), γ=(α−β)Δ/(μ1+μ2). Because K(1)=0, whenever x near1, x-logit derivative bK(x)r−c≤−β/2; hence x-logit has finite uniform upper bound. If r≤r0 with bKmax r0≤β/2, x-logit strictly decreases and cannot stay above risk break-even x*=μ1/(μ1+μ2) longer than T=(2/β)max(0,U−logit x*); risk-logit can drop by at most μ2 T during such an excursion, giving trajectory-dependent r≥ρ>0. Let v=logit r,w=log((c−β)/(α−c)), k=(α−β)(θ1+θ2)/(μ1+μ2); directly (w−kv)′=(α−β)(θ3+θ4)r+γ≥γ if Δ>0. Since r≥ρ, α−c≤C e^(−γt). If additionally bKmax<α, eventually c−bKmax>0, x-logit strictly decreases and x decays exponentially, then risk-logit rises with rate≥μ1/2 and r→1 exponentially. The first exact N3M2 witness Δ=4, β=1/5<bKmax=3/10<α=2/5 has two distinct positive-cost-face equilibria yet interior collapse; second Δ=3,bKmax=1/2>α has stable positive cooperative equilibrium, ruling out unrestricted benefit condition. Independent rational computations checked both Δ, mode and equilibrium identities, and the claimed eigenvalue signs; generality rests on comparison/log-odds proof, not these two examples.

## originality

PASS

Wang et al. classify equilibria and local stability for the same three-variable model; that information does not imply global interior convergence, and an equilibrium branch can be inaccessible to the open-box dynamics. The exact log-odds cancellation and global barrier are a new comparison beyond the inspected primary statements. Supplementary source gap noted.

## value

PASS

Distinguishes local/stationary coexistence from global basin accessibility in a concrete published adaptive risk–cost model. Explicit parameter-only conditions select an entire cost face and prove globally exponential interior collapse, plus an exact cooperative attractor delimiting the strict benefit hypothesis, a substantive dynamical insight.

The dated certificate retains the supplied scientific assessment, sources and limitations.
