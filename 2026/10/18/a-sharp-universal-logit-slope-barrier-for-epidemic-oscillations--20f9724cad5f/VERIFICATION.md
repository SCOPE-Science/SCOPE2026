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

For the homogeneous SIS/logit ODE xdot=L-x, Idot=I[beta(1-x)(1-I)-gamma], delta_x>=-m and 0<L(1-L)<=1/4 imply L_x<=sigma*m/4. The Dulac multiplier 1/I on the simply connected physical open square gives divergence -(1+sigma L(1-L)delta_x)/I-beta(1-x), strictly negative for sigma*m<=4 including equality, hence no periodic orbit. For sigma=1,m=4+eta, beta=eta,gamma=3eta/8, delta=m(3/2-x-4I), eta in (0,1), a1=m/2,b1=3m/2,a0=-7m/2,b0=-5m/2 meet standing payoff conditions. A monotonic scalar equilibrium equation yields unique endemic E=(1/2,1/4). Its Jacobian has trace eta/8>0, determinant eta(24+5eta)/32>0, discriminant -eta(192+39eta)/64<0, hence hyperbolic source. Disease-free boundary has a unique saddle whose physical stable manifold lies in I=0. At I<=1/16, x>=1/2 forces xdot<-1/6, so within 3 time units low-infection trajectories enter x<=1/2 unless I exits the strip, where Idot/I>=3eta/32. Along excursions Idot/I>=-gamma, giving uniform positive I lower bound from interior data. Thus every strictly interior omega limit is compact in open square and avoids the hyperbolic source, and Poincare–Bendixson gives a periodic omega limit. The explicit finite rational/script checks corroborate Jacobian and bounds, while unbounded-time existence is proved analytically.

## originality

PASS

Best-of-knowledge originality assessment of this EXACT final statement against published mathematical results and the source model, not certification of historical priority. General mathematical machinery and prior model definitions are attributed; claim-specific evaluated classification is not found among inspected primaries. A failed search is not novelty proof. One cannot infer the sharp universal threshold merely from finding a stable epidemic equilibrium: the below-bound half uses a global Dulac sign, while sharpness requires an admissible model with a repelling endemic source and uniform interior persistence. Original local-stability analysis does not logically force either.

## value

PASS

Exact universal no-cycle threshold with sharp arbitrarily close above-threshold oscillatory examples for the SAME epidemiological logit equations distinguishes structural impossibility from merely numerically observed oscillations and provides a useful model-level parameter criterion, rather than a generic Bendixson exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
