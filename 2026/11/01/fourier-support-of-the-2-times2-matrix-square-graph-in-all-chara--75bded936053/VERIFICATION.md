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

# Reproducibility and scope

The mathematical proof uses exact finite-field matrix algebra and character orthogonality. To test its quantitative statements, run `python3 verify_matrix_square_graph.py` with a standard Python 3 interpreter and no additional packages.

The standalone checker tests every additive Fourier frequency for \(q=2\) (256 total) and \(q=3\) (6561 total), and deterministic additional frequencies at \(q=4,5,9\). It independently enumerates all second-coordinate matrix radical-rank classes for each tested field, checks the predicted total support rank, and tests amplitudes as exact cyclotomic coefficients or binary Walsh integers. Successful execution ends with `ALL_MATRIX_SQUARE_EXACT_CHECKS_OK`. Actual successful execution was observed for all five field sizes.

The finite checks are not an exhaustive verification for all prime powers. The universal result depends on the proof in RESULT.md. It is not independently audited, and it does not determine phases of nonzero Fourier coefficients.
