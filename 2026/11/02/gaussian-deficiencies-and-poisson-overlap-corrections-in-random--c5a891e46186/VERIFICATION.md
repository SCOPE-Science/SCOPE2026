---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For each uniform partial injection X in I_n, number of rank n-d elements is n! binom(n,d)/d!, yielding P(D=d)=binom(n,d)/(d! L_n(-1)). Composition with prior image size n-s and missing next-domain random d-set gives H=|missing-domain∩previous-missing-image|, hypergeometric with conditional falling-factorial moments (s)_r(d)_r/(n)_r, and Snext=s+d-H. Laguerre Perron asymptotic L_n(-a)≈exp(2sqrt(an)-a/2)/(2sqrt(pi)(an)^(1/4)) yields centered (D-sqrt(n))/n^(1/4)=>N(0,1/2), mu_n=sqrt(n)-3/4+O(n^-1/2). For fixed m, Sprev/sqrt(n)→j-1, D/sqrt(n)→1, so joint conditional factorial moments yield mutually independent H_j=>Pois(j-1), independent of Gaussian defects; C_m=>Pois(m(m-1)/2) and scaled product deficiency=>N(0,m/2). Conditional expected retained rank multiplies by 1-mu_n/n, giving n(1-mu_n/n)^m=n-msqrt(n)+3m/4+binom(m,2)+O_m(n^-1/2). Independent exhaustive direct pair products for n=2 (49 pairs) and n=3 (1156 pairs) verified hypergeometric defect-overlap transition exactly. Finite checks do not substitute the fixed-m infinite argument.

## originality

PASS

Qualified best-of-knowledge original evaluated final claim relative to the inspected primary results and actual Resultary semantic search, not a universal historical priority certificate. Known one-factor Laguerre defect asymptotics alone do not determine joint overlaps or all finite product ranks.

## value

PASS

The complete finite product-rank/overlap transition and joint Gaussian–independent-Poisson multiscale law for uniform rook-monoid products quantify a natural previously non-obvious interaction of missing domains and ranges, beyond the classical one-factor typical rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
