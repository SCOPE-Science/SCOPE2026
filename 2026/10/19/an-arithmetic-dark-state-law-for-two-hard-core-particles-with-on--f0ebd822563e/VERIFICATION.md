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

The package's `verify.py` independently builds the ordered pair-configuration Hamiltonian by all admissible single-particle hops, without using the sine-basis construction to assemble the matrix. It then diagonalizes each tested Hamiltonian, assembles the orthogonal projector on the sink-invisible part of *each* numerical energy eigenspace, and checks that this projector is idempotent, sink-orthogonal, Hamiltonian-invariant and of predicted rank. Every diagonal is compared with the claimed formula for primes \(5,7,11,13,17,19\): 405 localized configurations in total.

The checker also directly exponentiates the effective non-Hermitian matrix for the paths of \(4\) and \(6\) sites, loss strengths \(0.5\) and \(2\), and times \(500\) and \(30000\) (84 state/time comparisons). The later time verifies convergence in these samples; the intermediate time demonstrates that convergence need not be fast. The maximum finite spectral-projector/formula discrepancy observed was \(1.32\times10^{-15}\). Numerical eigenspace clustering uses a \(10^{-8}\) tolerance and is not an exact certificate of arbitrary-degree nonresonance.

These are finite checks only. The analytical proof in `RESULT.md` establishes the claim at every odd prime and every positive loss rate. No independent audit or experimental replication has been performed.
