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

Run the supplied standalone verifier with `python verify.py` (Python 3 and SymPy). It constructs the exact two-state Markov transition matrix, independently solves both stationary conditional moment systems, checks every closed form and derivative in symbolic rational algebra, and enumerates independent finite-horizon sample paths for seven rational correlation values and seven time horizons. Observed result: `PASS: exact symbolic identities and 154 independent rational checks`.

The analytic proof of the continuum statement is not delegated to code: the moment matrices are strict column contractions, and the sign of the closed-form difference is set by an exact polynomial factorization with positive denominator on the specified interval. The numerical verifier is neither a proof of originality nor an independent scientific audit. Continuous-coefficient robustness is justified by nonsingularity of the same moment systems.

Unproved here: nonstationary-chain initialization formulas; last-iterate risk for higher-dimensional or nonlinear objectives; universal monotonicity conclusions; and equivalence with any uninspected prior specialized calculation. Endpoints of correlation are excluded from the irreducible aperiodic sampler domain.
