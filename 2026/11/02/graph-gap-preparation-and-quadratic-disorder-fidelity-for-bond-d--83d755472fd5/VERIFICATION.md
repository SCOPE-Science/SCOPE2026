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

The self-contained finite-dimensional proof is in `RESULT.md`. The supplementary `verify.py` with `requirements.txt` creates connected paths and cycles at dimensions 3, 4, 5 and 6, nontrivial gauge-compatible phases, random onsite disorder and positive weighted hoppings. It constructs each full Lindblad superoperator, solves the stationary linear problem subject to trace one, checks positive semidefiniteness, independently recomputes the onsite variance identity and both stationary infidelity bounds, and tests compensated evolution with exact matrix exponentials. It also checks a phase-frustrated triangle has trivial common annihilation kernel and realizes equality in the graph-gap derivative estimate. Execute `python verify.py` with NumPy and SciPy; it reports `checks 137` on a successful replay.

These are **137 finite numerical or algebraic checks**, not a proof of the quantified statements over all graphs, parameters or infinite times. The analytically verified critical identities are the rank-one bond identities, Laplacian positivity, fidelity derivative, stationary coherence estimate, induced trace-norm bound and Hamiltonian degree compensation. Bounds and rank claims hold with the assumptions stated; mixing-gap equality, interaction robustness and finite-size uniformity remain unproved and are not claimed.
