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

# Reproduction and logical limits

Run `python3 verify.py` using Python 3 standard library. The output concludes `ALL_EXACT_CHECKS_PASSED` when the exact integer-pair arithmetic agrees with the spectral tables. The program checks 20 nodes, the class-product counts \(1,6,7,3,3\), the zero-polynomial identities over \(\mathbb Z[\varphi]\), and enough power traces to uniquely determine every eigenvalue multiplicity through degree nine. The infinite-degree proof uses \(13+3\sqrt5<21\) and symmetric Gershgorin diagonal dominance for every integer degree at least ten. Thus finite computations do not purport to enumerate infinitely many degrees.

The analytic identity identifying this matrix with the Wigner evaluation Gram matrix follows from unitary representation theory and is stated in the proof. The standard icosahedral embedding assigns the two five-cycle classes angles \(2\pi/5\) and \(4\pi/5\), in either order. The code checks algebraic certificates for the group class model; it is not a separate software construction of the continuous Wigner matrices.

The originality review checks closely related published works and an existing distinct class calculation, but does not establish global novelty. No independent audit or validation has been performed.
