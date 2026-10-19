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

Run `python3 CHECK.py` with Python 3.9 or newer; no third-party dependencies are needed. The program enumerates cyclic rotation classes independently of the formula, computes circular \(k\)-factor multisets directly for each possible read length, and verifies that singleton status agrees with the piecewise threshold for every class of weight three and every length from three through thirty. At the threshold, a second modular-index construction checks each factor count. Below the predicted threshold, it separately verifies spectrum equality for every distinct-gap word and its cyclic reverse.

Expected stdout:

```
THREE_MARKER_K_SPECTRUM_PASS n=3..30 necklace_classes=1360 distinct_gap=1150 repeated_gap=210 uniqueness_decisions=20626
```

The checks cover 1,360 rotation classes and 20,626 comparisons of a spectrum singleton predicate; they are exhaustive only over the stated finite range. The mathematical argument is in `RESULT.md` and proves all lengths. There is no externally or independently performed audit.
