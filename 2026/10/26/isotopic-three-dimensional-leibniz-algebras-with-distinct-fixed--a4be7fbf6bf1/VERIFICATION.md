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

For a central non-Lie 3D Leibniz algebra defined by a nondegenerate symmetric form B on a 2D quotient, every automorphism uniquely has block triangular shape (A,ℓ,μ), with A in GO(B), μ multiplier and arbitrary ℓ∈V*, giving determinant(Φ−I)=(μ−1)det(A−I). Split GO(2) consists of all diagonal and anti-diagonal matrices (2(q−1)^2 total): imposing μ≠1 and det(A−I)≠0 leaves 2(q−2)^2. Anisotropic GO(2) identifies with maps x↦tx or x↦t x^q for t∈F_{q²}*, of order 2(q²−1); norm μ≠1 already prevents any nonzero fixed vector, leaving 2(q+1)(q−2). Multiplication by q² choices of ℓ yields exact automorphism and fixed-free counts; proportions are ((q−2)/(q−1))² and (q−2)/(q−1), distinct for every odd prime power. An explicit isotopism F=I,G=M_-⁻¹M_+,H=I preserves brackets, while any isomorphism would preserve existence of isotropic vectors, impossible for split versus anisotropic forms. Independently enumerated all GL2 matrices and tested AᵀGA=μG, μ≠1 and det(A−I)≠0 for F3,F5,F7: split/admissible (8,2),(32,18),(72,50), anisotropic (16,8),(48,36),(96,80). The general result rests on exact GO classification, not the samples.

## originality

PASS

La Rosa–Mancini–Nagy (arXiv:2302.08306) develops isotopism types for nilpotent Leibniz algebras with one-dimensional derived ideal and establishes the underlying bilinear-form classification. It does not in the inspected introduction/definitions and classification statements determine the fixed-point-free automorphism fraction. La Rosa–Mancini 2022 gives related Kronecker-module classification (only accessible abstract; full text priority risk). A published Heisenberg Lie algebra count in Resultary has split-value ((q−2)/(q−1))², but its bilinear form is alternating and cannot imply the *anisotropic symmetric* half or the isotopism counterexample. GO group orders are classical; novelty is specifically the noninvariance demonstration and exact two-field density split.

## value

PASS

A symmetry statistic that might be expected to be invariant under isotopism is shown to fail in the smallest 3D non-Lie, one-dimensional-derived-ideal setting, with sharp closed formulas uniform over odd finite fields. This is a motivated structural counterexample and complete quantitative comparison; it does not claim novelty for classical orthogonal similitude groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
