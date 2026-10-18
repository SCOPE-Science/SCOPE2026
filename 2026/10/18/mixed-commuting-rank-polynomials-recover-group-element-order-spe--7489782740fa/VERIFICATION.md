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

# Exact reproducibility

Run `python checker.py` with Python 3. The script uses only the standard library and exits with `VERIFY_OK` if all tests pass. It builds multiplication tables for finite groups, constructs every distinct restriction as a tuple of partial images, and tests both orders of partial-function composition against each idempotent. The bivariate generating polynomial is then independently computed from cycle patterns and binomial coefficients, not by inspecting the pairwise-composition result.

Cases checked: cyclic groups of orders one, two, three, and four; the Klein four-group; the symmetric group on three letters; and the dihedral group of order eight. Extra copies are checked for cyclic groups of orders two and three. All coefficients of the polynomial are compared, not only the total number. Exact Vandermonde inversion is also checked for the order spectra of selected groups.

Expected unrefined one-copy values include \(22\) for \(C_2\), \(104\) for \(C_3\), \(472\) for \(C_4\), \(508\) for \(C_2\times C_2\), \(8{,}344\) for \(S_3\), and \(127{,}192\) for the dihedral group of order eight. These are finite confirmation points, not the logical basis for the general proof.

There is no independent audit in this package. Bibliographic priority is subject to the literature-access limitation identified in `REVIEW.md`.
