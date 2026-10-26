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

The result is analytic. No finite enumeration or numerical log is used as evidence for the universal assertion. The following checks are mathematical and can be repeated symbolically.

1. **Seed:** With \(S=2^{t+1}-1>p\), \(b=(S-p)/2\) is an integer with \(0\le b<2^t\). Its binary digits correspond to distinct divisors of \(2^tp\). The divisor \(2^tp\) plus these digits sums to exactly half of \(\sigma(2^tp)\).
2. **Multiplicative closure:** For coprime positive integers \(K,w\), their divisors decompose uniquely as products of divisors. Each equal-sum partition of the divisors of \(K\) induces one for \(Kw\) by multiplying both sides by all divisors of \(w\).
3. **Residue check:** For odd \(n\) and odd \(p\nmid n\), \(n-K\) is odd and nonzero modulo \(p\). Thus \(\gcd(n-K,2pK)=1\).
4. **Exponents and positivity:** \(K\le2p^2\), \(M=2pK\le4p^3\). Linnik exponent \(5\) yields \(q\ll p^{15}\). If \(p\le2n^\delta\) and \(\delta<1/15\), then \(q+K=o(n)\) uniformly, ensuring the multiplier index is a positive integer.
5. **Distinctness:** Each eligible \(p>n^\delta\) divides the constructed Zumkeller summand \(z<n\), while any integer below \(n\) has no more than \(\lfloor1/\delta\rfloor\) such distinct prime factors. Therefore the many parameter choices yield at least the claimed number of *distinct* ordered additive representations.
6. **Asymptotics:** The prime number theorem applied to \((n^\delta,2n^\delta]\) gives \(\pi(2n^\delta)-\pi(n^\delta)\sim n^\delta/(\delta\log n)\); excluding the bounded number dividing \(n\) does not alter the limit.

The proof is self-contained apart from classical least-prime-in-progression and prime-number-theorem bounds. Verification of originality is literature-limited; this is not an independent audit or certification.
