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

# Reproducible verification

Run the standalone Python 3 standard-library program `verify.py` with `python3 verify.py`. Its expected terminal output is:

`VERIFY_OK 84 independent graph-field cases: group-square, conjugacy, F2-subspace census`

The verifier builds each finite graph from its edge bitmask rather than by a graph-library lookup. For every graph it enumerates vertex coordinates, evaluates the defining group cocycle over the base field, tests the square-zero condition, constructs all commutator images for square-zero elements, and independently checks the predicted conjugacy-class counts. It then constructs every binary linear subspace in reduced row-echelon form and checks the rank-by-rank formula for the full preimage subgroups containing the edge center.

The exact ranges are all labeled simple graphs on 2, 3, or 4 vertices over \(\mathbb F_2\), plus all labeled simple graphs on 2 or 3 vertices over \(\mathbb F_4\). There are \(2+8+64+2+8=84\) cases. The implementation represents \(\mathbb F_4\) using the irreducible polynomial \(t^2+t+1\). No external packages or downloaded data are needed. The program includes assertions testing the characteristic-two involution count, order-restricted conjugacy-class-size spectrum, full \(\mathbb F_2\)-subspace support census, and the multiplicity of the maximal possible subgroup order.

The general statements are proved by the square and commutator formulas and an exact support-inclusion-exclusion argument in `RESULT.md`. A finite exhaustive verifier does **not** prove the formulas for arbitrarily many vertices or extension fields. The existence or absence of earlier equivalent literature likewise is not certified by this computation. Independent mathematical audit remains unperformed.
