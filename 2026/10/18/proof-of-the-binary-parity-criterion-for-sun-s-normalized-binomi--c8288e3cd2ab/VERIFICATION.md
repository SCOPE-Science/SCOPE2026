---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Legendre yields ν2(F(j))=2s2(j), and ν2(binomial(3n,n))=2s2(n)-s2(3n). Thus each positive rational normalized summand Q_n,k has exact valuation t+2c with t=s2(3n), c=s2(k)+s2(n-k)-s2(n), the number of binary carries. Guo 2013 Theorem1.2 supplies termwise ordinary integrality. Exactly 2^{s2(n)} k are carry-free submasks; k↔n-k pairs them, and even n central k=n/2 is never carry-free because its carry count equals s2(n)>=1. Pair contributions at exact valuation t+1 are odd when normalized, while other contributions have larger valuation. Therefore s_n/2^{t+1}≡2^{s2(n)-1} (mod2), yielding ν2(s_2^r)=3 and ν2(s_n)>=s2(3n)+2 otherwise; since s2(3n)>=2, the stated n>=1 mod16 dichotomy follows. Endpoints n=1 and k=0,n are included. Independently computed convolution for n=1..33 confirms integer quotients, valuation bounds and mod16; finite check is not the proof.

## originality

PASS

A189286 itself identifies exact oddness of s_n/8 as Sun’s conjecture; the August 2026 source specifically reports a proof of *integrality*, not the binary-parity clause. Guo 2013 established termwise integrality and cited 8-divisibility, but did not establish the iff oddness criterion in the inspected full original article. The new reflection-pair 2-adic carry argument resolves the stronger exact parity statement for every n>0. No equivalent earlier complete solution found in exact-form searches or semantic Resultary hits; best-of-knowledge only.

## value

PASS

An exact classification for all n of a named natural binomial sequence addresses the distinct 2011 recorded parity conjecture and strengthens 8-divisibility with digit-sum valuation bounds. Reflection cancellation is a substantive uniform arithmetic mechanism, not a finite table or a routine restatement of integrality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
