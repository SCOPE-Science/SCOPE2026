---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For L=V⊕Λ²V, dim V=3, every Lie automorphism preserves Z(L)=Λ²V and has block form [A 0;B Λ²A] with A in GL3(q), B arbitrary q^9. Its fixed-space is zero precisely when det(A−I) and det(det(A)I−A) are nonzero, by Λ²A ≅ (det A)A^(−T); no characteristic restriction. Reconstructed all five disjoint rational-canonical types: irreducible cubic, irreducible quadratic+linear with norm-one exception, three distinct linear eigenvalues excluding reciprocal pairs, double+single repeated root including Jordan alternatives, triple root. Symbolic recombination yields q³(q^6−3q^5+q^4+4q^3+q²−3q−8−ε_q) eligible A, and multiplying by q^9 gives the claimed q^12 formula. Independently checked symbolic parity formulas and direct field matrix counts q=2,3, including 48 and 4860 eligible quotient automorphisms. Nonempty determinant-open locus in smooth irreducible GL3×A9 yields smooth geometrically irreducible dimension 18.

## originality

PASS

Best-of-knowledge originality survives comparison with published works on the same objects and with indexed semantic findings: Benito–de-la-Concepción 2014 survey: exterior-square free class-two description and general automorphism structure, characteristic-zero structural treatment, no finite q census. Furutani–Markina–Vasil’ev arXiv:1410.3767: free class-two cover and H-type quotients, not fixed-point-free count. The original result claims only the additional exact assertion, not classical inputs. The inaccessible or unindexed-source risk is retained, not treated as negative proof.

## value

PASS

The exact count, including a characteristic-parity correction, determines a natural automorphism-group invariant for the smallest free class-two Lie algebra with nontrivial reciprocal-eigenvalue interactions; the geometric description adds a uniform open-locus interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
