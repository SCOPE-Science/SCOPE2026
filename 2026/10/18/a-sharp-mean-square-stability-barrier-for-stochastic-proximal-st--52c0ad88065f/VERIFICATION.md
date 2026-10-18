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

# Verification of the exact two-client SPAM stability calculation

The included `verify_spam.py` is an ordinary Python 3 / SymPy checker. It does not require external datasets or network access. Run `python verify_spam.py` from the same directory.

The executed checks independently reconstruct the proximal step and its three-coordinate state matrix; symbolically build all six covariance coordinates; verify the closed polynomial for the mean-square threshold, the positive Lyapunov certificate at \(t=1/2\), the strict positive determinants of the second-step covariance and the observability Gramian, and the exact mean and second-moment characteristic polynomials at \(t=2\). Forty direct rational state-step comparisons and three full two-step enumerations verify the recurrence without using the lifted operator construction as an oracle.

The program checks exact algebraic identities. The all-positive-stepsize classification additionally uses the analytic cone-preserving Perron--Frobenius theorem, continuity of spectral radius, uniqueness of the positive polynomial root, and the positive-definite covariance/observability transfer as written in `RESULT.md`. It does not verify originality across all existing literature. No independent audit has been performed.
