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

# Reproduction

Run `python3 enumerate.py > regenerated.json` in a directory containing all the embedded files and compare `regenerated.json` with `census.json` as parsed JSON. Run `python3 independent_check.py` for the independent coefficient-ring smoothness test, Burnside fixed-point count, finite-field second-extension counts, and Newton third-extension checks. Both programs succeeded with the packaged sources before delivery.

The discriminant criterion is algebraically exact over \(\mathbf F_2[t]\); no finite-field search is used as a substitute for geometric smoothness. The extension computations concern rational-point counts of confirmed smooth representatives. The 39 embedding orbits cover all 1116 smooth coefficient masks, with sizes included in `census.json`.

The recorded results do not certify novelty against inaccessible literature or abstract isomorphism classes; no independent audit was performed.
