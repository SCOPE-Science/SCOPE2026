# The unique first orbit-refinement failure among connected interval graphs

## Finding

For every finite connected simple interval graph \(G\) with at most eight vertices, consider synchronous ordinary one-dimensional counting colour refinement beginning with a single common colour. The stable colour partition agrees with the automorphism-orbit partition, with precisely one isomorphism-type exception:

\[
H=K_3\mathbin{\xleftrightarrow{\text{path of 3 edges}}}K_3.
\]

Here the notation means that a chosen vertex in each triangle is joined by a *three-edge path* with two new interior vertices; both triangles remain otherwise disjoint. Equivalently, its vertex-labelled edge list is

```
(0,4) (0,7) (1,2) (1,3) (2,5) (2,6) (3,4) (4,7) (5,6)
```

The graph has eight vertices and nine edges, and is encoded by graph6 string ``GIc`KO`` (backtick included). Its stable colour classes have sizes \(2,6\); its automorphism orbits have sizes \(2,2,4\). Its automorphism group has order eight. In particular, **every connected interval graph of order at most seven is orbit-refinable**, and this is the unique obstruction at order eight.

## Assumptions and scope

A graph is *interval* when it is the intersection graph of finitely many closed intervals on the real line; graphs are simple, undirected, uncoloured, and connected. A graph is *refinable* here when the equitable partition reached by uncoloured one-dimensional counting colour refinement coincides with the partition into orbits under its entire automorphism group. Refinement updates each colour using the old colour together with the multiset of neighbours' old colours. No graph-identification claim is made: distinguishing vertices inside a graph is different from distinguishing two nonisomorphic graphs. The theorem is a complete finite classification through eight vertices, not an all-order statement.

## Proof

**Completeness of the finite search.** Every connected chordal graph of order greater than one possesses a simplicial vertex; deleting any simplicial vertex preserves connectivity because its neighbours form a clique. The deletion of a vertex from an interval graph remains interval. Hence every connected \(n\)-vertex interval graph for \(n\ge2\) is obtainable from a connected \((n-1)\)-vertex interval graph by adjoining one vertex whose nonempty neighbourhood is a clique. Conversely, adjoining a vertex with clique neighbourhood to a chordal graph preserves chordality, although it may cease to be interval.

For every candidate, test the interval property using the classical equivalence: a finite graph is interval if and only if it is chordal and has no asteroidal triple. Three pairwise nonadjacent vertices form an asteroidal triple if each pair is joined by a path avoiding the closed neighbourhood of the third. The function `contains_asteroidal_triple` directly tests this condition by vertex deletion and reachability. Exact isomorphism testing then removes duplicates. For orders one through seven the exhaustive, isomorphism-free NetworkX graph atlas is filtered for connectivity, chordality and asteroidal-triple freeness; for order eight every nonempty clique neighbourhood of each seven-vertex representative is adjoined. Isomorphic outputs are deduplicated only after `GraphMatcher` performs an exact isomorphism test; degree and Weisfeiler--Leman hashes are used only as necessary invariants for grouping potential duplicates, not as substitutes for an isomorphism decision. This yields the following exact numbers of connected interval-graph isomorphism types at orders one through eight:

\[
1,\ 1,\ 2,\ 5,\ 15,\ 56,\ 250,\ 1328.
\]

The counts independently match the established enumeration of connected interval graphs. Every graph in the complete list is then refined to stability. All graph automorphisms are enumerated by exact self-isomorphism, and their vertex orbits are constructed. No mismatch occurs through order seven; exactly one isomorphism type fails at order eight, represented by ``GIc`KO``. This is a finite exhaustive proof, relying on the stated graph-atlas completeness and the actual self-contained implementation and exact-library operations. The programs and outputs are included here, so the numerical assertion is reproducible.

**Independent census.** `alternate_clique_path_census.py` starts from *all* 272 connected seven-vertex chordal graph representatives, not just the 250 interval representatives. It independently tests interval-graph membership by examining permutations of maximal cliques and checking that the cliques containing any fixed vertex occur consecutively. This is exactly the clique-path characterization of interval graphs. Its exhaustive eight-vertex catalogue again has 1,328 isomorphism types; exactly one is non-refinable, isomorphic to the displayed \(H\). The alternate algorithm checks refinability by searching for an automorphism sending every same-colour vertex pair onto each other, without importing the orbit-construction code of the first program.

**Direct witness and its interval representation.** The maximal cliques of \(H\) admit the consecutive order

\[
\{0,4,7\},\quad \{3,4\},\quad \{1,3\},\quad \{1,2\},\quad \{2,5,6\}.
\]

