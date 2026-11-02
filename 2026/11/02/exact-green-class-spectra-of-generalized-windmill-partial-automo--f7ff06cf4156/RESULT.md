# Exact Green-class spectra of generalized windmill partial-automorphism monoids

## Finding
For integers \(m,s\ge1\), let \(W_{m,s}=K_1\vee(mK_s)\), the graph obtained by joining one central vertex to \(m\) disjoint cliques of size \(s\). Let \(P_{m,s}\) be the inverse monoid of all partial isomorphisms between **vertex-induced** subgraphs of \(W_{m,s}\), including the empty map. Write
\[
R_{m,s}(z)=\sum_{\alpha\in P_{m,s}}z^{|\operatorname{dom}\alpha|}.
\]
For a vector \(\mathbf c=(c_1,\ldots,c_s)\) of nonnegative integers put \(h=\sum_{j=1}^s c_j\) and \(d=\sum_{j=1}^s jc_j\). Whenever \(h\le m\), define
\[
N_{m,s}(\mathbf c)=\frac{m!}{(m-h)!\prod_{j=1}^s c_j!}\prod_{j=1}^s\binom sj^{c_j},\qquad
A(\mathbf c)=\prod_{j=1}^s(j!)^{c_j}c_j!.
\]
Set \(E_1=ms+1\), and \(E_j=m\binom{s+1}{j}\) for \(2\le j\le s+1\). Then the exact rank polynomial is
\[
\boxed{R_{m,s}(z)=1+\sum_{j=1}^{s+1}j!E_j^2z^j+
\sum_{\substack{\mathbf c\in\mathbb N_0^s\\2\le h\le m}}
N_{m,s}(\mathbf c)^2A(\mathbf c)(z^d+z^{d+1}).}
\]
The \(\mathcal D\)-classes are exactly one class for the empty graph, one for each clique \(K_j\) with \(1\le j\le s+1\), and two for each profile \(\mathbf c\) with \(2\le h\le m\): the disconnected graph \(D_{\mathbf c}=\bigsqcup_{j=1}^s c_jK_j\) and its cone \(C_{\mathbf c}=K_1\vee D_{\mathbf c}\). Their sizes are respectively \(1\), \(j!E_j^2\), and \(N_{m,s}(\mathbf c)^2 A(\mathbf c)\) for each of the two profile classes. The total number of \(\mathcal D\)-classes is
\[
\boxed{2\binom{m+s}{s}-s.}
\]
The maximal subgroups in the clique classes are \(S_j\). Those in each profile class, whether disconnected or coned, are \(\prod_{j=1}^s(S_j\wr S_{c_j})\), omitting empty factors. These statements include the complete-graph case \(m=1\), stars \(s=1\), and friendship graphs \(s=2\).

## Assumptions and scope
All graphs are finite simple undirected graphs, with vertex-induced subgraphs; \(m,s\) are arbitrary positive integers. An element of \(P_{m,s}\) is a bijection between two selected vertex sets preserving both adjacency and nonadjacency. Composition is composition of partial maps, and rank is domain cardinality. The empty map has rank zero. The symbols \(K_j\), \(S_j\) and \(\wr\) mean respectively a complete graph, a symmetric group and a permutational wreath product. Define an empty product to be the trivial group. All counting formulas concern actual partial maps, not isomorphism types of maps.

## Proof
**1. Induced graph profiles.** Write the \(m\) peripheral cliques as blades, disjoint away from the common central vertex. For a selected set omitting the center, let \(c_j\) count the blades from which exactly \(j\) vertices were selected; unselected blades contribute nothing. The induced graph is \(D_{\mathbf c}\). Selecting \(h\) distinct labeled blades, partitioning these into size classes \(c_j\), and choosing the appropriate \(j\)-subsets inside each blade gives exactly \(N_{m,s}(\mathbf c)\) vertex sets. Its automorphism group has size \(A(\mathbf c)\), because components of order \(j\) can be permuted and their vertices independently permuted.

For a selected set containing the center, the graph is \(C_{\mathbf c}\). If \(h\ge2\), the center is the unique vertex adjacent to every other vertex: every peripheral vertex misses each vertex in at least one other selected blade. Therefore \(C_{\mathbf c}\) is a connected noncomplete graph, its automorphism group fixes the center and has order \(A(\mathbf c)\), and its isomorphism type recovers the profile \(\mathbf c\). The disconnected graphs \(D_{\mathbf c}\), \(h\ge2\), are also distinguished by their multisets of complete components. No graph in either family is isomorphic to one in the other.

