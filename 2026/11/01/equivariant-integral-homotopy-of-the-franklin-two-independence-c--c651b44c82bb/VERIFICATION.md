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

# Reproducibility and limits

Execute `python3 verify_franklin.py` from the directory containing that file; it requires only Python 3 standard-library modules and prints the deterministic JSON certificate saved as `verification_output.json`.

Two independent definitions of admissible faces agree for all \(4096\) vertex subsets. The program checks \(723\) augmented faces, \(357\) augmented matching pairs, and the directed acyclicity of the ordinary-face Hasse diagram with \(2748\) incidences. Its signed integer Morse differential has dimensions \(2\times7\) and a determinant \(-1\) minor. Independent full simplicial boundary calculations over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) give the sole reduced Betti number \(\widetilde\beta_4=5\).

The same standalone checker enumerates all \(48\) adjacency-preserving permutations, calculates signed fixed-simplex traces on every automorphism and verifies that the trivial-representation multiplicity is zero. The character computation is not inferred from the Morse matching. Reaching the success marker `FRANKLIN_INDEPENDENCE2_EQUIVARIANT_OK` requires all these assertions to pass.

The computation is exhaustive only for the labeled twelve-vertex graph and its two-independence complex. The homotopy step uses the unit determinant and the Hurewicz description of the three-skeleton's attaching maps. Quotient rational homology follows by averaging over a finite group; no integral quotient classification or independent audit is asserted.
