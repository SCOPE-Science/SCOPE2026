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

# Reproducibility and limits

Run `python verify.py` with the independently installable Python library `mpmath` (65-decimal-place working precision). The program directly constructs the Hermitian Peierls matrix and evaluates its exponential, independently constructs the circulant spectral formula, and checks agreement; the result was `PASS: 150 deterministic assertion groups`. It also checks stochastic normalization, reciprocity on even cycles, vanishing chirality at real-gauge fluxes, reversed flux behavior, nontrivial odd-cycle coefficients and convergence of both the measurement-count chirality scale and leading escape probability. Tested cycle sizes are 3, 4, 5, 6, 7, 8, and 9.

These tests are finite consistency checks, not a certificate of the theorem. The proof applies for each fixed finite circumference and all real fluxes and positive hopping and observation times: bipartite conjugation establishes even-ring reciprocity, minimal-winding interference gives the first odd-ring antisymmetric term, and the stochastic-matrix telescoping expansion produces the asymptotics after repeated measurements. Remainder bounds are fixed-parameter bounds; no uniformity in simultaneous large circumference is asserted. Broader scientific priority and independent mathematical validation have not been performed.
