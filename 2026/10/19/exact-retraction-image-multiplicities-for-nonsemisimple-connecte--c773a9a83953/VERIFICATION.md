---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a quandle homomorphism, the identities intertwining right translations and their inverses hold even if the map is not bijective. The displacement products R_y R_z^(−1) give every translation by surjectivity of I−T; applying the intertwined translation at zero proves additivity after subtracting the constant, and using y=0 proves commutation with T. This argument also applies to isomorphisms between the connected image quandles, so their elementary-divisor arrays distinguish isomorphism types. An affine idempotent is an ordered invariant splitting V=U⊕W with one translation in W. The module automorphism group acts transitively on such splittings of assigned types with block-diagonal stabilizer Aut(U)×Aut(W). To verify the unit formula, for each φ-primary module reduce on M/φM and order blocks by length. A map from a shorter block into a longer one reduces to zero, so this reduction is block triangular. It is invertible exactly when each equal-length diagonal reduction is invertible, which also gives invertibility before reduction by nilpotence of φ. These diagonal residues are independent and unrestricted; each pair of lengths contributes Q^min(e,j) choices to End(M). This gives the stated automorphism factor, interpreting the diagonal unit product inside the product over φ as the proof specifies. For fixed U and a fixed image coset, complements are graphs of Hom(W,U), and each has exactly one coset representative, proving the fiber; multiplying by the count of distinct cosets recovers the total. The indecomposable boundary gives just constants and identity; V≠0 makes them distinct. Independent exact replay: python3 /workspace/branches/independent_checks.py 5 takes T=ωI+E12 over F4³ as an F2-linear map (one quadratic primary of lengths two and one). It enumerates the 1,024 matrices in the commutant by T^4=ωI, tests idempotency and groups literal affine image sets. The multiplicities (image size, fiber size) are (1,1):64, (4,4):64, (16,4):16, (64,1):1, matching the formula. This bounded check is not a proof of the general affine classification; the frozen checker was inspected, not executed.

## originality

PASS

Pass for the explicit image-type and prescribed-image census across arbitrary connected nonsemisimple primary data. Established ingredients are the Alexander split-epimorphism description, affineness, orbit–stabilizer and primary-module automorphism orders; the indecomposable no-proper-retract consequence is immediate from the split description and is not an independent novelty. A prior semisimple catalogue result and a catalogue result for equal-length linear-primary blocks give exact boundary or restricted profiles. Neither is an exact type and fixed-coset census for arbitrary mixed lengths and distinct primaries.

## value

PASS

Exact image distributions and counts onto each embedded coset are natural invariants of the finite quandle endomorphism monoid. Already at mixed primary lengths the choice of image module and its available complements depends on more than dimension; grouping isomorphism types and then aggregating equal cardinalities prevents losing that information. The all-type fiber and counting profiles are useful without treating the elementary indecomposability consequence or the known semisimple examples as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
