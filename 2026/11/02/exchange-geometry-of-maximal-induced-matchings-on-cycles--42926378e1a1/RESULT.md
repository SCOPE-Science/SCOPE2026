# Exchange geometry of maximal induced matchings on cycles

## Finding
For every integer \(n\ge7\), let the edges of the labeled cycle \(C_n\) be \(e_i=\{i,i+1\}\), with indices modulo \(n\). An **induced matching** is a set of edges whose endpoints induce a disjoint union of edges; it is **maximal** if no additional cycle edge can be added while remaining induced. Form \(\mathcal R_n\) by allowing an exchange of exactly one selected edge for one unselected edge, provided the result remains a maximal induced matching. An exchange necessarily preserves the number of selected edges.

For each \(k\) satisfying \(\lceil n/5\rceil\le k\le\lfloor n/3\rfloor\), let \(\mathcal R_{n,k}\) be the induced sector with exactly \(k\) selected edges and write \(e=n-3k\). All these sectors are nonempty, and their full connected-component classification is
\[
\mathcal R_{n,k}\cong
\begin{cases}
3K_1,&e=0,\\
5K_1,&e=2k,\\
C_n,&e=1\text{ or }e=2k-1,
\end{cases}
\]
with one connected Eulerian component of girth \(3\) when \(2\le e\le2k-2\). The latter statement describes connectivity, Eulericity and girth, not a claimed isomorphism type.

Set \(F(z)=z^3+z^4+z^5\), and let the rows and columns of \(B(z,u)\) be indexed in the order \(3,4,5\):
\[
B(z,u)=\begin{pmatrix}
z^3&uz^4&u^2z^5\\
uz^3&u^2z^4&uz^5\\
u^2z^3&uz^4&z^5
\end{pmatrix}.
\]
The complete vertex-degree polynomial of each sector is
\[
A_{n,k}(u)=\sum_{M\in V(\mathcal R_{n,k})}u^{\deg(M)}
=\frac nk[z^n]\operatorname{tr}(B(z,u)^k).
\]
In particular, every degree is even. The exact vertex, edge and triangle counts are
\[
|V(\mathcal R_{n,k})|=\frac nk[z^n]F(z)^k,\qquad
|E(\mathcal R_{n,k})|=n[z^n](z^7+3z^8+z^9)F(z)^{k-2},
\]
\[
\#K_3(\mathcal R_{n,k})=n[z^n]z^8F(z)^{k-2}.
\]
Consequently the total number of connected components across every cardinality is
\[
\left\lfloor\frac n3\right\rfloor-\left\lceil\frac n5\right\rceil+1
+2\mathbf1_{3\mid n}+4\mathbf1_{5\mid n}.
\]

## Assumptions and scope
The cycle is simple and labeled, with \(n\ge7\); configurations are **inclusion-maximal**, not necessarily maximum, induced matchings. The move is an arbitrary single-edge replacement preserving inducedness and maximality, **not** an alternating-cycle flip and **not** a replacement through a nonmaximal intermediate matching. The graph is undirected and unweighted. The statement is valid simultaneously for every feasible integer \(k\); for inadmissible \(k\), the sector is empty. Isolated-vertex sectors have no finite girth. The indicator \(\mathbf1_{m\mid n}\) is one if \(m\) divides \(n\), and zero otherwise. All coefficient extractions are formal-polynomial extractions.

## Proof
**1. Gap encoding.** List the selected edge indices in their positive cyclic order \(p_0,\ldots,p_{k-1}\), with cyclic gaps \(g_i=p_{i+1}-p_i\pmod n\) taking positive representatives. Two selected edges are compatible precisely when they have at least two intervening cycle edges, so \(g_i\ge3\). Maximality is equivalent to \(g_i\le5\): a longer gap contains a cycle edge compatible with all selected edges, whereas a gap of length at most five contains no insertable edge. Consequently \(g_i\in\{3,4,5\}\), \(\sum_i g_i=n\), and the claimed bounds on \(k\) are necessary and sufficient. The smallest feasible \(k\) is at least two for \(n\ge7\).

**2. Exact local moves.** Removing \(p_i\) merges its two adjacent gaps \(a,b\) into one gap of size \(a+b\ge6\). To restore maximality, its replacement must lie in that merged gap; no other insertion can repair it. If the new index differs by \(\delta\) positions, the new pair is \((a+\delta,b-\delta)\), so legality is equivalent to both entries lying in \(\{3,4,5\}\). Thus every possible nonzero \(\delta\) has absolute value at most two. The number of choices for the replacement equals
\[
f(a,b)=2-|a+b-8|,
\quad (a,b\in\{3,4,5\}),
\]
whose symmetric table has rows \((0,1,2)\), \((1,2,1)\), \((2,1,0)\). Each replacement changes one selected edge and is counted once. Summing \(f(g_{i-1},g_i)\) over selected indices gives the configuration degree. The number of pairs of adjacent gaps with one entry \(4\) and the other not \(4\) is even on a circle, while all other nonzero contributions are two. Hence every degree is even.

**3. Enumeration.** A gap word with a designated first selected edge has \(n\) possible placements. Every unmarked matching is represented by precisely \(k\) such pairs (first selected edge, gap word), even when the matching has rotational symmetries. This proves the vertex count and, using the local weight \(f\), the trace transfer-matrix formula for the degree polynomial. Summing local weights before dividing the degree sum by two gives
\[
|E|=\frac n2[z^n](2z^7+6z^8+2z^9)F(z)^{k-2},
\]
which simplifies to the stated edge formula.

