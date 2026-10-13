# Review of the mod-six balanced-domination phase of half graphs

## Correctness
PASS. The two families of closed-neighborhood equations are exact for the half-graph adjacency. Subtracting consecutive equations yields a deterministic two-coordinate recurrence, while the first and last equations supply the only boundary conditions. Starting with \((x_1,y_1)=(t,-t)\), the recurrence has the displayed six-periodic orbit. The final boundary is satisfied for nonzero \(t\) exactly when \(n\equiv1\pmod3\), and the six-term weight contributions sum to zero, giving the stated mod-six maximum. The converse is proved because the recurrence keeps every equation residual constant, so satisfying the endpoint residuals satisfies the entire system. Exhaustive finite checking agrees with the symbolic proof.

## Originality
PASS. The introducing 2021 paper was inspected at the definition, \(d\)-balanced classification, and open-problem sections; it treats regular graphs, complete multipartite graphs, generalized ladders, joins, and trees but does not state a half-graph, chain-graph, or Ferrers specialization. The latest same-invariant preprint was inspected in full-text form and treats convex-polytopes, trees, caterpillars, and grids; targeted searches found no half-graph, chain-graph, Ferrers, or bipartite occurrence. The general adjacency-spectrum literature for chain graphs gives characteristic-polynomial machinery but does not state the ternary balanced-function family or its weight maximization. Searches under object aliases and the equivalent closed-neighborhood-kernel formulation located no theorem implying the accepted claim.

## Value
PASS. Half graphs are the canonical twin-free chain graphs and therefore a natural benchmark for a neighborhood-linear domination invariant. The answer is not uniformly \(d\)-balanced: nonzero balanced functions appear with period three, while positive optimum weight appears only in one residue class modulo six. The complete six-periodic labeling classification explains this phase transition and distinguishes \(d\)-balanced graphs with nontrivial balanced functions from graphs with only the zero function.

Self-review: passed. Independent audit: not yet performed.
