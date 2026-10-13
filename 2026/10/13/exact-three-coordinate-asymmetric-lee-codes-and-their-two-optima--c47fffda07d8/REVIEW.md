# Scientific review

## Correctness — PASS

The local metric is the published \(\lambda=1\) ALD formula, checked against the four-by-four cost matrix. The correspondence between distance-three codes and cliques of the 64-word compatibility graph is exact. An exhaustive Bron–Kerbosch implementation enumerates 618624 maximal cliques, with largest size 19 and exactly 32 attaining that size. A separately written C++ greedy-color-bound maximum-clique search independently returns the same optimum and count; its branch upper bound is a proper coloring bound on the remaining candidate graph. Both verifiers were executed from the included source paths and passed. The claimed order-384 symmetries preserve the local metric, and both orbit sizes, representative spectra, and exhaustion of the 32 maxima are separately checked.

## Originality — PASS, with residual risk

The earliest primary version, arXiv:1506.00740v1, is dated 2015-06-02. In the expanded full text arXiv:1506.00740v5, Table V lists the length-three, minimum-distance-three, \(\lambda=1\) bounds \(6\le A_1(3,3)\le30\), not 19. The author-hosted 2015 ITW full text gives LP bounds and constructions, not an equality census. These two primary texts were examined for the same metric, same parameters, and potentially stronger implications. Targeted bibliographic and equivalent-formulation searches did not locate the exact optimum or orbit classification. The result is therefore assessed as not implied by the inspected sources; a nonindexed historical computation is still possible.

## Value — PASS

This is an exact solution of a specifically motivated short-code benchmark in the asymmetric DNA-readout metric, improving a 6-to-30 published interval to an exact value and classifying the full equality layer. The two inequivalent optimal geometries are structurally distinguished by their pair-distance spectra, showing that the maximum need not arise from a single design type. The finite scope is explicit and the result does not claim asymptotic gains.

## Limits of review

The code computations are complete over the specified 64-word space but provide no result for other lengths, distances, or metric parameters. Novelty searches cannot certify that no obscure equivalent enumeration exists. This is a self-review, not an independent external audit.

Self-review: passed. Independent audit: not yet performed.
