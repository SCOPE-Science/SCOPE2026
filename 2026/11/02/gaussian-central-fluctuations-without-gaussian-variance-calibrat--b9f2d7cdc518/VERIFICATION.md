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

With independent Rayleigh outgoing velocities, W=L/V_H+L/V_C has mean mu and tail P(W>x)~c/x² with c=L²(beta_H+beta_C)/2. The truncated variance is 2c log b and Gaussian normal attraction gives (T_n-nmu)/sqrt(c n log n)=>N(0,1); inversion yields renewal-count Gaussian variance c/mu³ at tlog t scale. Rewards R have mean nu=1/beta_H-1/beta_C and finite variance; marked-renewal/stopped martingale estimates make the centered reward contribution O_L2(sqrt(t)), so Q-jt has weak Gaussian coefficient c nu²/mu³. Distinct second-order renewal-moment asymptotic Var N(t)~2c tlog t/mu³ produces raw heat-current variance coefficient twice this, not weak-limit variance. At beta_H=beta_C rewards centered and Donsker/random time change yields sqrt(t) Gaussian with matching raw variance 2/(beta² mu). Independent inverse-Rayleigh tail/mean numerical checks at 3 parameter triples matched coefficients. The raw variance is explicitly prior; no claim finite check proves the limits.

## originality

PASS

Qualified best-of-knowledge original evaluated final claim relative to the inspected primary results and actual Resultary semantic search, not a universal historical priority certificate. Prior renewal-reward moment results use related not identical observables; check coefficients under cycle conversion.

## value

PASS

A sharp distribution-vs-raw-second-moment mismatch for a concrete heavy-tailed physical renewal-reward model is a nontrivial boundary phenomenon: it delineates exactly when a Gaussian current limit fails to calibrate variance and shows a discontinuous equilibrium scaling change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
