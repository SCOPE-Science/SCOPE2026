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

The included `verify.py` is a complete, standalone Python 3.10+ checker. It enumerates all 4095 nonempty subsets of the twelve cube edges and accepts precisely the 1698 subsets with maximum selected vertex degree at most two. It checks the equivalent eight forbidden-triple description, the 847 disjoint discrete-Morse matching pairs, all 7980 Hasse incidences and the acyclicity of the reversed matching via a topological sort of 1698 nodes. It also compares signed reduced Lefschetz traces against both character expressions for all 48 cube symmetries.

The successful execution terminates with `VERIFY_OK` lines. Homotopy equivalence uses the standard finite discrete-Morse theorem and the absence of attaching obstructions below dimension five. Character identification uses the rational Lefschetz formula and ordinary semisimple representation theory. Neither the checker nor the proof asserts results for higher-dimensional cubes or a canonical integral representation.
