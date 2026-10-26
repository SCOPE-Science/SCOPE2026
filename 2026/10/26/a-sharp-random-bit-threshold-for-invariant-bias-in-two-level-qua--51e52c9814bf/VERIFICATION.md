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

# Verification record

The exact transition matrix is built from the floor and ceiling probabilities for the two grid states. Stationarity is proved by balancing its two off-diagonal fluxes. Convergence is determined by its non-unit eigenvalue; no simulation is required for either claim. The sharp error envelope follows from a proof by integer and fractional parts of the product of bit budget and learning rate, with an explicit boundary-approaching family of targets.

The accompanying `verify.py` uses Python's exact `fractions.Fraction` type for rational targets and learning rates and checks 41,776 instances. Each ordinary instance checks matrix normalization, nonnegative transitions, the invariant law, one-sided error, the sharp universal upper bound, and the one-step/two-step spectral formula for each initial state. Additional rational instances approach the exact lower-bound witness from within the allowed open target interval. The program requires Python 3 and no third-party packages.

The checks do not constitute an infinite proof, establish independent audit, certify mathematical historical priority, or cover floating-point errors introduced before the final rounding operation.
