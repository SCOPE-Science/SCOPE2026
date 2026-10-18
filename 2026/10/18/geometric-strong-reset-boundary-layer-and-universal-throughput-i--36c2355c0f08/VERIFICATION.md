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

The analytic derivation uses the finite-state block generator \(Q_r=rR+S\), the one-reset absorption projection, a reduced chain with the single recurrent class \(A\), and the exact one-extra-particle flux recursion. For each fixed positive boundary rate pair and length, the block inverse has an analytic expansion in \(1/r\); therefore finite numerical checks are auxiliary rather than infinite proofs.

`check.py` is a standalone Python 3 standard-library verifier. It constructs all allowed microscopic jump rates independently, computes stationary probabilities using exact rational Gaussian elimination for lengths 2--5, checks stationarity and every first-order configuration coefficient at two large reset rates and multiple rational injection/extraction choices, and checks exact reduced balance identities for lengths 3--30. Actual execution completed with `PASS 1734 exact rational assertions`.

The numerical first-order inequalities in the checker are finite-rate tolerances, not analytic bounds for all rates. No claim is made for infinite length, time-dependent convergence, or absence of stronger prior theorems. The first-public-source date is sourced to the published 2022 journal record, not the later arXiv upload.
