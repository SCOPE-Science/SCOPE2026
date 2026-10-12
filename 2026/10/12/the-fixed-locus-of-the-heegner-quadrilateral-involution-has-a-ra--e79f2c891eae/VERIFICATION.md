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

The proof is symbolic and exact. On the nonzero domain, direct comparison of coordinates of Patterson's \(i_H\) gives the fixed equations \(d_{14}^2=d_{12}d_{13}\) and \(d_{14}d_{24}=d_{12}d_{34}\), with the third transformed-coordinate equality then redundant. The parametrization \((su^2,sv^2,suv,r,uz,vz)\) is reversible.

`verify_heegner_fixed_locus.py` reconstructs \(CM\) from the defining determinant, substitutes that parametrization, and verifies the displayed factorization by exact symbolic expansion. It separately verifies the rational conic parametrization and the witness \((100,25,50,117,90,45)\) with exact fractions. The recorded replay checks \(i_H(\mathbf d)=\mathbf d\), \(CM(\mathbf d)=0\), and all four strict triangle inequalities.

The verifier does not establish originality and is not an exhaustive search. The infinite-family conclusion is not inferred from finite computation: it follows from the rational parametrization of the conic, the explicit strict geometric point, continuity of strict inequalities, and density of \(\mathbb Q\) in \(\mathbb R\).
