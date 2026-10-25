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

# Reproducibility and verification

Run `python3 verify.py` with a standard Python 3 interpreter; no third-party packages or downloaded datasets are required. The script terminates with `"status":"VERIFY_OK"` only after checking the complete finite construction.

The checker regenerates the nine quadratic residues modulo \(19\), the \(19\) facets, all \(8247\) faces (including the empty face), and every one of the \(40033\) covering relations. A directed topological sort verifies the complete acyclic matching. The resulting nonempty-face Morse model has one critical vertex, four critical two-cells and eighty-one critical three-cells. Signed gradient-path substitutions compute the full integral \(4\)-by-\(81\) differential; its row relation bounds the rank by three and an explicitly displayed unimodular minor proves rank three with torsion-free cokernel.

An independent matching built by reversing the vertex priority leaves six critical two-cells and eighty-three critical three-cells. Exact rational Gaussian elimination on its separately constructed Morse differential gives rank five, independently recovering the same rational Betti numbers. Torsion-freeness in the principal certificate follows from its unimodular minor, not from calculations modulo any fixed prime.

The homotopy conclusion further uses the standard acyclic-matching CW theorem and the classification of attaching maps from two-spheres to simply connected two-dimensional wedges by \(\pi_2\). The calculation does not determine integral automorphism modules or extend to other tournament orders.
