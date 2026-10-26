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
# Reproducibility and boundaries

The supplied `verify.py` is a standalone Python 3 program requiring `sympy`, `numpy`, and `networkx`. Run `python verify.py` after installing those libraries. It makes no network requests and uses deterministic sampled random conductances.

Actual checks performed on this package's `verify.py`: exact symbolic budget and characteristic-polynomial identities, exact general lifting identities and strict-convexity stationary-point checks, 72 full Laplacian spectrum comparisons on vertex- and edge-transitive cores, 810 sampled asymmetric budget-feasible allocations, and 18 two-edge-orbit prism spectra with unequal core edge costs. Every check passed. The sample counts are finite, not an exhaustive proof of any infinite family or of global optimality.

The infinite-domain proof is in `RESULT.md`, using concavity of the spectral gap, finite-group symmetrization, the exact repeated-leaf spectral decomposition, the definition of the base optimal gap-to-budget constant, and a scalar strict-convexity argument. The theorem does not cover non-vertex-transitive cores with arbitrary private-leaf weights, and does not assert that every asymmetric optimal allocation has equal leaf rates.
