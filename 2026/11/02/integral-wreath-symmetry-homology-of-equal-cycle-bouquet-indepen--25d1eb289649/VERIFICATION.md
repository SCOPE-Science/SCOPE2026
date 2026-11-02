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
# Verification and reproducibility

The standalone `checker.py` (Python 3, standard library only) generates every independent face of a bouquet, computes the augmented simplicial chain ranks over \(\mathbb F_2\) by exact bitset elimination, and evaluates signed reduced Lefschetz traces over integers. It exhaustively tests every reflection/permutation group element in each listed case and compares the traces with the theorem's predicted one-dimensional characters.

Tested \((m,L)\) values are \((2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),(3,4),(3,5),(3,6)\). The group comprises \(8\) elements for two petals and \(48\) for three petals. Every tested full-group element passed both the signed-trace comparison and the homology-rank check. The generated output file `checker_output.txt` is included in this package, with terminating marker `BOUQUET_CYCLE_HOMOLOGY_AND_SIGNED_CHARACTER_CHECKS_OK`.

For the two-hexagon bouquet, the enumerated complex has \(193\) nonempty faces and mod-two reduced Betti numbers \(\widetilde b_2=\widetilde b_3=1\), with all other reduced mod-two Betti numbers zero. Independent evaluation of its independence polynomial gives value \(0\) at \(-1\), consistent with the two-sphere wedge of different dimensions and inconsistent with a lone odd sphere.

**Scope limits.** Computations on selected small finite graphs are not proofs of statements for all positive parameters or of integral torsion-freeness. The latter are established by path folds, the vertex cofiber sequence, and the integral homology exact sequence in the mathematical proof. The checker does not independently verify published source coverage or establish uniqueness, and no external independent audit has been performed.
