# Independent mathematical audit

## correctness

PASS

For a zero vertex in part i, the number of neighboring label-2 vertices is exactly T minus t_i, so the perfect-Roman condition is equivalent to T minus t_i equaling 1 on every zero-containing part. This yields four exhaustive and disjoint regimes: zero-free; T=1; T=2 with the two label-2 vertices in distinct parts; and T at least 3 with exactly one zero-containing part carrying T-1 label-2 vertices and exactly one label-2 vertex outside it. Counting the independent residual 0/1 choices in these regimes gives the displayed polynomial, and minimizing each regime yields min of N, the smallest part plus 1, and N minus the two largest parts plus 4; the T-at-least-3 regime is never smaller. The inspected verifier independently enumerates every ternary labeling for every nondecreasing multipartite type of total order 2 through 9 and matches every coefficient and the minimum formula.

## originality

PASS

The 2019 paper gives a linear-time algorithm for the minimum perfect-Roman weight on cographs, a class containing complete multipartite graphs, but it does not provide a closed complete-multipartite formula or count all feasible functions by weight. The 2024 enumeration paper studies pointwise-minimal perfect Roman dominating functions and parameterized enumeration rather than the polynomial counting every feasible function. Targeted Resultary searches found many exact complete-multipartite polynomials for other Roman-domination variants, but no perfect-Roman all-function polynomial. The full weight enumerator is strictly richer than the already algorithmically computable minimum and is not implied by the cited enumeration output object.

## value

PASS

Complete multipartite graphs are a canonical graph family, and the full feasible-function weight distribution is a natural refinement of the known minimum problem. The exact structural classification and polynomial recover every coefficient for arbitrary part sizes and can support later probabilistic, extremal, or enumeration questions; this is more than a finite table or a minimum-only specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
