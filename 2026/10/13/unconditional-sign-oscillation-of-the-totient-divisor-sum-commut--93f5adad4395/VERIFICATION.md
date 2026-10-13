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

# Verification record

The script `verify.py` uses only integer arithmetic and the Python standard library. Direct divisor-sum and totient formulas were recomputed separately for all exponent indices \(2\le k\le36\) and compared against the Mersenne reduction. The calculations confirmed that all eleven prime indices through \(36\) yield negative values, the indices divisible by \(12\) yield positive values, the complete set of positive indices in this finite window is \(\{12,20,24,28,30,36\}\), and the first positive index \(12\) gives \(C(2048)=319\).

Exact command: `python3 verify.py`

```
VERIFY_OK k=2..36 positive_indices= [12, 20, 24, 28, 30, 36] first_positive_n=2048 C_2048=319 prime_indices_negative= 11
```

The script was run successfully from the enclosed source file before packaging. The proof of the claims for every qualifying exponent is algebraic and does not depend on the computational cutoff; no infinite search or independent audit has been performed.
