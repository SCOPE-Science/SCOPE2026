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

The primary-paper check is theorem-level: Eq. (19) displays a largest-minus-the-rest expression and the following sentence labels the eigenvalues as increasingly ordered. The cited Uhlmann proposition instead states the same expression after imposing
\[
\lambda_1\ge\lambda_2\ge\cdots.
\]
These statements cannot both be read literally.

For a nondecreasing list and \(r\ge2\), the inequality
\[
\mu_1-\sum_{j=2}^r\mu_j\le\mu_1-\mu_2\le0
\]
is exact, so the printed convention collapses the roof to zero.

`verify_ordering_correction.py` uses exact rational arithmetic to check the Bell-white-noise spectrum and corrected roof on a rational grid, including the witness \(p=1/2\), and exhaustively checks the ordering-collapse inequality for bounded integer spectra used as replay cases.

The computation is supplementary. The correction follows analytically from the source wording, Uhlmann's ordering convention, and the displayed inequality.
