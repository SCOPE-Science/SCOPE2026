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

The accompanying `verify.py` was executed as `python verify.py` with available SymPy and mpmath installations and returned `VERIFY_OK`. Its assertions check the cancellation of the \(N^{-1}\) term and the exact rank-one \(N^{-2}\) coefficient in the conditional copula expansion; the summand partial fraction used to evaluate the digit information coefficient; the algebraic relation for the final constant; and positive quadrant dependence computed independently from Gamma-function expressions at four values of the threshold. These checks are reproducible and finite. The proof's infinite sums, uniform remainder and countable-alphabet information limits follow analytically from the stated Euler--Maclaurin estimate, exact marginal telescoping and dominated convergence. No external audit, formal proof assistant, numerical infinite certificate or historical priority certification has been performed.
