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

# Reproducibility

Use Python 3.10+ with SymPy 1.12+ (`pip install -r requirements.txt`) and run `python verify.py`. The script independently constructs the exact invariant-moment generator equations through degree four for the specified telegraph-driven oscillator; it solves symbolic linear systems, reconstructs the displayed denominator and mixed-covariance numerator, and compares both marginal fourth cumulants. It proves the crucial threshold comparisons with exact polynomial remainder identities and checks all coefficients of the remainders are positive for positive parameters. It also checks the stiffness-six boundary and limiting expansions.

The included execution succeeded with symbolic equalities, 168 exact rational parameter substitutions and seven representative numerical threshold-order cases. Those test points are diagnostics: the all-parameter conclusions depend on the symbolic polynomial identities, positivity, Descartes' sign rule and the explicit positive root. The validator checks the mathematical algebra but does not establish external publication priority or independence.

The state variables represent a stationary linear oscillator with symmetric telegraph forcing only. The full second-order time-dependent law is not claimed. No independent audit has been performed.
