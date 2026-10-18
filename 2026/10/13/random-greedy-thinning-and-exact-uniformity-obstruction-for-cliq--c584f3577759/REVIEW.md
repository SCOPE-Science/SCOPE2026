# Independent mathematical audit

## correctness

PASS

Assign continuous iid priorities. Within each core-plus-private K_(s+1) cluster, the first identity (core versus one of s privates) is independent of the first priority time. Independent cluster indicators select a Bernoulli-thinned core A with p=1/(s+1); relative cluster minima on A are uniformly ordered, giving exactly random-order core greedy on H[A]. A private vertex is accepted in each cluster whose core is not eventually selected, with independent uniform private labels conditional on S by within-cluster relabeling symmetry. This proves the mixture law and Pr(I)=s^(-(n-|S|))Pr(S). The core-empty event occurs iff A empty, so each fully private output has probability (s+1)^(-n). If H has an edge, its maximal independent-set count sum_{S independent}s^{n-|S|} is strictly below (s+1)^n, contradicting uniformity; if edgeless, every cluster is an independent uniform clique. For H=K_n, only empty/singleton core outcomes occur; deficits yield exact total variation s/(s+n)-(s/(s+1))^n. Fresh independent all-vertex-permutation enumeration agrees with exact mixture for five small instances (2904 permutations), including private-choice fibers and complete-core total variation.

## originality

PASS

Fairfax-Ball proves tree-only exact uniformity and mixed-spider distributions, while the published threshold- and chain-graph greedy laws concern particular classes that do not contain arbitrary clique coronas. The clique-corona independent Bernoulli thinning and conditional complete terminal distribution are distinct; the random-priority coupling itself is standard and is not claimed as a new technique. Random sequential adsorption and whiskering literature may contain the same coupling under alternative names.

## value

PASS

This is an exact distributional theorem for a natural graph operation on arbitrary finite core graphs, not a single graph-family table. It gives a simple simulation/reduction mechanism, uniformity iff the core is edgeless, and a sharp analytic total-variation bias on all complete cores. These quantities directly address the established random-greedy MIS output-uniformity question even when full core greedy probabilities are computationally difficult.

The dated certificate retains the supplied scientific assessment, sources and limitations.
