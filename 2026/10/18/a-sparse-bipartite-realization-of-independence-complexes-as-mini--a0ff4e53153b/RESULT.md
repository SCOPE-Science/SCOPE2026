# A sparse bipartite realization of independence complexes as minimum-domination reconfiguration graphs

## Finding

For every finite simple graph \(F=(V,E)\) with \(n=|V|\ge1\), define \(B(F)\) as follows. Subdivide each edge \(uv\in E\) exactly once, introducing \(w_{uv}\); then attach to every original vertex \(v\in V\) one new private pendant vertex \(\ell_v\). Thus \(B(F)\) has \(2n+|E|\) vertices and \(2|E|+n\) edges. Write \(\mathcal I(F)\) for the family of independent vertex sets, and \(I_F(t)=\sum_{I\in\mathcal I(F)}t^{|I|}\) for its independence polynomial.

**Theorem.** The domination number of \(B(F)\) is \(n\), and **all** minimum dominating sets, without exceptions, are
\[
D(I)=\{\ell_v:v\in I\}\cup\{v:v\notin I\},\qquad I\in\mathcal I(F).
\]
Consequently, if \(L=\{\ell_v:v\in V\}\) is the private-leaf set, the marked minimum-domination polynomial is
\[
\sum_{\substack{D\text{ dominating in }B(F)\\ |D|=\gamma(B(F))}} t^{|D\cap L|}=I_F(t).
\]
In particular, the number of minimum dominating sets is \(I_F(1)\).

Let \(R(B(F))\) be the **token-slide minimum-domination reconfiguration graph**: its vertices are all minimum dominating sets and two are adjacent exactly when one is obtained from the other by exchanging one selected vertex for an adjacent unselected vertex. Then both this graph and the corresponding unrestricted single-vertex-exchange graph are canonically isomorphic to the graph with vertex set \(\mathcal I(F)\) and edges \(I\sim J\) if \(|I\triangle J|=1\). Thus \(R(B(F))\) is the **simplex graph of the complement** \(\overline F\). It is a median graph with exact shortest-path distance
\[
d_{R(B(F))}(D(I),D(J))=|I\triangle J|.
\]
If \(c_k(R)\) counts induced subgraphs isomorphic to the \(k\)-dimensional hypercube (with \(c_0\) the number of vertices), then the full cube polynomial obeys
\[
\boxed{\displaystyle \sum_{k\ge0}c_k(R(B(F)))q^k=I_F(1+q).}
\]
Hence the independence polynomial of **any** finite simple source graph is recoverable from the complete cube-count profile of the minimum-domination reconfiguration graph of a **bipartite** graph with \(2n+|E|\) vertices.

