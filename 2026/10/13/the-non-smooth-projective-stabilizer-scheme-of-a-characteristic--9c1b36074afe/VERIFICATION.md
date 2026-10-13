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

# Computational and mathematical verification

The proof in `RESULT.md` is a functorial calculation for every commutative coefficient algebra over an algebraically closed field of characteristic two. The essential equations are the coefficient constraints from the identity of degree-four homogeneous polynomials. Nilpotence of the forbidden geometric matrix entries, followed by three unit-cancellation relations, proves their vanishing even over nonreduced algebras. Remaining equations yield the universal coordinate ring and the exact group law.

Running `python verify.py` with Python 3 and SymPy verifies polynomial invariance modulo the fourth-order nilpotent relation, the group law modulo the corresponding fourth-order relations for both factors, and the three decisive generic coefficient expressions. It enumerates all \(168\) invertible projective matrices over \(\mathbb F_2\) and obtains precisely two stabilizers, agreeing with the predicted reduced rational-point group. The enumeration is a finite sanity check and cannot prove the statement over arbitrary algebras.

The computation does not establish priority, independent mathematical review or universal classification of abstract automorphisms. No independent audit has been performed.
