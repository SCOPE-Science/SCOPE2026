# The 2,860 optimal decycling sets of the Desargues graph

## Finding

Let \(D\) be the twenty-vertex Desargues graph in its bipartite inclusion presentation: one class consists of all ten two-subsets of \(\{0,1,2,3,4\}\), the other of all ten three-subsets, and a two-subset is adjacent to a three-subset exactly when it is contained in the latter. A *feedback vertex set* (or *decycling set*) is a set \(S\) of vertices such that the induced graph \(D-S\) is a forest.

**Theorem.** The minimum feedback-vertex-set cardinality of \(D\) is \(6\). Among its \(\binom{20}{6}=38,760\) six-vertex subsets, exactly **2,860** are feedback vertex sets. Precisely **760** of these are independent sets whose complements induce forests with two components; the other **2,100** span one edge, and their complements induce trees on fourteen vertices. No other topology occurs at the minimum.

The complete distribution by component orders of \(D-S\) is:

| Component orders | Number of optimal sets |
| --- | ---: |
| \(1,13\) | 360 |
| \(2,12\) | 180 |
| \(3,11\) | 120 |
| \(4,10\) | 20 |
| \(7,7\) | 80 |
| \(14\) (one tree) | 2,100 |

The full automorphism group has order \(240\). Its action on the 2,860 optimal sets has exactly **19 orbits**: two of size \(20\), three of size \(60\), six of size \(120\), and eight of size \(240\). Nine orbits consist of independent decycling sets and ten consist of one-edge decycling sets. The accompanying `orbits.csv` gives one representative, the deleted two-subset count, and the remaining component orders for each orbit.

The main contribution is the exact multiplicity, the two topology classes, and the symmetry classification. The scalar minimum of six is explicitly prior knowledge for generalized Petersen graphs, in particular from Wei--Li (2013) and Gao--Xu--Wang--Zhu--Yang (2015). The contribution claimed here is the complete optimum-set census and symmetry classification.

## Assumptions and scope

All graphs are finite, simple, and undirected. The twenty vertices are numbered \(0,\ldots,9\) by lexicographically ordered two-subsets of \(\{0,1,2,3,4\}\) and \(10,\ldots,19\) by lexicographically ordered three-subsets. The `representative_mask` in `orbits.csv` has bit \(i\) set exactly when vertex \(i\) belongs to the *deleted* set. Orbits are taken under the full graph automorphism group, not merely under one chosen cycle or a drawing subgroup.

## Proof

**1. A sharp lower-bound calculation (not claimed new).** The graph has \(20\) vertices, \(30\) edges, and degree \(3\) at every vertex. If \(S\subseteq V(D)\) has size \(k\), let \(e(S)\) be its number of induced edges, and let \(c\) be the number of components of \(D-S\). The number of edges remaining after deletion is exactly \(30-3k+e(S)\). If \(D-S\) is a forest, its number of edges is also \((20-k)-c\). Therefore

\[
2k=10+e(S)+c.
\]

Any forest on at least one remaining vertex has \(c\ge1\), and \(e(S)\ge0\). Consequently every feedback vertex set with \(k\le19\) has \(k\ge6\); a set deleting all twenty vertices is obviously not smaller. At \(k=6\), necessarily \(e(S)+c=2\), leaving only the alternatives \((e(S),c)=(0,2)\) and \((1,1)\).

**2. Both alternatives are attained.** In the vertex indexing specified above, the set with mask `126`, consisting of the two-subsets \(\{0,2\},\{0,3\},\{0,4\},\{1,2\},\{1,3\},\{1,4\}\), has no induced edges and leaves forest component orders \(4,10\). The set with mask `1244`, consisting of the two-subsets \(\{0,3\},\{0,4\},\{1,2\},\{1,4\},\{2,3\}\) and the three-subset \(\{0,1,2\}\), induces exactly one edge and leaves a fourteen-vertex tree. These are checked directly by the adjacency definition and by the complete finite certificate. Thus the minimum is exactly six.

**3. Exact enumeration is a finite proof, not extrapolation.** File `verify.py` enumerates every tuple of six distinct vertex indices in increasing order, hence all \(\binom{20}{6}=38,760\) candidate subsets without repetition. It constructs the full graph from two-versus-three-subset inclusion, computes connected components of the complement by breadth-first search, and tests acyclicity by the exact equality between edge number and vertex number minus component number. It also constructs the independently defined generalized Petersen graph \(GP(10,3)\), checks a displayed twenty-vertex isomorphism, and checks each of the same 38,760 candidates by a disjoint-set-union cycle test in that second representation. Both methods agree on every candidate, with precisely 760 and 2,100 in the two cases. Grouping the complete positive list by component orders produces the displayed table. File `verify_gp.cpp` independently enumerates all \(\sum_{j=0}^{6}\binom{20}{j}=60,460\) deletions of size at most six in \(GP(10,3)\), testing cycles by disjoint-set union. It finds no smaller solution and the same two six-vertex counts.

**4. Completeness of the symmetry quotient.** Every permutation of the underlying five symbols induces an automorphism on both subset levels, and subset complementation swaps the levels and preserves inclusion adjacency. These yield \(120\cdot2=240\) distinct automorphisms. Conversely, the common-neighbor graph of the two-subset level is the triangular graph \(T(5)\), in which two two-subsets are adjacent exactly when they meet. Its five maximum four-cliques are the families of two-subsets containing one fixed symbol; an automorphism permutes these five cliques and is therefore determined by a permutation of the symbols. A side-preserving automorphism has at most \(120\) possibilities, as each three-subset is uniquely determined by its neighborhood of three two-subsets. A side-interchanging automorphism is a side-preserving one followed by complementation. Thus the full group has order \(240\).

