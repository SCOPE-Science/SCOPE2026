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

# Reproducibility and verification

The complete claim, assumptions, proof and source comparison are in `RESULT.md`. Its reproducible computational check is a standalone Python 3.9+ program `verify.py` using only the standard library. Run `python3 verify.py` from the same directory as these files. In a local run, it printed:

```text
PASS 593 deterministic identity, angular-integral, moment, kurtosis and rare-event comparisons
```

The checks evaluate the triangular-hat identity at multiple offsets, integrate powers by an independent midpoint quadrature, compare the derived finite Gaussian probability, expectation and second moment with a polar integration implementation, inspect asymptotic constants for orders zero through five, compare the normalized kurtosis with its predicted constant, and verify the independent-zero-pilot probability in the exact Gaussian subfamily.

**Mathematical limits of the computation.** The script uses bounded numerical ranges, deterministic pseudo-random inputs and a finite angular mesh. Those checks are diagnostic only. The infinite claims follow analytically from the exact triangular-hat integral, the central limit theorem, moment uniform integrability and continuity of the outer density. In particular, no finite simulation is offered as proof of a universal \(n\to\infty\) limit or a claim of exhaustive parameter coverage.

**Literature and scientific limits.** General moment upper bounds and the possibility of rapidly growing fine-level kurtosis are prior results. The claimed contribution is the specific exact constants, detection law, and normal finite distribution under the explicitly stated assumptions. A relevant initial-margin nested Monte Carlo paper was not fully accessible for a decisive priority comparison. Independent scientific audit and publication-priority validation have not been performed.
