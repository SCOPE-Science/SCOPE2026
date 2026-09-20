# Same-model scientific review

## Correctness

**PASS.** For a fixed physical load F and smooth full-rank T(mu), direct differentiation of

J = F_c^T K_c^{-1} F_c,  K_c = T^T K T,  F_c = T^T F

gives J' = 2 F_c'^T q - q^T K_c' q. Expanding the projected quantities and using Galerkin orthogonality gives the equivalent residual identity J' = -y^T K' y + 2 r^T T' q. The coordinate-change law follows by substituting T -> T R(mu). Both explicit examples were checked algebraically and by the standalone numerical artifact. In the rank-one example at mu=pi/4, finite differences give 0.1599999999..., the exact formula gives +0.16, and the stiffness-only formula gives -0.24. In the full-space orthogonal example the reduced state is exact, J=5/4 is constant, and the stiffness-only term is -3/2 while the omitted load term is +3/2.

The source paper was inspected at the relevant primary statements: Eq. (10) uses T^T F as the coarse right-hand side; Sec. 3 parameterizes T(mu); Sec. 4.2 states the general relation F_c(mu)=T(mu)^T F and then elects to hold the coarse force fixed because F is fixed; Eq. (39) uses only the stiffness derivative. This is enough to establish the stated modeling distinction without inferring anything from an abstract or search snippet.

## Originality

**PASS, to the best of our knowledge, with a deliberately narrow claim.** The chain rule itself, parameter-dependent trial spaces, transported/parameter-dependent reduced bases, and Pulay corrections from basis dependence are prior art and are explicitly excluded from the novelty claim. Nair and Balajewicz (2019) provide clear prior art for parameter-dependent reduced bases, and Ruiz-Serrano, Hine, and Skylaris (2012) discuss nonzero Pulay corrections caused by basis dependence in electronic-structure calculations.

The accepted contribution is source-specific: identifying that arXiv:2609.20053v1's fixed fine-scale load does not imply a fixed coarse vector under its own T(mu)^T F relation; deriving the coordinate-gauge defect of the stiffness-only sensitivity; and giving exact-ROM and wrong-sign counterexamples. Searches for the source title/identifier, EIFEM sensitivity, moving reduced loads, parameter-dependent-basis compliance gradients, and Pulay/reduced-basis combinations did not locate an equivalent correction. Repository searches for EIFEM, moving-basis compliance, Pulay, and coarse-load formulations found no overlapping SCOPE record.

The most relevant uninspected source is Rubio, Ferrer, and Hernández (2025), *Preconditioning iterative solvers via the Empirical Interscale Finite Element Method (EIFEM)*, DOI 10.1016/j.cma.2025.118257. Its accessible repository record states that the deposited full text is restricted until 2027-11-01; the accessible abstract concerns EIFEM as a linear-solver preconditioner rather than parameterized structural-optimization sensitivities. It could contain related inter-scale identities but is not concrete evidence that the correction here is already stated. The 2026 doctoral thesis by Rubio was located but not read in full; because it likely contains material underlying the new preprint, it remains a contemporaneous-source originality risk rather than evidence of prior coverage.

Because the motivating preprint is very recent, a revision or contemporaneous commentary may not yet be indexed. Originality is therefore asserted only to the best of our knowledge.

## Value

**PASS.** The correction changes an optimization derivative, not merely a presentation detail. A one-dimensional example produces the wrong sign, and a full-space exact-ROM example shows that the stiffness-only formula can report a nonzero gradient when the physical compliance is exactly constant. The coordinate-gauge calculation strengthens the diagnosis: under a parameter-dependent reduced-coordinate rescaling, the omitted formula can shift by an arbitrary amount while the physical problem is unchanged. The corrected formula is also inexpensive in the motivating setting because T(mu) is already represented by differentiable interpolation.

## Limitations

The finding does not establish that the published benchmark optimization histories are invalid. If the implemented loading satisfies T_j^T F=0 for every active design direction, the omitted term vanishes. The public paper does not establish that condition, and no source-code-level audit was performed. If the authors intentionally define a fixed coarse-coordinate force rather than the pullback of a fixed fine-scale force, Eq. (39) differentiates that surrogate correctly; the issue is then physical/modeling interpretation rather than calculus.

**Same-model review: passed. Independent audit: not yet performed.**
