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

The reproduced program `verify.py` uses only the Python standard library and requires no external dataset. Run `python3 verify.py` in a directory containing the program. Its printed record is included as `verify_output.txt`. The source constructs six explicit point/block designs, checks the STS pair-coverage axiom, evaluates two defining rank-five sentence conditions, and computes complete recursive first-order type signatures with orbit compression.

For binary projective tuples the orbit key is the kernel of the linear map sending formal coordinate coefficients to the selected vectors. For ternary affine tuples it is the kernel of the coefficient map on differences from the first selected point. These are complete orbit invariants under the applicable linear or affine group. Recursively taking the set of all one-point extension types produces exact Hintikka types for each tested finite structure. The code uses explicit algebraic Pasch-absence reasoning for the largest ternary example instead of claiming a brute-force scan over all 81-point quadruples.

This program checks six dimensions only. Infinite stabilization and the universal rank-four equivalence rest on the self-contained proof in `RESULT.md`. No independent external audit or machine-checked proof has been performed. One historical construction paper remained inaccessible in full text; that uncertainty concerns exhaustive originality coverage rather than the proven algebraic verification.
