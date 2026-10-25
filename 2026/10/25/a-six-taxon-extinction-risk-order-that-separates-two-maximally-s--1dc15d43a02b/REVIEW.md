# Assessment of the six-taxon extinction-loss shape theorem

## Correctness — PASS

The exact expectation calculation is by summing edge-loss indicators. Six shape enumerations follow from the root partitions \(1+5\), \(2+4\), and \(3+3\), and the five strict differences factor into positive powers of \(q\) and \(1-q\). The depth-preserving local graft changes only internal clade-size terms within the six-leaf fringe. A standard-library rational checker independently reconstructs every six-tip clade vector, all 64 extinction states over twelve parameter choices per shape, and the smaller-tree maximizers. This finite verification corroborates, rather than replaces, the exact proof. The theorem excludes \(q=0,1\), \(\theta=0\), and arbitrary unequal edge lengths.

## Originality — PASS with residual bibliographic risk

Faller and Steel (arXiv:0911.3441, 2009), sections on expected phylogenetic diversity under trait-driven extinction, establish a broader qualitative comparison between correlated and independent extinction; the model here is different and the cited theorem does not itself rank six rooted tree shapes. Fischer (arXiv:1801.10418, 2018; journal 2021), Theorem 2 and its six-tip illustration, identifies the two tied Sackin-minimal shapes but does not compare extinction losses. *Split sizes and extremal tree shapes* (2019), introduction and extremal functional framework, treats unrooted smaller-side split statistics, not this rooted clade generating sum. Maliet, Gascuel and Lambert (Systematic Biology, 2018) model ranked tree shapes and nonrandom extinctions; full-text access was unavailable, and the overlap risk is explicitly unresolved beyond the abstract-level distinction in models and conclusions. The comparisons of assumptions and mathematical implications, as well as relevant database searches, are recorded in `AUDIT.json`. No inspected statement subsumes the combination of the strict six-shape order, factorized tied-minimizer gap, and arbitrary-size depth-preserving graft; related uninspected combinatorial optimization results remain a possible risk.

## Mathematical value — PASS

Phylogenetic-diversity loss is a natural conservation statistic and correlated species extinction is a relevant modeling contrast. An exact all-parameter classification at the first leaf count where two Sackin-optimal topologies differ, together with an exact depth-preserving graft that applies inside any larger full binary tree, shows a substantive failure of leaf-depth balance to determine correlated-extinction excess. It is not merely a relabeling or finite numerical comparison; the proof provides the strict inequalities and a local structural rule.

Self-review: passed. Independent audit: not yet performed.
