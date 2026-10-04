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

The verification separates the arbitrary proof from finite stress tests.

The symbolic proof checks four points: gcd-cells are independent; distinct cells are completely adjacent exactly for incomparable divisor labels; a partial selection from a chosen cell cannot dominate the remainder of that cell; and a chain dominates exactly when it is maximal. Saturated maximal divisor chains then correspond bijectively to distinct orderings of the prime multiset.

For the extremal exponents, an adjacent swap of distinct primes \(a<b\) before a fixed suffix \(T\) replaces exactly one contribution \(\varphi(bT)\) by \(\varphi(aT)\). Euler's product formula gives \(\varphi(aT)\le\varphi(bT)\), so descending prime order attains the minimum and ascending order attains the maximum.

The standalone verifier performs direct graph-subset enumeration for small moduli and independent divisor-word checks on a wider suite. Its exact output is:

```text
VERIFY_OK
direct_graph_checks=n in {4,6,8,10,12,14,15,18,20}
word_chain_checks=28 composite moduli through 180
Z30_polynomial=z^3+z^4+z^5+z^8+z^10+z^12
Z48_polynomial=4z^15+z^16
```

The finite checks reproduce the published \(n=30\) and \(n=48\) polynomials. They are corroborative only; no finite computation is used as a proof for arbitrary \(n\).
