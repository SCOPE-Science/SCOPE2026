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

# Reproducible arithmetic checks

Run `python3 artifacts/verify.py` using Python 3 and only the standard library. Expected successful output:

```
VERIFY_OK matrix_periods=6,24 exact_period_residues=6,24 direct_indices=10000 f827_digit=809 l827_digit=802 f1654_digit=1592 smith_deficit=-19 factor_products=verified prime_certificates=not_independently_checked
```

The program separately calculates the two matrix-order identities, checks all \(6\) and \(24\) residues that are exhaustive because of those identities, compares the modular laws to \(10000\) exact recurrence indices, and checks the three digit sums at index \(827\) by full arbitrary-precision integer arithmetic. The latter check multiplies the factor lists published by B. Kelly and compares the products to independently generated Fibonacci and Lucas numbers. It does not issue independent primality certificates for those published prime factors.

The universal all-index result is a finite *proof certificate*, because the recurrence matrix identities show that its complete residue tables cover every integer index. The additional checks through index \(10000\) merely test implementations and are not substituted for the proof. Historical novelty and source completeness cannot be certified by an arithmetic program.
