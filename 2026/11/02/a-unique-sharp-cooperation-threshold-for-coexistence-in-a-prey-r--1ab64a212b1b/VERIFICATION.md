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

Use Python 3.9+ with standard library only:

```sh
python verify_refuge_fold.py
```

The script verifies the scalar criticality function, identifies the fold numerically by sign-bracketed bisection, samples strict pre-fold and post-fold monotonicity, and reconstructs equilibria on both branches for multiple \(c>c_*\) in seven selected admissible parameter triples. Each reconstructed point is checked by substitution into **both** original predator--prey update equations. The representative point \((\lambda,\beta,\gamma)=(3,4,1/10)\) yields \(c_*\approx2.319323453738\). A separate symbolic calculation of the derivative identity yielded exact zero difference, but this calculation requires no reliance for the proof.

The analytical proof of the global all-parameter fold theorem is in RESULT.md and does not rely on finite sampling or an exhaustive numerical scan. Floating-point estimates are not formal interval enclosures. Source-related conclusions use the explicitly cited printed model; no stability or basin claim is verified here.
