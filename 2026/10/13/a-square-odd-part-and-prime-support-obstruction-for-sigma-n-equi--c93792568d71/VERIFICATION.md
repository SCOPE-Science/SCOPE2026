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

# Reproducibility and exact checks

The standalone `verify.py` uses Python 3 standard-library arithmetic only. Run `python3 verify.py` from the directory containing this file. The verified execution printed:

```
VERIFY_OK range=6..1000000 residue_five_hits=0 support_violations=0 local_power_cases=1064 low_boundaries_passed=3
```

Its divisor-sum sieve uses exact integers and tests every \(n\) from \(6\) through \(1{,}000{,}000\) inclusive. For any remainder-five hit it checks the stated support and odd-square conditions. It also rechecks the strict rational bounds that reduce three odd primes to \(3,5,7/11/13\), and checks the exact local identity for \(1064\) even-exponent parameter triples. Absence of a witness in this finite interval and those local tests is not evidence that no larger witness exists. The unrestricted proof in RESULT.md separately proves every necessary structural statement.

The central symbolic identity is obtained from \(\sigma(2^a p^b)=2(2^a p^b)+5\), letting \(t=2^{a+1}\) and using \(p^b=1+(p-1)(1+p+\cdots+p^{b-1})\):
\[
(t-p)(1+p+\cdots+p^{b-1})=6.
\]
No independent audit or external verification is claimed.
