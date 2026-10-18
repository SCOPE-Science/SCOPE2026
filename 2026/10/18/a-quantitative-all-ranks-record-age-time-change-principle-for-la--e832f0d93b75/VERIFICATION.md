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

The deterministic proof reconstructs two explicit comparisons: each physical interval maps to one active interval with rescaled difference at most twice the clock maximal deviation, and extending the active record-age composition across two horizons modifies a matched interval by no more than their horizon difference. Both remain valid after decreasing rearrangement and zero padding.

The concentration statement is the two-sided maximal Hoeffding inequality for bounded centered Bernoulli partial sums; its integrated upper bound gives the expected coupling cost. The only invoked infinite-process theorem is Szabó–Vető Theorem 4 for the censored active-walk age partition.

The standalone verifier `verify_rank_ages.py` completed 118048 exact-rational path checks. Finite tests are corroboration, not proof. Its record-index patterns need not arise from a specific jump sample: this is deliberate because the deterministic comparison holds for every increasing set of record epochs.

The Wasserstein order concerns the distance to the finite no-holding law at effective deterministic time. No finite-size Poisson–Dirichlet rate or optimality claim is established. All proof and reproducibility code are ordinary mathematical checks; no independent audit has been performed.