The certificate generates all 240 operations, verifies that each preserves adjacency, and applies each to every discovered orbit representative. The resulting disjoint orbits cover all 2,860 valid sets and have the size multiset stated in the theorem; `orbits.csv` records canonical representatives in the fixed vertex indexing. Their sizes sum to \(2(20)+3(60)+6(120)+8(240)=2,860\), certifying the claimed complete partition.

## Verification

The proof of the lower bound and of the full group size is mathematical and independent of the enumerators. The remaining finite classification is supported by explicitly bounded complete enumeration, two different graph constructions, two distinct exact cycle predicates, and a separate compiled verifier. Execute `python3 verify.py` with Python 3, or compile `verify_gp.cpp` using `c++ -O2 -std=c++17 verify_gp.cpp -o verify_gp` and execute `./verify_gp`. No external Python modules or data downloads are required. The 19-row `orbits.csv` can be regenerated from the `ORBIT_CSV_BEGIN` to `ORBIT_CSV_END` section of the Python verifier's output.

## Relationship to prior work

Wei and Li (2013) studied the decycling number of generalized Petersen graphs and explicitly reported its sharp cubic bound; for \(GP(10,3)\), their scalar result yields \(6\). Gao, Xu, Wang, Zhu and Yang (2015) also treated the generalized-Petersen decycling number. Accordingly **neither the size-six result nor its construction is claimed as new**. Yang and Ren (2019) proved general regular-graph decycling identities; the equality \(2k=10+e(S)+c\) used above is a direct cubic specialization and is likewise not claimed to originate here. The available descriptions of those sources concern the minimum number, not the number of all minimizers. Their relevant complete texts were not accessible in this review, which leaves an explicit residual priority risk for any hidden exhaustive table or classification.

Kelly and Liu studied maximum induced forests in connected subcubic graphs of prescribed girth (first public arXiv version, 12 March 2016). Their graph-wide lower bounds concern the cardinality of a maximum induced forest; they do not enumerate Desargues optimal sets or quotient them by automorphisms. Hertz investigated algorithms for decycling bipartite graphs, with numerical tables for star graphs, bubble-sort graphs, Fibonacci cubes, and hypercubes, not a Desargues classification. Ghalavand and Li treated balanced bipartite graphs under minimum-degree conditions and other graph constructions. Their dense-degree hypothesis \(\delta(B)\ge n/2+1\) for \(2n\) vertices does not apply to the degree-three Desargues graph with \(n=10\).

The Desargues graph is standardly also denoted \(GP(10,3)\) or the bipartite Kneser graph \(H(5,2)\); all of these equivalent formulations were considered during prior-work comparison. The new statement is the complete **2,860-set / nineteen-orbit classification**, not an unqualified novelty claim for the scalar minimum.

## Limitations

This is an exact result for one specified twenty-vertex graph. It does not give the full induced-forest polynomial, extend automatically to other generalized Petersen graphs, or establish publication priority against unpublished or unindexed enumerations. The listed general-purpose primary articles with accessible full text were checked for the named graph, equivalent representations, and potentially dominating statements. The directly titled generalized-Petersen decycling papers of 2013 and 2015 could be read only at abstract/metadata level, so a duplicate optimum-set classification within them cannot be ruled out without full-text access; their reported scalar minimum is already credited. The 2019 regular-graph identity was also reported in its indexed scientific abstract. Lack of a found match is not proof of novelty. Verification here is self-review only; independent audit has not been performed.

## References

1. E. Wei and Y. Li, *Decycling Number and Upper-Embeddibility of Generalized Petersen Graphs*, *Acta Mathematica Sinica, Chinese Series* **56** (2013), 211–216, first published 2013-03-15. https://doi.org/10.12386/A2013sxxb0022
2. L. Gao, X. Xu, J. Wang, D. Zhu and Y. Yang, *The decycling number of generalized Petersen graphs*, *Discrete Applied Mathematics* **181** (2015), 297–300. https://doi.org/10.1016/j.dam.2014.09.005
3. C. Yang and H. Ren, *New Formulae for the Decycling Number of Graphs*, *Discussiones Mathematicae Graph Theory* **39** (2019), 125–141, published online 2018-11-22. https://doi.org/10.7151/dmgt.2064
4. T. Kelly and C.-H. Liu, *Size of the Largest Induced Forest in Subcubic Graphs of Girth at least Four and Five*, arXiv:1603.03855 (first version 2016-03-12); *Journal of Graph Theory* **89** (2018), 457–478. https://arxiv.org/abs/1603.03855
5. A. Hertz, *Decycling Bipartite Graphs*, *Journal of Graph Algorithms and Applications* **25** (2021), 461–480. https://doi.org/10.7155/jgaa.00567
6. A. Ghalavand and X. Li, *On Maximum Induced Forests of the Balanced Bipartite Graphs*, arXiv:2501.05145 (first version 2025-01-09). https://arxiv.org/abs/2501.05145
7. E. W. Weisstein, *Desargues Graph*, MathWorld (graph constructions and standard identities). https://mathworld.wolfram.com/DesarguesGraph.html
