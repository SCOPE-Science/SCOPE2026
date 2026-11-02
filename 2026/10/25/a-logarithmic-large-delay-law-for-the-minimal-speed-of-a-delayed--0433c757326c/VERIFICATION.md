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

For fixed d>0 the leading-edge characteristic dispersion is Delta_tau(c,lambda)=c*lambda-d*2(cosh(lambda)-1)-exp(-c*lambda*tau). The specified monotone front c_tau is characterized by its positive double root (model-specific primary theorem). Differentiating yields c*lambda=dL+E, c=dLprime-c*tau*E. The proof excludes any lambda>=epsilon as tau→infinity using E≤exp(-d*tau*L(epsilon)) and lambda*Lprime>L, so lambda,c,E→0. With p=c/(d lambda), y=d lambda² tau, z=py, ell=L/lambda²→1, m=Lprime/lambda→2, exact equations are E=d lambda²(p-ell), tau E=m/p-1, y(p-ell)=m/p-1. Thus ell<p<m and y→infinity (otherwise E bounded away from zero), p→1, tau E→1, z=log tau+o(1). Because lambda²~(log tau)/(d tau), y(ell-1)=o(1), so y(p-1)→1 and y=log tau-1+o(1). Finally tau c²/d=p²y=y+2*y(p-1)+o(1)=log tau+1+o(1). All limits use d fixed and unit delayed growth; the additive constant is derived analytically, not fit. A model-specific existence/minimal-speed double-root theorem is an established cited input rather than a new existence proof.

## originality

PASS

The original Guo–Zimmer (2014/2015) delayed nearest-neighbor lattice theory gives the same double-root speed characterization, but the inspected speed theorem and selected model sections do not state the sharp additive log tau+1 asymptotic. Ma–Weng–Zou (2006) is a serious broader delayed lattice source; its complete text remained inaccessible after lawful OA/arXiv attempts and authorized institutional request (VPN disconnected). Best-of-knowledge novelty rests on the additive constant and specified asymptotic, without claiming complete priority certainty.

## value

PASS

The minimal speed of a monotone delayed Fisher–KPP lattice front is a natural invariant. Its large-delay decay and sharp additive +1 correction are not a routine rewriting of the implicit double-root formula: the logarithmic asymptotic arises from balancing dispersive curvature against an exponentially delayed term. This is an exact, motivated asymptotic quantitative boundary useful for comparing delay laws; no general reaction/diffusion extension is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
