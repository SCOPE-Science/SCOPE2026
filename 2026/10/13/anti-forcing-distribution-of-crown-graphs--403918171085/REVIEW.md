# Review

## Correctness
PASS. The proof reduces \(af(\operatorname{Cr}_n,M_\pi)\) to a minimum feedback arc set in a contracted digraph. The contracted digraph has all arcs of the complete bidirected graph except the cycle-cover arcs \(i\to\pi^{-1}(i)\). Maximizing an acyclic subgraph over linear orders leaves exactly one missing forward arc per permutation cycle, giving \(n(n-3)/2+c(\pi)\). The recurrence, spectrum, and extremal multiplicities follow from standard labelled-cycle counting. Independent finite stress tests reproduce the formula by exhaustive topological orders through \(n=6\) and direct edge-deletion uniqueness through \(n=5\).

## Originality
PASS with stated residual risk. Full text of the 2014 foundational paper was inspected at the definition, alternating-cycle, and feedback-set reduction; searches within it found no crown, complete-bipartite, or derangement specialization. Full text of the 2016 extremal/spectrum paper was inspected and likewise produced no crown or complete-bipartite occurrence. Searches under “crown graph,” “\(K_{n,n}\) minus a perfect matching,” “complete bipartite graph minus a 1-factor,” and “bipartite Kneser \(H(n,1)\)” did not locate the stated distribution. General anti-forcing bounds and complete-bipartite examples do not imply the formula after deleting a fixed perfect matching. The residual risk is an unindexed equivalent result under another alias.

## Value
PASS. The crown graph is a canonical matching-deleted bipartite family, and anti-forcing a fixed perfect matching is generally a feedback-arc-set problem. Here the dense contracted digraph admits a complete exact solution, and the theorem classifies every perfect matching, not merely the minimum or maximum. The cycle-statistic form yields the whole distribution, a gapless spectrum, and exact extremal multiplicities, making it a reusable closed benchmark for anti-forcing theory.

Self-review: passed. Independent audit: not yet performed.
