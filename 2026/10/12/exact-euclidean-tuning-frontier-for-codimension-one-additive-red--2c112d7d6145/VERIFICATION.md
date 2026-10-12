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
# Reproduction and limits

Run `python verify.py` with NumPy installed as specified by `requirements.txt`. The script uses exact Python rational values for the displayed positive-definite \(3\times3\) witness, checks the precise Schur complement and the rational optimum, forms the preconditioned error matrices directly, and tests 3,500 reproducibly sampled SPD systems in dimensions two to eight. It compares the independently formed Euclidean spectral norms with the closed formula and checks four alternative regularization scalings per sampled block.

The completed check returned `VERIFY_OK exact_witness=1 random_SPD_blocks=3500`. This is a numerical verification of examples and a supplementary diagnostic; it does not exhaust continuous parameter spaces. The universal minimum and all strict-boundary claims depend on the symbolic determinant and Schur-complement proof in `RESULT.md`. These checks neither establish originality nor substitute for independent audit.
