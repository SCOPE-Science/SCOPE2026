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
The package contains an ordinary integer-arithmetic checker (`verify.py`). Run `python3 verify.py` using Python 3 standard library. It computes the exact five-window GCD for each \(k=1,\ldots,500\) and checks the prime-to-42 identity and prime-five valuation. The five-window reduction itself is symbolic: the squares satisfy the monic fifth-order recurrence with characteristic polynomial \((X-1)(X^2-6X+1)(X^2-34X+1)\). The checker independently computes \(b_n\), \(B_n\), and \(C_n\), asserts their initial identities, and checks isolated exact examples. Finite enumeration does not certify the theorem for unrestricted \(k\), which rests on the proof in RESULT.md. No claim is made for primes \(2,3,7\); no external or independent audit has been performed.
