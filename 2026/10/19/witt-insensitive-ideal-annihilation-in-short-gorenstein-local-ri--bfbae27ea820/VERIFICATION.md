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

Execute `python3 verify_ideal_probability.py` using a standard Python 3 interpreter. It produces `VERIFY_OK` after successful assertions.

The script enumerates every reduced-row-echelon subspace of the maximal ideal, tests whether each is an actual ideal by closure under ring multiplication, forms actual ideal-multiplication tables, and counts all products of ordered tuples of lengths one through four. The twelve finite-field models cover \(q=2,3,4,5\) and embedding dimensions \(d=1,2,3,4\), including alternating/nonalternating characteristic-two matrices and split/anisotropic characteristic-three binary forms. Their tested counts agree with the Gaussian formula; the two characteristic-three models have the same probability counts but different square-zero-ideal counts.

The characteristic-four test represents \((\mathbb Z/4\mathbb Z)[x,y]/(2x,2y,xy,x^2-2,y^2-2)\) by sixteen actual elements, checks associativity and distributivity exhaustively, enumerates all additive subgroups, filters all ideals, constructs their products as generated additive subgroups, and checks all length-one to length-four product counts. There are seven ideals and 25 zero-product ordered ideal pairs.

The proof for all finite residue fields, all embedding dimensions and every tuple length \(s\ge2\) is in `RESULT.md`, Steps 1–4. Exhaustive tests of finitely many rings do not prove that universal statement. No independent mathematical audit has been carried out.
