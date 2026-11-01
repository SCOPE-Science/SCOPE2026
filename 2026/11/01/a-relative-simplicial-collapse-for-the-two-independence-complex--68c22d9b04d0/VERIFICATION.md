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

# Reproducible verification

Run `python3 proof/verify_groetzsch.py` with the two supplied JSON certificates beside the script. The exact recorded console output is in `proof/verification_output.txt`. The certificate paths are relative within this package and require no external dependencies.

The verifier independently constructs all eleven vertices and twenty graph edges, checks all nonempty subsets against induced-component sizes, and verifies the 102 and 312 face counts. It replays each of 105 elementary-collapse pairs against the actual current face set, demanding that the lower face have exactly one strict superface; the final set equals the ordinary independence complex. It then replays 50 disjoint discrete-Morse matching pairs, enumerates and orients all 255 Hasse incidences, and proves acyclicity by exhausting a topological sort. The two unmatched faces have bitmasks `1024` (vertex) and `133` (triangle). Since there are no critical one-cells or higher critical cells, the Morse CW model is a single two-sphere. Mod-two boundary reductions provide an independent numerical cross-check, not an integral-homotopy substitute.

All numerical domains and graph parameters are finite and exhaustive. No larger Mycielski graphs, other cutoff values, or external independent validations have been checked by this certificate.
