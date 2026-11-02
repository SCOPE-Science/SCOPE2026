---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The root is defined for 0<rho<=1 as the unique mu in (0,1] solving I(mu,rho)=int_0^((1+rho)pi) t^(mu-1)sin(t-rho*pi)dt=0. At rho=1, mu=1; the source Lemma 7.2 supplies p=1-nu(1-epsilon)=O(epsilon^2) and J0=I_mu(1,1)>0. Direct integration gives I(1,1-epsilon)=1-cos(pi epsilon)=(pi^2/2)epsilon^2+O(epsilon^4). Differentiating I_mu in rho yields I_mu,rho(1,1)=pi int_0^(2pi) log(t)cos(t)dt=-pi Si(2pi), with vanishing moving-upper-endpoint term and vanishing logarithmic-by-sine boundary term. Uniform integrable log^k(t) domination gives I_mu(1,1-epsilon)=J0+pi Si(2pi)epsilon+O(epsilon^2) and bounded I_mu,mu. Expanding I(1-p,1-epsilon) in mu: 0=I(1,1-epsilon)-p I_mu(1,1-epsilon)+O(p^2), with p^2=O(epsilon^4). Dividing by the positive J0 yields p=pi^2/(2J0)epsilon^2-pi^3 Si(2pi)/(2J0^2)epsilon^3+O(epsilon^4), exactly for rho upward to 1, with no assertion outside local endpoint. Independent 65-digit mpmath quadrature/root values agreed: J0=2.43765339305722441181..., A=2.02440683921663419963..., B=-3.69997139635880357774..., p/e^2 at e=.02,.01,.005,.0025 =1.9544759801,1.9884566081,2.0061736066,2.0152241126 and cubic residual approaches B. These samples are corroboration only, not proof.

## originality

PASS

Qualified best-of-knowledge: Ma's 2026 all-parameter proof supplies the optimal implicit root, J0 and a certified quadratic bracket but not the exact limiting quadratic coefficient or cubic coefficient. The extra exact mixed derivative and reciprocal expansion have not been located in the inspected primary literature; they are short, standard-calculus refinements, a substantive priority limitation rather than a claim of a new general method. Koumandos–Lamprecht (2010) and Sangal–Swaminathan (2018) study fixed/near-interior rho values, not rho->1. An independent published Resultary result calculates the opposite rho->0 endpoint only. The original 2007 article and 2010 thesis remain residual full-text access risks, and Ma v1/v2 wording changes merit attention.

## value

PASS

The exact optimal sharp subordination parameter curve is a natural object that Ma's all-parameter theorem uses centrally. Its own endpoint section proves only 1.99<liminf p/epsilon^2<=limsup p/epsilon^2<2.05; here the precise tangency constant and negative cubic asymmetric correction are obtained for that same canonical sharp curve, supplying a calibratable local invariant for further global and higher-order analysis. This is a small exact analytic refinement rather than an intrinsically arbitrary parameter slice, a generic Taylor-method theorem, or a new certificate of Ma's global conjecture; its short textbook-calculus derivation makes value modest and is explicitly acknowledged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
