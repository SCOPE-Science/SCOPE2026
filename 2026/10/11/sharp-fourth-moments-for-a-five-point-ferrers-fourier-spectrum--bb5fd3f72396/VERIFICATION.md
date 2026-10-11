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

# Verification of the five-point Fourier fourth-moment inequality

Run the standalone `checker.py` with Python 3.9 or later. It uses only standard-library modules. Its actual successful run printed:

```text
PASS symbolic identities=4; pair-sum classification=1; total checks=4694; root=1.320162620401055; t=1.246542777672298; K=2.646915130955224
```

The exact symbolic checks verify the derivative of the reduced two-variable quotient, the substitution into the one-variable rational function, the numerator identity and the factorization of its derivative. Additional independent direct-complex evaluations compare the pair-sum convolution formula with the expanded moment for 2,400 integer-complex inputs; test 2,200 general complex inputs; match 80 direct discrete Fourier averages against convolution on four finite torus shapes; and verify three extremizing phase pairs. A rational interval contains the positive root of the quartic, and Descartes' rule proves it unique. The infinite-group inequality is justified by the analytic steps in `RESULT.md`, not by experiments.

No external mathematical audit or formal proof certification was performed. Possible equivalence to unlocated older short-sequence or two-dimensional \(\Lambda(4)\) literature is an explicitly retained bibliographic limitation.
