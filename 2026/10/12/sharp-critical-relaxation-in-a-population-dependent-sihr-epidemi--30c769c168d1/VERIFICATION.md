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

At R0=1 the source equilibrium condition f(N*)=c and invariant bound N<=N* imply I’=[f(N)-f(N*)−β(N)(I+H+R)]I <=−β* I², β*=β(N*)>0. This gives I->0 for I0>0; H,R,z=N*−N obey stable linear forced equations, hence decay to 0 and yield Lyapunov stability. Since I’/I->0, stable ratio equations H/I->h=δ/(m+μ+μ2), R/I->r=(γ+m h)/μ, z/I->d=(μ1+μ2h)/μ. Then differentiability at N*, f’≥0 and β(N)->β* give −I’/I²->K=β*(1+h+r)+d f’(N*)>0; integrating (1/I)’ gives tI->1/K, and t(H,R,z)->(h,r,d)/K. Integrating I∼1/(Kt) yields log t cumulative infection and confirmation flows. Boundary I0=0 is invariant with exponential stable subsystem and not included in nonzero tails. The bundled Jacobian/ratio checker and independent critical nonconstant-beta ODE replay corroborate identities but do not prove infinite-time asymptotics; the exact comparison/ratio proof does.

## originality

PASS

Jiao–Huang prove global disease-free stability strictly for R0<1, and their 2022 stochastic follow-up repeats the deterministic threshold gap. Other epidemic models had R0<=1 global stability and algebraic critical tails, so neither equality stability in general nor t^−1 by itself is novel. The source-specific exact coefficient K coupling hospitalization, recovery, demographic depletion and contact-law slope, the scaled vector and logarithmic cumulative case are not supplied by these earlier theorems. This is a meaningful new boundary regime for the printed population-dependent SIHR model.

## value

PASS

Critical slowing at the epidemic threshold is mathematically and epidemiologically meaningful because disease-free global attraction coexists with an O(1/t) infection/hospitalization tail and logarithmically divergent cumulative flow. The explicit positive coefficient K encodes the source model’s independent hospitalization, recovery, demographic mortality and population-sensitive contact slope. This is not an arbitrary parameter slice: R0=1 is the natural omitted equality boundary of the source’s strict-threshold theorem, and the proven global profile is stronger than a qualitative transcritical heuristic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
