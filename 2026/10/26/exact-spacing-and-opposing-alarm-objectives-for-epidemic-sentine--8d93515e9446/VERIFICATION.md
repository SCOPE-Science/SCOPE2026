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
# Verification record

Analytic verification consists of a direct enumeration of the two edge-disjoint arcs within each monitor gap, the exact identity for the discrete second difference of the gap penalty, the finite sequence of strict balancing transfers, and the two-route connection probability for a fixed monitor. These prove the theorem for arbitrary integer network size and arbitrary real \(0<p<1\).

The standalone `verify_cycle_surveillance.py` uses only standard-library Python and is executed as `python verify_cycle_surveillance.py`. Its output must match the accompanying UTF-8 `verification_certificate.json` byte-for-byte (including the final line feed). The checker enumerates every seed and edge-retention mask for \(3\le n\le8\), every permitted monitor placement, and three exact rational transmission probabilities. It also checks gap convexity, mean-alarm invariance, exact two-alarm probabilities, and further integer placement inequalities.

Finite experiments do not certify the infinite parameter range, the literature originality assessment, clinical applicability, or any separate independent validation. The source of universal validity is the analytical proof in `RESULT.md`.
