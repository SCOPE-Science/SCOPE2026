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

All formulas and the two noncongruent counterexamples are proved algebraically in `RESULT.md`. The independent executable `verify.py` uses only the standard Python library and exact rational arithmetic. From the extracted package run:

```sh
python3 verify.py
```

The expected output is:

```text
THREE_EVEN_DISTANCE_MOMENTS_EXACT_OK
```

The program expands each of the first three powers of the squared-distance polynomial \(A U^2+B V^2+2C UV\) by the multinomial formula, substitutes the exact even moments of the triangular distribution, and compares **all** monomial coefficients to the claimed identities. It additionally verifies the inverse matrix determinant, exact rational reconstruction over 300 seeded positive-definite parameter sets, and the two explicitly stated Gram matrices with coincident first two moments. This checker was executed from its packaged source and produced the expected marker. Its random tests are supplementary; the exact coefficient table and algebraic inversion provide the universal proof.

The theorem assumes exact population moments, nonzero edge lengths, and positive area. Empirical/noisy inverse stability, nonparallelogram quadrilaterals, and arbitrary two-statistic minimality are not established. Priority comparison includes an inaccessible preprint full text; no independent audit has been performed.
