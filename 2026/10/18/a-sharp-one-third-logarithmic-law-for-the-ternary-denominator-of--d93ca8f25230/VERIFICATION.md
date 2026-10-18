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

# Reproducible checks and limits

Run `python3 verify.py` with Python 3 and its standard library. The source program recalculates all reciprocal gcd sums for \(1\le n\le1000\) as exact rational numbers, reconstructs their multiplicative numerator and compares the prime-\(3\) denominator predicate, then counts the exact valuation predicate for every \(n\le500000\). The observed counts are \(1479\) at \(10000\), \(13507\) at \(100000\) and \(64093\) at \(500000\). It also evaluates the absolutely convergent leading-constant product using primes below \(20000\), obtaining approximately \(0.284087846498\); no rigorous truncation-error bound is claimed for that decimal. `verification_output.txt` records the program's actual output.

The infinite statement depends on the proof's exact Euler product and controlled variable-exponent Selberg--Delange argument, not finite enumeration. No external independent validation or audit was conducted.
