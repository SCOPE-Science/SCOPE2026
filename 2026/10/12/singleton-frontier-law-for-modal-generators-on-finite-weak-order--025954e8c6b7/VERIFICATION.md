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

# Reproducibility and checks

Run `python3 verify.py` with Python 3.10 or newer; the program uses only the standard library. Its independently generated output is:

```
VERIFY_OK exhaustive_labelings 1178754 parameter_censuses 504 direct_boolean_closures 640 random_cases 5000 sharp_depth_heights 14 max_exhaustive_depth 3 examples {'two_by_two': 4, 'two_one_one_q3': 12, 'two_one_one_q2': 0}
```

The exhaustive checker compares color-sensitive modal partition refinement with the adjacent-singleton criterion in 1,178,754 labeling cases. There are 504 direct count-to-formula comparisons, 640 Boolean modal closure checks, and 5,000 seeded random finite comparisons. Fourteen full-generation examples on all-two-point levels attain the claimed depth cutoff, with heights 2–15. The direct closure checker starts from actual subsets of the finite carrier and closes under complement, union, and modal predecessor; it is algorithmically separate from partition refinement.

The unrestricted assertions depend on the written proof, not on exhaustion of all finite parameters. The historical literature comparison may miss an equivalent earlier formulation; no independent originality or mathematics audit has been performed.
