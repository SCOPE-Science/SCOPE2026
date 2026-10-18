# Scientific review — worst-outage resistance on alternating-price cycles

## Correctness — PASS

The result is self-contained for integers \(m\ge2\), all positive prices and budgets, independent nonnegative conductances, and all possible single-edge outages. Equation (1) follows by counting the \(d(2m-d)\) pairs whose path traverses each surviving edge. All feasible finite-risk designs necessarily have strictly positive weights; the budget simplex and reciprocal blow-up give existence. Strict convexity is proved on the unrestricted budget hyperplane because any two different budget-feasible designs differ in at least two edge variables, and each post-outage resistance includes all but one variable. Thus each failure objective, and hence their finite maximum, is strictly convex on the feasible affine set. Price-preserving automorphisms reduce the unique optimum to two edge classes without imposing symmetry as an assumption. The two parity sums are exact, their difference is \(m\), and elementary one-dimensional differentiation proves the three regimes and both boundary cases. The nominal-design contrast follows from differentiable edge-transitive marginal derivatives and unequal cost multipliers.

The standalone verification code was executed and passed 2,478 symbolic and numerical checks, including direct post-failure eigenvalue constructions and random asymmetric competitors. The proof, not the experiments, establishes the all-size result. The separate derivative and asymptotic simplifications were checked symbolically.

## Originality — PASS, with explicit residual uncertainty

The closest inspected source is Johnson–Chertkov, arXiv:1004.2285, Section V, which already formulates optimization under worst-case line failures and explains its convexity, giving an important broader problem class. That contribution is **not** claimed here. Its full text does not present the exact solution for the alternating-price cycle, the reciprocal sharp thresholds, unrestricted optimizer uniqueness, or the positive-width equal-conductance plateau. Ghosh–Boyd–Saberi (SIAM Review 2008, sections 5 and 8) establish nominal total-resistance optimization and symmetry methods; their cycle discussion concerns the equal-price nominal problem. Boyd–Vandenberghe–El Gamal–Yun (ISPD 2001) address varying currents rather than a worst-post-edge-deletion objective.

Targeted searches of published mathematical records, together with the accessible prior conductance-allocation claims, found no equivalent statement. A prior paper or independent exact derivation outside the inspected and indexed literature remains possible; absence of a matching search hit is not a proof of uniqueness or absolute priority. The mathematical claim is original relative to the concrete results inspected, rather than merely a rename of the cited general convex program.

## Value — PASS

Protecting a network against **any** one link outage is a natural and established design objective. It changes the optimizer qualitatively: an entire interval of unequal construction prices admits equal conductances, while nominal effective-resistance minimization has no such interval. This is a structural three-regime phase diagram valid for all even cycle sizes, with both sharp thresholds and a precise large-size width law. It gives a concrete closed-form benchmark for nonsmooth robust network optimization and isolates when outage equalization outweighs price bias. The formula is elementary to evaluate after the proof but is not an arbitrary finite table, isolated numerical example, or mere restatement of the generic convexity framework.

## Remaining scientific risks and scope

An equivalent specialized result may appear in literature not indexed by the searches. The 2010 paper contains the general post-failure convex optimization model; the present result is a solved special family, not a general method. The model is restricted to alternating prices, independent conductance design, deterministic single outages, and the Kirchhoff-index objective. No inference about multi-edge outages or arbitrary graphs is made.

Self-review: passed. Independent audit: not yet performed.
