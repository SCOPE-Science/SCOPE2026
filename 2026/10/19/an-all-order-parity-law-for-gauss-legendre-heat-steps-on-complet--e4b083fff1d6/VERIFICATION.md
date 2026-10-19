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

# Reproducible verification

Run `python3 verify.py` from the directory containing this file. Python 3 standard library only; no network access or external packages.

Actual result:

`VERIFY_OK coefficient_pairs=1938 positive_entries=4656 projector_comparisons=3904 odd_diagonal_witnesses=12 path_witnesses=4`

The checker verifies rational polynomial coefficients and coefficient-ratio ordering for stages \(1\) to \(35\), and constructs exact completed-step matrices via rational inversion. Positive entry tests cover nine unweighted complete multipartite graph shapes, even stages \(2,4,6,8\), and steps \(1/4\), \(1\), \(4\), \(100\). It also confirms explicit large-step counterexamples with exact arithmetic and checks that each completed step has unit row sums.

The infinite-stage, all-graph conclusions rest on the factorial-ratio, integral, and graph-projector proofs in `RESULT.md`, not numerical extrapolation. The printed finite counts make no claim of exhaustive verification of the infinite theorem.
