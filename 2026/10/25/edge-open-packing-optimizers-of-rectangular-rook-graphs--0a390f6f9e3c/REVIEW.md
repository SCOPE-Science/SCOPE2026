# Scientific review: maximum edge-open packings of rook graphs

## Correctness (PASS)

The local forbidden-third-edge condition forces an exact decomposition into mutually row- and column-disjoint horizontal edges, vertical edges, and two-edge bends. If there are \(\ell\) bends, \(h\) horizontal singles and \(v\) vertical singles, their selected-edge, row, and column counts are \(2\ell+h+v\), \(2\ell+h+2v\), and \(2\ell+2h+v\). These equations prove the general bound, the odd-square exclusion, and the exhaustive equality cases. Block partitions, labeled column assignments, and the four choices of bend center yield the stated factorial counts without overcounting. The exact-adjacency verifier reproduces both formulas on twelve finite boards; that computation is corroboration, not an infinite proof.

## Originality (PASS, subject to stated bibliographic risks)

The closest directly applicable paper is Brešar–Dravec–Hedžet–Samadi, *Induced matching vs edge open packing: trees and product graphs* (arXiv:2406.04020, Section 5). Its Corollary 5.3 gives only a general Cartesian-product lower bound; on two cliques this is one, whereas the claimed answer is essentially the smaller clique's order. The 2024 Brešar–Samadi bounds paper and the 2025 Pandey–Santra characterization paper were inspected at their relevant sections: neither contains the exact labeled rook-board optimum, exhaustive optimizer types, or factorial counts. The introductory 2022 source supplies the definition, not a reported rook-graph theorem. Searches for rook graphs, line graphs of complete bipartite graphs, complete-graph Cartesian products, induced-star packings, parity exceptions, and factorial enumerations did not identify a covering result. This does not exclude an unindexed result or a later full-text version containing such a theorem.

## Value (PASS)

The theorem gives a complete solution to a natural product-family packing problem, including all maximizing sets and their multiplicities, rather than merely an isolated value. The odd-square parity obstruction is sharp, the counting formulas exhibit a different asymptotic regime with growing aspect ratio, and the exact result demonstrates arbitrarily large slack in a general product lower bound when both factors are cliques. The graph family is canonical: these rook graphs are precisely line graphs of complete bipartite graphs.

## Scope and residual risk

The result concerns maximum (not every inclusion-maximal) edge-open packings of two-factor rook graphs, with both dimensions at least two. The finite verifier does not certify the universal argument. Possible unindexed prior formulas and the most recent journal-version wording are bibliographic risks; independent validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
