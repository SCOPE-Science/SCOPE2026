# Self-review

## Correctness — PASS

The finding is a theorem for every \(a,b\ge2\) and every finite field of characteristic two, not an inference from a bounded census. The incidence identity \(F=B^{\mathsf T}B\) holds because every edge has exactly two endpoints, so the line-graph adjacency has diagonal zero in characteristic two. Connectivity makes \(B\) surjective onto the even-coordinate vertex subspace, and its transpose has only the global constant kernel. Splitting ordinary coordinates into sums and zero-sum spaces reduces the matrix of \(BB^{\mathsf T}\) to the three explicit parity cores and scalar blocks. Their power ranks and the extra scalar blocks force the stated Jordan forms. Kernel counting then gives all first-entry populations and period-two orbit counts. The two separately implemented checkers passed for 100 parameter pairs and 419400 direct states, respectively. Risk: matrix verifications are finite supporting checks, not a substitute for the all-size decomposition, and no independent audit has been performed.

## Originality — PASS, qualified

The 2015 arXiv full manuscript by Ducey, Gerhard, and Watson establishes critical/Smith group structure for intact square rook graphs, not adjacency iteration after one square is deleted. Peeters (2002), Section 3, studies modular spectra and minimal polynomials of intact Hamming graphs, including rook products, but not the punctured graph. Marr and Hütt (2005) treat a different class of graph CA update rules. Published records about complete-multipartite parity and distance-two-cube parity analyze distinct adjacency operators. Existing mixed-parity intact-rook and deleted-hypercube dynamical results do not imply this one-square deletion theorem. The novelty is solely the punctured-graph Jordan classification and corresponding transient/cycle census, not the known incidence identity or intact graph facts. Risk: historical indexing is incomplete, and an equivalent deleted-rook calculation may exist elsewhere.

## Value — PASS

Deleting one vertex is a natural minimal perturbation of the rook graph, and the classification shows a strong structural dynamical change: in mixed parity, primitive two-cycles vanish while a sharp five-step transient appears, with its final-entry probability \(1-1/q\) uniform in both board dimensions. The parity trichotomy gives all Jordan blocks, exact finite-field orbit counts and all time layers for an infinite graph family. This is a motivated perturbation question, rather than an arbitrary parameter slice or numerical improvement. Its scope is only single deletion and characteristic two.

## Closest sources and limitations

J. E. Ducey, J. Gerhard and N. Watson, *The Smith and Critical Groups of the Square Rook's Graph and its Complement*, arXiv:1507.06583v1 (2015-07-23), https://arxiv.org/abs/1507.06583; R. Peeters, *On the p-Ranks of the Adjacency Matrices of Distance-Regular Graphs*, Journal of Algebraic Combinatorics 15 (2002), 127–149; C. Marr and M.-T. Hütt, arXiv:cond-mat/0502509v1 (2005). Prior results on intact or differently punctured graph families may inform the method but do not entail the present complete classification. An unindexed exact equivalent remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
