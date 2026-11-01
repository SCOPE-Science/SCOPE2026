# Mathematical review

## Correctness — PASS

The statement concerns every integer \(n\ge3\), all real times \(t\ge0\), and the original shortest-path Wasserstein-\(1\) metric for the **combinatorial** Laplacian heat kernel. The four spectral projections in `RESULT.md` are exhaustive, mutually orthogonal and have eigenvalues \(0\), \(n-2\), \(n\), and \(2(n-1)\). For each pair orbit, a graph-symmetry reduction of the Kantorovich dual gives an explicit finite-dimensional optimization. All sign and feasibility restrictions are justified, including the exceptional \(n=3\) case where the generic-to-generic edge is absent. Sharpness is realized by explicit feasible dual potentials, not inferred from the numerical checker.

The independently executable rational checker recomputes 24 finite heat-kernel matrices and their three orbit types, tests 72 explicit attaining potentials and exhausts 2359 anchored integer Lipschitz potentials for smaller sizes. Integer exhaustive search is sufficient for those test instances by incidence-matrix total unimodularity; the proof for all sizes and times is analytic. No claim about weighted or degree-normalized generators is made.

## Originality — PASS, qualified

Ollivier (arXiv:math/0701886) establishes the transport curvature framework. Lin, Lu and Yau (DOI:10.2748/tmj/1325886283) analyze local graph curvature, including cycle/cube examples. Münch and Wojciechowski (arXiv:1712.00875) provide general graph heat semigroup curvature-gradient results. Klee and Stamps (arXiv:2008.01669, Proposition 8) give precisely the crown-graph Laplacian eigenvalues. **Those eigenvalues are previously known**; the new claim is the exact three-orbit Wasserstein transport optimization, not the spectral calculation. Inspected relevant primary statements do not give the *exact full-time* three-orbit transport profiles of the crown graph. The local first-order behavior of the six-cycle and cube is already part of the context and is **not** presented as new.

Searches also compared the aliases “crown graph”, “complete bipartite minus a perfect matching”, “heat-kernel Wasserstein”, “graph-Lipschitz semigroup”, and the characteristic two-exponential formula. Published crown-graph records located concerned a sequence spectrum and odd colorings, not transport. A previous exact profile on complete bipartite graphs does not cover deleted matching edges; a previous complete multipartite heat-transport result likewise does not cover crown graphs, whose complement is not a union of disjoint cliques. No dominating implication was found among the inspected results.

**Residual priority risk:** Equivalent older derivations might appear in unindexed distance-regular graph calculations. Searches and materially read primary sections are not a proof of absolute publication priority; full exhaustive scrutiny of every potentially relevant publication was not possible.

## Mathematical value — PASS

Crown graphs are a natural diameter-three, edge-transitive, distance-regular family, with the six-cycle and the three-cube as its first two members. Obtaining a sharp **all-time** transport value for all three distance orbits gives strictly finer information than a curvature lower bound or one-time contraction test. The vanishing contribution of the middle heat eigenmode in *all* Wasserstein maxima is a structural cancellation; the exact shortest-path additivity failure at precisely the six-cycle is a sharp graph-family boundary. These results provide explicit semigroup-gradient benchmark examples and potential input for transport comparison questions.

## Scope and limitations

The proof and package are confined to real graph-Lipschitz seminorms and Wasserstein-\(1\) on unweighted crown graphs under counting measure and the combinatorial Laplacian. They do not classify higher Wasserstein exponents or all finite graphs, nor do they guarantee exhaustive novelty. The numerical checks are supplementary. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
