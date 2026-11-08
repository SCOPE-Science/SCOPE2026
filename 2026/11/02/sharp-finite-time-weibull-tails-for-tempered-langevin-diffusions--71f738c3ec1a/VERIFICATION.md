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

Take q=d+r and α=1-ℓq>0. For Φ(y)=||y||^α/(sqrt(2) α) outside radius 2, Itô gives Φ(X_t)=Φ(x)+M_t+∫g(X_s)ds; quadratic-variation density v(y)=(||y||^qπ(y))^-2ℓ→cπ^-2ℓ and radial drift g(y)=||y||^-α (||y||^qπ(y))^-2ℓ[d+α-2+(1-2ℓ)y·∇logπ(y)]/sqrt2→0. Both globally bounded after smooth extension, implying nonexplosion by martingale control. For the upper logarithmic bound, stop or cutoff inside a large ball so v≤v∞+ε; DDS and reflection yield Gaussian exponent -1/[2(v∞+ε)t] per Φ(R)^2. For the lower bound, start in a remote annulus with positive reachability probability in time t-s; choose Brownian paths above -B throughout [0,v_+s] and above H_R throughout [v_-s,v_+s], forcing the radial clock to stay outside radius R0 until s with v_-s≤bracket≤v_+s. The Brownian bridge and Gaussian endpoint exponent give -1/(2v_-s); sending s↑t and ε↓0 matches the upper bound. Because Φ(R)^2=R^(2α)/(2α²), the logarithmic tail coefficient is -cπ^(2ℓ)/(4α² t). Tonelli tail integral establishes strict θ<κt finite, θ>κt infinite; θ=κt remains open. Independently checked transformed algebra exactly on a rational grid and with π=(1+x²)^(-3/2), d=1,r=2,ℓ=.2, radius 10–1000; no finite computation substitutes for the full tail proof.

## originality

PASS

The source Mijatović–Xie Theorem 2.2(1) identifies the critical Weibull exponent and two nonmatching sufficient/divergence time constants; the exact fixed-time radial log-tail coefficient and sharp strict time boundary require the localized quadratic-variation and long Brownian bridge argument not present in inspected source. Qualified against potential broader Gaussian heat-kernel asymptotics.

## value

PASS

The result closes a concretely motivated quantitative gap for a natural subcritical tempered Langevin diffusion: it identifies the sharp time separating existence from divergence of critical exponential moments, beyond generic exponent classification. Boundary equality is responsibly unclaimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
