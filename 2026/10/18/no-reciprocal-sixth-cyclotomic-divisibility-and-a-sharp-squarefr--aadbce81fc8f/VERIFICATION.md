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

# Reproducibility checks

Run `python3 verify.py` in the same directory as the other scientific files. No third-party Python package is required. The observed successful output is:

```
VERIFY_OK quotient_divisor_cases 17642 three_cycle (349, 121453, 9710803) value 410433300314317
```

The script enumerates every positive divisor \(b>a\) of \(g(a)\) for \(2\le a\le5000\), verifies the strict descent quotient and the key polynomial congruence, checks the nonexistence of a reciprocal pair within this finite collection, and verifies the full prime witness via exact trial division and exact arithmetic.

For the infinite theorem, independently reconstruct the proof in `RESULT.md`: (1) \(g(a)\equiv1\pmod a\) rules out a loop; (2) a reciprocal pair with \(2\le a<b\) yields \(z=g(a)/b\) with \(1\le z<a\) and \(a\mid g(z)\); (3) induction on the maximum element gives a contradiction; (4) squarefree Euler-product integrality forces a directed cycle of length at least three. Program output alone cannot establish any unbounded assertion.

The exact three-prime example proves sharpness only; neither minimality among such examples nor infinitude is claimed. No independent audit has been performed.
