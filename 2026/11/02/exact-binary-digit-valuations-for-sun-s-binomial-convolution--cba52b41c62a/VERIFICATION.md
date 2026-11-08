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

The actual proof specializes classical Clausen hypergeometric square to obtain exact finite expansion T_n=sum_{k=ceil(n/2)}^n (-432)^(n-k)a_k binom(2k,k)binom(k,n-k). Legendre gives v2(a_k)=2s2(k) and v2(binomial(2k,k))=s2(k). The k=n summand has exact valuation 3s2(n), while any k=n-j earlier contributes valuation >=4j+3s2(k)>=3s2(n)+j by binary subadditivity, strictly greater, so cancellation cannot change the unique minimum. Since 2n-1 is odd and v2(binomial(3n,n))=2s2(n)-s2(3n), the normalized valuation follows, using Guo for integer normalization. A separate exact-integer Python computation compared direct convolution and transformed sum plus both valuation identities at n=1..69; this is corroboration, not universal proof.

## originality

PASS

Sun states the convolution and divisibility questions; Guo establishes divisibility/integrality of the normalization, which yields no exact valuation. Yang 2017 Theorem 1.2 from actual full PDF asserts a lower bound on the valuation of individual normalized summands with equality at endpoints; those lower bounds do not imply the exact valuation of their SUM, where cancellation may change it. Clausen 1828 gives the analytic series identity; selecting its unique minimum 2-adic term is the additional arithmetic argument. Resultary search returned a Sun multinomial prime congruence, different summand/claim. Classical identities create a possible implicit-coverage priority risk, but no stronger valuation theorem identified.

## value

PASS

It provides the exact power of two in every term of a named arithmetic convolution and in its established integer normalization, sharpening earlier divisibility and termwise lower bounds by explicit digit-sum formula. The full index quantifier and noncancellation argument make it mathematically motivated beyond a small modulus experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
