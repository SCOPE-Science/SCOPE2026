# Scientific assessment: nonlinear heat-flow gradient dissipation on complete multipartite graphs

## Correctness — PASS

The claim covers exactly one finite unit-edge complete multipartite graph with at least two nonempty parts at each fixed real exponent \(p>1\). The proof independently derives the active-edge derivative identity, treats both possible excursions of unconstrained same-part vertices, constructs a feasible extremizer for every pair of parts, and evaluates the scalar minimum using concavity or convexity. The maximization over all pairs uses the two largest parts, with a separate case at \(2s=N\), avoiding a zero-denominator boundary. Homogeneity and the maximum-of-finitely-many-derivatives rule imply the global Dini inequality. The explicit witness proves necessity. The numerical checker validates but does not replace these arguments.

Critical limits were checked: all part sizes are positive, the two-part case has no other-part vertices, the nonlinear flux is continuous at zero for \(p>1\), and \(1<p<2\) does not require a Lipschitz right-hand side for uniqueness because monotonicity provides it. The finite-time comparison estimates apply only when the sharp rate is strictly negative. The coefficient may vanish at the phase boundary.

## Originality — PASS, qualified

Compared with Mugnolo, *Parabolic theory of the discrete p-Laplace operator* (arXiv:1207.1996), the new statement evaluates a particular edge-gradient operator norm rather than vertex-norm order or contractivity. Hua--Mugnolo (arXiv:1410.1584) address time regularity and long-term behavior, Lin--Liu--Yang (arXiv:1509.07981) a positive-function relative carré-du-champ gradient estimate, and Münch--Wojciechowski (arXiv:1712.00875) the linear curvature/heat case. Their inspected theorems do not yield the nonlinear two-largest-part exact rate. The linear \(p=2\) multipartite condition and pure-clique/star subcases are explicitly excluded as standalone novelty claims. Searches using alternate descriptions of nonlinear edge-Lipschitz dissipation, multipartite heat and sharp Dini rates found no equivalent evaluated theorem, but this is not a proof of priority; unindexed and differently named coverage remain risks.

## Mathematical value — PASS

Graph heat semigroups are routinely contractive in vertex supremum or energy norms, but edge-Lipschitz contraction is a genuinely finer spatial question. The sharp coefficient gives a concrete optimal dissipation law, a phase boundary stable under arbitrary nonlinear power, and a non-obvious dependence on the second-largest part only for \(p>2\). It includes both immediate failure witnesses and nontrivial finite-time decay bounds. This infinite-family classification is motivated by gradient regularization, not by a numerical curiosity or a parameter-renamed special case.

## Limits and literature

The theorem is restricted to positive integral part sizes, unit masses/conductances, real data, finite graphs, and one-input edge-gradient behavior. It does not classify heterogeneous weights, infinite graphs, two-input Lipschitz stability or fixed-positive-time sharp amplification. The finite checker's sample counts are not mathematical completeness certificates. The cited primary sources and remaining originality risk are listed in `RESULT.md` and `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
