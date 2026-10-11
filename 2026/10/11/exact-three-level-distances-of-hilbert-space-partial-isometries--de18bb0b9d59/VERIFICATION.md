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

# Verification of the partial-isometry distance theorem

The logical dependencies are an identified published theorem and direct operator-theoretic reasoning. There is no numerical approximation, computer-assisted exhaustion, or finite-dimensional certificate in the proof.

1. **Published lemma.** For a noncompact operator in the norm closure of the absolutely norm-attaining operators, Ramesh–Sequeira (2022), Theorem 3.7 and Corollary 3.8, yield a strictly positive scalar-plus-compact modulus and a finite-dimensional kernel. The full text of the cited first public version was examined.
2. **Essential lower bound.** Any orthonormal sequence is weakly null, and a compact operator sends it to a norm-null sequence. One sequence in the initial space and one in the kernel yield the sharp joint lower bound \(\max\{\alpha,|1-\alpha|\}\ge1/2\).
3. **Unitary witness.** If both the kernel and cokernel are infinite-dimensional and the Hilbert space is separable, they are unitarily isomorphic. The direct-sum unitary extending the partial isometry gives an absolutely norm-attaining half-scale approximant at distance exactly \(1/2\).
4. **Cokernel obstruction.** A less-than-one perturbation has an invertible compression from the initial to the final space. The graph of its negative inverse correction embeds the infinite kernel into a subspace that the approximant sends into a finite-dimensional space, so that approximant's kernel must be infinite-dimensional. This contradicts the cited finite-kernel property for noncompact approximants; compact approximants already have distance at least one.
5. **Boundary checks.** Finite-rank and finite-kernel partial isometries themselves are absolutely norm attaining. The zero approximant realizes distance one. A projection and a coisometry with identical initial projection realize two different distances. Every case exhausts the ranks/nullities possible on a separable infinite-dimensional Hilbert space.

No independent validation or external certification has been carried out. The 2026 related paper was available only at abstract level and therefore was not assigned a full-text noncoverage verdict.
