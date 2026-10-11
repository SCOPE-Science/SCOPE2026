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
The bundled `verify.py` is a deterministic Python 3 checker using only the standard library.

It reconstructs the simplicial complex from the 54 published tetrahedra and verifies the exact face vector \((12,66,108,54)\). It uses the star at vertex \(1\) as a spanning tree, represents the integral cycle lattice by the \(55\) non-tree edges, and constructs the \(55\times108\) triangle-boundary matrix.

A fixed list of \(55\) columns has exact Bareiss determinant \(-3\). The full matrix has rank \(54\) modulo \(3\). These two checks prove that the first integral homology quotient is finite of order exactly \(3\), hence \(H_1\cong\mathbb Z/3\).

The checker then exhausts all \(220\) vertex triples. Exactly \(112\) are missing triangles, and every one evaluates nontrivially in the mod-three homology quotient. Thus all \(112\) are shortest simple nonzero integral-homology cycles.

The two published permutations generate exactly six facet-preserving automorphisms. Exhaustive orbit enumeration yields \(15\) missing-triangle orbits of size \(6\), \(6\) of size \(3\), one of size \(2\), and two singleton orbits. Exhausting all three-vertex subsets for global invariance leaves exactly \(\{7,8,9\}\) and \(\{10,11,12\}\). Finally, exact chain transport and quotient evaluation give generator scalars \(-1\) and \(+1\), proving the sign action.

The checker proves only the packaged finite-complex statement. It does not prove uniqueness of the triangulation or classify longer homology representatives.
