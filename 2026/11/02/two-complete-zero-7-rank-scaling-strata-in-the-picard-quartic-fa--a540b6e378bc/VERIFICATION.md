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
# Reproducible verification and limits

Run `python verify_picard7.py` with Python 3 and `sympy==1.14.0`; no network access is needed. The verifier asserts polynomial identities in \(\mathbb F_7[a,b,c]\) for the quartic discriminant, the decisive equality \(\Delta=3R\), the characteristic-seven Cartier coefficient matrix, its determinant, and the Frobenius-twisted composition. It also constructs the polynomial expansions by an independent sparse convolution and checks finite-field rank examples using modular Gaussian elimination. The finite-field test examines all \(343\) coefficient triples in \(\mathbb F_7^3\) and excludes singular quartics; completeness over \(\overline{\mathbb F}_7\) comes from the symbolic identities and proof, not this enumeration.

The expected program output starts `VERIFY_OK:` and displays the smooth rational test count \(294\), Cartier rank counts \(1:42,3:252\), and stable rank counts \(0:12,1:30,3:252\). The identity \(\Delta=3R\) proves that rank two cannot occur at any smooth algebraically closed coefficient choice. The only geometric-isomorphism equivalence asserted is the weighted-scaling equivalence of the two individual branches; no full unmarked moduli equivalence is proven.
