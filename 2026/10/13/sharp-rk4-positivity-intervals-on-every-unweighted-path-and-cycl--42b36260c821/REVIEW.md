# Self-review: RK4 heat-step positivity on paths and cycles

## Correctness — PASS

With unit-rate graph Laplacian \(L\), the completed RK4 map is the exact matrix polynomial \(R(-hL)\). Row sums are one; each diagonal is positive because \(R(-x)>0\) for \(x\ge0\), as follows from Taylor's integral remainder. A finite-radius walk calculation covers all possible off-diagonal entries of order at most four. Seven nearest-neighbor cubics and five distance-two quadratics have strictly positive Bernstein coefficients for \(0<h\le2/3\). Distance-three coefficients provide sharp, permanently negative entries beyond the cutoffs for all paths from four vertices and cycles from six vertices. On the five exceptional small graphs, exact cubics with strictly negative derivative give unique positive roots and remaining off-diagonal entries have positive discriminant-free quadratic factors. No numerical search substitutes for this all-size argument. The standalone pure-Python checker independently reconstructs the short-walk coefficient catalogues and checks 245752 rational entries on 57 graphs.

## Originality — PASS, with residual risk

Comparison of the actual statements distinguishes the all-size exact RK4 finished-step theorem from general positivity/absolute-monotonicity theory, two-stage heat methods, RK4 applied to advection and flux-limited semidiscretizations, and previously published positivity results for other rational time integrators or directed pure-birth Markov chains. Horváth (2005) treats Dirichlet heat stencils but examines other methods and invariant cones rather than these endpoints. The specific all-path/all-cycle cutoffs and their nonmonotonic small-cycle behavior were not covered by inspected primary text or relevant published-result queries. An overlooked earlier specialization in numerical-PDE literature remains a priority risk; this is not a claim of exhaustive historical uniqueness.

## Value — PASS

A sharp orthant-preservation timestep for explicit RK4 on the canonical one-dimensional finite-difference heat discretizations is a practically motivated invariant, especially because classical RK4 has zero general RK positivity radius and end-step positivity can still hold for these restricted systems. The result gives complete size-dependent necessary-and-sufficient bounds, including nonmonotonic cycle-size behavior and a universal large-size bound. It is not merely a small table or an unmotivated numerical census: one infinite theorem covers every connected undirected unit-weight graph of maximum degree two.

## Closest sources and limitations

Fekete–Ketcheson–Lóczi, arXiv:1610.00228, Section 6.2: periodic heat stencil with two-stage explicit schemes and general semidiscrete criteria; no classical RK4 all-size path/cycle cutoffs. Khalsaraei, DOI:10.1016/j.asej.2015.05.018: explicit fourth-order Runge–Kutta positivity in flux-limited/advection settings. Horváth 1998, DOI:10.1016/S0168-9274(98)00050-6, Section 5 and Example 1: zero classical RK4 general-stage positivity radius. Horváth 2005, DOI:10.1016/j.apnum.2004.08.026, Section 4 and Table 1: Dirichlet heat equation with theta, Lobatto, and Radau tests; no exact RK4 result here. Restrictions: completed RK4 step only, unit weights, degree at most two, exact arithmetic. Priority remains subject to external historical verification.

Self-review: passed. Independent audit: not yet performed.
