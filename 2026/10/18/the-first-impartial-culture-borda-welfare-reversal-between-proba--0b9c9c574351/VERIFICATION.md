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

# Reproducibility and checked scope

Run `python3 verify_ps_rp_borda.py > observed.json`, then compare `observed.json` byte-for-byte with `certificate.json`. The verifier requires only Python standard-library modules.

Two independent exact algorithms are called for **every** normalized strict profile of size two, three or four. One constructs the full probabilistic-serial lottery matrix and averages over all uniform random priorities. The other integrates welfare over piecewise-constant probabilistic-serial demand and uses a finite-state Bellman recursion for uniform priority. Both operate on rational values, and each exact difference is compared before inclusion in the histogram.

Because strict first-agent preferences determine a unique object relabeling, the enumerated counts cover exactly every labeled strict preference profile, without sampling. The certificate stores the full signed difference histogram and its exact rational first moment, as well as both opposite-sign four-agent witnesses. All assertions completed successfully against the actual packaged verifier. Arbitrarily large market sizes are covered by the separate analytic embedding, not by the finite program.

Limitation: the certificate does not independently audit bibliographic uniqueness, compare alternative rank utility functions, or cover experimental rather than impartial-culture preferences.
