---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification scope
The proof consists of exact identities and denominator arguments in `RESULT.md`; no unproved computational lemma is needed. The accompanying `verify.py` uses exact integer arithmetic and `sympy` factorization, not floating point approximations. Executing `python verify.py` confirmed 15,980 parameter triples with \(p<501\), \(1\le a\le10\), \(1\le b\le17\), plus 1,080 triples with exponents \(b\in\{1,p+1,2p+1\}\) and \(p<201\). There were zero disagreements with the derived criterion and the final restricted classification. The finite ranges make no assertion about the infinitely many other inputs.

The primary logical checkpoints are: the exact derivative formula; comparison of the \(p\)-denominator; elimination of \(t\ge3\); squarefreeness of the odd part; and exhaustive analysis of zero, one, or two odd prime factors. A subsequent independent audit is not represented by these tests.
