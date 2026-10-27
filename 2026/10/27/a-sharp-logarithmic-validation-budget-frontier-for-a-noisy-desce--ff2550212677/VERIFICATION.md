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

# Reproducible checks

Run `python verify.py` with Python 3 and no third-party dependencies. The included `verification_output.json` is the output obtained by executing that exact embedded program.

The verifier enumerates both possible training labels and all \(2^B\) possible validation label vectors for each integer \(B\) from \(1\) to \(11\), and for each of three starting states. This is \(24,564\) exact enumeration cases. All state-transition counts agree with the binomial formulas in the result. Four finite, nonconstant and constant batch schedules are then propagated with rational transition matrices; survival and objective-gap identities agree exactly. A separate finite-size numerical consistency test compares the binomial tail against the scale \(B^{-1/2}\exp(-IB)\) at six batch sizes. This floating-point check is diagnostic, not a certificate of the limiting exponent.

The infinite-horizon almost-sure statement, positive-survival criterion, sharp \(\log\) and \(\log\log\) thresholds, and upper confidence bound depend on the analytical argument in `RESULT.md`: elementary exact conditional probabilities, a consecutive-binomial-term ratio bound, uniform Stirling estimates, and convergence/divergence of standard positive series. Finite experiments alone are insufficient for these conclusions.

The checker tests only the stated three-state fixed-step procedure. No separate validation of full adaptive preconditioner learning or broad stochastic optimization convergence is claimed. No independent audit was performed.
