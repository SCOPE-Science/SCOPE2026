---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The original fixed-a, kappa>0 system has the exact invariant H=g(x)^2 y^2/2+int_0^x u g(u)^2 du; q=int_0^x g du is a global increasing diffeomorphism, and p=gy yields dot q=p, dot p=-W′(q) in physical time. The coercive single-well W has exactly two turning points, one minimal oval period at every E>0. At both signed infinities q~g/(kappa x-a), V~g²/(2kappa), so W(q)~q²log|q| and W′(q)~2qlog|q|. Exact W″(q)=1+x(kappa x-a)=O(log(2+|q|)) yields locally uniform and equi-Lipschitz scaled force F_E(z)=W′(Q_Ez)/(Q_E logE)->z; positive-turn initial z_E->1 and z′_E=0. Continuous dependence gives (z,z′)->(cos tau,-sin tau), with unique-monotone turn/crossing structure excluding spurious shorter returns; sqrt(log E)T(E)->2pi. The tail turning-coordinate equation yields x_±=a/kappa ±sqrt(logE/kappa)+o(1), and inverse q forces x/R_E->sgn cos(2pi s) except at the two transition phases, uniformly bounded by turning values; dominated convergence proves finite Lp and the two-atom occupation law. An independently implemented symbolic check verified H cancellation, canonical dp/dt and W″; independent high-precision quadrature at a=0,kappa=1 and A=3,5,8,10,14 shows normalized periods tending toward one, not proof of the universal limit.

## originality

PASS

Best-of-knowledge: the original cubic global-center classification, the accessible full general separable-Hamiltonian 2019 preprint and 2000 leading-term theorem, and close published mathematical records do not mathematically imply the joint universal logarithmic physical period, uniform canonical sinusoid, and inverse-coordinate two-atom law. Full relevant theorems have been inspected; old center existence and generic conjugacy are not claimed new.

## value

PASS

This fixed two-parameter cubic global-center family is a natural coefficient slice in a published qualitative classification; asymptotic dynamics on its entire high-energy annulus is a motivated question. The exact physical-time 2pi/logarithmic-frequency law, globally uniform canonical cosine/momentum limit, and sharply nonuniform inverse-coordinate square wave/two-atom time measure are complementary structural asymptotic facts not obtained by the existing center classification. The latter distinguishes phase-space canonical harmonicity from observables measured in original physical coordinates; a researcher studying long orbits and residence statistics could use the precise limit. The algebraic conjugacy alone is standard; the mathematical value lies in the full quantitative asymptotic regime rather than a named new tool. No stronger multi-parameter, finite-energy monotonicity or jump-layer theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
