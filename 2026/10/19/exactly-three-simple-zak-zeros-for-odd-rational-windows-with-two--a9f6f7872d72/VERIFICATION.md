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

# Computational checks and analytical limits

Run `python3 check_zak.py` with Python 3's standard library. The checker evaluates the rational window's Zak transform both by a long symmetric truncation of its original defining series and by an independently implemented hyperbolic formula, including the repeated-pole derivative. It samples distinct-pole and coincident-pole pairs and checks three prescribed zeros, nonzero finite-difference Jacobians, and a further finite grid of nonzeros.

Execution on the packaged standalone script returned:

```
VERIFY_OK 3185 formula, nondegenerate-zero, and grid checks; standard library only
```

The numerical tolerance and finite grids are checker details. They are not proofs of universal nonvanishing or nondegeneracy; these conclusions follow from the strict hyperbolic monotonicity inequalities and exact Fourier identities in `RESULT.md`. Neither scientific independence nor a formal external audit is asserted.
