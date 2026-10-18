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

The reproduction commands and expected outputs are in `REPRODUCE.md` and the accompanying text files. The full coefficient census produces 139392 smooth models and 6096 maximal-point models. The second method reconstructs all 10368 sections with four split rational fibers via cubic interpolation and returns 6096 smooth ones, split as 3888, 1872, and 336 by branch type. The orbit script generates 286 smooth orbits, of which fifteen are maximal-point; the maximal orbit weights sum to 6096. The symbolic independent check certifies squarefreeness for all 286 smooth-orbit representatives, and the extension-field checker enumerates all rational points over the nine-element field for each maximal representative. These checks establish a reproducible finite exact calculation, not an external independent audit or a claim about unexamined higher-degree cases.
