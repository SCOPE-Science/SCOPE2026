# Scientific review

## Correctness — PASS
The unnormalized four-by-four minor is a Vandermonde determinant. Its six-chord product factors exactly as \(64(T-X)(1-T-Y)(1-X-Y)\) in opposite-gap coordinates. Integer and half-integer parity sectors exhaust all integer gap quadruples; strict cosine inequalities exclude nonoptimal integral configurations from equality, and monotonicity plus the half-grid constraint gives the exact upper bound and all equality cases in the other sector. Translation-orbit counting is unambiguous because three unmoved nodes determine the original square. The independent finite test enumerated 825,642 subsets in twelve grid sizes, confirming the derived bounds and equality counts. The infinite claim depends on the analytic proof, not numerical extrapolation.

## Originality — PASS (best knowledge)
The closest same-object published mathematical result, *Exact four-frequency determinant optimum on every cyclic grid* (2026), determines the first optimum and its equality gaps, but its statement does not bound the second optimum on the complement of the maximizers. Ferguson–Mayeli–Sothanaphan (arXiv:1904.04487, full text, Definitions 3.9–3.10 and Proposition 4.10) define the determinant invariant and give the orthogonality maximum, without a next-best classification. Dubickas–Pritsker (arXiv:1902.08348, full text) treat continuously placed or weighted Fekete points, not second-best points restricted to finite grids. Batenkov et al. (arXiv:1809.00658) address conditioning estimates, not this exact second-order determinant statistic. Statement-level overlap searches found no direct covering result. Residual risk: an earlier equivalent calculation under discrete logarithmic energy or experimental design terminology might exist.

## Mathematical value — PASS
A determinant gives the volume and D-optimality objective for a four-coordinate harmonic sampler. Once every perfectly conditioned orthogonal sample is forbidden, the theorem supplies the exact performance ceiling, a strictly positive sharp separation, all 2N witnesses, and the first-order geometric defect (one grid-step perturbation). The loss has an explicit leading term of order \(N^{-2}\), giving a precise robustness scale for constrained sampling. The scope is natural rather than an arbitrary finite parameter slice: it is the entire infinite divisible-by-four family in which perfect four-point orthogonality is feasible.

## Scope and bibliographic limits
The statement neither extends to different frequency rows nor derives a bound on minimum singular value. The checker uses finite floating-point corroboration. Publication search cannot eliminate every earlier synonymous discrete-Fekete second-extremal result; independent verification is outstanding.

Self-review: passed. Independent audit: not yet performed.
