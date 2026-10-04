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
The claim was checked directly against the full primary source at the following logical interfaces.

1. **Covering lemma.** A spanning two-factor has degree \(2\) at every base vertex. Its inverse image in a universal-cover tree therefore has degree \(2\) at every lifted vertex. Acyclicity rules out finite cycle components, leaving only bi-infinite lines. Pullback under the covering map makes the ensemble invariant, and spanning gives root coverage probability \(1\).

2. **Eigenvalue obstruction.** In Proposition 4.1 of arXiv:2003.12765v1, the Hamiltonian cycle is used to obtain a full invariant line ensemble. After that, the proof invokes the invariant labeling and von Neumann-dimension argument for that ensemble. Thus the pullback two-factor supplies the same hypotheses.

3. **Spectral-bottom step.** Section 4.3 proves \(a_0<\mathcal E_D\) before applying the Hamiltonian-base eigenvalue obstruction. Replacing that obstruction by the two-factor version shows \(a_0\) is not an eigenvalue. A spectral bottom of a self-adjoint operator that is isolated would be an eigenvalue, so it is non-isolated.

4. **Band conclusion.** Theorem 1.2 decomposes the spectrum under (C1) into closed bands with purely absolutely continuous interiors and isolated points. The non-isolated bottom therefore forces at least one nondegenerate band.

5. **Petersen witness.** In the standard \(G(5,2)\) labeling, \(0-1-2-3-4-0\) and \(5-7-9-6-8-5\) are disjoint five-cycles covering all ten vertices, so they are a spanning two-factor.

No finite computation, truncation, or numerical experiment is used to infer the infinite spectral statement. The result does not claim necessity of the two-factor condition or absence of Dirichlet eigenvalues.
