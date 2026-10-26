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

The mathematical proof computes the exact conic-pencil base schemes and the relevant projective stabilizers. The projective-bundle and nef-cone argument ensures that these are full abstract automorphism groups, not merely the groups induced by an arbitrarily restricted coordinate ansatz. The orbit normal module is obtained from an explicit tangent quotient and a characteristic-zero representation decomposition.

Run `python verify_symmetry.py` with SymPy. The script computes all four \(3\times3\) determinants of triples among the four generic base points, obtaining units or nonzero multiples of the parameter, and verifies the equations of the four base points. It then computes the four independent off-diagonal tangent directions in \(\operatorname{Hom}(W_0,\operatorname{Sym}^2 E/W_0)\), obtaining rank \(4\) in an ambient eight-dimensional tangent space, and compares the residual torus weights with those of \(\operatorname{Sym}^3(V^*)\otimes\det V\). It also calculates the symbolic derivative of the determinant cubic and checks that its coefficient map has rank four. The projective rigidity and Clebsch--Gordan arguments are mathematical proofs, not inferred from finite symbolic samples.

The result does not assert that a linear normal representation is a complete analytic deformation classification. No independent audit has been performed.
