# The ten maximum induced matchings of the Tutte–Coxeter graph form a complete-graph incidence geometry

## Finding
Let \(T\) be the Tutte–Coxeter graph. Its induced-matching number is \(\nu_s(T)=9\), and precisely ten induced matchings attain this size. Every graph edge lies in exactly two of the ten maxima, while any two maxima intersect in exactly one graph edge. Consequently their incidence geometry is that of the vertices and edges of \(K_{10}\). The characteristic words of the ten maxima form a constant-weight-nine, length-45 binary code whose pairwise Hamming distance is 16. In particular, no two maxima are adjacent under a one-edge replacement; changing eight of the nine chosen edges is necessary and sufficient to pass from one maximum to another in a single simultaneous exchange.

## Assumptions and scope
All graphs are finite, simple, and undirected. Put \(S=\{1,2,3,4,5,6\}\). A **duad** is a two-element subset of \(S\), and a **syntheme** is a partition of \(S\) into three duads. Write \(\mathcal D\) for the 15 duads and \(\mathcal L\) for the 15 synthemes. The bipartite graph \(T\) has vertex classes \(\mathcal D\) and \(\mathcal L\), and an edge (or **flag**) \((d,L)\) precisely when \(d\in L\). Every duad is contained in three synthemes, every syntheme contains three duads, and \(T\) has 45 edges. This is the standard duad–syntheme realization of the Tutte–Coxeter graph.

A set of graph edges is an **induced matching** if no endpoints of distinct selected edges are adjacent. In the present incidence graph, this means that for flags \((d,L)\) and \((e,M)\) selected together, neither \(d\in M\) nor \(e\in L\) is permitted.

For an **unordered** partition \(\{A,B\}\) of \(S\) into two triples, define
\[
M_{\{A,B\}}=\bigl\{ (\{a,b\},\ \{\{a,b\},A\setminus\{a\},B\setminus\{b\}\}) : a\in A,\ b\in B\bigr\}.
\]
In this expression the second coordinate is a syntheme: its entries are three disjoint duads. Swapping \(A\) and \(B\) does not change the selected flags.

## Proof
**1. Universal bound.** Let \(M\) be an induced matching of size \(r\), and let \(X\subset\mathcal D\), \(Y\subset\mathcal L\) be its selected duad and selected syntheme endpoints. They each have \(r\) members. The induced condition means every selected duad is incident with exactly one selected syntheme and with exactly two synthemes outside \(Y\). Counting incidences from \(X\) to \(\mathcal L\setminus Y\) therefore yields
\[
2r\le 3(15-r),\qquad\text{hence }r\le9.
\]

**2. Six perfect matchings force the complete bipartite graph.** We need the following elementary lemma.

*Lemma.* A simple nine-edge graph \(H\) on six labeled vertices has at most six perfect matchings. Equality holds exactly when \(H\cong K_{3,3}\).

*Proof of lemma.* If \(H\) is triangle-free, each edge \(uv\) satisfies \(\deg(u)+\deg(v)\le6\), because the two neighborhoods are disjoint. By Cauchy–Schwarz,
\[
54=\frac{18^2}{6}\le\sum_v\deg(v)^2=\sum_{uv\in E(H)}(\deg(u)+\deg(v))\le9\cdot6=54.
\]
Thus all degrees are three. A triangle-free, three-regular graph on six vertices is \(K_{3,3}\): the three neighbors of any vertex are independent and must share the other two vertices as their remaining neighbors. The graph \(K_{3,3}\) has exactly \(3!=6\) perfect matchings.

Now suppose \(H\) has a triangle on vertices \(A\), and write \(B=S\setminus A\). Let \(\ell\) be the number of edges induced by \(B\). There are \(6-\ell\) edges between \(A\) and \(B\). Each perfect matching is either entirely across the two triples (count \(Q\)), or consists of one cross edge, one edge of the triangle on \(A\), and one internal edge of \(B\) (count \(R\)).

If \(\ell=0\), then \(R=0\), and at least one edge of the full \(K_{3,3}\) is absent, ruling out two of its six perfect matchings: \(Q\le4\). If \(\ell=1\), only the unique vertex \(b\) outside the edge induced by \(B\) can be the \(B\)-endpoint of a one-cross matching; hence \(R=\deg_{A}(b)\). With only five cross edges, \(Q\le2\), since three distinct perfect matchings on three-by-three vertices need at least six distinct cross edges. If \(\deg_A(b)\le2\), then \(Q+R\le4\); if \(\deg_A(b)=3\), only two cross edges remain at the other two vertices of \(B\), so \(Q\le1\) and \(Q+R\le4\).

If \(\ell=2\), there are four cross edges. Two distinct perfect matchings of a three-by-three bipartite graph require at least five distinct edges, so \(Q\le1\). If \(Q=0\), then \(R\le4\). If \(Q=1\), at least one cross edge must meet the \(B\)-vertex not opposite an internal edge, leaving at most three cross edges contributing to \(R\); thus \(R\le3\). Finally, if \(\ell=3\), only three cross edges exist and every such cross edge can contribute at most one one-cross matching, so \(R\le3\) and \(Q\le1\). Thus a graph containing a triangle has at most four perfect matchings. This proves the lemma. \(\square\)

