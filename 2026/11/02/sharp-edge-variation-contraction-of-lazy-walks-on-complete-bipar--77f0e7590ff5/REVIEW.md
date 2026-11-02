# Scientific review

## Correctness

**PASS.** The claim concerns the one-input edge-variation ratio of the *linear, constant-preserving* lazy neighbor average on real signals on finite unweighted complete bipartite graphs with both classes nonempty and of size at least two, for all holding probabilities in the closed unit interval. Edgewise coarea converts the exact operator seminorm into a maximum over indicator cuts, without any unjustified inference from finite search. For each cut, the positive/negative/zero edge counts and update difference are explicitly derived. The integer lemma \(U>V\Rightarrow U\ge pq/\max\{p,q\}\) and the two sign regimes yield the upper envelope. A whole-part indicator and a singleton of a larger part attain the two active branches; their intersection yields a unique optimum. Exact-rational direct checks support, but do not replace, this proof.

## Originality

**PASS, with priority risk.** Searches for biclique neighbor averaging, graph-edge BV contraction, optimal holding probability, Markov shift norms, and the related total-variation terminology did not identify an earlier statement covering the exact two-branch formula with the unique graph-dependent optimum. Relevant full texts on graph Markov square functionals (Feneuil, arXiv:1404.1353), graph filtering with a different shift-based variation (Sandryhaila–Moura, arXiv:1307.0468), signal variation minimization (Chen et al., arXiv:1411.7414), and nonlinear graph TV flow (Kirisits et al., arXiv:1807.10514) were inspected. Those statements do not dominate the present result, but an older equivalent under cut-norm or variation-diminishing terminology cannot be excluded. Standard coarea itself is not claimed as new.

## Mathematical value

**PASS.** The entire family of unit-edge biclique lazy neighbor filters admits an exact one-step graph BV stability curve and a unique optimal holding probability. Both depend only on the size of the larger bipartition class, despite the graph having two independent size parameters. The phase switch between a full-part cut and a singleton cut identifies distinct stability obstructions and supplies explicit equality cases. This is a natural and usable filter-design invariant beyond an isolated numeric example; it is not an arbitrary small-subgraph computation or a rephrasing of ordinary stationary-distribution mixing.

## Scope and limitations

No conclusion is given for noncomplete or weighted bipartite networks, higher-step filters, anisotropic holding, or another notion of variation. The named works were compared by mathematical implication rather than title only. Independently verifying historical priority remains appropriate.

Self-review: passed. Independent audit: not yet performed.
