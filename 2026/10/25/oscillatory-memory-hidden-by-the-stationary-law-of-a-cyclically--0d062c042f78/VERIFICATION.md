---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Construct the stationary chain and reset clock as independent two-sided processes. The backward reset age is Exp(r), while the directed cycle is stationary uniform, giving a mixture of three planar Brownian resolvent densities and E|X|²=a²+4D/r. The chain vertex complex eigenvalue is -lambda with lambda=3nu/2-i sqrt(3)nu/2, yielding E[v(Y0)·v(Ys)]=a²exp(-3nu s/2)cos(sqrt(3)nu s/2). Conditioning on the last reset between 0 and t and integrating an independent backward age gives C(t)=(a²+4D/r)e^{-rt}+a²r² Re[(e^{-lambda t}-e^{-rt})/(r²-lambda²)]. For r>3nu/2 the oscillatory complex mode is the slow nonzero term, forcing unbounded negative windows; for r<3nu/2 the e^{-rt} coefficient is algebraically positive; at equality the offset 10a²/13+4D/r competes with amplitude 3a²/sqrt13, giving Dc=3nu a²(3sqrt13-10)/104 and all strict/equality cases. Independent nested numerical age/time quadrature agreed in 108 cases to 9e-16, and critical-envelope algebra was cross-checked, but all-times and all-parameters assertions use the analytic proof.

## originality

PASS

Classical Poisson resetting and independent random reset positions yield the Bessel resolvent marginal; this part is covered and not asserted as novel. A persistent, autonomously cycling three-state target changes two-time structure while leaving marginal fixed. The relevant new statement is a sharp sign classification of time covariance for a different coupled protocol, not the stationary resolvent formula.

## value

PASS

The exact stationary one-time spatial distribution is blind to the cyclic target speed, but the two-time covariance records it and exhibits a sharp late-negative-lag transition including a nontrivial critical diffusivity. This is a motivated dynamical identifiability and oscillatory-relaxation result for the precise autonomous-environment model, not merely a routine Bessel integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
