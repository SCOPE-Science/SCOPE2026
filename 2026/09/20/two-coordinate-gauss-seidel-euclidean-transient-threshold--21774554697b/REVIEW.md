# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The one-sweep error matrices follow directly from exact coordinate minimization:
`T12=[[0,-c/a],[0,q]]`, `T21=[[q,0],[-c/d,0]]`, with `q=c^2/(ad)`. Each has rank at most one and exactly one nonzero column, so the stated spectral norms are immediate. Their comparison proves the larger-diagonal-first rule.

For fixed eigenvalues `lambda<=Lambda`, the identities `a+d=Lambda+lambda` and `ad-c^2=Lambda*lambda`, together with `|c|<=(Lambda-lambda)/2`, give `|c|/max(a,d)<=delta` and `q<=delta^2`, where `delta=(Lambda-lambda)/(Lambda+lambda)`. The balanced-diagonal matrix attains both inequalities simultaneously, so the envelope `delta*sqrt(1+delta^2)` is genuinely sharp rather than a combination of incompatible estimates. Solving `delta^2+delta^4<=1` yields the displayed threshold. Direct multiplication verifies `T^2=qT`, so the post-first-sweep statement follows exactly.

The deterministic verification artifact reconstructs the two sweep matrices from rotated diagonal matrices, matches their norms to the closed formulas to floating-point precision, checks `T^2=qT`, matches the minimax envelope on dense rotation grids, evaluates the threshold and its quartic, and checks the explicit ordering-separation examples.

## Originality — PASS, to the best of our knowledge

The literature search checked the claim family under Gauss-Seidel/SOR ordering, cyclic coordinate descent ordering, random reordering, Euclidean/operator-norm convergence, transient behavior, nonnormality, and two-dimensional/2x2 formulations.

Varga (1959) is a classical source on ordering of SOR and Gauss-Seidel, but its central ordering comparison is spectral/asymptotic. In the present two-dimensional SPD setting the two permutations have the same spectral radius `q`, while their one-sweep singular norms can differ drastically. Oswald--Zhou (2017), with its 2023 correction, studies random reordering and energy-seminorm convergence bounds for SOR-type methods. Lee--Wright (2019) analyzes random-permutation cyclic coordinate descent on a structured worst case. Zhou (2022) gives dimension-dependent and favorable-permutation estimates connected to triangular truncation. Wright (2015) surveys cyclic coordinate descent. Mohlenkamp--Young--Barany (2020) explicitly studies transient block-coordinate dynamics and notes that early block order can matter, including formulas for special valley models.

No inspected source stated the exact quantity
`sup_{kappa_2(A)=kappa} min_pi ||T_pi(A)||_2`, the formula `delta*sqrt(1+delta^2)`, the larger-diagonal-first minimizer for the two static permutations, the threshold `kappa≈8.352410032`, or the exact `T^2=qT` interpretation tying all two-dimensional ordering dependence in Euclidean error to the startup sweep. Searches using exact and synonymous formulations, the numerical threshold, and the quartic did not locate prior coverage.

Residual originality risk remains because the result is elementary once the two-by-two iteration matrices are written down. Full theorem-level inspection was not available for several broad historical monographs, especially Varga's *Matrix Iterative Analysis* and Young's *Iterative Solution of Large Linear Systems*, and an equivalent two-dimensional calculation could appear there or in older exercises/notes without searchable terminology. This risk is substantive but did not amount to concrete evidence of coverage.

## Value — PASS

The result separates two notions that are easy to conflate: asymptotic spectral convergence and finite-sweep Euclidean behavior. It gives a closed-form order choice, a sharp condition-number boundary for when ordering can always prevent startup expansion, an extremal matrix attaining the boundary, and an explicit family on which the wrong order has unbounded `Theta(sqrt(kappa))` first-sweep amplification while the reverse order stays bounded. These statements are useful as a small exact model of nonnormal transients and ordering sensitivity in Gauss-Seidel/coordinate descent.

## Scientific limitations

- Two variables only; no higher-dimensional ordering optimality is claimed.
- Euclidean error norm only; the result does not replace standard SPD energy-norm convergence theory.
- Exact arithmetic and exact scalar coordinate minimization only.
- The threshold is a uniform worst-case statement over matrices at fixed condition number, not a necessity for an individual matrix.
- No finite-precision, residual-gap, cache, or parallel-performance claim is made.
- Historical prior-coverage risk remains because broad older monographs were not fully inspected theorem by theorem.
