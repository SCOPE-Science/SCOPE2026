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
# Verification

The focal primary source arXiv:2610.01628v1 was inspected for its submission date, MSC classification, Theorem A, the coefficient normalization \(\lambda_{\mathcal U}^k(I)=1\), and its identity-factorization corollary. The full text contains no occurrence of “compact” or “strictly singular”.

For a selected block coefficient \(\lambda\ne0\), the proof verifies the quantitative perturbation estimate
\[
\|I-T_\eta\|\le\|Q_t\|\eta/|\lambda|,
\]
so Neumann inversion is valid for sufficiently small \(\eta\). The resulting exact factorization product tends to \(\|Q_t\|/|\lambda|\). The ideal step uses only two standard facts: two-sided bounded composition preserves strict singularity, and an invertible operator on an infinite-dimensional Banach space is not strictly singular.

No computation, finite enumeration, or external certificate is needed. The proof does not establish sharpness or a converse characterization.
