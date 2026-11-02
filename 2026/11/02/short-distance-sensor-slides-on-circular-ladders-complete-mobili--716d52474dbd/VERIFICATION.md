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

# Reproducibility and limits

Both attached programs were run from their delivered contents. `verify_direct.py` constructs the prism and reproduces the power-domination rule without using the cited pair characterization. It checks all one-vertex starting placements and all two-vertex starting placements, builds every adjacent valid slide, and checks exact degrees, connectivity, bipartiteness, and four-cycle totals for lengths 8 through 20.

`verify_symbolic.py` separately constructs the six families of pairs without simulating power-domination and verifies the neighbor and square-incidence table using the common-neighbor identity at lengths 8 through 17, 19, 23, and 31. Both checks passed.

The numerical ranges are finite. Infinite validity rests on the cited exact pair criterion and the proof that the six local move and four-cycle templates are stable for every length at least eight. No expert, formal-prover, or independent external audit was performed.
