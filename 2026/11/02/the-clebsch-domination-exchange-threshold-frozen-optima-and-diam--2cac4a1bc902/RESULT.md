# The Clebsch domination-exchange threshold: frozen optima and diameter-five mobility

## Finding
Let \(C\) be the five-regular Clebsch graph (the folded five-cube), with vertices \(\mathbb F_2^4\) and edges \(\{x,x+d\}\) for \(d\in\{1,2,4,8,15\}\), where the integers denote four-bit vectors and addition is bitwise XOR. For \(k\in\{4,5\}\), define \(J_k(C)\) to have all dominating \(k\)-vertex subsets as vertices; two such subsets are adjacent if one selected vertex is replaced by one unselected vertex. There is no adjacency restriction on the removed and inserted vertices.

The domination number is \(\gamma(C)=4\). Exactly \(80\) minimum dominating sets exist: \(40\) induce an empty four-vertex graph and \(40\) induce a four-cycle. Their jump graph is \(J_4(C)=80K_1\).

At precisely one additional selected vertex, \(J_5(C)\) has \(1056\) vertices, \(10320\) edges, and one connected component. It is self-centered, with radius and diameter both \(5\). Exactly \(960\) states have jump degree \(19\) and \(96\) states have jump degree \(25\). Their exact distance-shell profiles, from distance zero through five, are respectively
\[
(1,19,94,316,507,119)\quad\text{and}\quad(1,25,130,250,570,80).
\]

Under the full automorphism group of order \(1920\), the dominating five-sets form exactly five orbits. Their sizes are \(16,80,160,320,480\); in that order their induced-subgraph types are \(5K_1\), \(K_{1,4}\), \(K_{1,3}\sqcup K_1\), \(K_2\sqcup3K_1\), and a four-cycle with one pendant vertex. The first two orbits have jump degree \(25\), and the other three have jump degree \(19\). The two four-set orbits each have size \(40\).

## Assumptions and scope
All graphs are finite, simple, and undirected. The five-regular graph, rather than its ten-regular complement (also occasionally called the Clebsch graph), is intended. Its vertex set is the sixteen integers from \(0\) through \(15\), interpreted as four-bit vectors. The five allowed nonzero differences are \(1,2,4,8,15\). A subset \(A\) dominates if every vertex belongs to \(A\) or is adjacent to a vertex of \(A\). The fixed-cardinality jump rule keeps domination true after every replacement and does not allow a temporary larger set.

The theorem concerns exactly \(k=4\) and \(k=5\), and makes no dimension-uniform assertion. It is not about token sliding, connected domination, minimum edge-metric bases, or token addition/removal under a size cap.

## Proof
For \(v\in V(C)\), let \(N[v]\) be the closed neighborhood. The graph is strongly regular with parameters \((16,5,0,2)\), as follows directly by enumerating the five XOR differences. Thus every closed neighborhood has six elements, and \(|N[u]\cap N[v]|=2\) for every distinct pair \(u,v\), whether adjacent or nonadjacent. For any three distinct vertices, inclusion-exclusion gives
\[
|N[u]\cup N[v]\cup N[w]|=3\cdot6-3\cdot2+|N[u]\cap N[v]\cap N[w]|\le14.
\]
No triple dominates. The four-set \(\{0,1,2,3\}\) dominates, so \(\gamma(C)=4\).

For exact equality cases and their exchanges, the following is a finite exhaustive proof on a completely specified universe. Encode a vertex set \(A\) by the sixteen-bit mask \(m(A)=\sum_{a\in A}2^a\), and set \(b_v=\sum_{w\in N[v]}2^w\). A mask dominates exactly when \((m\mathbin{\&}b_v)\ne0\) for every \(v\in\{0,\ldots,15\}\). For cardinalities four and five, examine all \(\binom{16}{4}=1820\) and \(\binom{16}{5}=4368\) masks. The two bundled independent implementations enumerate this entire finite universe by different loops and graph representations. They find \(80\) dominating four-masks and \(1056\) dominating five-masks. Testing degrees inside the induced subgraph yields precisely the two four-set types and five five-set types listed above; their multiplicities sum to the respective exhaustive totals.

