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

# Reproducibility and scope

Run `python3 verify.py` using Python's standard library. The expected status lines begin `DIRECT_UPDATE_OK cases=2800` and `EXACT_OK exhaust_checks=231388 qualifying_orders=33314 nonqualifying_signings=798 max_exact_updates_after_initial=2 random_checks=7818`.

The script implements the full-reception signed update directly using exact fractions and compares it with the derived score formula, including ties. It exhausts every complete signed graph signing and strict opinion ordering for \(2\le n\le5\), verifies the degree-sum iff boundary and the strict integer potential increase, and checks deterministic sampled cases for \(6\le n\le8\). The maximum of two post-initial-score updates is **only** a finite-enumeration observation and is not claimed universally.

The all-size proof is analytical: the denominator becomes \(n\) for fully receptive pairs; the next-step opinion range is bounded by the top two hostile degrees; a fixed hostile-edge extreme-order construction proves the converse; the hostile-edge absolute-distance function gives a genuine convex subgradient and strict Lyapunov inequality; and the finite post-first-update score range proves termination. An unverified general network convergence claim, an optimal termination-time bound, and an independent audit are not supplied.