If \(h=0\), omitting the center gives the empty graph, while including it gives \(K_1\). If \(h=1\), selecting \(j\) peripheral vertices gives \(K_j\) when the center is omitted and \(K_{j+1}\) when it is included. Hence the only collisions among descriptions occur for complete graphs. There are \(ms+1\) induced singletons. For \(2\le j\le s+1\), an induced \(K_j\) is either a peripheral \(j\)-subset (\(m\binom{s}{j}\) choices) or the center plus a \((j-1)\)-subset from one blade (\(m\binom{s}{j-1}\) choices). Thus their number is \(E_j=m\binom{s+1}{j}\) by Pascal's identity. This remains valid at \(j=s+1\).

**2. From induced graphs to partial isomorphisms.** If an isomorphism type \(H\) occurs on exactly \(t_H\) selected vertex sets, then there are exactly \(t_H^2|\operatorname{Aut}(H)|\) partial isomorphisms having domain and image of type \(H\): choose both sets and one of their \(|\operatorname{Aut}(H)|\) isomorphisms. The generic inverse-monoid \(\mathcal D\)-relation identifies maps precisely when the induced graphs on their domains are isomorphic (equivalently, one can prove this by composing domain and image isomorphisms and their partial inverses). The maximal subgroup at an idempotent with domain inducing \(H\) is \(\operatorname{Aut}(H)\). Applying these facts to Step 1 proves the \(\mathcal D\)-class sizes, maximal subgroup descriptions and full rank polynomial.

**3. Class number.** The number of vectors \(\mathbf c\in\mathbb N_0^s\) with \(\sum c_j\le m\) is \(\binom{m+s}{s}\), by stars and bars. Exactly one has \(h=0\), and exactly \(s\) have \(h=1\). The remaining \(\binom{m+s}{s}-s-1\) profiles each give two classes. Adding the empty class and \(s+1\) complete-graph classes yields \(2\binom{m+s}{s}-s\).

## Verification
Run \(\texttt{python3 verify.py}\) from the directory containing the accompanying standalone file. It uses only Python's standard library. For seven parameter pairs, including complete graphs, stars, friendship graphs and larger blades, it enumerates **every** partial injection between all vertex subsets and checks adjacency and nonadjacency pairwise, independently of the profile-counting formula. It also checks all rank coefficients against the formula, along with boundary cases for 42 additional parameter pairs. For \((m,s)=(2,3)\) it obtains
\[
R_{2,3}(z)=1+49z+450z^2+1194z^3+1608z^4+1296z^5+504z^6+72z^7,
\]
so \(|P_{2,3}|=5174\). For \((m,s)=(3,2)\), the total is \(4154\). An independent induced-subgraph isomorphism grouping for \((m,s)=(2,2),(2,3),(3,2),(3,3)\) found respectively \(10,17,18,37\) distinct types, agreeing with the class-count formula. These finite checks are not substitutes for the universal combinatorial proof.

## Relationship to prior work
Jajcay, Jajcayová, Szakács and Szendrei give the general inverse-monoid theory of partial graph automorphisms; in particular their Proposition 3.1 supplies the correspondence between \(\mathcal D\)-classes and induced-subgraph isomorphism types. That correspondence is used here as established mathematics and is not claimed as new. The additional result is the **complete explicit classification, class-size calculation, maximal-subgroup list and rank enumerator** for the connected generalized-windmill family. Earlier work on partial isometries of star graphs considers a different family and a metric-preservation notion, not this induced-graph isomorphism enumeration. The literature comparison did not identify a pre-existing windmill-specific formula; this is not a certification of publication priority.

## Limitations
The theorem covers the specified generalized windmill graphs and induced-subgraph partial isomorphisms, not arbitrary partial injective graph homomorphisms or all graphs formed by gluing arbitrary cliques. The \(\mathcal D\)-class isomorphism principle is prior theory. Independent mathematical audit and independent publication-priority verification have not been performed. The self-contained proof gives all integer parameters, while the exhaustive computational checks necessarily cover only small instances.

## References
1. R. Jajcay, T. Jajcayová, N. Szakács and M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422, first posted 2018-09-12; Journal of Algebraic Combinatorics (2021), DOI:10.1007/s10801-020-00944-5, especially Proposition 3.1.
2. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a finite star graph*, arXiv:2203.05504, first posted 2022-03-10. The objects and preservation requirements differ from those studied here.
3. T. B. Jajcayová, *On Computational Aspects of Finding Inverse Monoids of Partial Automorphisms*, RIMS Kôkyûroku 2229 (2022), 88–96, dated 2022-05-27. General context; complete full-text comparison was unavailable.
