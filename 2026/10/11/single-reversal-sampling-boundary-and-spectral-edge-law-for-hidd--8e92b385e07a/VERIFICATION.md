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

At frozen RESULT.md blob d83a9b64f6809c0ca339b2c03f451ecd0482b7ce, independence and stationary OU covariance yield C_a(t)=(r e^{-at}+a q(t))/(r+a), r=A/B. Direct quotient differentiation gives sign F_a(t)=e^{at}q(t)-1-(a+r)t. If a<=b=inf supp ν>0, F_a<0. If a>b, F_a(0)=0, F_a'(0)=-(r+Eβ)<0, F_a''(t)=∫(a−β)^2e^{(a−β)t}ν(dβ)>0, and positive spectral mass β<a forces growth, proving exactly one positive crossing. At crossing ∂_a F=t²(a+r)>0 gives decreasing t_*(a); endpoint limits and the inverse t→0 law follow from q(t)=1−Eβ t+o(t). Laplace–Stieltjes integration by parts and ν([b,b+h])~Kh^κ give q(t)~KΓ(κ+1)e^{-bt}t^{-κ}; substituting the exact root yields the long-lag (κ+1)log(t)/t correction and the stated constant. The finite 3-rate numbers in source are examples, not proof. Checked fixed A,B,ν, positive t, κ=0 atom, and κ>0 edge.

## originality

PASS

Best-of-knowledge PASS for the all-positive-mixture global unique reversal and conditional sharp spectral-edge law, distinguishing mere covariance identities and shared-noise early-warning studies from theorem implication. Highly relevant Ditlevsen full text was inaccessible, documented without turning lack of access into scientific FAIL. Failed Resultary service and no-result search are not novelty proofs.

## value

PASS

A population-level sharp sampling-lag reversal criterion and monotone unique boundary for a full spectral-measure class are mathematically motivated by ambiguous early-warning trends; the Tauberian edge constant identifies which nuisance spectral feature controls long-lag inversion. The exact formulas, rather than only qualitative masking, may guide future modal covariance calculations. Does not claim finite-sample detectability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
