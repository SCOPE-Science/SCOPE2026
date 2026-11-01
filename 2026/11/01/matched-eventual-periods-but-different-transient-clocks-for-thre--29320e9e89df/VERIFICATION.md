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

## Standalone checks

`verification.py` requires Python 3 and only the standard library. From this directory run `python3 verification.py`. The script verifies every row of `support_certificate.csv` directly from both definitions of the cellular automata, rederives palette periods and transient depths, validates pointwise equality of eventual period, and compares complete microscopic phase trajectories on 145,440 labelled colorings with all ten GHM and six CCA formulas. Independent exact support-weight testing covers 800 additional model-by-shore-size cases. Its recorded observed output is in `verification_output.txt`.

## Logical status and limits

These tests are finite. The infinite-family claim is proved by the exact reduction to 49 palette pairs, the bijective return maps on recurrent palettes, and symbolic surjection counting. The table of 49 pairs is a complete finite-state certificate, not a sample of large graphs. The proof does not assert that the two models share transient times or all periodic configurations. No independent validation or certification has been performed.
