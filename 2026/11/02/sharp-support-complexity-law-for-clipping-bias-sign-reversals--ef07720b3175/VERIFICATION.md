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

The analytical argument proves the finite-support upper bound, the exact \(m\)-atom construction for all \(m\ge3\), uniqueness of each constructed population equilibrium, and convergence of the deterministic population map for \(0<\eta<2\).

Run `python verify.py` using Python 3.9 or later; it requires only the standard library. Observed output:

```
VERIFY_OK exact_family_m=3..80; all_midpoint_zeros; signs; unique_root_diagnostics; random_monotone_lipschitz=2000
```

The exact-rational tests cover \(m=3,\ldots,80\) and check normalization, zero mean, vertices, sign reversals, and half-integer crossings. The numerical tests compare root directions for \(m\le12\) and check 2,000 random Lipschitz-monotonicity pairs with a fixed seed. Such tests cannot alone establish the infinite family or prior-work novelty.

The result is limited to population mean drift and deterministic population updates, not sample-path convergence of stochastic iterates. Independent scientific validation has not been performed.
