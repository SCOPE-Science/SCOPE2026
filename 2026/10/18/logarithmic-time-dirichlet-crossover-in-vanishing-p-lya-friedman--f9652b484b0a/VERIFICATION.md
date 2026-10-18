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

# Verification of the balanced mixed-urn crossover

An exact-rational finite-state enumeration in `verify.py` was run with Python 3 and returned `Exact finite-state and deterministic asymptotic checks passed: 280206`.

Each enumerated state is advanced by all colors and both Bernoulli replacement outcomes, with exact rational probabilities. The checker compares the one-step conditional drift with the theorem's formula and separately checks the finite-time expectation against the product formula, preserving mass one at each step. It spans two and three colors, multiple initial compositions and reinforcement strengths, and five rational mixing probabilities including both endpoints.

The script also evaluates selected finite logarithmic-time contraction factors; these are illustrative computations, not a proof of convergence. Infinite asymptotic assertions rely on the exact martingale recurrence, the square-summable rescaled noise bound, finite-prefix coupling to a pure Pólya urn, and uniform harmonic-product asymptotics. The normalizer and the Dirichlet reference law are explicitly defined, and no numerical or external proof certificate is needed.

There is no independent audit or independent validation in this package.
