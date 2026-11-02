# Review of upper-dominating-set rigidity in open ladders

## Correctness — PASS

The proof reconstructs the private-neighbor injection behind the upper bound \(\Gamma(L_n)\le n\), with no unproved finite-to-infinite extrapolation. Equality forces the number of full and empty columns to coincide. Distinct private neighbors of the selected full-column vertices occupy every vertex of every empty column. Those boundary obligations separate singleton and full/empty regimes; in the singleton regime the selected rows are period-two, and in the full/empty regime unlike-adjacency edges form the unique perfect matching of the column path. Both directions of the classification are verified. Direct graph-definition enumeration for lengths \(2\) through \(10\) found exactly the claimed extremal sets; separate all-subset enumeration recovers known totals through length \(9\). Risks: only labelled ordinary open ladders are covered, and finite tests do not replace the general argument.

## Originality — PASS, qualified

Sahbi (arXiv:2610.03785, full accessible text, Theorem 3.1) already establishes the upper domination **number** for all rectangular grids. Goddard and Henning's matching bound provides the upper inequality more generally. Neither accessible statement classifies maximizers. OEIS A290379 records the same ladder family's numbers of *all* minimal dominating sets, but not counts conditioned on the maximum size or the word classification. Semantic searches of published mathematical results, including alias and parity-pattern formulations, returned adjacent variants (chain-graph perfect domination and ladder homology), not a covering maximum minimal-domination result. The general matching article's full text was not retrieved, and hidden broader equality classifications remain a residual priority risk. No novelty inference rests solely on unsuccessful search.

## Value — PASS

This is a natural complete equality classification motivated by the 2026 exact upper-domination number for grids. The result supplies the extremal coefficient (four or six) and distinguishes independent checkerboards from additional non-independent maximum sets, showing a genuine parity-sensitive structural effect invisible to the known numerical parameter. It is an infinite structural statement, not an isolated small example or relabelling of the bipartite bound.

## Limitations and closest literature

The theorem applies only to labelled two-row *open* ladders. It is not a complete minimal-domination polynomial and does not address wider or cylindrical grids. Sources: Sahbi, arXiv:2610.03785 (2026); Goddard–Henning (2025), doi:10.1007/s00010-025-01196-z; OEIS A290379 (scalar ladder counts, 2017). Historical priority and the proof have not been independently assessed.

Self-review: passed. Independent audit: not yet performed.
