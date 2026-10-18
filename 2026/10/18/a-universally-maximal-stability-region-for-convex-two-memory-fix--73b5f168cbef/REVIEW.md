# Self-review

## Correctness — PASS

The final claim is that the convex-memory weight \(q=1/3\) has the unique, globally inclusion-maximal stability region for \(e_{k+1}=A[(1-q)e_k+qe_{k-1}]\), where \(A\) is any finite-dimensional complex matrix. The proof checks the monic quadratic Schur–Cohn inequalities, expands them into the explicitly defined polynomial \(F\), and factorizes its derivative in the weight. For \(|a|>1\), the two relevant boundary values are nonpositive and the extra critical point has the exact nonpositive value \(-(\operatorname{Im}a)^2(|a|^2-1)^2/(|a|^2-\operatorname{Re}a)^2\). Hence any positive feasible value forces a positive value at \(q=1/3\). The \(|a|\le1\) cases, strictness via negative real spectra, scalar-to-matrix lift, and imaginary-axis endpoint are handled separately. No numerical sample is used to infer an infinite-domain claim. The attached standard-library checker passed 97,272 tests.

## Originality — PASS, with material bibliographic uncertainty

The September 18, 2026 Epperlein–Wirth paper describes uniform moving-average stability regions indexed by the **window length**, whereas the present claim fixes the memory length at two and proves inclusion-maximality across **all constant convex weights**. The classical Schur–Cohn test gives a stability criterion for any one weight, but the universal maximizing-weight theorem requires an additional comparison across weights. The Chebyshev inertial fixed-point literature uses iteration-varying relaxation and does not supply the present all-complex-spectra inclusion theorem. Searches of published research records under weighted-memory, convex two-step, stability-region, and quadratic-root aliases did not yield an implication-equivalent claim. This negative search is not proof of uniqueness. The full motivating preprint was not available to inspect; its published abstract and a detailed independent synopsis were the available material. An uninspected section could overlap the finding, and older unindexed work is a remaining risk.

## Value — PASS

A single explicit coefficient serves all complex spectra and all finite matrix dimensions: no individual eigenvalue estimate is required merely to maximize the *set of systems that can be stabilized* with a constant two-memory convex scheme. This is a natural complete classification rather than a narrow parameter check. It improves the negative-real stability endpoint from \(-2\) for uniform two-point averaging to the sharp \(-3\), and obtains an exact oscillatory-axis margin. It does not promise faster convergence on a specified system; a different weight may yield a smaller spectral radius for that system. Its scope excludes nonlinear maps, variable weights, longer memories, floating-point error, and transient norm growth.

Self-review: passed. Independent audit: not yet performed.
