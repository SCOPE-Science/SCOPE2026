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

The proof is symbolic and requires no unbounded computation.

1. For exactly three prime supports, the maximal possible geometric-tail sum with all primes odd is less than \(1\), forcing the smallest prime to be \(2\).
2. With smallest prime \(2\), the defining positive integer is less than \(2\), hence equals \(1\).
3. For every maximal prime power \(s^a\Vert n\), reduction of the exact identity modulo \(s^a\) gives \(m(1+s+\cdots+s^{a-1})\equiv1\pmod{s^a}\), where \(m=n/s^a\).
4. The squarefree branch forces \(n=30\).
5. The complete total-multiplicity-four patterns \(2^2qr\), \(2q^2r\), and \(2qr^2\) yield respectively \(380\), \(306\), and no solution.
6. The final reciprocal identities verify all three survivors exactly.

A separate exact-rational enumeration through \(200000\) returned only \(30,306,380\) under the same finite filters. That computation is a regression check only and does not certify exhaustiveness beyond its bound.

Limit: no statement is made for three-prime-support prime power Giuga numbers with \(\Omega(n)\ge5\), or for support size at least four.
