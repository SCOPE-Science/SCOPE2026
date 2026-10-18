---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Direct differentiation of exact Eq.(6) gives Phi-dot=z²-(1+b)y² and E={y=z=0}. For b≤-1, the nonnegative integral vanishes on an interval only if z=0 and then y constant; if y !=0, zdot=wy=0 forces w=0 but wdot=-y²<0, contradiction. Strict Φ increase excludes recurrence and, on compact forward/both-sided orbits, LaSalle restricts limit sets to E; bounded x ensures w−Phi=bxy→0. Compact invariant probability stationarity gives E[z²]=(1+b)E[y²], and b=-1 support invariance plus bounded x forces y=0. A periodic orbit has zero-mean y and integral z²=(1+b)y², hence Wirtinger T≥2pi/sqrt(1+b); equality y sinusoidal incompatible with zdot=w(y-a z) for a!=0 or wdot at extremum for a=0. Independent SymPy coboundary/parameter identity checks passed.

## originality

PASS

Best-of-knowledge original model-specific exact scalar coboundary and its structural b=-1 gradient-like and strict periodic duration consequences. Full 2016 defining paper addresses numerical chaos at b=0.1 and local eigenvalues; a plausible 2019 multistability study remains only abstract-read and residual risk, not evidence of covering the analytical all-a,b theorem.

## value

PASS

The exact b=-1 transition from possible recurrence to a gradient-like flow is an intrinsic dynamical boundary for a canonical chaotic example with a whole plane of equilibria. The forced invariant-measure balance and strict, parameter-dependent period slowdown are mathematically motivated structural constraints, not simulations or arbitrary tiny gains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