Moreover, \(B(F)\) has maximum degree \(\max\{\Delta(F)+1,2\}\) when \(E\ne\varnothing\), and girth at least six. It preserves planarity, and it is connected exactly when \(F\) is connected. Using the known \(\#P\)-completeness of independent-set counting on 3-regular graphs, counting minimum dominating sets is \(\#P\)-hard even on the explicit family of bipartite graphs of maximum degree four and girth at least six formed from 3-regular source graphs. This hardness statement concerns the specified family and does not assert that an arbitrary graph comes with a polynomial-time certificate of its domination number.

## Assumptions and scope

All graphs are finite, simple, undirected and labelled. The source graph \(F\) may be disconnected or have isolated vertices. A dominating set \(D\) meets the closed neighborhood of every vertex. \(\gamma(G)\) is the least size of a dominating set, and a minimum dominating set is one of size \(\gamma(G)\). An independent set is a set containing no adjacent pair, including the empty set. A token slide exchanges \(x\in D\) for \(y\notin D\) along an edge \(xy\) while preserving minimum domination. The complement \(\overline F\) has the same vertex set as \(F\), with precisely the nonedges of \(F\) as its edges. Its simplex graph includes the empty clique as a vertex. A hypercube \(Q_k\) means the usual graph on \(\{0,1\}^k\) with edges at Hamming distance one; every \(k\)-cube count is an unlabeled *vertex-induced* copy, not a quotient by automorphisms.

## Proof

**1. Domination bound and rigidity.** The pairs \(P_v=\{v,\ell_v\}\), for \(v\in V\), are pairwise disjoint. Since \(\ell_v\) has only \(v\) as a neighbor, each dominating set must contain at least one vertex of \(P_v\). Hence its size is at least \(n\). All original vertices form a dominating set: they dominate themselves, every private leaf and both ends of each subdivided edge. Thus \(\gamma(B(F))=n\). Equality forces exactly one vertex of every pair \(P_v\), and no subdivision vertex.

**2. Exact classification.** A set with exactly one vertex from each \(P_v\) already dominates all original and pendant vertices. The subdivision vertex \(w_{uv}\) has neighborhood exactly \(\{u,v\}\), so it is dominated if and only if at least one of \(u,v\) is the chosen representative of its pair. Equivalently, it is forbidden that both \(\ell_u,\ell_v\) are chosen. Thus \(I=\{v:\ell_v\in D\}\) must and need only be independent in \(F\). This proves the bijection and the marked generating-function identity, including isolated vertices and disconnected inputs.

**3. Exact reconfiguration geometry.** Under this bijection, changing one minimum dominating set into another by one selected/unselected exchange must flip the representative of **one and the same** pair: otherwise one pair would become empty and another double-occupied. The flipped vertices are \(v\) and \(\ell_v\), which are adjacent, so every admissible single exchange is also a token slide. Such a flip changes \(I\) by adding or removing one vertex and is admissible precisely when the resulting set is independent. Therefore both reconfiguration graphs equal the induced hypercube on characteristic vectors of independent sets, equivalently the simplex graph of \(\overline F\).

Any path changes at most one coordinate per step, so it has length at least \(|I\triangle J|\). Conversely remove each vertex of \(I\setminus J\), arriving at \(I\cap J\), then insert the vertices of \(J\setminus I\); every intermediate set is a subset of \(I\) or \(J\) and hence independent. This path has exactly \(|I\triangle J|\) steps. The graph is therefore isometric in a hypercube. For any three independent sets, their coordinatewise-majority set is independent: if both endpoints of a source edge were in the majority, some one of the three sets would contain both (two subsets of a three-element index set, each of size at least two, intersect). The majority is the unique Hamming median of those three vectors, hence also their unique reconfiguration-graph median.

**4. Cube polynomial.** Every embedded \(k\)-cube inside a hypercube \(\{0,1\}^n\) is a coordinate face: every square has opposite edges in the same coordinate direction, so the connected parallel-edge classes of an abstract \(Q_k\) force \(k\) distinct constant coordinate directions. This applies to every induced \(k\)-cube in the reconfiguration graph because it sits in that ambient hypercube. Such a face has a unique maximum characteristic vector \(I\) under coordinate inclusion and a unique set \(J\subseteq I\) of \(k\) freely toggled coordinates. All its \(2^k\) vertices are independent exactly when \(I\) is independent. Thus for every independent set \(I\) there are precisely \(\binom{|I|}{k}\) cubes whose coordinatewise top is \(I\), giving
\[
c_k(R(B(F)))=\sum_{I\in\mathcal I(F)}\binom{|I|}{k}.
\]
Summing in \(k\) and applying the binomial theorem yields \(\sum_k c_kq^k=\sum_I(1+q)^{|I|}=I_F(1+q)\).

**5. Restrictions and counting complexity.** Original vertices have degree \(\deg_F(v)+1\), subdivision vertices have degree two and pendant vertices degree one. All edges run between the original-vertex class and the subdivision/pendant class; hence \(B(F)\) is bipartite. Subdivision doubles the length of every cycle of \(F\), and leaves create no cycles. A simple source graph has no cycles shorter than three, so the girth is at least six. Edge subdivision and leaf attachment preserve planarity and connectedness components. Finally the polynomial-time map \(F\mapsto B(F)\) preserves the independent-set count **exactly**, without multiplicative correction. Greenhill's theorem proves \(\#P\)-completeness for independent-set counting in 3-regular graphs; for those inputs, \(B(F)\) is bipartite with maximum degree four and girth at least six. The displayed counting-hardness consequence follows by a parsimonious reduction.

## Verification

The standalone standard-library script `verify.py` constructs \(B(F)\), independently enumerates **every** vertex subset of its derived graph, tests domination from the adjacency relation, identifies its actual minimum dominating sets, and compares them with the predicted independent-set bijection. For all labelled graphs on one through four source vertices and six specified labelled graphs on five vertices, it also constructs the minimum-domination reconfiguration graph, checks every pairwise shortest-path distance, independently enumerates all induced coordinate hypercubes, and compares their coefficient counts with \(I_F(1+q)\). The actual execution (saved in `verification_output.txt`) tested 1,369,076 vertex subsets across 81 source graphs, to derived-graph order 20; every check passed. The infinite result follows from the five proof steps, **not** finite testing.

## Relationship to prior work

Allagan–Gray–Sawyer–Morgan (2026, arXiv:2601.03485, originally publicly submitted January 7) study the number of minimum dominating sets on special tree families, including complete combs and Fibonacci-type variations. The present result asks instead for a universal correspondence between minimum dominating sets and independent sets in arbitrary source graphs, retaining their whole weight distribution and solution-reconfiguration geometry.

The **existence of a graph with any prescribed family of minimum dominating sets** was established earlier by Honkala–Hudry–Lobstein and generalized in DeVos–Dyck–Jedwab–Simon (2020, Theorem 1.5). Accordingly, bare γ-graph realizability is **not new**. What is claimed here is the specific linear-size **bipartite**, small-degree, high-girth realization, with a canonical bijection, exact all-size polynomial transfer, and induced-cube enumerator. The cited general realization theorem does not imply these restrictions or quantitative identities from its stated conclusion.

The concept and median nature of **simplex graphs** are older and treated explicitly by Xie–Xu (2025, arXiv:2503.17160); Fibonacci and Lucas cubes as simplex graphs are already known. No novelty is claimed for simplex graphs, median graphs or their general theory. The 2020 survey by Mynhardt–Nasserasr distinguishes token-slide and unrestricted-exchange γ-reconfiguration. Here both exchange models happen to agree by a forced-pair argument; that property is particular to this construction.

Dettlaff–Raczek–Yero (2016) analyze domination subdivision numbers for generalized coronas; their original graph-operation setting is closely related. Their inspected paper computes the *number of edge subdivisions needed to change domination parameters*, not the all-minimum-set bijection or solution-graph/cube transfer under subdivision of every core edge. Greenhill (2000) supplies the known counting-complexity input. The complexity of counting independent sets is not claimed as new.

## Limitations

The theorem concerns only the explicit class \(B(F)\), not all bipartite graphs or all minimum-domination reconfiguration graphs. The cube polynomial counts embedded induced hypercubes; it is not the graph's characteristic polynomial. The asserted \(\#P\)-hardness holds by an exact reduction on this graph family; no general \(\#P\)-membership claim is made for inputs with an unknown domination number. Previously established generic realization and simplex-graph facts are outside the novelty claim. Relevant literature searches did not identify this exact restricted realization, but cannot prove definitive bibliographic priority. The 2016 related source and the general existence theorem have been inspected; broader unindexed work under other graph-operation terminology remains a residual risk. No independent mathematical review has been performed.

## References

1. J. Allagan, E. Gray, J. Sawyer, G. Morgan. *Four Dominion Growth Regimes in Trees: Forcing, Fibonacci Enumeration, Periodicity, and Stability.* arXiv:2601.03485 (2026), https://arxiv.org/abs/2601.03485.
2. M. DeVos, A. Dyck, J. Jedwab, S. Simon. *Which graphs occur as γ-graphs?* arXiv:1810.01583v2 (2020), https://arxiv.org/pdf/1810.01583.
3. Y.-T. Xie, S.-J. Xu. *Characterizing simplex graphs.* arXiv:2503.17160 (2025), https://arxiv.org/pdf/2503.17160.
4. C. M. Mynhardt, S. Nasserasr. *Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey.* arXiv:2003.05956 (2020), https://arxiv.org/pdf/2003.05956.
5. M. Dettlaff, J. Raczek, I. G. Yero. *Edge subdivision and edge multisubdivision versus some domination related parameters in generalized corona graphs.* *Opuscula Mathematica* 36(5) (2016), 575–588, https://www.opuscula.agh.edu.pl/vol36/5/art/opuscula_math_3634.pdf.
6. C. Greenhill. *The complexity of counting colourings and independent sets in sparse graphs and hypergraphs.* *Computational Complexity* 9 (2000), 52–72, https://web.maths.unsw.edu.au/~csg/papers/complexity.pdf.
