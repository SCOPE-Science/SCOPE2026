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

# Verification and reproducibility

The proof in `RESULT.md` is the primary mathematical evidence. It uses explicit effective-resistance identities, a nonnegative support certificate for the strictly concave log-determinant problem, the matrix-tree determinant identity, and closed one-sided differentiations. These are all-parameter mathematical arguments, not deductions from a numerical sample.

Run `python3 verify_asymmetric_book.py` from this directory. The script uses Python standard-library modules only and must print `CHECK_PASS 102`. The program checks 96 numerical full-grounded-Laplacian inverses spanning six parameter positions for each of 16 choices of dimension and spoke lengths; one distinct exact-rational matrix configuration in the middle phase; four additional dimensional plateau checks; and one paired finite-difference check of the two predicted curvature jumps. It also checks contact complementary slackness in all sampled cases. The script is standalone and has no unstated local inputs.

During the derivation, 80 additional full zero-sum Euclidean inverse configurations and 20 independent unrestricted symmetric-matrix log-determinant optimizations were checked in an external numerical implementation; those computations were exploratory cross-checks, not necessary inputs to the proof and not claimed as separately replayable artifacts here. The 102 scripted checks are the independently replayable evidence included with this package.

No exact rational enumeration over infinitely many dimensions is claimed. Numerical tolerance comparisons are not proofs of uniform bounds. The displayed formulas are proved only in the stated parameter range. Reproduction of the program is not independent external validation or certification.
