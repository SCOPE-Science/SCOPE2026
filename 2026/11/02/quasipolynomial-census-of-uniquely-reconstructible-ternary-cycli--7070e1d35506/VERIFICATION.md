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

# Reproducibility checks

Run `python3 verify.py` and `python3 crosscheck.py` from the directory containing both scripts. Both use only Python's standard library.

The first verifier enumerates all realizable balanced transition profiles through length 25 using the integral-flow normal form, independently computes each number of cyclic rotation classes with a directed matrix-tree/BEST formula followed by Burnside's lemma, and compares the structural classification and closed formula. It separately constructs the exact cross-multiplied monotonicity polynomials using integer polynomial arithmetic and confirms coefficientwise nonnegativity after each of two necessary variable shifts. It printed `VERIFY_OK` when run from the final source files.

The second program builds all indexed ternary circular words through length 12, computes complete cyclic adjacent-pair profiles, reduces words to a lexicographically least rotation and counts one-necklace profile fibers. It printed `CROSSCHECK_OK` when run from the final source files.

The proof for all lengths is the explicit BEST-factorial and monotonicity argument in RESULT.md. Finite checks do not establish all-length statements on their own. Historical priority and completeness of external literature are not independently certified.