For fixed cardinality, the complete neighborhood of a valid mask \(m\) consists of the valid masks \(m\mathbin{\mathrm{xor}}2^a\mathbin{\mathrm{xor}}2^b\) over all \(a\in A\), \(b\notin A\). There are no other single-replacement neighbors. This explicit test finds zero neighbors at cardinality four. At cardinality five it returns \(10320\) undirected edges and the asserted two degree classes. For every one of the \(1056\) five-masks, a breadth-first search traverses all \(1056\) masks and gives the corresponding stated distance-shell profile, with no distance greater than five and a positive number at distance five. This proves connectivity and radius and diameter five without extrapolation.

For the symmetry assertion, translations act transitively on the sixteen vertices. Any permutation of the five generating differences extends to a linear automorphism because their XOR is zero and any four are independent; this gives \(16\cdot5!=1920\) automorphisms. Conversely, after fixing the zero vertex, an automorphism permutes its five neighbors. Each of the remaining ten vertices is uniquely determined by its unordered pair of neighbors among those five: in the \((16,5,0,2)\) graph it is the other common neighbor of that pair besides zero. The point stabilizer therefore injects into \(S_5\). Hence the group above is the full automorphism group. Applying its explicitly enumerated actions to the complete list of dominating sets gives two four-set orbits of size \(40\) and five five-set orbits of sizes \(16,80,160,320,480\). The induced types distinguish the five orbits, so no finer or coarser classification is concealed.

## Verification
Run `python3 verify.py` with Python 3.8 or later. It enumerates all relevant subsets, regenerates the entire jump graph, computes all-pairs distances, and enumerates the \(1920\) affine automorphisms and their subset orbits. It finishes with `ALL_VERIFY_OK` on success.

As an independent implementation, run `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt && ./verify_alt`. This second program constructs the same graph by folding the five-dimensional cube onto its sixteen even-weight binary words, builds all subset candidates by scanning every one of the \(2^{16}\) masks, and recomputes jump edges and distances. It finishes with `INDEPENDENT_VERIFY_OK` on success. Both sources are included in the present package and use no third-party libraries.

## Relationship to prior work
The literature establishes the concepts of dominating-set reconfiguration and jump-\(\gamma\) graphs. Suzuki, Mouawad and Nishimura study the addition/removal graph of dominating sets with an upper size cap. Their theorems do not compute the fixed-cardinality jump graph of the Clebsch graph. Mynhardt and Nasserasr survey jump-\(\gamma\) graphs and related models, but do not supply this graph-specific threshold or distance and orbit classifications.

The Clebsch graph and its folded-cube identification and strong regularity are classical. The OEIS folded-cube independence polynomial already records the counts \(120\) independent four-sets and \(16\) independent five-sets; those counts are not asserted as new. The exact relationship of all dominating sets to one-vertex replacement, particularly the sharp cardinality-four to cardinality-five connectivity transition, is the focus here.

## Limitations
This is a finite exact theorem about the sixteen-vertex folded five-cube. The computation is complete, but it is not a general formula for folded cubes of arbitrary dimension. Some ingredients, including the graph's automorphism group and the independent-set polynomial, are established background. Searches and full-text comparisons cannot exclude an equivalent classification in unindexed literature; independent scholarly audit and priority verification have not been performed.

## References
1. A. Suzuki, A. E. Mouawad, and N. Nishimura, *Reconfiguration of Dominating Sets*, arXiv:1401.5714v1, first publicly posted 2014-01-22; https://arxiv.org/abs/1401.5714.
2. C. M. Mynhardt and S. Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey*, arXiv:2003.05956v1, first publicly posted 2020-03-12; https://arxiv.org/abs/2003.05956.
3. R. Haas and K. Seyffarth, *The k-Dominating Graph*, Graphs and Combinatorics 30 (2014), 609–617; institutional accepted-manuscript listing https://scholarworks.smith.edu/mth_facpubs/3/.
4. OEIS A355227, independent-set enumerator of folded cubes, https://oeis.org/A355227; originally submitted 2022-06-24.
5. E. W. Weisstein, *Clebsch Graph*, MathWorld, https://mathworld.wolfram.com/ClebschGraph.html (graph nomenclature, strongly regular parameters, classical references).
