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

The exact count-means and their parameter derivatives are given in `RESULT.md`. Run `python3 verify_cutoff.py` using the standard library to reproduce 2,200 seeded checks of the Fisher identity, bounded global-maximum comparisons, comparison with unbinned information, and the numerical limiting constants. The output is stochastic-parameter deterministic because the pseudo-random seed is fixed. The theorem is established analytically, not by finite numerical testing.

The code covers dimensionless horizons \(0.04\le L\le16\) for randomized tests and selected asymptotic cases. Arbitrarily large or small horizons, model misspecification and physical catalog reliability are not established by that program.
