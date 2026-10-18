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

The proof is symbolic: threshold calculations for both modalities, an induction for all formulas, independent realization of both monotone coordinate sequences, and an endpoint sharpness argument. The standalone `verify_im_chain.py` was run in Python 3 with no dependencies. It returned:

```
exhaustive_raw 1 1 classes 1
exhaustive_raw 2 49 classes 9
all_quotient_classes 1 1
all_quotient_classes 2 9
all_quotient_classes 3 100
all_quotient_classes 4 1225
all_quotient_classes 5 15876
two_neighborhoods_sharp_at_terminal_world True
```

The direct finite semantic evaluator is separate from the profile predictor. These tests check all admissible frames for \(n\le2\) and every canonical profile representative through \(n=5\), not every raw frame at larger sizes. The infinite family of cases \(n>5\) is justified only by the proof, not by numerical extrapolation. No independent human or external validation has occurred.
