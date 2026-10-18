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

With unit proximal step, two strict scalar contractions x/(kappa+1) and (x+1)/2 (kappa>=1) admit a unique invariant law for each p in [0,1] and all finite starts. Independent stationarity gives mean mu=(1-p)w2/W and variance p(1-p)w1^2w2^2/(W^2 S), with w1=kappa/(kappa+1),w2=1/2,W=pw1+(1-p)w2,S=p(2w1-w1^2)+(1-p)(2w2-w2^2)>0. Fixed equal-weight target x*=1/(kappa+1): R=Var+(mu-x*)^2. Independently differentiated exact rational R to recover derivative sign P(p)=A p^2+B p-3(kappa+1)^4 where A=(kappa-1)(kappa+3)(kappa^2+4kappa+5), B=6(kappa+1)^2(kappa+3). P increases on [0,1], P(0)<0 and P(1)=-2kappa(kappa+2)(kappa^2-2kappa-7); hence unique optimizer interior for 1<=kappa<1+2sqrt(2), exactly p=1 for kappa>= boundary (root p=1 at equality). The unbiased-stationary-mean p_ub=(kappa+1)/(kappa+3) is less than optimal for kappa>1 and gives R(p_ub)/R(1)=kappa^2/(2kappa+1). Source derivative, rational boundary, unbiased identities were independently reconstructed with SymPy. Fixed objective is NOT optimized in the usual unbiased algorithm sense by p=1.

## originality

PASS

Asi–Duchi 2018 studies stochastic approximate proximal convergence, Bianchi–Hachem–Salim 2017 the general constant-step random-resolvent invariant framework, and Défossez–Bach 2014 optimizes explicit LMS sampling with different objective conventions. None of the materially inspected general statements yields the displayed exact scalar uncorrected sampling transition kappa=1+2sqrt(2) or normalized stationary-risk comparison. Resultary other coordinate-sampling and STORM stationary covariance claims concern other update laws.

## value

PASS

The stationary variance/bias policy problem is a natural quantitative diagnostic of constant-step stochastic resolvents. Its exact critical curvature 1+2sqrt(2), unique optimal policy, and unbounded relative risk of an unbiased stationary mean reveal a non-obvious phase boundary with an explicit warning about implicit objective shift. It is a motivated small theoretical benchmark rather than a universal recommendation to omit components.

The dated certificate retains the supplied scientific assessment, sources and limitations.
