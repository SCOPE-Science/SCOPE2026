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

The file `verify_cover.py` is a stand-alone numerical cross-check of the analytical proof and requires Python 3, NumPy and SciPy. Running `python verify_cover.py` produced `PASS checks 53`, with the mean-location spinodal at approximately 1.253739325812 in \(s=L\sqrt{r/D}\), and global transition at approximately 1.465715351947.

The program compares the exact all-location mean with an independently constructed three-flag-state killed random-walk approximation to the reflecting diffusion, keeping visits to each boundary across resets. It separately compares one-sided survival exponents from analytic renewal roots with finite-state generator principal eigenvalues. Finite checks cannot establish uniqueness or the entire continuum theorem: those claims follow from the algebraic derivative sign and positive killed-semigroup comparison in `RESULT.md`. The program does not claim independent formal or expert verification.