**3. Forced form of every optimum.** Suppose \(|M|=9\). Equality holds in the incidence bound. Consequently all six unselected synthemes consist exclusively of the nine selected duads. Regard these selected duads as the nine edges of a graph \(H\) on \(S\). Each unselected syntheme is a perfect matching of \(H\), so \(H\) has at least six perfect matchings. By the lemma, \(H=K_{A,B}\) for some partition of \(S\) into two triples. Its six perfect matchings are exactly the six unselected synthemes. Each of the remaining nine synthemes has exactly one cross duad, and must be matched to that duad. Therefore \(M=M_{\{A,B\}}\), with no choices left. Conversely, the explicit set \(M_{\{A,B\}}\) contains nine flags, and no selected duad is incident with a different selected syntheme, so it is an induced matching. There are exactly \(\binom63/2=10\) unordered triple partitions, proving both the maximum and the complete classification.

**4. Flag incidences and pair intersections.** Fix any flag \((\{a,b\},L)\) and write the two other duads of its syntheme as \(\{c,d\}\) and \(\{e,f\}\). To appear in \(M_{\{A,B\}}\), the first duad must cross the partition, and the other two duads must lie inside different triples. Exactly two unordered triple partitions meet these conditions:
\[
\{\{a,c,d\},\{b,e,f\}\},\qquad
\{\{a,e,f\},\{b,c,d\}\}.
\]
Thus each of the 45 flags belongs to exactly two maxima. The natural action of \(S_6\) on the ten triple partitions is transitive on unordered pairs of *distinct* partitions: relative to any fixed partition, each other one swaps a single element of the two triples. Hence the intersection size of any two distinct maxima is a constant \(j\). Double-counting triples consisting of a flag and a pair of distinct maxima containing it gives
\[
\binom{10}{2}j=45\binom22=45,
\]
so \(j=1\).

Identify each maximum with one vertex of \(K_{10}\), and each original flag with the unique pair of maxima containing it. This is a bijection from the 45 original flags to the 45 edges of \(K_{10}\), with exactly the asserted incidence relation. A pair of characteristic words of weight nine and overlap one has Hamming distance \(2(9-1)=16\), completing the coding and exchange consequences. \(\square\)

## Verification
Two executable, independent finite checks are included. `verify_duad_syntheme.py` builds all duads, synthemes, and 45 flags, checks the ten constructed matchings, their pairwise intersections and flag multiplicities, and enumerates all \(\binom{15}{9}=5005\) nine-edge simple graphs on six vertices to confirm the perfect-matching lemma's equality cases. Its histogram of perfect-matching counts is \((0:75,1:360,2:1380,3:2040,4:1140,6:10)\).

`verify_symplectic_cliques.py` constructs the same incidence graph by a separate \(\mathbb F_2^4\) symplectic model, builds the 45-flag compatibility graph, and enumerates all maximal compatible cliques with a complete Bron–Kerbosch search. It finds 8,950 maximal induced matchings, of respective sizes five, six, seven, and nine with counts \((3060,5520,360,10)\). Both programs verify ten maxima, one common flag per pair and two maxima per flag. These computations check the finite instance; the preceding argument proves the result independently.

Run both scripts with Python 3 from the directory containing them. No nonstandard Python packages are required.

## Relationship to prior work
The classical duad–syntheme model is described by Baez (2015). Horák, Qing and Trotter (1993) proved general strong-edge-colouring bounds for cubic graphs; Basavaraju and collaborators (2013) bounded the number of maximal induced matchings in arbitrary triangle-free graphs. Lužar and collaborators (2021) explicitly established that the Tutte eight-cage is not strongly six-edge-colourable. These prior results are not restated as new. Colangelo, Monzillo and Siciliano (2024) studied association schemes on generalized-quadrangle flags. Their relation and clique analysis addresses a different family of flag graphs and does not supply the present exact ten-optimum classification in the inspected text.

The contribution here is the complete classification of **largest induced matchings of this specific incidence graph** and the forced complete-graph incidence relation among the maxima. Neither an upper bound on colours, a triangle-free maximal-matching bound, nor a general flag association scheme directly gives the asserted classification.

## Limitations
No claim is made about the exact strong chromatic index, total numbers of arbitrary induced matchings, or uniqueness of the result in the entire historical literature. An independently published or unindexed equivalent description may exist. The code verifies a finite graph rather than replacing the written proof. Independent scholarly audit has not been performed.

## References
1. P. Horák, H. Qing, W. T. Trotter, *Induced matchings in cubic graphs*, Journal of Graph Theory 17 (1993), 151–160, doi:10.1002/jgt.3190170204; author copy at https://trotter.math.gatech.edu/papers/85.pdf.
2. M. Basavaraju, P. Heggernes, P. van ’t Hof, R. Saei, Y. Villanger, *Maximal induced matchings in triangle-free graphs*, arXiv:1312.5180v1 (first posted 18 December 2013), https://arxiv.org/abs/1312.5180.
3. J. Baez, *Tutte–Coxeter Graph*, Visual Insight, American Mathematical Society (15 August 2015), https://blogs.ams.org/visualinsight/2015/08/15/tutte-coxeter-graph/.
4. B. Lužar, E. Mačajová, M. Škoviera, R. Soták, *Strong edge colorings of graphs and the covers of Kneser graphs*, arXiv:2101.04768v1 (2021), https://arxiv.org/abs/2101.04768.
5. F. Colangelo, G. Monzillo, A. Siciliano, *The association scheme on the set of flags of a finite generalized quadrangle*, arXiv:2406.03942v1 (2024), https://arxiv.org/abs/2406.03942.
