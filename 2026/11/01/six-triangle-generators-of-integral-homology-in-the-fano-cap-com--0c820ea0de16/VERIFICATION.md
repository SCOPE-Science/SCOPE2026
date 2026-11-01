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

## Reproduction
Execute `python verify.py` after installing SymPy. The file `verify_output.txt` is the captured actual output. The source reconstructs the complete line and face incidence data; computes integer boundary ranks; enumerates all mod-two cycles supported on at most six triangles; tests geometric equality with all 42 bipyramid supports; checks each integral cycle; checks rank and all 13 unit Smith invariants; and enumerates the 168 collineations and orbit of the 42 supports. Last line must be `VERIFY_OK`.

## Boundaries and limitations
The enumeration is exact and exhaustive in this seven-vertex complex, not in an infinite family. Integer Smith form is computed with SymPy. The mod-two enumeration alone would not prove an integral result; the external-edge argument and saturation computation provide the necessary separate steps. No independent mathematical audit is claimed.
