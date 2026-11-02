# Three-axis scientific review

## Correctness — PASS

For every integer \(p,q\ge2\) and total smaller-side stationary mass \(0<a\le1/2\), the proof establishes two independent SLEM bounds from the partition-contrast vector and the zero-sum larger-part subspace. Uniform flow saturates them, leading to a scalar minimax whose unique solution is \(T_*=a\) for \(a\le1/3\) and \(T_*=2a(1-a)/(1+a)\) otherwise. At equality, compression-trace saturation forces **every** larger-side zero-sum direction to be an eigenvector; full extremal Rayleigh equality and row-capacity saturation eliminate every asymmetric optimal kernel. The cutoff and endpoint \(a=1/3\) are checked analytically. The 1,971 reproducing checks are finite corroboration, not the proof of all-parameter quantifiers.

## Originality — PASS, qualified

Boyd–Diaconis–Xiao (2004, https://doi.org/10.1137/S0036144503423264, sections 6 and 7.1) already give a general stationary-prescribed optimization framework and an exact **uniform-stationary** biclique optimum. Boyd–Diaconis–Parrilo–Xiao (2009, https://doi.org/10.1137/070689413, section 5.4.2) give the uniform symmetric-block solution. Jafarizadeh (2010, https://arxiv.org/abs/1008.2588) studies a different symmetric multipartite assumption, and Jafarizadeh (2020, https://doi.org/10.1109/TSIPN.2020.2964211) considers stars and clique-lifted families. An available earlier complete-tripartite formula gives some coinciding optimal values, but not a statement of all nonsymmetric optimal kernels on this feasible support. The current result is assessed only for its **all-cardinality prescribed two-mass classification, unique nonsymmetric-edge-flow optimizer and sharp Metropolis criterion**. Other specialist results might supply a stronger implicit implication. Some related documents were not read exhaustively; no worldwide novelty guarantee is asserted.

## Mathematical value — PASS

When sampling a prescribed two-level population on a complete bipartite network, the theorem gives explicit optimal transition probabilities and proves that no asymmetric edge-weight tuning can beat or even tie the unique uniform-flow solution. It gives a directly actionable sharp \(1/3\) threshold for ordinary Metropolis–Hastings. The all-flow uniqueness proof goes beyond computing an invariant optimizer and is important for identifiability of optimal designs.

## Limits

The claims require independent-set bipartite support, self-loops, reversible transitions, two stationary masses uniform within each part, and at least two vertices per part. The objective is SLEM, not finite-horizon total-variation distance. Nonreversible chains and arbitrary per-vertex stationary weights are excluded. The scientific review is not independent.

Self-review: passed. Independent audit: not yet performed.
