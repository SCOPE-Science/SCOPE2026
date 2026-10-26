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

Run `python3 verify.py` with Python 3 and no third-party libraries. On the packaged script, the output was:

```
PASS: four-value integer templates, exact GCD reductions, invertible fourth-order recurrence
PASS: all four exact summation identities and direct GCDs, lengths 2..160 and starts 0..7
```

The script evaluates both Fibonacci and Lucas sequences exactly as integers, including negative subscripts as needed by the templates. It tests the four integer-linear template expressions for parameters from \(-100\) through \(100\), the fourth-order recurrence for shifts from \(-9\) through \(9\), and all four symbolic summation identities and direct four-shift GCDs for half-lengths \(1\) through \(80\) and eight starting positions.

The universal result is proved symbolically in `RESULT.md`: the recurrence is invertible over the integers because the constant coefficient is one; this makes the GCD of a tail equal to the GCD of any four consecutive template values. The direct substitutions reduce the GCDs to \(2\gcd(t-18,30)\) and \(2\gcd(t+6,30)\); cube triple-angle identities and telescoping then produce the stated closed forms. These symbolic steps, not the finite enumeration, cover all positive half-lengths and every nonnegative start. No independent mathematical or publication-priority review has been performed.
