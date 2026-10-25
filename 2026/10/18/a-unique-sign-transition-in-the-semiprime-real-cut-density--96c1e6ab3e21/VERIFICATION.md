---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Belton defines semiprime density Delta2(t)=a1(t)U(t)+a2(t)/2 with a1=1,a2=0 on 1/2<t<1, so exact branch-normalized density is U(t). For 1/2<t<1, the fractional-part integral gives zeta(t)<0 and derivative bounded by -(1-t)^(-2)+1/t<0; therefore (d/dt)log|zeta(t)|>0. For n>=2, local uniform convergence justifies Möbius/zeta differentiation and interchange with Euler-product log derivative: U_prime=zeta_prime(t)/zeta(t)-sum_{m>=2}Lambda(m)F(m^(-t)), F(z)=sum_{n>=2}mu(n)z^n. For 0<z<=1/sqrt(2), mu(2)=mu(3)=mu(5)=-1 and mu(4)=0, while mu(n)<=1 gives F(z)<=-z^2-z^3-z^5+z^6/(1-z)<0 since z^4/(1-z)<1. Hence U_prime>0 everywhere. At t down to 1/2, n=2 term yields (1/2)log(2t-1)+O(1) -> -infinity; at t up to1, log|zeta(t)|=-log(1-t)+O(1)->+infinity. This proves unique tau with one sign crossing. Integrability of logarithmic endpoint singularities, plus derivative of G(y)=e^(-tau y)B(e^y), gives G_prime=sum-integral of (t-tau)U(t)/t * exp((t-tau)y)>0, and opposite divergent limits; unique integrated zero follows. The supplied verify.py is numerical illustration only; every quantified step above is analytic.

## originality

PASS

Belton (2026) introduces precisely this semiprime upper-real-cut density and integral, discusses signed densities without the strict-monotone one-zero classification. The claimed novelty is an exact real-branch sign theorem for both density and integrated cut—not the definition of prime zeta, Möbius inversion, or generic Laplace transform positivity. The recent primary arXiv full text was consulted; no mathematically dominating statement or table found in the inspected sections; older prime-zeta monotonicity sources remain bibliographic risks.

## value

PASS

A density with logarithmic endpoint divergences and potential changes of sign is a natural analytic invariant in a published almost-prime continuation construction. A global unique density zero and a unique zero of the weighted semiprime contribution are structural facts permitting unequivocal sign interpretation; monotonicity of the Laplace-normalized integral is an independently usable analytic lemma, not a redundant restatement of an endpoint sign test. Scope remains strictly upper real cut and does not claim a full semiprime-counting error theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
