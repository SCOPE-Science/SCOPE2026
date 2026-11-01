---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The exact error after ordered row picks i,j is ||e||^2-ai^2-(aj-cij ai)^2. For two rows F12-F21=c^2(d^2-a^2) establishes choosing the initially larger residual first is the better of the only two nonrepeating sequences, and the p-weight of that first row grows monotonically; p=0 allows repeated rows and can only worsen conditional error. Degenerate residual-zero and equal-residual cases are handled. For the 3x3 rational full-rank example, independent exact reconstruction verifies unit rows, determinant 13/27, all nine Fij entries, uniform mean 65572/6561, first-row-2 probability at p=40 greater than 100/101 and conditional second-step error 7748/729. This gives the strict lower bound >21/2 while first-step expected decrease increases with p. No longer-horizon or positive-sparsity-regularization claim is made.

## originality

PASS

Steinerberger (2020) already introduced residual-power randomized Kaczmarz and proved geometric convergence-rate estimates based on one-step weighted residuals; Zhang et al. extend sparse/Bregman variants; Nutini et al. give multistep convergence bounds for greedy rules. A geometric rate guarantee is not a monotone ordering of exact unconditional two-step risks. The sharp two-row restriction and fully rational finite-exponent three-row reversal were not found in inspected primary statements. A dedicated finite-horizon stochastic-ordering result remains possible outside indexed literature.

## value

PASS

It determines a sharp and surprising smallest-row-count boundary where a seemingly beneficial adaptive row-sampling rule can worsen actual two-step error, despite improving the first-step conditional expected error. This gives a concrete methodological caution for finite-horizon iterative solvers, not a trivial restatement of convergence rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
