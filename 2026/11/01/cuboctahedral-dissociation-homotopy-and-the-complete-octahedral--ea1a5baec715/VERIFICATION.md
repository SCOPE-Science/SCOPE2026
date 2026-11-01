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

# Verification

The attached Python source (`checks/cubocta_dissociation_verify.py`) uses only the Python standard library. Run it with `python3 checks/cubocta_dissociation_verify.py`; compare its output byte-for-byte with `checks/replay_output.txt`.

The program reenumerates all \(4096\) vertex subsets, checks both the maximum-induced-degree and forbidden-connected-triple predicates, and builds the complete face list. It constructs \(211\) matchings by fixed coordinate toggles and checks the entire reversed Hasse diagram is acyclic (\(455\) vertices and \(1512\) incidences). It calculates independent mod-two boundary ranks \((11,55,109,36)\). It constructs all \(48\) cube symmetries, verifies adjacency preservation, counts fixed oriented faces, and computes all ten conjugacy-class traces and the exact rational irreducible multiplicities. An explicit end marker `ALL_CHECKS_PASS` is printed only after assertions succeed.

The integral homotopy conclusion uses the discrete-Morse critical-cell dimensions, not mod-two homology. The irreducible decomposition and quotient assertion follow from rational character theory and finite-group averaging. These checks cannot establish global novelty, integral quotient torsion, or an equivariant homotopy model.
