# The Klein graph inside maximum induced-matchings of the Coxeter graph

## Finding

Let \(\Gamma\) be the cubic Coxeter graph on 28 vertices, and let \(\mathcal M\) be the family of its maximum induced matchings. For \(v\in V(\Gamma)\), write \(S_3(v)=\{x:d_\Gamma(v,x)=3\}\), and let \(F_v\) be the six-edge matching induced by \(S_3(v)\). Then
\[
\nu_s(\Gamma)=7,\qquad
\mathcal M=\bigl\{F_v\cup\{\{v,w\}\}:v\in V(\Gamma),\ w\sim v\bigr\},
\qquad |\mathcal M|=84.
\]
All 84 displayed edge sets are distinct. In particular, the statement is a complete classification of the largest induced matchings, not merely a construction of examples.

For \(k\in\{1,2,\ldots,7\}\), form the exact-exchange graph \(J_k\) on \(\mathcal M\) by connecting different matchings \(M,N\) exactly when \(|M\setminus N|=k\) (equivalently, exactly \(k\) chosen edges are replaced). Then \(J_1\) is the disjoint union of 28 triangles, \(J_2\) and \(J_3\) have no edges, and
\[
\boxed{J_4\cong L(\mathcal K)},
\]
where \(\mathcal K\) is the classical 56-vertex, three-regular Klein graph (Foster-census label `F056B`). This four-replacement graph has 84 vertices, 168 edges, degree four, 56 triangles, and uniform breadth-first distance shells
\[
(1,4,8,16,22,26,7).
\]
It is connected with both radius and diameter six. Every edge lies in exactly one triangle and every vertex lies in exactly two triangles. The triangles and their vertex overlaps recover \(\mathcal K\) as a simple cubic graph.

If replacements of **at most** \(k\) edges are allowed, the sharp connectivity threshold is \(k=4\). The at-most-four exchange graph \(J_1\cup J_4\) is six-regular, connected, has 252 edges, and has uniform distance shells \((1,6,24,45,8)\), so its diameter is four. With at most three replacements only the 28 disconnected triangles remain.

For unordered pairs of distinct optimal matchings, the exact replacement-count histogram is
\[
\#\{|M\setminus N|=k\}=\begin{cases}
84,&k=1,\\
168,&k=4,\\
672,&k=5,\\
1470,&k=6,\\
1092,&k=7,\\
0,&\text{otherwise.}
\end{cases}
\]
The counts sum to \(\binom{84}{2}=3486\).

## Assumptions and scope

All graphs are finite, simple, undirected graphs. An **induced matching** \(M\) is a set of edges for which the induced subgraph on all endpoints of edges in \(M\) has exactly the edges of \(M\). The Coxeter graph here is explicitly defined as follows: take the Fano plane on \(\mathbb Z/7\mathbb Z\), with lines \(\{i,i+1,i+3\}\), and make one vertex for each of its 28 three-element subsets that is not a line. Two such triples are adjacent precisely when they are disjoint. This gives 42 edges, cubic degree and diameter four. A different, independently checkable presentation as three seven-cycles and seven stars is given in `scripts/verify_stars.py`.

The named Klein graph is the **cubic** 56-vertex graph `F056B`, not the 24-vertex seven-regular Klein graph. Its independent adjacency representation is copied from the published SageMath `Klein3RegularGraph` data (credited below). The theorem concerns these fixed graphs and does not claim the same properties for arbitrary cages or cubic graphs.

## Proof

**1. Exact finite strong-matching bound.** Number the Coxeter edges \(0,\ldots,41\). Construct a 42-vertex compatibility graph \(H\) whose vertices are Coxeter edges; distinct \(e,f\) are adjacent in \(H\) exactly if the four endpoints of \(e,f\) are distinct and span only those two graph edges. Then \(k\)-cliques of \(H\) correspond bijectively to induced matchings of size \(k\) in \(\Gamma\). Both supplied checkers construct \(H\) directly from one of the two independent Coxeter presentations. One uses Bron–Kerbosch exhaustive maximal-clique enumeration; the other performs a distinct lexicographic recursion through all candidate seven- and eight-cliques. The first produces the maximal-clique size histogram \((4:84,5:924,6:3710,7:84)\), while the second finds precisely 84 seven-cliques and zero eight-cliques. Absence of an eight-clique rules out every larger clique as well, because any larger clique contains an eight-clique. Thus the maximum is seven and exactly 84 induced matchings attain it. Neither program relies on a heuristic or sampling for this bound.

**2. Intrinsic description of all optima.** The Coxeter graph has the classical distance-regular intersection array \(\{3,2,2,1;1,1,1,2\}\) (Dejter, Introduction). Thus each distance-three sphere has \(3\cdot2\cdot2=12\) vertices, and each of its vertices has exactly \(a_3=3-1-1=1\) neighbour in the same sphere. Consequently the induced subgraph is six disjoint edges \(F_v\). Each program independently also checks this identity by breadth-first search on all 28 vertices. For every one of the three neighbours \(w\) of \(v\), the seven-edge set \(M_{v,w}=F_v\cup\{\{v,w\}\}\) satisfies the pairwise strong-matching test. These 84 labelled constructions are mutually distinct and, as edge-set masks, agree exactly with the independently enumerated 84 seven-cliques. Hence they exhaust all optimal induced matchings. The sphere and equality checks can be replayed line for line in both scripts.

