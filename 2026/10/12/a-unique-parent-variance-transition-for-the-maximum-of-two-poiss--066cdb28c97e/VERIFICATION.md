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

Independent identical Pois(lambda), lambda>0: M=(X+Y+|X-Y|)/2. Skellam series yields k=e^{-2lambda}I_0(2lambda) and h=lambda e^{-2lambda}(I_0+I_1), E[M]=lambda+h and Var(M)=lambda+lambda*k-h^2. Derive h'=k from Bessel derivatives and Cov(S,|D|)=2lambda*k; for r=I_1/I_0, R=h^2/(lambda*k)=lambda*k*(1+r)^2 has (log R)'=(1-r)[2+1/(lambda(1+r))]>0 as 0<r<1. The small- and large-lambda Bessel asymptotics give R->0 and R->infinity, hence exactly one crossover, root 1.16679740191840365086656...; sign before/after follows from lambda*k*(1-R). E[M]-Var(M)=h^2+lambda*exp(-2lambda)*I_1>0. Independent direct finite Poisson-max probability mass summation verified exact-moment formulas at six intensities; this finite check is not the crossing proof. Asymptotic Var(M)/lambda->1-1/pi is consistent. No claim for unequal rates or more than two counts.

## originality

PASS

The published own-mean ultra-log-concavity theorem and classical Skellam/Bessel identities are credited. The question here is parent variance lambda rather than E[M]; strict monotonicity of R and unique sign switch is not an immediate restatement of own-mean underdispersion. No equivalent parent-crossing theorem was identified among targeted primary and Resultary records, but older order-statistic/Bessel work could contain an equivalent special case.

## value

PASS

Whether taking the larger of two replicate counts raises dispersion relative to a single parent Poisson count is a natural statistical benchmark, distinct from the Fano ratio relative to the selected maximum's own mean. The unique global positive-intensity phase transition is a meaningful complete classification, not a point estimate or routine lower/upper bound; generalizations to unequal means remain unproved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
