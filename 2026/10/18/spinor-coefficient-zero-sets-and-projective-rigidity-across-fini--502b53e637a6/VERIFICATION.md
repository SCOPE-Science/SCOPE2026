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

# Reproducibility and finite checks

The proof of the general real-plane kernel lemma, exact zero-set realization, projective rank-one fibres and the infinite dicyclic formula is contained in `RESULT.md`. The standalone script `verify_spinor_coefficients.py` uses only Python standard-library rational arithmetic in two quadratic fields, not numerical tolerances, external data or a computer algebra server. From this directory run:

```sh
python verify_spinor_coefficients.py
```

The checker constructs all 24, 48 and 120 unit-quaternion vertices, checks exact norms and distinctness, groups axes by the vanishing of an exact algebraic cross product, reproduces exceptional cyclic-axis orders and reports the number of zero sets and projective rigid classes. It separately constructs every dicyclic group \(\mathrm{Dic}_n\) for \(2\le n\le12\), enumerates maximal cyclic subgroups and all their left cosets, and checks predicted counts. Its successful terminal assertion is `PASS exact finite axis and coset certificates`.

The finite enumeration is corroboration for the enumerated orders only. The full theorem for all groups follows from the stated quaternionic-plane and elementary group-theoretic argument, not from extrapolation of the finite experiment. Only self-review is reported. Independent audit remains unperformed.
