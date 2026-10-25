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

Run `python3 verify_king.py` under Python 3 (standard library only). The accompanying `verify_output.txt` was obtained from that file and includes 13 exact partition/refinement checks for all square side lengths from 3 through 15. It checks global uniqueness of the distinguished-inner-orbit colors at every intermediate radius, equality of final colors precisely with swap orbits, a necessary final outer-corner split, and stability of a further update.

The universal proof is independent of these finite computations. This record does not claim infinite computational verification or any independent audit.
