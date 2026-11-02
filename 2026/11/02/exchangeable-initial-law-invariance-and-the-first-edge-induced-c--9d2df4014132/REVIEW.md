# Scientific review: exchangeable voter consensus on four sites

## Correctness — PASS

The backward graphical representation is valid for independent rate-one copying clocks on any finite strongly connected zero-diagonal copying network. Initially all four ancestral lineages occupy all sites, so the first coalescence has exponential rate four regardless of edge probabilities. The hypergeometric probabilities of nonconsensus conditional on one, two or three uniformly chosen initial ones imply \(T_2-4T_1/3=-1/12\) after exact survival integration; complementation gives \(T_3=T_1\). These are universal analytical identities and do not rely on small-graph sampling. Independently, the first-step equations were solved over exact rational numbers for all 38 connected labeled graphs on four vertices and every connected graph on three vertices. Complete isomorphism reductions give six four-vertex graph types and six oriented edge-insertion transitions, with the two strictly positive increments stated in RESULT.md. Endpoint cases and already-consensual initialization are covered.

## Originality — PASS (subject to historical-priority risk)

The standard voter model, its coalescing-walk dual, and finite-state absorption-time recursions are established. Masuda (2014) obtains consensus-time scaling on two-clique networks; Iwamasa and Masuda (2014) give general exact matrix recursions and network optimization but do not report the weighted-network universal four-site identity or the six graph-type edge table in the inspected relevant sections. Gastner and Ishida (2019) establish qualitatively nonmonotone effects from adding interclique edges; the generic possibility of edge-induced slowdown is NOT a claimed discovery here. The combined graph-independent identity, initial-law invariance, complete four-vertex transition census, and minimum size are the specific comparison targets. A hidden corollary of earlier general coalescent identities or an unpublished small-network table remains possible; absence in searches is not proof of absolute priority.

## Mathematical value — PASS

A natural methodological uncertainty in short social networks is whether the distribution of initial dissenters changes which topology reaches agreement faster. The four-site genealogy identity shows that **every** nontrivial exchangeable initial law gives an identical topology ranking, even for weighted directed copying matrices; this is an exact and non-obvious structural simplification. For unweighted undirected social graphs, the complete edge-insertion census identifies the precise first population size where extra communication can retard consensus and the two graph motifs at that boundary. This is a motivated structural cutoff rather than an arbitrary numerical example.

## Risks and limitations

The clock normalization is rate one at **each** vertex; a single global update clock scales all numerical times. Irreducibility and zero diagonal are essential for the stated universal proof. Different agent rates, self-loops, nonexchangeable initial opinion assignments, zealots, or alternate voter rules are not covered. A general finite-state algorithm can of course compute the small graph values, and historical literature may already imply the combined result without stating it in this form. Independent validation has not been performed.

## Closest sources inspected

N. Masuda, *Voter model on the two-clique graph*, arXiv:1403.4763 (2014), sections I–II, numerical initial conditions, and scaling arguments. Y. Iwamasa and N. Masuda, *Networks maximizing the consensus time of voter models*, arXiv:1404.6360 (2014), methods for finite-state equations, four-site worked example, N=10 optimization, and the relevant derivation appendix. M. T. Gastner and K. Ishida, *Voter model on networks partitioned into two cliques of arbitrary sizes*, arXiv:1908.00849 (2019), community setup and nonmonotonic link-effect arguments. These inspectable claims concern different parameter classes or consequences; no claim is made that every historical source has been exhaustively read.

Self-review: passed. Independent audit: not yet performed.