**4. Gap-space connectivity.** Put \(x_i=g_i-3\in\{0,1,2\}\). Any elementary transfer of one unit between consecutive \(x_i\)'s, while staying in \(\{0,1,2\}\), is realized by moving the separating selected edge by one position. These transfers connect every length-\(k\) bounded composition with a fixed total \(e\): repeatedly fill the first entry not yet at its left-packed target of two, by transporting a unit leftward from the first later nonempty entry through the intervening zero entries. Repeating produces the canonical vector \((2,\ldots,2,r,0,\ldots,0)\), where \(r\in\{0,1\}\). Thus any two configurations with the same \(k\) can be connected up to a common translation of their selected indices.

For any nonconstant extremal gap word (that is, unless all gaps are \(3\) or all are \(5\)), this remaining translation can itself be realized. Mark each selected index \(p_i\) as not-yet-shifted or shifted right by one, with flag \(\delta_i\in\{0,1\}\). Its current gap to the next index is \(g_i+\delta_{i+1}-\delta_i\). For each original gap \(3\), require \(p_{i+1}\) to shift before \(p_i\); for each original gap \(5\), require \(p_i\) to shift before \(p_{i+1}\); gaps \(4\) impose no ordering. These are orientations of some edges of the cyclic index graph, and form a directed cycle only when all the original gaps are \(3\) or all are \(5\). They therefore admit a topological ordering in every other case. Move each selected edge right by one in that ordering: every intermediate gap stays between \(3\) and \(5\). The final matching is the original translated by one. Repeating supplies every common translation. This proves connectivity for \(0<e<2k\).

At \(e=0\), all gaps equal \(3\), giving exactly three shifted configurations, each frozen. At \(e=2k\), all gaps equal \(5\), giving five frozen configurations. At \(e=1\) or \(e=2k-1\), there is a unique intermediate gap among otherwise extremal gaps. The vertex formula yields exactly \(n\) configurations, the local degree table gives degree two everywhere, and connectivity makes the sector exactly \(C_n\). Every other connected sector is Eulerian because all vertex degrees are even.

**5. Triangles.** Any three pairwise adjacent \(k\)-sets in a Johnson graph either share a common \((k-1)\)-set or are three subsets obtained by deleting three different elements from a \((k+1)\)-set. The second possibility is impossible here: an incompatible pair in the union would have to be removed by each of three different deletions, while a compatible union would make all three matchings nonmaximal. Thus a triangle fixes \(k-1\) edges and varies one edge among three positions in one merged gap. There are three legal positions exactly when the merged gap has length \(8\), corresponding to adjacent gap pairs \((3,5),(4,4),(5,3)\). Each triangle contributes three (configuration, movable-edge) markings, one per vertex, so marking such a pair and dividing by three gives \(n[z^n]z^8F(z)^{k-2}\) triangles. This is positive precisely for \(2\le e\le2k-2\) and zero in the two degree-two boundary sectors. Those connected interior sectors therefore have girth three. Finally, adding the separate extreme-sector components gives the stated total-component formula.

## Verification
The included `verify_primary.py` directly enumerates subsets of the cycle-edge set, tests inducedness and inclusion-maximality, builds all permitted exchanges without using the gap-move theorem, and checks every sector for \(7\le n\le18\). It independently checks all component sizes, degree-polynomial coefficients, edge and triangle counts, and the three girth regimes. The included `verify_alt.cpp` generates cyclic compositions rather than subsets, reconstructs the full exchange graph, and checks the component, parity, edge and triangle formulas for \(7\le n\le27\). Both were executed successfully against their supplied source files. These experiments are finite corroboration; the proof above establishes the all-parameter assertions.

## Relationship to prior work
The induced-matching concept and its identification with independent sets in the square of the line graph are established; Basavaraju et al. prove general maximal-induced-matching bounds and enumeration algorithms for triangle-free graphs. Bonsma, Kamiński and Wrochna analyze reachability for fixed-size independent sets in claw-free graphs without imposing inclusion-maximality on all intermediate sets. Neither their general decision algorithm nor the counting bound states the present all-parameter sector structure, degree polynomial or triangle counts for maximal induced matchings of cycles. Results about maximal independent sets in ordinary cycles instead concern two gap lengths; passing to the cycle's squared line graph introduces a third gap length and triangles. The present result neither reproves nor claims the earlier general theorems.

## Limitations
This classification covers simple cycles with \(n\ge7\), and only one-edge exchanges with **maximal induced matching** intermediates. It does not establish exact diameters in the connected sectors having triangles, nor cover arbitrary graphs or larger exchange moves. No claim of external independent validation is made. Although targeted published-literature and mathematical-result searches identified no statement subsuming the complete theorem, equivalent work may occur in unindexed or differently named reconfiguration literature; the originality assessment is therefore qualified rather than a proof of priority.

## References
1. M. Basavaraju, P. Heggernes, P. van 't Hof, R. Saei and Y. Villanger, *Maximal induced matchings in triangle-free graphs*, preprint arXiv:1312.5180v1 (first publicly submitted 18 December 2013), later *Journal of Graph Theory* 83 (2016), 231–250. https://arxiv.org/abs/1312.5180
2. P. Bonsma, M. Kamiński and M. Wrochna, *Reconfiguring independent sets in claw-free graphs*, arXiv:1403.0359v1 (3 March 2014). https://arxiv.org/abs/1403.0359
3. K. Cameron, *Induced matchings*, *Discrete Applied Mathematics* 24 (1989), 97–102 (the correspondence is cited and used by Basavaraju et al.).
