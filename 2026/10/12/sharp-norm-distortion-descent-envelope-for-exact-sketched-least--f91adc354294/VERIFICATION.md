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

Run `python verify.py` using Python 3 and only the standard library. The direct execution reported:

`VERIFY_OK rational_witness=1 sharp_extremizers_and_comparisons=5000`

The verifier independently reconstructs one two-row exact rational witness with \(\varepsilon=4/5\), \(\delta=9/4\), true quadratic difference \(-25/12\), and the sketch eigenvalue interval. It also tests 5,000 exact-parameter constructed extremizers numerically, compares unrelated positive-definite metrics satisfying the embedding, and verifies the sharp sign threshold. The universal argument is the sketched normal-equation orthogonality and spectral minimax proof in RESULT.md, not the finite tests.

The certificate does not establish independent audit, randomized-sketch probabilities, approximate-solver acceptance, nonlinear convergence, or finite-precision stability. The endpoint \(\delta=0\) is an equality case, not a failure witness.
