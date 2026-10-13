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

# Reproducibility and checks

Run `python3 verify.py` from the unpacked directory using Python 3. The verifier independently enumerates every total map between nonempty-subset state spaces for seven source/target atom-size pairs. It directly enforces forward preservation of the intersection relation and the back-lifting condition, and checks equality with the maps induced by every surjection of atoms. The expected passed pairs are `(1,1): 1`, `(1,2): 0`, `(2,1): 1`, `(2,2): 2`, `(3,1): 1`, `(3,2): 6`, and `(3,3): 6`. They comprise 825,763 tested candidate maps. The program exits with a failing assertion on any mismatch.

The main theorem uses a fully symbolic proof valid for arbitrary sets. The finite calculation is *not* a universal proof. It does not establish independence or exhaustive prior-art coverage.
