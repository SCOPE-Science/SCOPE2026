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
# Verification of the flat-spectrum trace calculation

## Reproduction

Run `python3 check_flat_trace.py` using standard Python 3; no third-party packages, network connection, or external data are required. The program is included with its exact bytes in this research package. A successful run prints `PASS: 13545 algebraic, exact-projector and seeded numerical checks`.

## What is checked

The program uses `fractions.Fraction` arithmetic to verify beta-angle moment reductions and covariance, MSE, indicator-expectation, and calibration identities for every integer rank from 1 through 80 and every permissible budget. It then constructs numerous explicit full- and leave-one-out rational subspaces, independently projects probes by Gram–Schmidt, and checks the source estimator against the asserted residual-energy identity. Finally, deterministic pseudorandom Gaussian draws reconstruct the actual leave-one-out energies directly and check their mean squared risk and sample-indicator means at representative ranks and budgets, including the rank-plus-one exactness case.

## Analytical proof boundary

The implementation cannot prove chi-square or beta distribution identities for arbitrarily many dimensions. Those facts follow from conditional Gaussian rotational symmetry and standard uniform-sphere moments, derived within `RESULT.md`. Nor can finite sampling establish the mathematical novelty of the claim; the primary-source comparison and the residual bibliographic risks are recorded separately. Calculations in the package apply only to the flat-spectrum unnormalized real-Gaussian model in the result.
