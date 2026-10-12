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

# Verification

The theorem in `RESULT.md` is symbolic and unbounded. The accompanying `verify.py` is finite regression evidence only.

The proof-critical checks are:

1. For a prime power \(p^a\), the equation reduces exactly to \(a=p-1\).
2. For \(p^a q^b\), it reduces exactly to \((a+1)q+(b+1)p=pq+1\).
3. When \(p=2\), parity forces \(a+1\ge3\), contradicting the size of the right side.
4. For odd \(p\), the coefficient \(a+1\) lies in \(\{2,\ldots,p-1\}\) and is the unique inverse of \(q\bmod p\); the second exponent is then forced and positive.
5. The squarefree specialization is exactly \((p-2)(q-2)=3\).

`verify.py` checks these formulas against direct exponent enumeration over a finite box of prime supports and confirms the initial solutions. A finite pass does not establish the infinite theorem; exhaustiveness is supplied only by the symbolic proof.
