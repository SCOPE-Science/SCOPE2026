---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Published 2026 outer-extremizer theorem for every bounded H^p functional with p<1 makes any maximizer zero-free and outer; take analytic fourth root g in H2, norm1. Coefficients of g^4 give |a0+tau a2|<=x²+4tau x^(3/2)sqrt(v)+6tau x(1-x-v), where x=|g0|²,v=|g2|², |g1|²=1-x-v, tails waste H2 norm. Exact v optimization gives v=x/9 if x<=9/10 and v=1-x if x>=9/10; a one-variable calculus step yields tau=1/2 change of extremizer family and N(tau) piecewise. Independently verified SymPy N(1/2)=27/20, N''(left)=81/125 and N''(right)=486/125. Phase equality gives unique even fourth power for tau<=1/2 and two conjugate-sign linear-term fourth powers for tau>1/2; both outer by root moduli. Supporting-line duality identifies Phi2 for t>=81/256 and terminal Phi2=Phi1 for t>=81/100 using published Theorem12(ii). Finite checker is corroboration, not H^p outer theorem proof.

## originality

PASS

Brevig–Søvik arXiv:2610.21788 Thm1 establishes necessity of outer extremizers for 0<p<1 (enabling fourth-root reduction) but no mixed coefficient norm. Brevig–Saksman arXiv:1905.09547 gives pure second coefficient bound 27/16. Brevig–Grepstad–Instanes 2023 Thm12 computes Phi1 and Question2 asks terminal Phi2=Phi1; in p=1/2 case proposed threshold t0=81/100, exactly the new proven interval, not prior answer.

## value

PASS

Direct analytically sharp answer to an explicitly posed Hardy coefficient extremal Question 2 in the natural p=1/2 case; identifies full mixed functional phase bifurcation, all equality functions and a nontrivial fixed-origin boundary, not a substitution of known pure coefficient bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
