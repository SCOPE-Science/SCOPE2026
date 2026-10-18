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

Run `python3 verify.py` using Python 3. The script is standalone and imports only standard-library modules. It reports `VERIFY_OK` after 3,600 deterministic Gaussian-vector support/width comparisons, twelve one-dimensional numerical quadrature versus Monte Carlo diagnostics of the finite CDF, the exact three-vertex equilateral benchmark, and non-certifying large-size numerical diagnostics. It does not download data or require an external file.

The closed support formula follows algebraically from the three coordinate vertices attached to each leaf. The exact CDF is obtained by conditioning on the common hub Gaussian and multiplying two independent Gaussian order-statistic CDFs. The individual angular probabilities follow from exchangeability and symmetry of maximizers, not numerical integration. Convergence of the Gaussian maxima to their common \(\sqrt{2\log m}\) level follows from Gaussian upper and lower tail estimates, providing the limiting angular law and Gaussian width fluctuation. The radial projection of a standard Gaussian onto the zero-sum subspace gives the uniform intrinsic direction, and its independent chi radius supplies the normalization.

The script's bounded checks cannot establish a formula for arbitrary size or an infinite-dimensional limit. The proof in `RESULT.md` supplies those arguments. The first-public-source date, 2022-09-16, is the date of the original arXiv submission rather than its later journal version. The complete source convention and primary MSC2020 52B05 appear in the first page of the published article and in the freely available arXiv full text.

No independent mathematical audit is asserted.
