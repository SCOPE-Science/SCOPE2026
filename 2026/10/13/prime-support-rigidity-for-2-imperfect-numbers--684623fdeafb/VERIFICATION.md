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
# Verification of the classification

The included standalone `verify.py` was run with Python 3 in an isolated working directory using exact integers. It constructs the arithmetic function by independent trial-factor and sieve-based factorizations, compares their outputs for all \(1\le n\le5000\), and enumerates both \(2\beta(n)=n\) and the prime-support restriction through \(300000\). It also checks the exact reduced exponential equation on \(2\le a\le118\) (even) and \(1\le b\le99\) (odd).

The recorded output is:

```text
VERIFY_OK limit=300000 support_le2_count=119838 all_hits=[2, 12, 40, 252, 880, 10880, 75852] two_support_hits=[2, 12, 40] sharp_boundary=252 checked_power_box=a2..118_even_b1..99_odd
```

The infinite classification depends on the ratio bounds, the parity argument, and the exact difference-of-squares identity proved in `RESULT.md`, not on extrapolation from these finite tests. External independent validation has not been performed.
