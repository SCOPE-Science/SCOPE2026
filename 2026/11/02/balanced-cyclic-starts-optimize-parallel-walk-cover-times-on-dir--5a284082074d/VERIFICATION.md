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

# Verification

The standard-library program `check_cyclic_cover.py` was run directly from the embedded source and printed `PASS: 190,907 exact finite assertions`. All finite checks use exact integer or rational arithmetic. They include strict coupon-collector CDF log-concavity for \(2\le n\le12\), all mechanical circular-window lengths for \(3\le d\le16\) and \(1\le k\le38\), exhaustive start-class allocations and all relevant times for \(2\le n\le5\), \(3\le d\le6\), \(1\le k\le6\), and small direct enumeration of actual independent walk trajectories against the separate occupancy formula. The unequal-size boundary table was checked exactly for all six allocations of two walkers.

The unrestricted theorem relies on its written proof: geometric-sum log-concavity, strict cumulative log-concavity, balanced circular telescoping, all-time converse, and coupon missing-count Poisson factorial moments. Finite enumeration does not imply the infinite theorem. The 2020 and 2023 closest-source statements were compared at the level of models, quantifiers, and theorem conclusions. Independent review and exhaustive priority checking have not been performed.
