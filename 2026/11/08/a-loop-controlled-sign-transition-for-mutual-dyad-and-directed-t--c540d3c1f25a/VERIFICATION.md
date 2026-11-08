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

# Verification evidence

Reproducible with the Python 3 standard library:

```sh
python verify_covariance.py
```

The checker evaluates the exact motif-overlap covariance and its two simplified forms for 952 integer parameter settings spanning sizes from 3 to 30. It also enumerates every admissible directed graph for 27 manageable combinations of graph size, fixed outdegree and self-loop convention at sizes 3, 4 and 5. Across 218,118 graphs, it independently recomputes the exact rational means and covariance. All assertions passed. The exhaustive enumeration is finite supporting evidence only. The proof of the all-size identities is a symbolic double count in RESULT.md, and the large-size limits follow by algebra.

The source date is verified from the original arXiv submission history, February 25, 2013, not a revision or journal date. Full primary-source text was compared for Seshadhri et al. (2013); Durak et al. (2012) was inspected in full text (Sections I–III in particular), while Roberts and Coolen (2011) was compared using its accessible abstract. Historical priority is not independently certified.
