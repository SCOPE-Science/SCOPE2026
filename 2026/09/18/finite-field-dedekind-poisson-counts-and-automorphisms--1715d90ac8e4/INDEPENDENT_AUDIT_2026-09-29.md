# Independent Audit — 2026/09/18/finite-field-dedekind-poisson-counts-and-automorphisms--1715d90ac8e4

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `50ac9bdb9474a3520d96a5c93d5589a990e977f5`
- Disposition: **PASSED**

## Correctness

**PASS** — The finite-field specialization follows correctly from the arbitrary-field Type I/II classification. In characteristic two, beta(v,v) is the square of a linear form, so anisotropy forces dim V=1; in odd characteristic, Chevalley-Warning forces dim V<=2. For an odd-characteristic mixed plane, T defined by omega(u,v)=beta(u,Tv) is beta-skew, trace zero and invertible, so T^2=kappa I with kappa=-det(omega)/det(beta), a nonsquare; exact kappa, not just its square class, is invariant under simultaneous similarity. Counting epsilon, z and the active classes gives N_q(n)=2,3,4,... in even characteristic and 2,3,(q+9)/2,q+5,... in odd characteristic. The triangular automorphism decomposition contributes q^(dz+d+z)|GL_z(q)| times the active similitude group; the latter has orders q-1, 2(q^2-1), and q^2-1 in the one-dimensional, pure anisotropic plane, and mixed plane cases. Independent finite checks at q=3,5,7 agree with the pure and mixed stabilizer formulas.

## Originality

**PASS** — Plakosh-Pypka supply the arbitrary-field structural classification and simultaneous-similarity criterion, and a contemporaneous Petrov-Pypka preprint overlaps with low-dimensional normal forms. The all-dimension finite-field orbit collapse, stable class counts, mixed nonsquare enumeration, and automorphism-order table were not found in those sources or in targeted searches of the finite-field Dedekind-Poisson literature. The novelty claim is restricted to this specialization and remains qualified because both source preprints are recent.

## Scientific value

**PASS** — The result converts an abstract classification by simultaneous bilinear-form similarity into a complete finite-field counting theorem with explicit automorphism orders. The stabilization at q+5 for odd q and 4 for even q, together with the factor-of-two difference between pure and mixed binary active similitude groups, gives concise moduli data not visible from the raw arbitrary-field statement.

## Sources

- Dedekind Poisson Algebras over Arbitrary Fields (A. I. Plakosh; O. O. Pypka): https://arxiv.org/abs/2609.13767 — Primary arbitrary-field structural classification and isomorphism criterion.
- On the Structure of Low-Dimensional Poisson Algebras over Arbitrary Fields (A. V. Petrov; O. O. Pypka): https://arxiv.org/abs/2609.13784 — Contemporaneous low-dimensional classification overlapping with small-dimensional normal forms.
- The problems of classifying pairs of forms and local algebras with zero cube radical are wild (G. Belitskii; V. M. Bondarenko; R. Lipyanski; V. V. Plachotnik; V. V. Sergeichuk): https://doi.org/10.1016/j.laa.2004.12.016 — Background on the general bilinear-form classification problem.

## Limitations

- The arbitrary-field classification is a prior input and is not claimed as new.
- Low-dimensional normal-form phenomena overlap with contemporaneous prior work.
- Originality is qualified because the source classification preprints are recent.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository write was performed. Open-access/preprint sources were checked first; Oxford Download was not needed for this record.
