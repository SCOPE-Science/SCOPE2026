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

# Verification of square-identity rigidity

The complete proof and all hypotheses are in `RESULT.md`. Reproduction requires Python 3 and SymPy. In a directory containing the embedded files under their relative paths, execute:

```sh
python checker/check_jordan_poset.py
python checker/check_rp2_torsion.py
```

The first script independently constructs incidence basis multiplication for seven finite posets, then assembles and solves the original linear constraints for square-identity derivations and ordinary derivations. Their solution dimensions agree over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) in all 21 instances, and integral Smith forms give equality of **all** solutions modulo four in five additional instances. The second script constructs the triangle-edge boundary matrix, verifies nine unit invariant factors and one factor of two, and computes the 31-element face poset and its 121 comparable pairs. Original captured stdout is stored in `checks/output.txt`.

The finite calculations are complete **within the specified finite systems**, but not an infinite proof across all posets or coefficient rings. That generality follows only from the basis proof and universal coefficients. Computations of \(\mathbb F_4\) and \(\mathbb Z/4\mathbb Z\) counts for the large witness use the proved cohomological formula and the independent integral Smith presentation; the script does **not** enumerate its astronomically many derivations.

The classification is limited to finite antisymmetric posets and coefficient-linear maps over commutative unital rings; publication priority and an independent mathematical audit remain outstanding.
