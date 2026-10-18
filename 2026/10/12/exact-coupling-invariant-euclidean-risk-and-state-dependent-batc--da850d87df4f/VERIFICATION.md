---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For H=diag(Bρ,Bρ), Bρ=[[1,ρ],[ρ,1]] and 0<ρ<1, four equal coordinate marginals and exactly two sampled indices imply opposite-edge equalities p12=p34=α/2, p13=p24=β/2, p14=p23=γ/2 with α+β+γ=1. For each coupled pair the four marginal update cases have probabilities α/2,α/2,(1−α)/2,(1−α)/2; using simultaneous pre-update gradients, conditional summation gives u_{k+1}=r u_k, z_{k+1}=α r z_k−ρ(1−α)u_k/2, r=(1+ρ²)/2. Solving gives E||x_k||²=r^k u0 and Ef=r^k[(1−ρ²)/(2(1+ρ²))u0+α^k(ρz0+ρ²u0/(1+ρ²))], k≥0 including α=0 with α^0=1. The sign of C is exactly the endpoint sampler criterion at all k≥1; first constant ± initial eigenmodes reverse preference. x0=(1,1,1,1) has ratio (1+ρ²)/(1−ρ), unbounded as ρ↑1 despite both rates r<1. A fresh rational full-state enumeration over α in {0,1/3,1}, ρ=2/5, three starts and k through 3 matched formulas; recurrence proves all horizons.

## originality

PASS

At claim/implication level, no inspected prior source states or entails the precise final result; closest frameworks, partial results and source gaps are explicitly distinguished. No failed search is treated as proof of absolute priority.

## value

PASS

Same per-coordinate sampling budget and identical expected squared Euclidean risk do NOT determine expected objective even on a natural SPD block-coupled quadratic; the exact optimizer depends on initial eigenmode and has an arbitrarily large prefactor gap. This makes a structurally interpretable counterexample to naive marginal-only sampling prescriptions and separates two fundamental loss metrics without falsely claiming accelerated asymptotic rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
