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

# Reproducibility and limits

The standalone artifact `verify_mapping.py` requires only the Python standard library. Run `python verify_mapping.py` directly. It exhaustively enumerates \(n^n\) independent mapping outputs for each integer \(2\le n\le6\), totaling 50,068 mappings. It compares exact distributions conditional on each orbit length \(T=m\) and repeat index \(J=j\) to the enumeration and verifies a conditional total-variation inequality with exact rational arithmetic. The completed run produced:

```
VERIFY_OK mappings 50068 conditionals 210 assertions 802
```

The checker verifies finite joint and conditional counting facts. It does not compute an infinite asymptotic bound or establish historical originality. The infinite result follows from the conditional coupling, birthday tail bound, multinomial/Poisson tail ratios, and factorial-moment convergence stated in `RESULT.md`. No independent scientific audit has been performed.
