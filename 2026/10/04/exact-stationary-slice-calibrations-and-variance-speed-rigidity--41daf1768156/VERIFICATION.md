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

For the positive Brusselator, s=x+y satisfies sdot=A-x=(A-s)+y; bounded complete positive trajectories obey s(t)-A=∫_{-∞}^t exp(-(t-u)) y(u)du>0. Invariance tested against all smooth antiderivatives of s gives E[x|s]=A; against all antiderivatives of y gives B E[x|y]=y E[x²|y]. Positivity yields the conditional variance formula m(B/y-m), with m=E[x|y]>0. Bias dν=(x/A)dμ leads to Eν[x|y]=B/y. E[x|s]=A implies Cov(x,s)=0, hence Var(y)-Var(s)=Var(x)=E[(sdot)²]. If zero, x=A throughout invariant support, and xdot=0 forces y=B/A. Other invariant measures must have positive mass on both sides of x=A. Correctness for compact support in strictly positive quadrant; no extrapolation to boundary or stochastic model.

## originality

PASS

The 1971 classical work already obtains E[x]=A for periodic orbits; that is expressly excluded from novelty. The stronger conditional E[x|x+y]=A, inhibitor-fiber identity, biased nullcline and variance-speed equality require additional test functions and do not follow from the single unconditional average alone. A best-of-knowledge novelty conclusion is limited to the complete final theorem, not prior equations/local lemmas/classical parameters. Targeted original searches were undertaken but Resultary returned temporarily_unavailable/search_completed:false, not zero matches; full-text access gaps are candid risks.

## value

PASS

The two conditional slice calibration laws are stronger than the classical unconditional period mean and identify a size-biased nullcline relation. Together with a backward recurrent barrier and exact variance/speed identity, they supply nontrivial stationary orbit constraints for the canonical positive oscillating chemical model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
