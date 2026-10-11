---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

If \(\sigma(n)\) is odd, the standard parity criterion gives \(n=2^c m^2\) with odd \(m\). The pure two-power case reduces to \(2^{c+1}-1=3^b\), whose only nontrivial solution is \(c=1,b=1\). If an odd prime \(p^{2e}\) divides \(n\), multiplicativity forces \(1+p+\cdots+p^{2e}\) to be a power of three. For \(p\equiv0\) or \(2\pmod3\) that sum is not divisible by three; for \(p\equiv1\pmod3\), divisibility requires \(2e+1=3t\), and the factor \(p^{2t}+p^t+1\) has 3-adic valuation exactly one but is larger than three, so has another prime factor. A fresh divisor-sum sweep through 50,000 found only \(n=1,2\), corroborating the symbolic proof.

## originality

PASS

Sándor's foundational paper was materially reread in full around the definition and initial values of the maximum sum-of-divisors function \(\Sigma^*\). It tabulates \(\Sigma^*(3)=\Sigma^*(9)=\Sigma^*(27)=2\) and proves general bounds, but it does not state the all-exponent ternary ray. Fresh searches for the inverse divisor-sum equation \(\sigma(n)=3^b\), including OEIS and Resultary aliases, did not locate a stronger published classification. The submitted proof is symbolic and closes the whole ray.

## value

PASS

The theorem closes an infinite prime-power ray that the defining paper explicitly begins with the values 3, 9 and 27, and gives a complete inverse-divisor-sum classification behind it. This is a natural exact structural continuation of a foundational arithmetic-function table, not a bounded recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
