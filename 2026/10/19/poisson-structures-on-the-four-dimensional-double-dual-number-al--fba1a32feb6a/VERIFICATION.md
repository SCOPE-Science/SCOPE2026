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

# Verification of the classification

The standalone `verify.py` constructs the four-dimensional algebra in the basis \(1,x,y,xy\), evaluates each bracket by the two-variable Jacobian formula, and checks Jacobi and Leibniz on all ordered basis triples. In characteristic two it tests every coefficient quadruple over \(\mathbb F_2\) and \(\mathbb F_4\), then exhaustively enumerates the full algebra-automorphism group and the bracket orbits. In odd characteristic it checks all allowable parameters and monomial automorphism actions over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\).

Run `python verify.py` with a standard Python 3 interpreter. The expected lines include labeled bracket counts 16, 3, 256, 5, and 7 for field orders 2, 3, 4, 5, and 7; the characteristic-two orbit counts are 6 and 12, with orbit-size distributions respectively \(\{1:2,3:2,4:2\}\) and \(\{1:4,15:4,48:4\}\). Odd-characteristic orbit counts are 2, 3, and 4. These checks were actually run successfully on the packaged standalone script.

**Proof/computation boundary.** Finite-field enumeration does not prove the theorem for every field. Generality is supplied by the written generator-relation argument, automorphism normal forms, coefficient comparison, and ideal-theoretic simplicity proof. The program assumes the standard concrete field constructions in its arithmetic routines: \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\) and prime fields for the other cases.

**Residual limits.** No independent external mathematical audit has been performed. The bibliography search establishes no absolute novelty certificate.
