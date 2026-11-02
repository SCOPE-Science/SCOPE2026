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

# Exact verification and scope

The analytic all-dimension proof is in RESULT.md. Two executable checks use only standard Python 3, exact integer arithmetic and no network access. Run `python verify.py` and `python verify_recursion.py` from this directory.

The first script enumerates every binary upper triangular matrix through size five, constructs the full target-fiber array, computes its independent Walsh–Hadamard transform and the factorized Gauss-sum transform, verifies the full spectrum is nonnegative, identifies exactly two maximal targets, checks that the positive spectrum spans the codimension-one subspace, and confirms the flat Walsh-magnitude lemma for every quadratic Boolean form in at most four variables. It ends in `VERIFY_OK`.

The second script compares every direct fiber count to an independently implemented memoized first-pivot recurrence, for every symmetric target in dimensions one through five. It ends in `VERIFY_OK`.

Expected records are in `verification/verify_output.txt` and `verification/recursion_output.txt`. The programs are finite corroborations; the proof covering all \(n\ge1\) uses the explicit quadratic Gauss-sum identity and Fourier inversion. The source literature establishes the zero-target numbers in the expected records, so those numbers are not described as original. No external independent validation is asserted.
