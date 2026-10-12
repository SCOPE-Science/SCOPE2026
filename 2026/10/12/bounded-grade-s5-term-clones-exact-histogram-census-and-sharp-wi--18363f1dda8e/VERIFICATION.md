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

The theorem was checked by the accompanying standalone `verify.py` script (Python standard library only). All checks completed, with output:

```text
VERIFY_OK histogram_comparisons 72 direct_term_closures 6 random_formula_checks 30960 sharp_plateau_cases 9 full_grade_cutoff_checks 308
```

The independent implementation enumerates labelled Boolean input tuples, computes local-type count histograms and their clipping, and cross-checks the support-weight exponent against its closed-form realizability criterion. For one input set, it separately constructs the full clone closure under Boolean complement, intersection and the actual counting-modal operations on small domains, not by using the proposed histogram formula. Random nested formulas are evaluated on complete labelled frames and tested for clipped-histogram invariance. Additional direct weak-composition enumerations test the sharp grade-width cutoff, while boundary cases test stabilization in cluster size.

The finite comparisons cover 72 histogram parameter triples, 6 direct complete term-clone closures, 30,960 random-formula/valuation evaluations, 9 plateau boundaries, and 308 grade-cutoff boundaries. These checks are finite sanity tests. They neither exhaust all formula trees nor constitute a proof for arbitrary finite domain sizes; the proof is the structural induction and explicit characteristic-formula construction in RESULT.md. No independent mathematical audit was performed.
