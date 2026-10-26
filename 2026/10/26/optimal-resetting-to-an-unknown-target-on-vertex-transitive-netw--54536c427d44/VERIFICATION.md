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

# Reproducibility and verification

Execute `python verify.py` with NumPy, SciPy and SymPy available. The included file contains its own cycle, complete-graph and hypercube transition matrices, direct first-hitting backward-equation solver, Green-resolvent calculation, strict-penalty comparisons, exact fifth-cycle symbolic identities, and finite cycle-size asymptotic comparisons.

The executed program printed:

`PASS: backward equations, resolvent identity, regret, sharp cycle threshold, radicals and large-cycle checks`

The same source file is included as `verify.py` for repetition. Finite conditioning becomes poor when reset probabilities are near one and deterministic relocation concentrates on a remote vertex; the finite tests use graph sizes and reset probabilities where the direct linear systems are well conditioned. The general conclusions are analytic, not extrapolations from numerics. The proof explicitly treats the initial-hit convention, strictly positive subunit reset rates and both endpoints. This record does not represent independent scientific validation.
