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

# Verification and proof boundaries

Run `python3 verify.py` with Python 3 and no third-party packages. The code uses `fractions.Fraction` to compare the full likelihood-vector Bayesian choice against the outcome of linear-effort weighted majority; it does not use floating-point likelihood weights for the oracle. It tests 576 two-member precision profiles, 1,330 ordered strictly positive three-member profiles on a rational lattice, and an exact family approaching the sharp bound. These tests check finite rational instances and do not, by themselves, establish the global theorem.

The proof in RESULT.md supplies the required universal statement by reducing disagreement to the two patterns where the strongest delegate faces the other two, deriving the odds threshold \((y+z)/(1+4yz)\), expanding the exact probability gap, bounding its two parameter regimes, and giving a rational family approaching \(1/16\). The fair weighted-tie convention is essential to the stated boundary formula.

This verification is not independent external validation. The scientific analysis is conditional on genuine sincere signal-following votes; payment-game equilibria, implementation of the Bayesian benchmark, correlated reports and nonuniform priors are outside scope.
