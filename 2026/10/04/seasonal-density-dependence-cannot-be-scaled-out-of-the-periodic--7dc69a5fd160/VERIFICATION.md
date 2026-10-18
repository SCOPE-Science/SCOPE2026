---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For positive periodic mosquito recurrence w_(n+1)=w_n*(r_n+mu_n*eta_n*w_n)/(1+eta_n*w_n), setting z_n=eta_n*w_n gives z_(n+1)=(eta_(n+1)/eta_n)*z_n*(r_n+mu_n*z_n)/(1+z_n), not the ratio-free equation when eta varies. Ratio cancellation for every positive state is iff eta_(n+1)=eta_n each step. Global common multiplier eta->c eta can be absorbed by w->w/c; seasonal relative eta cannot. Linearized one-period multiplier alpha=product r_n is unchanged by telescoping. Independent sympy exact composition for eta=(1/4,3/4), r=6/5,mu=1/2 verifies H(x)=3x(5x+48)(5x²+80x+128)/(20(x+4)(15x²+184x+160)), positive fixed point root of 225x³+2960x²+4480x-5632, x~.8039743679, next~.8705842366. Source-implied back-scaled (8/5,8/15) immediately fails because first step from 8/5 returns 8/5.

## originality

PASS

Best-of-knowledge originality accepted on the basis of direct statement/implication comparisons; prior components explicitly credited. Seasonal density dependence cannot be scaled out of the periodic mosquito map. Risks and partial readings disclosed.

## value

PASS

The original ecology application explicitly studies seasonal density dependence yet sets eta=1 to simulate on a claimed normalization. The corrected scaling shows the seasonal profile changes the actual attracting two-cycle while preserving the origin stability threshold. An admissible, exact counterexample prevents interpreting constant-eta simulations as universally rescalable; not just a dimensionless-units observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
