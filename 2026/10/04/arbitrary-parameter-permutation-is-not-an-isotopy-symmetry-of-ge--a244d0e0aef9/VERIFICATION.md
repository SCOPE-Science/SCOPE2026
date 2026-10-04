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

The target source was checked in its primary arXiv PDF at Theorem 13. The theorem first states the three-parameter permutation fact and then says that the conclusion holds for general pretzel links.

The supporting full text was checked where it describes parameter reorderings. It states that nonunitary parameters can be cyclically permuted and reversed without changing knot type, while further permutations may produce nonisotopic knots. It gives the explicit four-strand pair \(P(3,5,7,2)\) and \(P(3,7,5,2)\) as nonisotopic.

A second supporting check uses fiberedness. The same source identifies \(P(3,-7,5,-5,8)\) as fibered and the reordered mutant \(P(3,5,-7,-5,8)\) as nonfibered. Because fiberedness is an ambient-isotopy invariant, this independently certifies failure of arbitrary parameter-permutation isotopy.

The bundled program `artifacts/verify_parameter_symmetry.py` checks the finite group-theoretic bookkeeping and prints:

`VERIFY_OK D3=S3; D4=8<24; D5=10<120; both published reordered witnesses lie outside their dihedral orbits`

The finite program does not prove nonisotopy. Its role is only to verify that the valid cyclic/reversal symmetries exhaust all parameter permutations at three strands but not at four or more strands, and that the cited reordered examples lie outside those universal dihedral orbits.

No conclusion is drawn here about the correctness of every downstream quandle-coloring formula.
