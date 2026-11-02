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

# Verification and boundaries

Run `python verify_binomial.py` with Python 3 from the directory containing the extracted files. The checker uses `fractions.Fraction`, exact binomial coefficients, and exhaustive enumeration of small uniform-rank allocations; it does not require third-party packages. Its observed output was:

```
PASS: 3068 exact binomial identities/monotonicity checks; 1560 exhaustive uniform-rank profiles.
```

The exact-tail checks cover \(2\le n\le14\), \(1\le t\le34\), seven rational benchmark choices per population, both sides of the critical probability, the exact step convolution, the polynomial lower bound, and equality/strictness at the critical boundary. Exhaustive allocation checks cover all vectors of uniform-rank caps for up to six goods and two, three or four agents as selected in the source code. These are finite diagnostic checks. The proof for all population sizes, all matroids, all numbers of goods and the supercritical arbitrarily-large-instance impossibility is mathematical, not established by the test sweep.

The maximin-share existence theorem and the matroid-intersection reduction are credited in the full result. Priority assessment remains provisional. No independent external audit has been conducted.
