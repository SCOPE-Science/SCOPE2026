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

# Reproducibility of the exact mixed-moment theorem

Execute `python verify.py` with standard Python. The saved verifier independently follows disjoint cycles in each permutation, extracts relative-order pattern labels from each consecutive three-image window, and tests the rational six-covariance vector for every order from \(3\) through \(9\). Exactly \(409{,}110\) distinct permutations were visited. A second calculation iterates distinct triples of prescribed images, counts all closed partial cycles directly, and checks the separate degree-one, degree-two and degree-three cycle contribution tables. Algebraic exact-rational substitutions for orders \(10\) through \(30\) were also checked. Output from the packaged source: `PASS: 294 exact rational assertions; exhaustive 409,110 permutations (orders 3..9); independent cycle enumeration plus closed-component counts.`

The universal theorem rests on the **symbolic proof** in `RESULT.md`: uniform path-component completion, explicit binomial closed-one-cycle summation, direct pair/three-cycle counting, and cancellation against \(H_n\). The enumerations alone would not prove universal quantification. No independent audit has been performed, and no completeness assertion is made for unrelated literature.
