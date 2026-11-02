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

The divisor formula was compared to independently constructed adjacency-eigenspace projectors for 715 finite spider graphs, totaling 7,973 vertex probabilities; maximum absolute discrepancy was \(2.22\times 10^{-15}\). The same runs checked dark-space dimensions by projector trace and the exact site-capture criterion.

Four finite-time non-Hermitian semigroup tests were performed with \(J=\kappa=1\), at \(T=12000\), comparing numerically computed no-jump survival to the derived infinite-time projection. The maximum discrepancy was \(1.17\times10^{-12}\). This is a finite-time numerical consistency check, not a proof of the infinite-time assertion.

Run `python3 verify_spider.py` in a directory containing that script, with NumPy installed and optionally SciPy for the non-Hermitian semigroup checks. The analytical proof separately establishes all integer arm lengths, all positive hopping and loss rates, and every allowed initial site. No independent validation has been performed.
