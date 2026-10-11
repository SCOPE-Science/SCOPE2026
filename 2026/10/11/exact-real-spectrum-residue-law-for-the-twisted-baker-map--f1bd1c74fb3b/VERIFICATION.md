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

# Verification record

The algebraic proof uses the identity that each branch derivative is a signed monomial matrix. The right branch shifts coordinates cyclically and introduces one negative factor for each wrap; the left branch is positive diagonal. The induced permutation of an iterate is addition by the number of right visits modulo the dimension. The signed cycle products establish the exact characteristic-polynomial factorization and the real-spectrum equivalence. The published coding theorem identifies all nontrivial iterate-fixed points with non-all-left words.

The standalone checker `check_spectrum.py` uses exact matrices and rational arithmetic, exhausts the \(2^n-1\) nontrivial symbolic words for each \(2\leq M\leq6\) and \(1\leq n\leq6\), solves the affine fixed-point equation for each word, checks the branch itineraries and the return, verifies the signed-cycle factorization, and verifies the binomial residue count. Run `python -m pip install -r requirements.txt` followed by `python check_spectrum.py`; success ends with `CHECK_OK`.

This finite enumeration is a diagnostic, **not** a proof for all integers \(M\) and \(n\). The infinite claim follows from the signed-cycle argument and the exact symbolic coding, not from extrapolating a table. No independent external audit has been performed.
