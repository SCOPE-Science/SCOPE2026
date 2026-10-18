---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Independent row-fixed uniform subsets have hypergeometric pair overlaps; conditioning on a leaf row of any forest leaves the leaf-edge overlap with fixed law independent of every other edge, giving joint product by induction. All distinct pair contributions are pairwise independent; factorial-moment expansion of (a-X)(b-X) gives exact pair mean/variance and global C-score variance sum/M^2. Independent full enumeration of 500 matrices for H=5, occupancies (2,3,4) recovers mean 7/5 and variance 49/75. In a 3-cycle over H=2, all overlaps one has probability 1/4 not 1/8, so cannot claim general joint independence or tails.

## originality

PASS

Gotelli establishes ecological SIM2 null and checkerboard model, Veech exact pairwise hypergeometric overlaps, and Arita pairwise/Fisher equivalence. A single pair law does not determine cross-pair covariance. Leaf-conditioning forest factorization and exact global null variance are not reported in their inspected relevant sections; generic random-set U-statistic identities might cover an equivalent result under different terminology.

## value

PASS

The standard ecological fixed-row equiprobable null needs a calibrated community-level C-score variance, not only per-pair marginal p values. Exact forest zero covariance supplies a reusable finite-sample normalization for heterogeneous species occupancies and delineates non-Gaussian cycle dependence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
