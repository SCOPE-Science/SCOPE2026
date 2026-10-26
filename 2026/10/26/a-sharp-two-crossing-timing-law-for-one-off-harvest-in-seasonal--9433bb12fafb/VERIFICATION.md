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

The exact logarithmic ratio in the proof is obtained from two independently written positive compositions of the seasonal Ricker maps, not from a numerical approximation. Every denominator used is positive in the stated domain.

Run `python verify.py` (Python standard library only). At preparation, it printed:

```
PASS: 8,000 two-season composition and logarithmic-ratio identities
PASS: 2207 root-bracketing and three-region sign cases
PASS: exact-rational three-point witness, threshold, stable-map example
Finite tests are not a proof of the universal classification.
```

The theorem itself follows from the explicitly differentiated function \(h(z)=e^{-sz}-e^{-z}\) and the strict one-peak structure of that function. The sole critical point, its exact value, and the limiting values at \(z=0\) and \(z\to\infty\) establish the root count globally, not just on tested intervals. Taylor's theorem with nonzero second derivative at the critical point establishes the local square-root splitting.

No stochastic sampling theorem, harvesting-yield optimum, extension beyond two recruitment seasons, or independent scientific validation is asserted. The oldest primary paper and one particularly relevant historical order-of-events article were available only via bibliographic/abstract material in this review; see REVIEW.md.
