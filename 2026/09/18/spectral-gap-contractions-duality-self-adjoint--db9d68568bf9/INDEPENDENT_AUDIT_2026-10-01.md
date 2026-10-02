# Independent audit — Contractive spectral tails for compact duality-self-adjoint operators

Audited: 2026-10-01 UTC

## Correctness — PASS

Self-adjointness iterates through powers, and the duality identity gives \(\|T\|^2\le\|T^2\|\), hence \(\|T\|=r(T)\). Nonzero eigenvalues are real, and the range-annihilation argument excludes nontrivial Jordan chains. For a nonzero eigenvalue, every vector in the Riesz complement is in the range of \(T-\lambda I\), so the norming functional of an eigenvector annihilates that complement; the Riesz projection is therefore contractive. More generally, when a finite spectral block is separated by a modulus gap, powers force the norming functional of each residual vector to annihilate the block, making the residual projection contractive. Restricting \(T\) to that smooth residual subspace preserves duality-self-adjointness, so its norm equals its spectral radius and gives the exact next-modulus tail norm. These steps repair the unjustified projection-norm step in the cited 2026 spectral-representation proof.

Risks: The older 2020 foundational article was available only through abstract/citation material, not full text.

## Originality — PASS

The full six-page primary 2026 spectral-representation paper was inspected. It constructs successive complements from Auerbach/norming functionals and then bounds the remainder by assuming \(\|z\|\le\|x\|\) for the residual component; no contractive Riesz-projection or complete-modulus-block theorem is proved there. Searches of the García-Pacheco self-adjoint literature and published archive found no prior theorem giving these contractive spectral tails and exact remainder norms.

Equivalent-formulation search: Queries covered both projection-contractivity and exact-tail formulations.

Broader-coverage search: No inspected broader theorem supplies the audited modulus-block contraction as an immediate corollary.

Database/table check: The claim is an infinite-dimensional operator theorem.

Claim-versus-prior implication: The audited theorem supplies exactly the missing geometric implication and additionally handles tied eigenvalue moduli.

### Source inspections

- **Spectral theorem for compact self-adjoint operators on smooth Banach spaces** — Complete six-page preprint, including Lemma 1, Theorems 2--3, the construction of successive complements, and references. Assessment: The source proves a spectral representation but does not prove contractivity of the natural projections; its norm-convergence proof uses the residual-component norm estimate without establishing it.
- **The adjoint of an operator on a Banach space** — Accessible article page, abstract, metadata, and scope description. Assessment: It develops the adjoint framework and does not state the audited compact spectral-tail theorem.

## Scientific value — PASS

The result closes a concrete operator-norm convergence gap in a new Banach-space spectral theorem and gives exact tail norms after modulus blocks. Contractive spectral decompositions are structurally useful, especially when eigenvalues have equal modulus, so this is more than a cosmetic proof patch.

## Limitations

Specific to self-adjointness with respect to the normalized duality map on a smooth complex Banach space. Exact remainder norms are asserted after complete eigenvalue-modulus blocks. The 2020 García-Pacheco full text was not available in this run, so older prior-coverage risk remains.
