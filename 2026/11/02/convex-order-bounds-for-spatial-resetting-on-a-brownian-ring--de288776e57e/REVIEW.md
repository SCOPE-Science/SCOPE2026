# Scientific review

## Correctness — PASS

The formula for the killed Brownian motion follows from the two-endpoint Dirichlet boundary-value problem. The search-time renewal identity is solved exactly, and its derivative with respect to the reset-location transform has a strictly positive sign for positive Laplace argument. The second derivative of the killed transform with respect to unreset search cost is strictly positive, including the antipodal endpoint by continuity. Strict Jensen/chord inequalities identify unique extremizers in the cost distribution. Uniform small-rate Taylor expansion and exponential large-rate estimates recover both quantitative limits. The finite checker passes 921 tests; the theorem does not rely on finite enumeration.

## Originality — PASS (qualified best-knowledge)

The closest primary source, Julián-Salgado et al., arXiv:2605.08414, treats rate optimization, fixed reset sites and associated transitions on the same Brownian ring. The accessible source text does not state sharp extrema over arbitrary reset-position distributions with fixed unreset search cost, nor the all-parameter convex-order theorem. The full source arXiv:2401.01125 studies equivalent resetting positions at one prescribed rate but does not assert the simultaneous strict fixed-cost endpoint extremal law. The inspected full PDF arXiv:2507.14483 studies half-line distributed resets, mainly selected density families and optimal rates. Evans and Majumdar (2011) supply older resetting principles; only summary material was available here. Published research-record searches did not identify the precise theorem. The absence of a found match is not proof of priority; the principal risk is that a stronger preexisting stochastic-ordering or renewal-optimization result may imply the theorem. Independent priority audit remains unperformed.

## Value — PASS

The constraint fixes the free-search mean of reset locations, making the comparison substantive rather than favoring a trivially nearest site. It establishes a strict monotonic hierarchy that simultaneously controls all positive time-discounted completion probabilities and the mean, and identifies the unique extremal distributional designs across every reset rate. Equal-budget designs differ only at quadratic order for weak resetting but exhibit exponential relative separation in the strong-reset regime. This resolves a natural spatial-reset-design question beyond optimization over a scalar resetting frequency.

## Limits

The theorem is limited to a one-target homogeneous circle, Poisson resetting, complete independent position draws in a compact interval bounded away from the target, and a fixed mean free first-passage cost. It does not give ordinary stochastic dominance, optimality under arbitrary cost criteria, or uniqueness of the physical angular distribution. The numerical checks do not constitute a proof. Literature overlap risk persists.

Self-review: passed. Independent audit: not yet performed.
