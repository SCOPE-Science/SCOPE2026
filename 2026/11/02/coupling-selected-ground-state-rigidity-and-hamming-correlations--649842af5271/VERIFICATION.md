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

The standalone file `reproduce.py` uses only the Python standard library. Invoke `python3 reproduce.py`; the reproduced output should conclude with:

`PASS SUMMARY exhaustive_cases=33 evaluated_spin_assignments=723888 exact_distance_correlations=132 complete_walsh_cases=35`

The exhaustive tests count all labelled spins for \(d\in\{2,3,4\}\) at 11 integer or half-integer ratios \(K/J\) each, including the dimension-dependent exact transition, and compare minimum energies, entire minimizer sets and all pair-distance correlations. Separate direct adjacency action tests compare all Walsh eigenvectors in 35 dimension/coupling pairs over \(2\le d\le8\). These checks are finite evidence, not a computer proof for all dimensions. The mathematical proof establishes all \(d\ge2\), \(J>0\), and real \(K\).

Independent scientific assessment has not been performed. The source-comparison limitations are stated in `REVIEW.md`.
