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

# Reproducibility and boundaries

Run `python3 verify.py` in the same directory as this file. It reconstructs the subalgebra parameter families and computes group orbits using a generating family for the full coefficient-field-linear substitution group. The expected orbit counts at field sizes \(2,3,4,5,7,8\) are \(17,18,19,12,12,17\), respectively. Every resulting orbit-size multiset is compared with the theorem's own characteristic-sensitive specification; all generated images must stay in the classified family.

Run `python3 verify_rref.py` to enumerate subspaces of the radical as reduced-row-echelon matrices and test closure of every candidate under the truncated multiplication in the small fields \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\). The exponent-six totals expected from the family count are \(24,42,66,96\).

The finite-field implementations use exact modular or binary-polynomial arithmetic. They are not a proof for infinitely many finite fields. The general result is supplied by the echelon closure classification and symbolic transformation calculations in `RESULT.md`. In particular the complete characteristic-two parameter orbits depend on the multiplicative cube-class index \(\gcd(3,q-1)\).

The total subalgebra-count polynomial and the unquotiented parameter families were already available in prior literature. No independent audit has been performed.
