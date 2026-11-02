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

# Verification

The fully embedded standalone `verify.py` was run successfully using exact Python rational arithmetic. Its output was:

```
EXACT_FIBER_CHECK_OK zero_fibers=5 nonzero_fibers=1 quadratic_pairs=4
```

The tests evaluate five distinct real-zero Blaschke fibers of degrees one through five exactly via an inverse Bergman Gram matrix; one nonzero fiber of the degree-two power map; and four degree-two matrix-defect determinants (two opposite-pair equality cases, two strict cases). The derivation in RESULT.md, not any finite test, proves the statements over all allowable complex parameters.

The analytic proof checks the normalization \(dA=\pi^{-1}dx\,dy\), the Jacobian multiplicity \(d\), the possibility that one zero lies at the origin in the partial-fraction lemma, strict positivity of interpolation Gram matrices for distinct nodes, invariance under disk automorphisms, and the complete odd-subspace range of derivative composition for the quadratic normal form.

Independent audit remains not performed. No external certification is claimed.
