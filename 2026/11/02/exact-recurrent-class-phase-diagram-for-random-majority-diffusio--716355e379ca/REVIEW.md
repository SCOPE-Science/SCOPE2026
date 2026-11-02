# Scientific review: tripartite random-majority recurrence

## Correctness — PASS

The claim is a complete finite-state classification with explicit graph, update, tie-independence and positive-integer hypotheses. The proof first establishes a positive-probability one-step route from every labeled coloring to a monochromatic-by-part corner. It then analyzes all eight corner patterns by ordering the three part sizes; the displayed classes are checked to be closed and irreducible, and every state has a positive-probability route to one. This rules out unlisted recurrent classes without extrapolating from finite experiments. The two-large-part tie class is checked separately for small-part arbitrary colors, its period is exactly two, and the uniform stationary measure and deterministic disagreement count follow directly from transition probabilities. The standalone checker independently recovers the sink components for 216 lumped and 27 labeled parameter triples, with 104 tied-class support and numerical-count checks. There is no claimed uniform absorption-time bound.

## Originality — PASS with priority risk

Zehmakan (arXiv:2302.06760v1, Section 2.3 and Appendix A.4) establishes exponential absorbing classes on specially constructed graphs and analyzes cycle dynamics, but neither statement supplies the exact complete-tripartite three-regime theorem, including the all-equal consensus boundary and tie-largest uniform distribution. The 2019 Weber–Theisen–Motsch stochastic consensus paper studies a different updating mechanism, not independent binary neighbor-majority ties. Relevant literal/alias searches for complete-tripartite random majority and semantic comparisons of close indexed results found no exact dominating claim. A prior complete-bipartite classification has no third part and cannot yield the tie-largest noisy component by substitution. Residual risk: unindexed specialist literature or deeper results not identified by the accessible searches; full text of the less-relevant 2019 paper was not reviewed.

## Mathematical value — PASS

The result completely determines recurrent behavior on an infinite natural family rather than adding a single graph example. Equality of two largest communities triggers a \(2^{c+1}\)-state irreducible recurrent class, exact fair-coin stationary noise, and an invariant number of disagreeing edges; equality of all three eliminates that nonconsensus class. This distinguishes persistent stochastic polarization from eventual consensus and gives exact phase and stationary quantities at every finite size. Those precise structural boundaries are not implied by general examples of exponential recurrence.

## Scope and risks

All source and proof comparisons are about this model only. Generalization to four or more parts, biased ties, nonbinary opinions or asynchronous updates is not established. Source completeness and external mathematical priority are not guaranteed.

Self-review: passed. Independent audit: not yet performed.
