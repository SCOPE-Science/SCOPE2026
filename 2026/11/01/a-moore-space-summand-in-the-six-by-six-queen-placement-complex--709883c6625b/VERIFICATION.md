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
# Reproduction and limits
Execute `python3 verify.py` with an ordinary Python 3 installation. The program requires only the standard library and reconstructs every claim from the finite board coordinates.

The run builds two independent face enumerations and compares them; forms the full directed Hasse graph and verifies its acyclicity by topological sorting; calculates the signed Morse boundary matrix directly from recorded pairs and orientations; reduces it by explicit integer-unimodular pivots and checks the final gcd; independently computes ranks of unreduced simplicial boundaries in characteristics two, three and five; computes signed Lefschetz traces for all eight square symmetries; and checks torsion-free models for all smaller boards. The recorded run terminates `VERIFY_OK`.

The unit-pivot and gcd output yields the complete integral Smith type of the matrix because exactly one row remains. Combined with the no-one-cell and no-four-cell Morse model, this proves the complete homotopy splitting by the usual homotopy classification of two-sphere attaching maps. The program does not certify any analogous result for board sizes larger than six, nor an external independent audit.
