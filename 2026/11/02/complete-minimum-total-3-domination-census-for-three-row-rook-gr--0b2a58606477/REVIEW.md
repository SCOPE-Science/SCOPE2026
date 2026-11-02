# Scientific review: total-three-domination multiplicities on three-row rook graphs

## Correctness — PASS

The graph is the simple Cartesian product \(K_3\square K_n\), \(n\ge2\), and the condition counts three distinct *open* neighbors in the chosen set at **every** vertex (including selected vertices). If \(r_i\) and \(c_j\) denote selected row and column totals and \(x_{ij}\) denotes membership, the selected-neighbor count is exactly \(r_i+c_j-2x_{ij}\), not \(r_i+c_j-x_{ij}\). Consequently feasibility is equivalent to checking this count against 3 for every cell. A row of size two forces its two selected columns to be full and forbids empty columns. These facts imply minima 6, 8, 8 and 9 for the stated ranges. An eight-element optimum has two full columns plus either one double column or two same-row singleton columns. A nine-element optimum either contains a size-two row (possible only at five columns, with two full and three same-row singles) or has row totals all three; the latter forces exactly three full columns or one full and three doubles missing the three different rows. These alternatives cover all row/column profiles, prove sufficiency and disjointness, and give the exact labeled counts.

An independent checker constructs vertex adjacencies from scratch and exhaustively enumerates all subsets of weight at most the proposed optimum for \(2\le n\le7\). It independently counts frequency vectors of column types for \(8\le n\le12\), multiplied by exact multinomial placement weights. The recorded output was `VERIFY_OK: 6 exhaustive graphs, 5 independent column-multiset counts`. Computational checks are finite evidence, not a substitute for the quantified proof.

## Originality — PASS, with publication-priority risk

Bermudo, Sánchez and Sigarreta, *Total k-domination in Cartesian product graphs*, DOI `10.1007/s10998-017-0191-2` (2017), explicitly imply the *number* \(\gamma_{3t}(K_3\square K_n)=9\) for \(n\ge5\). That numeric stabilization is attributed, not offered as a new result. Their inspected Theorem 3.1 and Proposition 3.2 do not give the classification or the labeled counts. Carballosa and Wisby, *Total k-domination in Cartesian product of complete graphs*, `arXiv:2001.07850` (2020), give product bounds and square-parameter results, but not the full three-row optimum-count classification. Other chessboard-graph literature addresses different adjacencies. Six semantic database queries for exact total-three-domination and rook graphs yielded no equivalent count theorem. Other compared mathematical claim statements do not supply an equivalent or a stronger statement subsuming the enumeration. Prior-database absence alone does not prove global novelty, and unindexed enumerations remain a risk.

## Mathematical value — PASS

A minimum size alone does not identify the space of extremizers. The proof gives all minimum subsets of a canonical family of line graphs \(L(K_{3,n})\), with labeled optimum multiplicities growing as an explicit quartic polynomial after a sharp five-column exceptional pattern. The distinctions among full-column, double-column and singleton-column configurations are motivated by the exact open-neighborhood inequalities. The enumerator is also the first nonzero coefficient of the total-three-domination activation polynomial and can support reliability sampling of minimum configurations. It is a complete infinite-family classification, not an arbitrary finite case or trivial normalization of a known scalar minimum.

## Closest literature and boundaries

- S. Bermudo, J. L. Sánchez and J. M. Sigarreta, *Total k-domination in Cartesian product graphs*, Periodica Mathematica Hungarica 75 (2017), 255–267, DOI `10.1007/s10998-017-0191-2`: known scalar minimum in the range \(n\ge5\).
- W. Carballosa and J. Wisby, *Total k-domination in Cartesian product of complete graphs*, `arXiv:2001.07850` (originally 2020-01-22): relevant general product bounds, without extremal multiplicities for this family.
- P. A. Burchett, *k-domination and k-tuple total domination for some chessboard graphs*, Utilitas Mathematica 124 (2025), 53–81, DOI `10.61091/um124-04`: queen/bishop/king/knight moves rather than rook-only products.

No classification for other thresholds or other clique widths is claimed. An independent mathematical audit and independent publication-priority verification remain unperformed.

Self-review: passed. Independent audit: not yet performed.
