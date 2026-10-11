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

Run `python3 verify.py` with Python 3. The standard-library script enumerates every permutation of zero through six labels (874 cases) and every union of its point cycles. It counts fixed binary tensor-basis assignments under the graded permutation and under the composition with the two-meridian swap, then compares the resulting trace coefficients with the stated separate closed-form products. It also verifies the identity-specialized binomial Betti formula. Executed on the included script, this returns `VERIFY_OK 874 permutations in 0<=k<=6`.

These exact finite checks catch grading and parity errors only. The all-length assertion follows from the symbolic Künneth, free-product Mayer--Vietoris, two-column spectral-sequence, and signed permutation-cycle arguments in `RESULT.md`. The mixed configuration space itself is not asserted to be a classifying space; integral and ring-structure invariants are outside scope.
