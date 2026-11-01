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

# Executable finite verification

Run `python3 verify.py` with a Python 3 standard-library interpreter. The script requires no external files, packages, network or random seeds. It constructs the 12 graph vertices and 18 graph edges directly.

Actual successful checks: 1,104 augmented simplices; face vector \((18,117,336,420,192,20)\); matching polynomial \((1,18,117,336,420,192,20)\) by independent vertex-deletion recursion; 545 acyclic ordinary-face-poset pairs; 13 critical cells, one in dimension zero and twelve in dimension three; 4,002 complete codimension-one incidences and successful topological sort of all 1,103 nonempty simplices; reduced mod-two Betti numbers \((0,0,0,12,0,0)\). The discrete-Morse result proves the integral wedge of spheres, not merely the mod-two ranks.

The same script checks all 24 element actions of \(D_6\times C_2\), the exact signed Lefschetz character rows, character orthogonality, the rational irreducible multiplicities, the layer-swap eigenspace dimensions \((5,7)\), and a unique fixed rational homology line.

The Morse matching is not asserted to be group-equivariant; the homology character is computed independently from signed simplicial traces. There is no claim about larger circular ladders, integral representation lattices, or independent validation.
