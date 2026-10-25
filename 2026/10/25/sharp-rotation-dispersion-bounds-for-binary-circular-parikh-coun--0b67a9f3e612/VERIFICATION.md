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

# Reproducibility and proof scope

Run `python verify.py 14` with Python 3 (standard library only). The program exhaustively enumerates every nonconstant binary word of lengths 2 through 14; independently counts the scattered pair `01` in each cyclic rotation and compares those values to the increment recurrence, checks the mean, tests both sharp bounds and both extremal classifications, and verifies the pairwise cyclic-distance identity. The expected terminal line is `VERIFY_OK exhaustive_binary_words=32738 lengths=2..14`.

The infinite theorem is justified by the elementary proof in `RESULT.md`, not by the bounded test. In particular, the lower bound uses exact residue classes and equality for the discrete variance inequality, while the upper bound uses strict concavity of a quadratic gap functional over the full real gap simplex. All variables, normalization, and equality cases are stated in `RESULT.md`. No external executable or dataset is required.
