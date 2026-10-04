# Review of Coefficientwise extremals for visibility polynomials of complete multipartite graphs

## Correctness
PASS. In a complete multipartite graph, only selected pairs from the same part require an internal geodesic vertex; such a pair is visible exactly when some unselected vertex lies outside that part. Passing to the nonempty complement gives a disjoint bad-event count
\[
r_{N-t}=\binom Nt-\sum_{n_i\ge t+2}\binom{n_i}t.
\]
This yields the coefficientwise maximum class immediately. It also shows that the star is the unique cubic-coefficient minimizer, while
\(r_{N-1}=\sum_{n_i\le2}n_i\), producing the sharp obstruction from \(K_{3,N-3}\) for every \(N\ge6\).
The small orders \(N=3,4,5\) are completely resolved by the same two coefficients. Definition-level exhaustive verification agrees through order ten, and partition-level checks agree through order thirty.

## Originality
PASS. The closest direct polynomial source already gives the complete-bipartite polynomial and a general join recurrence, so the basic multipartite counting formula is treated as prior-implied machinery rather than as the novelty. The 2026 complete-multipartite game paper gives the maximum mutual-visibility number and maximal-set structure but does not compare complete coefficient vectors across multipartite partitions. The other inspected 2026 polynomial paper treats wheels, friendship graphs, shell graphs, and bow graphs. Targeted searches for coefficientwise extremals, multipartite visibility-polynomial orderings, and absence of a minimum did not locate the stated fixed-order extremal theorem. The surviving claim is specifically the coefficientwise maximum class and the exact \(N=6\) threshold at which a minimum ceases to exist.

## Value
PASS. Coefficientwise comparison is a natural strengthening of comparing only the largest feasible set: it asks whether one graph has at most or at least as many feasible visibility sets at every size. The theorem identifies all maximizers and proves a sharp structural boundary for minimization. The nonexistence result is not an isolated numerical crossing: it holds for every \(N\ge6\) and is forced by two mathematically distinct regimes, the cubic coefficient and the near-top coefficient.

Same-model review: passed. Independent audit: not yet performed.
