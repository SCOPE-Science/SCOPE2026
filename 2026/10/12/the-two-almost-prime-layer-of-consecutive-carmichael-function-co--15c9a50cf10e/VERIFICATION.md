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

The proof uses only the standard prime-power formula for Carmichael's function and an exhaustive factorization split.

If the even member has \(\Omega\le2\), it is \(2\), \(4\), or \(2p\) with odd prime \(p\). For \(2p\), equality forces the Carmichael value of the adjacent odd integer to be \(p-1\). The odd integer is prime, a prime square, or \(qr\) with distinct odd primes. The first two cases are eliminated directly. In the last case,
\[
\lambda(qr)=\frac{(q-1)(r-1)}{\gcd(q-1,r-1)},
\]
and combining this with \(qr=2p\pm1\) produces the two sign contradictions in `RESULT.md`.

The packaged checker independently computes Carmichael values from factorizations for every \(n\le2{,}000{,}000\). It confirms that the only pair satisfying both \(\Omega\)-bounds is \((3,4)\), while also finding many unrestricted consecutive coincidences. The finite scan is corroborative only.
