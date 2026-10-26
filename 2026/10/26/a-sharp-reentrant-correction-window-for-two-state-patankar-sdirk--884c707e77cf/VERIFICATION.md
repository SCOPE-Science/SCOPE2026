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

# Reproducibility and verification boundaries

The accompanying `verify.py` uses only Python 3's standard library and a fixed local pseudorandom seed. It independently constructs the SDIRK stages by two-by-two linear solves, builds the ratio-scaled conservative corrector, and compares them with the closed formulas. It checks 1,800 parameter tuples with five assertions each and 20 additional assertions, for **9,020 passed assertions**.

The exact algebraic identities for the stability minimum, critical equilibrium fraction, and example are verified in the proof using \(\gamma=1-1/\sqrt2\). The coded tolerance tests are finite diagnostics, not a proof of uniformity or of an infinite family. The scientific statement concerns \(\varepsilon\downarrow0\) at each fixed positive timestep and positive rates; no statement of convergence in machine arithmetic is made. No separate independent audit has been carried out.
