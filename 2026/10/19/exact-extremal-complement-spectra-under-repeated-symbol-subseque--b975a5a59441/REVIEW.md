# Scientific assessment of repeated-symbol complement spectra

## Correctness — PASS

The proof gives a bijection between distinct complements and bounded deletion-count vectors indexed by maximal runs of the distinguished symbol. A coefficientwise polynomial identity shows that balancing those run lengths never reduces the number of outcomes for any deletion order. Optimizing the number of runs therefore gives an exact, attained all-parameter formula, not just a lower bound. The closed three-deletion specialization is derived by counting the three possible run-occupancy partitions and proving that its maximizer has the asserted location. Reproducible exhaustive checks were executed, but do not replace the infinite proof.

## Originality — PASS, subject to residual prior-art risk

The closest primary source is Adamson–Fleischmann–Huch, arXiv:2603.20790v1 (March 21, 2026), Sections 3–5. Its algorithms and singleton-complement criteria are acknowledged; it explicitly leaves bounds and special closed formulas open. The theorem here concerns the exact extremum for the fixed deleted subsequence \(a^k\), not that open problem for arbitrary deleted words. The older multiplicity-counting paper of Torres-Jimenez et al. (DOI:10.1142/S1793830917500422) concerns an inequivalent statistic; Vatter's arXiv:2608.22147 abstract concerns unrestricted subsequence counts by length. Searches for repeated-letter complements, deletion-output spectra, and balanced run polynomials did not locate an equivalent theorem. This is not a proof against older unindexed research, and the two secondary sources were only scope-checked from abstracts.

## Value — PASS

The result supplies exact upper bounds for all lengths and every repeated-symbol deletion order, with explicit witnesses and a simultaneous coefficientwise optimality principle. That is a natural, motivated family of a newly studied complement-spectrum invariant; it resolves a genuine special case of the cited open cardinality problem rather than recomputing a known table. The unusual length-seven triple-deletion exception and the eventual closed binomial law illustrate why the optimized run structure matters.

## Limits and supporting literature

The result does not classify every maximizing word, handle nonconstant deleted patterns, or replace a future independent assessment. Relevant sources: arXiv:2603.20790v1 (full relevant text inspected); DOI:10.1142/S1793830917500422 and arXiv:2608.22147 (abstract/scope only). Some earlier equivalent theorem may have escaped the literature searches.

Self-review: passed. Independent audit: not yet performed.
