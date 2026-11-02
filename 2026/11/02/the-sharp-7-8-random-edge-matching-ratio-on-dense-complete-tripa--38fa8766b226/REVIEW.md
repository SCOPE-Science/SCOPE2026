# Scientific review: random-edge matching on complete tripartite graphs

## Correctness — PASS

The claim concerns a precisely specified uniformly feasible-edge matching process on \(K_{a_n,b_n,c_n}\) with strictly positive proportional limits. Conditional on the remaining part sizes, the next edge type has probability proportional to the product of the two part sizes. Independent exponential edge clocks of rate \(1/n\) reproduce that embedded transition law exactly and lead to a density-dependent Markov chain with quadratic drift. Uniform finite-horizon convergence follows from bounded predictable quadratic variations and Gronwall's inequality. The proposed scalar integral representation solves all three drift equations by direct differentiation. Terminal-time convergence is justified separately: when the largest limiting part is strictly larger than the second largest, it eventually outnumbers both smaller parts together; when the largest two limiting sizes tie, all fluid coordinates vanish. Pair-type counts are the compensators integrated along the trajectory, with negligible tails by depletion. Optimization over positive proportions yields the claimed unique \(7/8\) minimum. Exact finite-state enumeration, labeled-graph enumeration and symbolic polynomial identities are independently checked by `checker.py` (3311 assertions). These checks corroborate, rather than prove, the asymptotic theorem.

## Originality — PASS, with residual literature risk

The closest full-text comparison is Hertz et al. (arXiv:2204.10236, first posted 2022-04-21), particularly its introduction, Sections 3–5 and conclusion. It explicitly defines uniform current-edge greedy matching but analyzes the **uniform average over all maximal matchings**, warning that the distribution produced by the greedy process is unequal. Its families comprise paths, cycles, chains, ladders and trees, not this dense tripartite family; its results do not imply the edge-type flow or the class-sharp ratio. Arnosti (2021/2022, author's full PDF) analyzes RANDOM-EDGE on bipartite graphs and averages over random bipartite edge sets, not deterministic three-part graphs. Dyer and Frieze (1991) provide the original fixed-graph random-edge algorithm and general performance context; the accessible abstract concentrates on worst-case and sparse graph families. Pippenger (1989) analyzes sequential adsorption in locally restricted graph settings, not dense complete tripartite graphs. No equivalent claim was found in the recorded published-finding corpus searches or the accessible earlier-claim comparisons. Existing nearby claims about \(K_{n,n,k}\) in a sparse-third-class regime or complete split graphs neither cover \(K_{2n,n,n}\) nor imply this sharp global tripartite ratio.

The full text of Dyer and Frieze (1991) was not obtained; its possible special cases remain a genuine priority risk. Search non-detection does not establish universal historical novelty, and the result has not received independent scientific priority review.

## Value — PASS

The theorem gives an exact asymptotic answer for a canonical randomized algorithm on a natural dense graph class, beyond routine finite enumeration: the process loses \(bc/(2a)\) matches per scaling unit to edges between the two smaller parts. It supplies the complete three-type matching profile, a sharp efficiency bound and its unique worst-balanced part proportions. The extremal graph \(K_{2n,n,n}\) is natural because it has a perfect matching but random greedy selection sacrifices an asymptotic \(1/8\) of its size. The parameter dependence distinguishes the effects of part imbalance and makes the precise constant useful for random sequential matching and dimer adsorption benchmarking. No claim about general graphs, finite-order sharp inequalities or a Gaussian limit is made.

## Closest literature and remaining scope

Primary motivating source: A. Hertz, S. Bonte, G. Devillez and H. Mélot, *The average size of maximal matchings in graphs*, arXiv:2204.10236 (2022-04-21).

Additional comparisons: N. Arnosti, *Greedy Matching in Bipartite Random Graphs* (2021/2022); M. Dyer and A. Frieze, *Randomized greedy matching* (1991); N. Pippenger, *Random Sequential Adsorption on Graphs* (1989).

Unproved: nonuniform edge weights, multipartite graphs with four or more parts, finite-size optimal ratio bounds, second-order fluctuations. The exact checker is finite and does not establish historical priority.

Self-review: passed. Independent audit: not yet performed.
