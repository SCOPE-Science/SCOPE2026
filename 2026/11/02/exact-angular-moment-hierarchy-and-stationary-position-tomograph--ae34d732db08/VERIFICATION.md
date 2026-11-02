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

# Verification and limits

The standalone `verify_moments.py` is executable with Python 3 and no third-party dependencies. It compares the exact stationary Fourier-generator recurrence with the independent ordered-time/Wick product in rational arithmetic for multiple nondegenerate parameter sets through degree 32, including the nonrotating boundary. It checks the fourth-to-second inversion and strict moment feasibility for nonaligned axes, then tests two angular Brownian occupation moments using a fixed-seed Monte Carlo time discretization. The recorded run completed 98 assertions.

The infinite-order formula, identifiability, feasibility region, degeneracies, and quantitative limit are established in the mathematical proof, not by the finite checker. The Monte Carlo check has sampling and time-discretization error and cannot prove exact identities. No independent scientific validation or independent audit has been performed.
