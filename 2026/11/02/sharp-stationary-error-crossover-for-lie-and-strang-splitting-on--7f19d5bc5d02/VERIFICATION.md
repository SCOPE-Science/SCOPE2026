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

# Reproducible checks and boundaries

The executable file `verify.py` reconstructs and tests the complete claimed formula, rather than merely checking stored numerical output. Run `python verify.py` with SymPy version 1.12 or later. It verifies exact invariant equations, two independent stationary-law constructions, normalization, all necessary deviation sign identities, the exact factorization proving the crossover threshold, positivity of the derivative's coefficients, endpoint expansions, and 300 independent exact-rational instances.

The verified numerical values are \(q_*=0.22049649387432393013\ldots\) and \(h_*=3.0237469700367444937\ldots\). Decimal values are presentation approximations, not the theorem's definition: the defining root and all comparison boundaries are exact.

Finite checks do not prove uniqueness across an interval. That follows from the explicit polynomial derivative and the intermediate value theorem. Long-time convergence follows from primitive finite-state stochastic matrices. The general-rate large-step comparison is a limiting statement; it makes no claim about a unique general-rate threshold. No independent scientific audit has been performed.
