# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

Let \(q\) be the number of non-singleton parts and \(s\) the number of singleton parts. The upper bound is given by one unit-spoke star coordinate for every non-singleton part: vertices of that part go to distinct leaves and all other vertices go to the center. These coordinates realize all distance-two pairs and all cross-part distances except distances between two singleton vertices. When \(s\ge2\), one additional half-unit-spoke star realizes exactly those missing singleton-singleton distances.

For the lower bound, choose one pair at distance \(2\) in each non-singleton part. If a single tree coordinate realized two such pairs, then their within-pair four-point sum would be \(4\) while both cross sums would be at most \(2\), contradicting the tree four-point condition. Hence at least \(q\) coordinates are necessary.

When \(s\ge2\), equality with only \(q\) coordinates is impossible. Each coordinate must realize one of the selected distance-two pairs. Every vertex outside that pair's multipartite part is at graph distance \(1\) from both endpoints, so its coordinate image must be the unique midpoint of the length-two geodesic. Thus two singleton vertices collapse in every coordinate, contradicting their graph distance \(1\). The edge cases \(q=0\), stars, complete graphs, and \(K_4-e\) are covered separately by the same argument.

The formula agrees with the directly relevant known values: complete bipartite graphs with both parts non-singleton have rank \(2\), complete graphs and stars have rank \(1\), \(K_4-e\) has rank \(2\), and complete graphs minus perfect matchings have rank \(n/2\).

## Originality

The September 2026 paper *The phylogenetic rank of a graph* was inspected in full at its definition, Section 3 examples, four-point lower-bound method, and open questions. It proves the complete-bipartite value in Proposition 3.5 and separately treats complete graphs minus perfect matchings in Theorem 3.3(2), but does not state the arbitrary complete-multipartite formula. The full text has no occurrence of “multipartite”. Question 7.3 asks for structural characterizations of graphs with phylogenetic rank at most \(k\ge2\).

The earlier Speyer--Sturmfels exposition was checked at the research problem defining phylogenetic rank as a pointwise maximum of tree metrics. Exact and synonymous searches using “complete multipartite”, “partition metric”, “two-distance metric”, “product of metric trees”, “mixture of tree metrics”, “tree rank”, and “phylogenetic rank” did not locate the formula or an equivalent complete-multipartite classification.

Cartwright--Chan (2010) was examined because it contains a graph-cover characterization for a notion also called tree rank. That paper explicitly states that its tree-rank convention differs from the Pachter--Sturmfels mixture notion; its Proposition 13 therefore does not provide prior coverage of the present theorem.

Originality is assessed as PASS to the best of our knowledge, not as certainty. No inaccessible source was identified as concrete evidence of prior coverage. The main residual risk is an older or poorly indexed result in metric-embedding or tropical-mixture terminology, or very recent parallel work following the new graph-phylogenetic-rank paper.

## Value

The theorem gives an exact formula on a basic infinite graph family and unifies several examples that the source paper treats separately. It shows that all non-singleton multipartite parts impose mutually incompatible distance-two obligations, while singleton parts create exactly one additional global obstruction. The formula depends only on the singleton/non-singleton pattern, not the actual non-singleton part sizes.

It also gives a complete bounded-rank characterization inside the complete multipartite family:
\[
r_{\mathrm{phy}}(G)\le k
\quad\Longleftrightarrow\quad
q+\mathbf 1_{\{s\ge2\}}\le k,
\]
which is a concrete structural special case of the source paper's Question 7.3.

## Limitations

The theorem is specific to connected complete multipartite graph metrics. It does not solve the general bounded-rank characterization problem or the extremal problem for arbitrary \(n\)-vertex graphs. Originality is to the best of our knowledge, with residual risk from differently named older metric-decomposition results and very recent parallel work.
