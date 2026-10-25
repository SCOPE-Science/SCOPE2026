---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The exact generating-tail identity P(T_e>=r)=e^r A^(r-1)(1-e)/(r-1)! is established by tail summation, where A(z)=sum_{k>=1}P(X>=k) z^(k-1). The critical a_k~c/k Abelian estimates give P(T_e>=1)~ce log(1/e), P(T_e>=r)~ce/(r-1), and fixed conditional masses (r-1)/[j(j-1)] (j>=r) whose total is 1; countable Scheffe supplies TV convergence. For canonical P(X=k)=1/[k(k+1)], the beta integral yields D=e(1-e+e log e)/(1-e)^2, p2=e(1-e^2+2e log e)/(2(1-e)^3), and exact TV=1/2-p2/D. Beta(j-1,2) stochastic order and strict covariance put j=2 below and j>=3 above baseline for every 0<e<1. Independent numerical integration at e=0.2,0.5,0.8 reproduced D and exact TV; those values are corroboration only.

## originality

PASS

Exact mathematical comparison to subcritical Sibuya and thinning literature; neither the finite-mean collapse nor 0<alpha<1 regularly varying Sibuya theorem logically supplies fixed r>=2 conditional law or epsilon log epsilon canonical exact TV at alpha=1. Primary extracts inspected; residual priority is explicit.

## value

PASS

Critical-tail exponent 1 and fixed-r multiple-survivor law are plausible original boundary phenomena, along with canonical all-e likelihood-ratio one-crossing and sharp exact TV rate, not just standard finite-mean or 0<alpha<1 Sibuya thinning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
