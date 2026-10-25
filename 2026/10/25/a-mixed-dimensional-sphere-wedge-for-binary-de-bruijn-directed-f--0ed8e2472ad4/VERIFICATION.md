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
# Computational verification and limitations

Run `python3 verify.py` next to `certificate.json` using Python 3 (standard library only). The program rebuilds every arc, valid face, maximal face, discrete-Morse pairing and critical cell from the graph definition, independently re-enumerates parent-selection faces, and compares all these objects with the embedded complete certificate. It verifies acyclicity by checking all 10,192 incidences, exactly computes the signed Morse boundary between the six- and five-cells, checks ordinary mod-two ranks independently, and checks rational top homology under bitwise complement using a separate boundary-kernel elimination and signed Lefschetz formula. The included output file is from an actual successful execution.

The finite verifications and standard topological implications establish the exact assertion for this eight-vertex graph. They do not establish an all-orders result or a comprehensive claim that no earlier unindexed theorem exists. In particular, some historically relevant full texts could not be checked comprehensively. Independent scientific audit has not been performed.
