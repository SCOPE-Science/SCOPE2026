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

## Reproducible checks

Run `python3 verify_exact.py` using the Python 3 standard library. The checker builds independent vertex shortest-path tables and compares all endpoint routes for arclength sample points with the three analytical conditional distance expressions for complete bipartite networks with part sizes from one through five. It also compares the exact density-mixture and closed CDF representations, conditional moments, fixed-order stochastic comparisons, and the sharp thresholds and Wasserstein/total-variation constants.

One completed execution reported **PASS: 40570 exact rational independent checks**. These checks are finite. The universal statements for all integer part sizes and real edge positions are proved by the edge-pair classification and polynomial argument in `RESULT.md`, not by enumeration or simulation.

## Scientific limits

The result uses equilateral edges and normalized arclength sampling. The compared graphs share vertex count, not total length. The older 1982 literature was not accessible in full; prior coverage remains a historical risk. No independent audit or external certification has been performed.
