---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Direct weighted covariance calculation for weights (u,1,v)/(1+u+v), D=2(S+P)/(1+S)^2, CthetaG=(x^2-a^2)[Sx-a(v-u)]/[2(S+P)], CGG=S(a^2-x^2)^2/[2(S+P)] yields F(x)=(1-omega)x+omega a*tanh(ax/kappa^2), with 0<omega<1 for |x|<a. Strict increase/concavity of tanh gives unique stable ±x* for a^2/kappa^2>1 and origin otherwise; convex-map ordering prevents overshoot. At equality F=x-omega0*x^3/(3a^2)+O(x^5), telescoping 1/x_n^2 gives limit sqrt(n)|x_n|. The artanh inversion provides both branch asymptotics. Independent test directly evaluates covariances, without presuming reduced map, on 120 samples. Finite checks corroborate rather than prove the all-n limits.

## originality

PASS

Original statement is the complete global discrete-time basin diagram, strictly positive false-attractor residual at each fixed positive polarization scale, pitchfork threshold kappa=a and exact critical rate for a specific finite-ridge polarized EKI; earlier cited method papers give ingredients and linear or continuous-time theory but no inspected implication of this entire result. Best-of-knowledge with explicit priority risk.

## value

PASS

A minimal multimodal inverse-problem configuration with two already-correct particles exhibits a rigorously persisting false middle-particle attractor. The precise finite-polarization threshold, residual and ridge-dependent critical slowdown delimit what the practical local weighting accomplishes; the toy model is mathematically motivated and not a routine restatement of generic EKI convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
