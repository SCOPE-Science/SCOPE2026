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

# Reproducible checks and limits

Execute the embedded standard-library-only files from the same folder:

```sh
python3 verify_normal_form.py
python3 verify_boundary.py
```

The first program enumerates all 7,232 canonical width-at-most-two forms with at most twelve points. For each, it builds every strict comparison, computes all predecessor/successor pairs, decodes the unlabelled profile into the canonical form, checks profile uniqueness against all same-order forms, and compares equal profile pairs with the proved canonical orbit signature. Its complete standard output is `normal_form_output.txt`.

The second program recursively enumerates all canonical series–parallel posets through six points, evaluates width by every subset, and computes automorphism orbits by **testing all permutations** of the underlying set. This tests every structure, not a sample, over its stated finite range. It finds no first-round orbit failure at orders one to four, and exactly two order-five failures, both of width three and dual to one another. Its complete standard output is `boundary_output.txt`.

No imported packages are required. No external solver or infinite certificate is asserted. Completeness of the finite enumeration follows from the explicit canonical recursive generator, while the all-order reconstruction and orbit theorem follow from the mathematical proof in `RESULT.md`. No independent audit has been performed.
