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

# Reproducibility and mathematical limits

Run `python3 verify_ordinal.py` in a directory containing the supplied checker; no nonstandard packages or external data are required. The script uses rational interval endpoints and exact fractions to reconstruct each cell and transition probability, enumerates actual coordinate preimages for entrance delays 1–10, and compares all 60 probabilities to the Taylor coefficients of the proposed rational generating functions. It also recomputes the three first and second moments by differentiation and verifies the stationary entrance intensities.

The complete infinite-time generating functions are proved by the Markov-partition and first-entrance resolvent identities in `RESULT.md`, not by the ten-step finite check. Entrances in the stationary process have the correct conditional uniform current-cell distribution; consecutive in-cell visits are not counted as distinct entrances. The proof applies only to the fair dyadic map with identity observable and the three-observation, unit-lag ordinal code.

There is no independent audit or independent validation. No universal noisy-system claims, computer-assisted infinite certification, or exhaustive bibliographic priority claim is made.