**3. Exchange structure.** Two seven-edge matchings require exactly \(7-|M\cap N|\) replacements. Inspecting all \(\binom{84}{2}\) unordered pairs yields precisely the histogram in the Finding section. The 84 one-exchange edges split into one triangle for each Coxeter center \(v\), namely the three sets \(M_{v,w}\) with \(w\sim v\). There are no edges of exact exchange size two or three. The 168 four-exchange edges are characterized intrinsically: one occurs between the center blocks for \(v,w\) if and only if \(d_\Gamma(v,w)=3\). For such centers, exactly one neighbour \(a\sim v\) has \(d_\Gamma(w,a)=3\), and exactly one neighbour \(b\sim w\) has \(d_\Gamma(v,b)=3\). The edge joins \(M_{v,a}\) to \(M_{w,b}\). The checker establishes both existence and the **equality of the entire labelled edge sets**, not only an edge-count match. The quotient by the 28 one-exchange triangles is therefore exactly the distance-three graph of the Coxeter graph, with one lifted edge above each of its 168 edges.

**4. Recovering the Klein graph.** All triangles of \(J_4\) are exhaustively enumerated. There are 56; each of the 84 vertices lies in two and each of the 168 edges lies in one. Make a graph \(K\) whose vertices are these 56 triangles, joining two triangles if they share an exchange-graph vertex. Every exchange vertex belongs to precisely two triangles, hence defines an edge of \(K\); the unique-triangle property guarantees a simple cubic graph, with \(J_4=L(K)\). To identify the named graph rather than only the isomorphism class of an unnamed cubic graph, `scripts/verify_stars.py` reads an independently recorded sparse6 encoding from the SageMath `Klein3RegularGraph` generator and checks a complete explicit bijection of all 56 vertices, preserving the entire adjacency relation. This is an executable isomorphism certificate, not a guess from equal graph parameters.

**5. Shortest paths and the threshold.** Exact breadth-first search from **each** of the 84 optimum matchings in \(J_4\) gives the same distance shells \((1,4,8,16,22,26,7)\). Repeating with the union \(J_1\cup J_4\) gives \((1,6,24,45,8)\). These enumerations establish connectivity, radius, diameter, and the sharp four-replacement threshold.

## Verification

Run either of the independent, standard-library-only Python 3 checkers in the same directory as this document:

```sh
python3 scripts/verify_fano.py
python3 scripts/verify_stars.py
```

The first must emit `FANO_BRON_KERBOSCH_84_MAXIMA_PASS`, `SPHERE3_CORE_AND_LATERAL_ARC_LIFT_PASS`, and `EXCHANGE_ONE_FOUR_SHELLS_AND_56_CUBIC_PASS`. The second must emit `STARS_7_AND_8_EXACT_CLIQUE_EXHAUSTION_PASS`, `STARS_84_MAXIMA_AND_METRIC_PASS`, and `KLEIN_F056B_SAGE_GRAPH_EXACT_ISOMORPHISM_PASS`. Assertions raise an exception on any contradiction. The complete separate graph constructions, exact clique algorithms, bit-mask representation, all-pairs intersections, breadth-first searches, triangle checks and fixed 56-vertex isomorphism witness are explicit in the files. The computation uses integer and finite set operations, without numerical tolerance, randomization or external packages.

## Relationship to prior work

Dejter (2010) establishes an earlier, quite different construction of the same classical Klein graph from the Coxeter graph by oriented seven-cycle/short-path zipping; this pre-existing Coxeter–Klein connection is **not** claimed as new. Its inspected theorems concern cycle incidences and graph ultrahomogeneity, not maximum induced matchings or their exchange geometry. The present theorem contributes a nontrivial optimum-matching classification and a new **exactly four-edge replacement** representation of the line graph of the Klein graph. Joos, Rautenbach and Sasse (2013) establish strong-matching lower bounds for general subcubic graphs, without obtaining this finite classification or reconfiguration graph. SageMath supplies the independently named Klein graph data, not this induced-matching interpretation.

The distinction between ordinary matchings and induced matchings is essential; counts of perfect matchings, ordinary matching complexes or independent vertex sets in the Coxeter graph do not imply the statements proved here. The originality search found no equivalent induced-matching construction. An unindexed historical description under alternate strong-edge or seven-cycle terminology cannot be excluded.

## Limitations

This is a finite, machine-checkable theorem for the named Coxeter graph only. The scripts give a fully exhaustive finite proof for the extremal and exchange assertions; they do not establish a parameterized family theorem. The literature comparison is a best-knowledge search, not a proof of priority, and an equivalent historical construction could exist. No independent scholarly audit has yet been performed.

## References

1. I. J. Dejter, *From the Coxeter graph to the Klein graph*, public preprint February 9, 2010, https://arxiv.org/abs/1002.1960 .
2. F. Joos, D. Rautenbach, T. Sasse, *Induced Matchings in Subcubic Graphs*, public preprint December 4, 2013, https://arxiv.org/abs/1312.1110 .
3. SageMath named-graph generators, `Klein3RegularGraph`, https://github.com/sagemath/sage/blob/develop/src/sage/graphs/generators/smallgraphs.py .
