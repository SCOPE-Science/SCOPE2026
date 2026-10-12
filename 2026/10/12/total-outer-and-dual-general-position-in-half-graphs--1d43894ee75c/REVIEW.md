# Review of Total, outer, and dual general position in half graphs

## Correctness
PASS. The only simplicial vertices are \(a_n\) and \(b_1\), so the total statement follows from the published characterization. The mutually maximally distant pairs are exactly the distance-\(3\) cross nonedges \(\{a_i,b_j\}\) with \(j<i\); all same-side and adjacent cross pairs have an explicit neighbor farther from the opposite endpoint. This gives the entire strong resolving graph and the outer result. For dual general position, every set of size at least three is first forced to be independent, and convexity witnesses then restrict selected vertices to \(a_n\) and \(b_1\). A complete case split excludes every other two-vertex set. The direct-definition checker exhausts \(21{,}760\) subsets for \(4\le n\le7\) and matches every maximum family.

## Originality
PASS. The 2024 introducing paper was inspected in full searchable text: it proves the three general characterizations but has no half-graph or chain-graph occurrence. A 2025 full-text paper uses half graphs for mobile ordinary general position and states the ordinary value, but not the total, outer, or dual variants. Exact web searches and semantic published-result searches under half-graph, chain-graph, strong-resolving, convex-complement, and variant terminology found no equivalent theorem. A recent strong-metric chain-graph result is a genuine nearby comparison, but its stated strong-metric dimension and basis classification optimize vertex covers of the strong resolving graph rather than the clique structure needed for outer general position.

## Value
PASS. The three variants were introduced precisely to separate different shortest-path visibility requirements. Half graphs are a canonical ordered bipartite family already used in later general-position research. Here all three new scalar invariants collapse to \(2\), while their extremal geometry sharply diverges: total and dual have one forced leaf pair, whereas outer general position has all \(\binom n2\) diametral cross nonedges. The complete strong-resolving-graph description and the unique dual optimum make the result structural rather than a routine scalar evaluation.

Self-review: passed. Independent audit: not yet performed.
