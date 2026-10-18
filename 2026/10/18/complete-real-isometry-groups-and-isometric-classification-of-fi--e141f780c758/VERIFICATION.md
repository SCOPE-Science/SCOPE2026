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

`RESULT.md` supplies the complete universal proof, including the open-set polynomial lemma, incidence form, joint-eigenspace identification and group conclusion. `check_examples.py` runs with the Python standard library and exact rational arithmetic; execute `python3 check_examples.py`.

Observed output:
```text
facet_families: 126
twin_pairs: 61
exact_equality_checks: 4545
coordinate_permutation_checks: 2795
```

The script exhausts dimension at most four only and tests finite grids; it does not certify real-variable identities in every dimension. For all dimensions the proof relies on exact symbolic polynomial arguments, not experiment. First public literature date is the arXiv v1 date of May 22, 2023. No third-party independent audit has been performed.
