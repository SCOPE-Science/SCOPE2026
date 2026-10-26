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

# Exact verification scope

Run `python3 verify.py` using standard Python 3 from a directory containing `verify.py`; its exact output must coincide byte for byte with `certificate.json` in the same directory. The code constructs full continuous-time Markov generator transitions from disagreeing neighbor incidences, with positive opinion adopted at rate `plus` and negative at rate `minus`. It directly checks stationary balance on *all* states and ensures all states can reach the proposed unique recurrent support. It confirms the exact full distribution, first moment, and both endpoint masses.

The generated certificate counts 175 full generators, 8,960 full-state configurations, 1,645 stationary-support configurations, and 56,300 directed flips for 3 to 9 vertices and five rational rate ratios. Additional exact checks cover 1,805 strict neighboring-placement comparisons and 185 complete stationary probability mass functions on 4 to 40 vertices. The invariants use integer/rational arithmetic; no floating-point tolerance or random draws are involved.

Finite verification cannot establish strict curvature for every positive real persuasion ratio or the classification for arbitrarily many voters. These claims are proved analytically in `RESULT.md`. Source comparisons and novel implications have not been independently audited.
