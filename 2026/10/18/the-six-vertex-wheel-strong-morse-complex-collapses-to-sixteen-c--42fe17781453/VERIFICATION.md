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

The graph, filtration rule and the twenty elementary collapse pairs are self-contained. Run `python verify_collapse.py` and `python verify_character.py` in a directory containing `collapse_certificate.json`. The scripts use only the Python standard library.

The first verifier examines all \(720\) total vertex orders, checks \(20\) vertices, \(55\) edges and \(20\) triangles, verifies each free-face deletion against the current complete simplicial face set, and checks that the remaining \(20\)-vertex \(35\)-edge graph is connected. The integral homotopy statement follows from collapses, not from field homology.

The second verifier independently creates simplicial faces, computes mod-two boundary ranks \((1,19,20)\) in cardinalities one through three, and calculates exact signed chain traces under all ten dihedral automorphisms. These give \((16,1,-4)\) for the rational first homology and the \(4\varepsilon\oplus3V\) decomposition. The two output text files record actual execution results; the code and certificate must be rerun to reproduce them.

No infinite-family extrapolation, integral dihedral module classification, equivariant collapse or independent scientific audit is claimed.