The cliques containing each vertex occur consecutively, which supplies an explicit interval model: assign to each vertex the integer interval from its first to last occurrence in that five-clique ordering. The two vertices of degree three are \(2\) and \(4\); the other six have degree two. Each degree-three vertex has three degree-two neighbours; each degree-two vertex has one neighbour of each degree, so the degree partition is equitable with quotient-neighbour count matrix

\[
\begin{pmatrix}0&3\\1&1\end{pmatrix}
\]

(rows in degree-three, degree-two order). Ordinary colour refinement stabilizes immediately at this two-cell partition. The actual automorphism orbits are \(\{2,4\}\), \(\{1,3\}\), and \(\{0,5,6,7\}\): the first consists of the triangle-to-path attachment vertices, the second of the two internal connecting vertices, and the last of four terminal triangle vertices. The orbits cannot merge because triangle membership and graph distances are automorphism invariants; reflection and the independent swaps of terminal twins show each listed class is an orbit. This proves the exception is genuine. `verify_interval_independent.py` separately checks the adjacency data, maximal-clique ordering, refinement, orbit sizes, and automorphism group order.

## Verification

With Python 3 and NetworkX 3.6.1, invoke from this directory:

```
python enumerate_interval_refinability.py
python alternate_clique_path_census.py
python verify_interval_independent.py
```

The expected complete executions are in `enumeration_output.txt`, `alternate_output.txt`, and `independent_output.txt`. The first and second searches independently report exactly 1,328 connected eight-vertex interval graph types and one failing type. The third reports its explicit orbit partition and group order eight. The recognition and isomorphism tests are exact; no randomized numerical approximation, sampling, extrapolation, or numerical timeout is counted as a negative case. The catalogue comes from `networkx.graph_atlas_g()`, a complete graph atlas through seven vertices, not from an arbitrary graph sample.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky give the general definition of refinability and locate it within the hierarchy of colour-refinement properties; their results do not state the connected-interval eight-vertex cutoff. Kiefer, Schweitzer and Selman classify graphs identified by two-variable counting logic; *identification of a graph among all graphs* is stronger than orbit recovery within a graph, and their classification does not give the asserted interval-family census. Cameron, Hoàng and Lévêque discuss the classical chordal-and-asteroidal-triple-free characterization, which supplies the exact recognition criterion rather than an orbit-refinement conclusion. Hanlon's enumeration, recorded as OEIS A005976, independently supplies the unlabelled connected interval graph counts, but not the comparison of stable colours against automorphism orbits.

The particular eight-vertex graph and its degree-cell mismatch are also obtainable as the line graph of a double-broom tree; that special-family obstruction is pre-existing and is **not** asserted to be new here. The additional assertion is that, among **all** connected interval graphs on at most eight vertices, it is the **only** graph whose stable colours fail to equal automorphism orbits. Earlier work on colour-refinement collisions between *different* connected chordal graphs addresses a distinct equivalence relation and does not imply this orbit-classification. No novelty claim rests solely on a mismatch of graph names.

## Limitations

The theorem stops at eight vertices; nothing here establishes the number or structure of exceptions on nine or more vertices. The finite proof depends on the completeness of the standard seven-vertex graph atlas and on exact isomorphism and automorphism algorithms; the matching literature count is a cross-check, not by itself a proof of uniqueness. No formal proof assistant or independent human audit has been used. A specialized earlier published enumeration of non-refinable interval graphs could cover the new classification, although the inspected sources and research-index comparisons did not reveal one. This is a self-review only; it is not an independent validation or a priority certificate.

## References

1. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first publicly posted 2015-02-04, especially Section 8. https://arxiv.org/abs/1502.01255
2. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first posted 2015-03-30. https://arxiv.org/abs/1503.08792
3. K. Cameron, C. T. Hoàng and B. Lévêque, *Asteroids in rooted and directed path graphs*, arXiv:0812.2734, first posted 2008-12-15; especially the restatement of the Lekkerkerker--Boland interval-graph characterization. https://arxiv.org/abs/0812.2734
4. P. J. Hanlon, *Counting interval graphs*, Trans. Amer. Math. Soc. 272 (1982), 383–426, DOI:10.1090/S0002-9947-1982-0662044-8. The finite connected counts are also recorded in OEIS A005976: https://oeis.org/A005976
5. NetworkX, `graph_atlas_g`, `GraphMatcher`, `find_cliques`, and `weisfeiler_lehman_graph_hash` API, version 3.6.1. https://networkx.org/documentation/stable/
