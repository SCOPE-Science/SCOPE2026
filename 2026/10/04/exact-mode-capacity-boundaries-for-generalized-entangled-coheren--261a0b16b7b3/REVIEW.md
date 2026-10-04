# Same-model review

## Correctness

**PASS.** The source normalization ellipse was rederived directly from its quadratic normalization equation. Substituting each published unconstrained optimum into \(|b|\le\Gamma\) reduces exactly to a depressed cubic in \(s=\sqrt d\). For \(x\ge1\), every relevant cubic coefficient is positive, so each cubic is strictly increasing on \(s\ge0\) and has a unique positive root. The large-\(x\) expansions follow by perturbing those roots from their zero-overlap limits. The standalone checker independently verifies the algebraic equivalence and the integer examples.

## Originality

**PASS, narrowly scoped.** The direct source gives the normalization bound, both unconstrained optima, and figures separating reachable from unreachable parameter regions. It does not state the cubic boundaries, the exact maximum integer phase count at fixed amplitude, or the asymptotic \(16\)-to-\(1\) capacity ratio. Targeted searches using the paper identifier, coefficient names, normalization bound, phase-count language, and fourth-power amplitude scaling did not locate an equivalent statement.

The originality claim does not include the generalized ECS construction, the QFIM formulas, or the formal optimized quantum Cramér--Rao bounds.

## Value

**PASS.** The source's formal optimum is useful only when a normalized probe state with that coefficient exists. The exact boundary therefore answers a necessary design question left graphical in the source: how many phases can be estimated while retaining the claimed optimum at a given coherent amplitude? The resulting \(d\sim|\alpha|^4\) versus \(d\sim|\alpha|^4/16\) laws expose a substantial feasibility distinction between the linear and nonlinear protocols that is hidden by their identical formal \(d\)-dependence.

Same-model review: passed. Independent audit: not yet performed.
