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

# Reproducible verification

Run `python3 checker.py` with standard Python 3, with no additional packages and no network. The program independently computes every prime count through \(89\,700\) by (1) sieve of Eratosthenes and (2) trial division, asserts their equality at every integer, enumerates every \((n,k)\) with \(5\le n\le299\) and \(1\le k\le n\), then checks \(\pi(kn)^{k+1}>\pi((k+1)n)^k\) by exact integer exponentiation. It also verifies \(\pi(300)=62\), the exact pair count \(44\,840\), and \(11^4<62\cdot4^4\).

Observed output:

```
verified exact small cases: 44840
maximum argument counted: 89700
prime-count at 300: 62
minimum positive integer-power margin: 4
minimum-margin cases: [(6, 1, 3, 5)]
prime-count cross-check: agrees at all integers 0..89700
certificate: PASS
```

The code proves the stated small-range inequalities once executed and inspected; it does **not** certify the analytic theorem's infinitely many instances. The large-range argument separately invokes the explicit Montgomery–Vaughan Brun–Titchmarsh bound and the Rosser–Schoenfeld lower bound, and derives the strict comparison with the exact threshold \(\pi(300)=62\). No external or independent audit has been performed.
