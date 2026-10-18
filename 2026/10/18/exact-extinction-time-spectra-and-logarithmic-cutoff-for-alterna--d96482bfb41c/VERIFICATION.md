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

# Reproducible checks

Run `python verify.py` with Python 3; the code has no third-party dependencies. It constructs the two equivalence partitions from each cycle-size list, directly computes the lower approximation over every subset, and checks the exact output-window conditions and inclusion–exclusion formula. It also tests decomposable cases and independently counts four-symbol cyclic words avoiding forbidden runs.

Observed result:

`VERIFY_OK connected_subsets=87380 step_window_checks=669924 disconnected_subsets=6736 independent_run_counts=28 n_up_to=8`

The exhaustive tests cover connected cycles with one through eight \(E\)-pairs and selected disjoint unions of at most six pairs. The formula for all dimensions is proved in `RESULT.md`. The asymptotic Poisson claim is proved using factorial moments; numerical tests do not constitute its proof. Earlier literature was compared semantically within the accessible material, but publication priority and independent review remain open.
