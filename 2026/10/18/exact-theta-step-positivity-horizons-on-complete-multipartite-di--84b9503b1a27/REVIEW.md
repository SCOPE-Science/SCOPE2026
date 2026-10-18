# Scientific review

## Correctness — PASS
The complete Laplacian eigenspace decomposition proves the resolvent diagonal formula. Its exact ordering by part size identifies the unique obstructing vertex orbit. Inverse positivity makes the diagonal criterion necessary and sufficient for the full stochastic step, and the quadratic crossing proves all endpoint and infinite-horizon cases, including forward Euler. The asymptotic assertion follows from the same resolvent with a scaled step. A standard-library exact-rational checker replayed 29,662 finite assertions; enumeration is corroboration, not proof of all orders.

## Originality — PASS, subject to literature risk
Horváth (2004) concerns general cone invariance and safe steps, and Schatz–Thomée–Wahlbin (2010) study related \(	heta\)-method positivity in finite-element systems. The published 2026 resolvent-return theorem covers the generic diagonal criterion and abstract spectral crossings, which are explicitly acknowledged. The present claim supplies an exact evaluated horizon for every unweighted multipartite graph with all parts at least two, the reduction to total order and minimum part size, the limiting-part classification, and the exact scaling. Database and accessible-literature comparisons did not identify an implication-equivalent explicit result; unindexed literature is a real residual risk.

## Value — PASS
The result turns a graph-dependent positivity-restricted numerical time step into a closed-form design rule depending on just two natural network statistics. It identifies precisely which community is the positivity bottleneck and when arbitrarily large steps are safe, improving general sufficient graph bounds and covering infinitely many nonisomorphic structures. The particular closed formula is motivated by end-step sign preservation in diffusion, not arbitrary parameter selection.

## Scientific limits
Applies only to the unweighted combinatorial Laplacian and classes of size at least two. Finite checks do not certify the all-order theorem. Related specialized graph-theta literature could contain an equivalent algebraic expression.

Self-review: passed. Independent audit: not yet performed.
