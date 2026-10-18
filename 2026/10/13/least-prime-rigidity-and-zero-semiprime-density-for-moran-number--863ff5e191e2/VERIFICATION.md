---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For Omega(n)=2 the square case r^2 forces S(r^2)=r and r≡1(mod9) or r=3. Digit-sum bound r<=18 log10 r+9 gives r<41; remaining r=3,19,37 have S(r^2)=9,10,19, never r. For pq (p<q), quotient prime forces S(pq)∈{p,q}; if S(pq)=q, q<41 and q(p−1)≡0 mod9 give q=3 with p=2 or p=19 and q∈{23,29,31,37}, all eliminated by explicit digit sums. Thus S(pq)=p; converse immediate. Bound p<=9 digits(n) limits p to O(log x) in n<=x. A prime-counting upper bound uniform over p<=O(log x) plus Mertens gives M_2(x)=O(x logloglog x/log x), and Landau gives zero relative semiprime density. Independently checked exceptional cases and generated all 1617 semiprime Moran numbers <=10^6, all squarefree with digit sum equal to smaller factor. This finite enumeration is corroboration, not an infinite proof.

## originality

PASS

The closest primary literature and published-result searches were compared for statement implication and actual mathematical object, not just titles. Witno 2010 construction n=12p and repunits does not imply that all semiprimes must satisfy S(pq)=p; its conjectural global count does not imply relative zero density within semiprimes. The submitted use of support and modulo-nine exceptions does. The term Moran number equals Niven number with prime quotient n/S(n); searching both aliases and Omega(n)=2, biprimes, products of two primes found no prior exact rigidity under those formulations. Residual risks are retained; inaccessible full text alone is not equated to scientific failure.

## value

PASS

Complete multiplicative-layer classification in the naturally defined Moran/Niven-prime class and a quantitative relative-density-zero conclusion. This is a substantive connection of digit constraints, prime-factor support and analytic semiprime counting, not an arbitrary cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
