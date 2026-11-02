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

Use `python verify.py` with Python 3, SymPy, and optionally NumPy. The executable is packaged alongside this document; no external data files are needed. In the actual run it returned:

```
VERIFY_OK: symbolic determinant identity, 2 exact examples, 128 sampled signature checks
```

The symbolic determinant identity and the two witness signatures are exact. The 128 deterministic nonzero-det numerical inertia comparisons are supplementary finite checks. No finite sampling establishes the theorem for all real symmetric invertible matrices; the proof instead uses trace zero, determinant sign, real Witt index, and the real Segre description. The checker does not independently establish the orbit-counting argument, the general existence theorem, or novelty. No independent audit has been performed.
