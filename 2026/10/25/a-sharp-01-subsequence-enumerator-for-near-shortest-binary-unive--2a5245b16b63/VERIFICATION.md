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

The provided `verify_near_minimal_universal.py` uses standard-library Python 3 and enumerates every word with \(k+1\) zeros and \(k\) ones, for \(1\le k\le9\). It computes the exact scattered-\(01\) count from positions and uses a greedy arch test to select universal words. For \(1\le k\le5\), it also checks universality by testing all \(2^k\) distinct length-\(k\) patterns independently. It reconstructs the right-hand polynomial coefficients using ordinary binomial coefficients and checks equality at every exponent, together with total \((k+2)2^{k-1}\).

The actual command `python3 verify_near_minimal_universal.py` returned:

```
VERIFY_OK: k=1..9 full fixed-composition enumeration; k<=5 direct all-pattern tests; q-polynomials and totals
```

The all-integer result is proved by the unique arch decomposition in `RESULT.md`. The finite tests do not certify arbitrary parameter values; an independent audit has not been performed.
