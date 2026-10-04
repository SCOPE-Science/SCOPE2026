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

The proof uses Stewart's odd almost-practical criterion and the closure of odd almost practical numbers under multiplication by a prime already dividing the number. These theorem statements were checked in the full text of arXiv:2207.09053, Section 3, where they are attributed to Stewart's 1954 paper.

`verify.py` performs independent finite arithmetic checks. It generates the divisor lists of \(945\), \(1575\), \(2205\), and \(315\); evaluates every transition in Stewart's criterion; verifies by exact subset-sum bitsets that each positive base misses exactly \(2\) and \(\sigma(n)-2\); checks the \(a=1\) obstruction; and tests all \(216\) triples with \(1\le a,b,c\le6\) against the theorem.

The finite grid does not prove the infinite classification. Infinite coverage comes from the proved three-base partition of exponent space together with Stewart's multiplication closure. Direct full-text access to Stewart's original article was unavailable, so originality retains that source-access risk.
