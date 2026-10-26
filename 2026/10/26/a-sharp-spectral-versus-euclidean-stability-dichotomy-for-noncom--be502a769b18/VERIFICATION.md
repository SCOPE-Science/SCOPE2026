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

# Verification and limitations

The analytic argument in `RESULT.md` is the proof. In particular, its two symmetric similarities, the exact Loewner comparison, and the extreme-eigenvector construction quantify all positive step sizes and all SPD matrices under the stated hypotheses. The rank-one limiting matrix is used only through an explicit strictly positive-definite perturbation; no semidefinite input is passed off as an admissible final witness.

Run `python3 verify.py` with Python's standard library. The script uses exact `fractions.Fraction` arithmetic for the positive-definiteness and norm-expansion witness, and it performs additional deterministic finite parameter checks for sharpness. No external dependencies or precomputed artifacts are needed. Finite tests do not certify general matrices or infinitely many step sizes. Reproducibility rests on the derivation and checked rational witness, and an independent scientific audit has not been performed.
