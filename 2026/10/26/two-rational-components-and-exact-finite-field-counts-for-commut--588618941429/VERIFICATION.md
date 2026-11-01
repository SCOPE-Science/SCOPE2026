---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In odd characteristic, pairwise associative commutation of odd parts is exterior orthogonality. Wedge-degree 2 forces the degree-one tuple rank <=1. On the nonzero rank-one locus a complete affine chart is parametrized by alpha_1,beta_1,eta_j,zeta_j of dimensions 20,6,10,5 and rank-one linear data, giving dim X_s=48s+16; substitution verifies ALL pair constraints. On zero degree-one locus the wedge pairing of 20 degree-three monomials is nondegenerate alternating; its isotropic tuple variety is irreducible and rational via Lagrangian incidence, dimension Y_s=58s-s(s-1)/2 for s<=10 and 48s+55 otherwise. Its dimension exceeds X for every s>=3, proving exactly two components. Counting symplectic isotropic ordered frames plus rank-one matrices yields the exact odd-q formula. A fresh finite-field wedge test and brute-force small symplectic enumerations agreed with the formula, including 736,36352,26001.

## originality

PASS

Maximal commutative subalgebras (Domokos–Zubor), basic symplectic isotropic Grassmannian formulas, and a known length-two exterior commuting-pair polynomial are acknowledged. They do not automatically supply exactly two reduced components and full length-s>=3 finite-field point formula, especially the rank threshold s=10. No identical prior tuple classification was found.

## value

PASS

The components are inequimensional at every s>=3, with a stable dimension gap 39 past length10 and a complete geometric and arithmetic census. This structural classification is a natural algebraic-geometric invariant of a fixed classical exterior algebra, not a bare computation of an already known pair count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
