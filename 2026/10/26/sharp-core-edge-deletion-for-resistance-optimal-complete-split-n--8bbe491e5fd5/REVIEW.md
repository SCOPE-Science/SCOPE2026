# Scientific review: resistance-optimal complete split networks

## Correctness — PASS

The graph, feasible budget and connectedness boundary are explicitly defined. The Laplacian has exact nonzero eigenvalues \(ra+sb\) (multiplicity \(r-1\)), \(rb\) (multiplicity \(s-1\)), and \((r+s)b\), yielding \(\mathcal K=n(r-1)/(ra+sb)+s(n-1)/(rb)\). Strict convexity of \(\operatorname{tr}(L+J/n)^{-1}\) and injectivity of the edge-to-Laplacian map prove uniqueness and justify global automorphism reduction. The Cauchy–Schwarz equality ratio \(H=\sqrt{nr(r+1)/(n-1)}\) is clipped at the feasible boundary \(ra+sb\ge sb\). The exact signs at \(s=r\) and \(s=r+1\), together with monotonicity, establish the sharp phase for every admissible integer. Independent symbolic and matrix implementations check finite instances but are not substituted for the proof.

## Originality — PASS, with residual risk

Ghosh–Boyd–Saberi (2006 proceedings; 2008 expanded article) prove the general convex optimization framework and give analytic examples for trees, wheels, and barbells, but their inspected material does not state this complete-split optimum. Yang (2014, §2.1) establishes a unit-conductance complete-split index extremum under a graph-structure constraint, not allocation of a conductance budget. Sedlák–Slavík (2025, §3.3) evaluate fixed unit-resistance split joins, not the optimum over allowed edge weights. Searches for core/periphery aliases, join spectra, edge-deletion support, and fixed-budget trace-inverse design did not reveal a dominating result. Strongly related fixed-weight results were compared by implication rather than by title. The possibility of specialized prior optimization under another terminology is an explicit residual risk; failed searches do not prove absolute novelty.

## Mathematical value — PASS

A complete split graph is a canonical core/periphery topology: a fully interconnected core serves otherwise independent vertices. The precise relative population of those groups controls which edges should receive scarce conductance. The theorem shows that **every** core edge receives exactly zero investment once the periphery is larger than the core, whereas **all** core edges are strictly beneficial when the periphery is not larger. The all-allocation uniqueness, exact resource shares and sharp discrete support transition provide a natural topology-design rule; this is not a mere unweighted Kirchhoff-index evaluation or an arbitrary small numerical slice.

## Boundaries and literature risk

The theorem assumes \(r\ge2\), \(s\ge1\), uniform per-unit cost, nonnegative weights, and total budget \(B>0\). Disconnected weighted supports have infinite objective. Positive lower bounds on all available edge weights change attainability in the deletion regime. The source-date upper bound is inferred from the dated July 2006 conference proceedings rather than an identified daily timestamp. Full literature exhaustiveness and independent verification have not been established.

Self-review: passed. Independent audit: not yet performed.
