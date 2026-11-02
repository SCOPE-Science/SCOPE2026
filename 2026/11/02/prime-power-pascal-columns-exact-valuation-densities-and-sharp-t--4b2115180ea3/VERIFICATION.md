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

The proof uses Kummer's borrow theorem, independent residue-class counting, and explicit least-period witnesses. The independent numerical checker uses Legendre factorial valuations of \(\binom{n-1}{p^a-1}\) and direct exact integer binomial arithmetic for spot checks and row-number divisibility.

Run `python3 verify.py` from the directory containing this file and the verifier. No third-party packages, downloads, or precomputed lookup tables are required.

Tested primes: \(p=2,3,5,7\). Tested exponents: \(1\le a\le5\) for \(p=2\), \(1\le a\le3\) for \(p=3\), \(1\le a\le2\) for \(p=5\), and \(a=1\) for \(p=7\). Tested positive valuation levels extend through \(v=5\) (or through \(v=4\) and \(v=3\) for the larger primes). For each such triple, a full period of valuation-mass counts, two consecutive periods of threshold indicators, and the constructed counter-witness to the shorter period are checked. For every \((p,a)\), one full period of \(n\mid\binom{n}{p^a}\) is compared to the density formula using exact rational arithmetic.

Observed final success line:

```
VERIFY_OK independent_factorial_valuations=True exact_period_witnesses=True all_cases=11
```

No finite test certifies claims for arbitrary primes, exponents, or thresholds. No independent mathematical audit has been performed.
