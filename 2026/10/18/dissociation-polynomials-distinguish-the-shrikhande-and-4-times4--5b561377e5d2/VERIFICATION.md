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

# Reproduction and verification

The standalone `verify_dissociation.py` requires only Python 3.8+ standard-library modules. Run `python3 verify_dissociation.py` in the directory containing the script. It constructs the rook graph and two equivalent Shrikhande presentations on the sixteen pairs of residues modulo four. Both presentations are independently checked to have every vertex of degree six and precisely two common neighbors for each distinct vertex pair; an explicit invertible coordinate map checks equivalence of the Shrikhande descriptions.

For each graph, the script loops over all \(65536\) bit masks and directly checks the induced-degree-at-most-one definition. Separately it evaluates the proven deletion/isolated/pairing recurrence by memoized exact integer polynomial arithmetic. Every coefficient agrees, including the trailing zeros for sizes above the dissociation number. It also classifies large valid sets by their selected-edge counts. The script asserts the complete arrays, matching polynomial difference, and graph parameters; unexpected differences terminate with an assertion failure.

The run's recorded terminal output is embedded as `verification_output.txt`. Its final line must read:

`VERIFICATION_OK masks_per_graph=65536 methods=brute_and_recurrence graphs=rook_shrikhande`

The proof is a complete finite exhaustive recurrence, not an inductive claim about growing graph orders. The two methods share graph adjacency constructors but not the counting implementation. They do not provide independent external scientific review or comprehensive literature-priority certification.
