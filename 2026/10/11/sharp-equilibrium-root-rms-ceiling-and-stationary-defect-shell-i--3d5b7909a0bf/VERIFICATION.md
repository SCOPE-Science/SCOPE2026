---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

With generator L, antiderivatives in each coordinate establish the three conditional regressions from invariance. Stationarity of x^2 and z gives h=E[z]=E[x^2]=E[xy]; h=0 would force x=0 and contradict c>0 in the mean y equation. Orthogonality of residual R=y-x gives Var(y)=Var(x)+s, s=E[R^2]. Direct differentiation of V=x^2/sigma+y^2+z^2 yields Var(z)+s=h(r-1-h)+cm. By Cauchy m<=sqrt(h)=q, so q^3-(r-1)q-c<=0, and the cubic has one positive root xi+. Equality forces m=q, s=Var(z)=Var(x)=0 and hence the positive equilibrium atom. The zero-speed-defect support must be equilibrium by the 1D z-flow and invariance. The independent exact rational algebra and high-precision numerical-root checks agree, but neither substitutes for the generator proof.

## originality

PASS

The primary 2016 same-system full article studies equilibria, dynamics, bifurcations, periodicity and chaos but does not imply the invariant-probability all-state moment theorem. General generator orthogonality is known, but the combined sharp positive-equilibrium mean-height ceiling is a separate statement. The short generator derivation entails an unindexed earlier observation risk.

## value

PASS

The stationary RMS ceiling calibrated to the positive convective equilibrium is sharp for all compact recurrent regimes, including possible chaotic invariant measures, while the speed-defect shell quantifies departures from regression. The bound offers exact consistency tests for observed nonstationary/chaotic parameter regimes without claiming chaos existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
