---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reconstruct the discounted no-reset transforms using the backward equations: the diffusive transform f and the mean ballistic transform b satisfy Df″=(r+p)f−pb and v²b″=(r+q)²b−q(r+q)f off the target. Evenness, continuity of the ballistic transports through the blind target, and absorption only in diffusion give b′(0)=0 and f(0)=1. Bounded decaying solutions have the stated modes: writing H=(r+q)²/v², the characteristic polynomial is (z−(r+p)/D)(z−H)−pq(r+q)/(Dv²). Its value at H is negative, product of roots is positive, and both roots are positive with H between them. In each mode b/f=q(r+q)/(v²(H−z)); solving the two boundary equations recovers the stated transforms. Independent exponential reset attempts give success probability F_j>0 and mean attempt length (1−F_j)/r, hence the stated mean. The sign of F_B−F_D is that of c_-−c_+exp(−(λ_+−λ_-)x), with c_+>c_- and c_+>0. Since K<H, factoring P(K)=(λ_-²−K)(λ_+²−K) gives c_->0 precisely for v²>D(q+r). The sign expression is strictly increasing in distance, also excluding equality at finite distances on the parameter boundary. As r→0, λ_-²∼Cr for C=q(p+q)/(pv²+Dq²), λ_+→λ₀, and P(K) has positive linear leading term for v²>Dq. Thus c_- has order √r and c_+ has positive limit, yielding the first logarithmic coefficient. At r_c the roots are r_c/D and (r_c+p+q)/D, P(K) vanishes linearly in r_c−r and c_- does likewise. This yields the second coefficient with the stated positive root gap. Continuity and both divergences imply a finite attained interior minimum of x_*, giving strict reentrance for targets beyond it, without a claim of a unique minimizing rate.

## originality

PASS

The published same-model first-arrival transforms and the far-target ratio are antecedents; the necessary far-field inequality is close algebraic coverage. The inspected primary work stops short of the global unique crossing and, in particular, of the two singular endpoint laws for its distance. An exact indexed overlap on the entire fixed-rate crossover, including its formula, exists in b18dc798ce49. It is catalogued later, cites the 2024 transforms, and contains neither endpoint law. The supported distinct contribution is the quantitative two-endpoint reset-rate reentrance together with its proof; priority for the overlap is not certified from catalog dates.

## value

PASS

The sharp starting-mode rule answers a natural comparison holding parameters fixed, rather than optimizing separate experiments. The two endpoint scales quantify how large a target distance is needed to profit from ballistic initialization as the reset rate goes to zero or approaches its finite cutoff. This quantification gives a reentrant preference that a raw far-field ratio does not exhibit at fixed distance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
