# Three three-round theories of line graphs of Johnson graphs

## Finding
For integers \(n\ge 2k\ge4\), let \(J(n,k)\) have as vertices the \(k\)-subsets of \([n]\), with adjacency when two subsets intersect in exactly \(k-1\) points. Let \(X(n,k)=L(J(n,k))\), the ordinary simple undirected line graph, whose vertices are edges of \(J(n,k)\) and whose adjacency means sharing an endpoint in the Johnson graph. Work in first-order logic with equality and adjacency, without named coordinates or counting quantifiers. Write \(\equiv_3\) for agreement on all sentences of quantifier rank at most three.

**Theorem.** For every \(n\ge2k\ge4\) and \(m\ge2\ell\ge4\),
\[
X(n,k)\equiv_3 X(m,\ell)
\quad\Longleftrightarrow\quad
\begin{cases}
(n,k)=(m,\ell)=(4,2),\quad\text{or}\\
(n,k)=(m,\ell)=(5,2),\quad\text{or}\\
n,m\ge6.
\end{cases}
\]
Thus precisely three rank-three theories arise. Their smallest representatives have \(12\), \(30\), and \(60\) vertices, respectively, so the sharp uniform representative bound is \(60\). In particular, \(L(J(6,2))\equiv_3 L(J(6,3))\equiv_3 L(J(9,4))\).

## Assumptions and scope
The inequalities \(n\ge2k\ge4\) specify integer parameters and exclude the degenerate complete-graph case \(k=1\). There is no bound on \(n\) or \(k\). The graphs have no loops. A third selected graph vertex may coincide with a previous selection in an Ehrenfeucht–Fraïssé game; all such choices are included.

For convenience let \(G=J(n,k)\). It has \(N=\binom nk\) vertices and degree \(d=k(n-k)\ge4\). Its line graph \(X=L(G)\) has \(M=Nd/2\) vertices and is regular of degree \(D=2(d-1)\). Permutations of \([n]\) act transitively on the edges of \(G\), hence transitively on vertices of \(X\).

## Proof
### The three-round extension principle
For distinct vertices \(e,f\) of a vertex-transitive graph \(X\), record their adjacency bit and the presence or absence of a fresh third vertex \(z\) in each of the four classes: adjacent to both; adjacent to \(e\) only; adjacent to \(f\) only; adjacent to neither. A fresh vertex means \(z\ne e,f\). When these signatures agree as sets for two vertex-transitive graphs, Duplicator wins the three-round Ehrenfeucht–Fraïssé game: match any first vertex by transitivity; match the second by its ordered-pair signature (or equality); and match the third by the recorded adjacency/equality pattern. For any first vertex, all signatures that occur anywhere occur with that vertex first, by vertex transitivity. Hence the set of signatures determines the rank-three theory. Conversely, a signature missing from one graph but present in another is detected by an existential/universal sentence of rank at most three.

### Extension patterns for adjacent line-graph vertices
Let \(e=uv\) and \(f=uw\) be edges of \(G\) with their common endpoint \(u\). The line-graph vertices \(e,f\) are adjacent. Their common-neighbor count in \(X\) is \(d-2+\varepsilon\), where \(\varepsilon\in\{0,1\}\) indicates whether \(vw\) is an edge of \(G\): the common neighbors are all edges from \(u\) other than \(e,f\), together with \(vw\), if present. This count is positive. Since \(X\) has degree \(D\), the number of fresh neighbors adjacent to \(e\) but not \(f\) is \(D-1-(d-2+\varepsilon)=d-1-\varepsilon\ge2\); the reverse count is identical.

If \(n\ge5\), then \(N\ge10\), so \(M=Nd/2>4d\). At most \(4d\) edges of \(G\) meet any prescribed four original vertices. Therefore an edge of \(G\) avoids the three vertices \(u,v,w\), producing in \(X\) a third vertex adjacent to neither \(e\) nor \(f\). For \(n=4\), \(G=J(4,2)\) is the octahedral graph \(K_6\) minus a perfect matching: any three of its vertices contain an edge. The three vertices of \(G\) outside \(\{u,v,w\}\) therefore contain an edge, giving the same neither-adjacent extension. Consequently all adjacent pairs have signature \((1,1,1,1)\), where the final three entries mean that a fresh common, one-sided, and neither-sided neighbor exists, respectively.

### Extension patterns for nonadjacent line-graph vertices
Now let \(e=uv\) and \(f=st\) be disjoint edges of \(G\), so the corresponding line-graph vertices are nonadjacent. A common neighbor of \(e,f\) in \(X\) is precisely an edge joining a vertex of \(\{u,v\}\) to one of \(\{s,t\}\) in \(G\). Hence at most four common neighbors exist. Since the line-graph degree is \(D=2(d-1)\ge6\), at least \(D-4\ge2\) vertices are adjacent only to \(e\), and likewise at least \(D-4\ge2\) are adjacent only to \(f\).

For \(n\ge5\), the inequality \(M>4d\) again guarantees an edge of \(G\) avoiding all four endpoints \(u,v,s,t\). This yields an \(X\)-vertex adjacent to neither \(e\) nor \(f\). For \(n=4\), there are exactly two remaining original vertices, and such a third edge exists precisely when those two vertices are adjacent in \(G\). Both possibilities occur. Write \(12\) for the \(2\)-set \(\{1,2\}\), etc. The original Johnson edges \(e=(12,13)\) and \(f=(24,34)\) leave the nonadjacent pair \(14,23\), giving no neither-adjacent third vertex. By contrast, \(e=(12,13)\) and \(f=(14,24)\) leave the adjacent pair \(23,34\), giving such a third vertex. In both examples a cross-edge joins an endpoint of \(e\) to an endpoint of \(f\), so a common-neighbor extension exists.

The existence of a common-neighbor extension for nonadjacent \(e,f\) persists for every \(n\ge2k\ge4\): fix a \((k-2)\)-subset and allow two further positions to range through four unused ground elements. This gives an induced copy of \(J(4,2)\) in \(G\) and preserves the displayed crossed pair of original edges.

A nonadjacent line-graph pair *without* a common neighbor is exactly an induced matching of size two in \(G\), i.e. an induced \(2K_2\). When \(n=4,5\), necessarily \(k=2\) and \(G=J(n,2)=L(K_n)\). Two disjoint original Johnson edges with no cross-edge would correspond to two pairs of incident edges in \(K_n\) supported on disjoint three-element subsets. This requires at least six underlying vertices, impossible for \(n\le5\). Thus every nonadjacent pair in \(X(4,2)\) and \(X(5,2)\) has a common neighbor.

For \(n\ge6\), an induced \(2K_2\) in \(G\) always exists. Put \(a=n-k\). If \(a\ge4\), fix a \((k-2)\)-subset and choose six distinct unused ground elements labelled \(1,\ldots,6\). The four \(k\)-sets obtained by adjoining \(12,13,45,46\) induce exactly the two edges \((12,13)\) and \((45,46)\). If \(a=3\), the assumptions \(n\ge2k\ge4\) and \(n\ge6\) force \((n,k)=(6,3)\); the four sets \(123,124,156,256\) induce exactly the two edges \((123,124)\) and \((156,256)\). No case \(a<3\) can have \(n\ge6\) in the stated parameter range. This proves existence of the zero-common-neighbor signature exactly when \(n\ge6\).

### The three signatures and separation
Write \((b,c,o,z)\) for a pair signature, where \(b\) is adjacency of the pair, \(c\) means a common neighbor exists, \(o\) means both one-sided neighbor types exist, and \(z\) means a neither-adjacent neighbor exists. The exact signature sets are
\[
\begin{aligned}
\Sigma_{4,2}&=\{(1,1,1,1),(0,1,1,0),(0,1,1,1)\},\\
\Sigma_{5,2}&=\{(1,1,1,1),(0,1,1,1)\},\\
\Sigma_{n,k}&=\{(1,1,1,1),(0,1,1,1),(0,0,1,1)\}\quad(n\ge6).
\end{aligned}
\]
The extension principle proves equivalence within each class. Two explicit rank-three sentences separate the classes. First, some distinct nonadjacent vertices have *no fresh vertex nonadjacent to both* exactly when \(n=4\). Second, some distinct nonadjacent vertices have *no common neighbor* exactly when \(n\ge6\). Both properties are expressed by choosing the original pair with two existential quantifiers and forbidding a third witness with one universal quantifier (all distinctness and adjacency conditions are quantifier-free). Thus all three classes differ at rank three.

Finally, \(|V(X(n,k))|=\frac12\binom nk k(n-k)\). In the small classes the only permissible parameters are \((4,2)\) and \((5,2)\), yielding \(12\) and \(30\). In the stable class \(n\ge6\); the smallest \(\binom nk\) and degree over the permitted range occur at \((6,2)\), yielding \(\frac12\binom62\cdot 8=60\). Indeed \(\binom nk\ge\binom n2\) and \(k(n-k)\ge2(n-2)\) for \(2\le k\le n/2\), so the product cannot be smaller. The bound \(60\) is attained and sharp.

## Verification
Run `python check_pair_spectra.py` and `python check_ef_types.py` with Python 3. The first program computes every unordered pair's four extension-presence bits directly from bitset adjacency in the line graph for the sixteen parameter pairs \(4\le n\le10\), \(2\le k\le\lfloor n/2\rfloor\), including a graph with \(3150\) vertices. The second program independently constructs the graph via set intersections and computes complete three-move rooted logical types, including repeated choices, on seven parameter pairs. Both return the three predicted theories. Recorded outputs are included; the infinite theorem is proved above and does not depend on finite enumeration.

## Relationship to prior work
Pikhurko, Veith, and Verbitsky (2003), *The First Order Definability of Graphs: Upper Bounds for Quantifier Rank*, supplies the general Ehrenfeucht–Fraïssé language and distinctness criterion, not this family classification. Broersma and Veldman (1987), *3-Connected line graphs of triangular graphs are panconnected and 1-hamiltonian*, studies connectivity and Hamiltonian properties of line graphs; its term “triangular graph” there means a graph in which every edge belongs to a triangle, not specifically the Johnson graph \(J(n,2)\). It does not classify logical theories. Standard studies of Johnson-graph automorphisms and first-order properties of Johnson graphs do not automatically transfer a fixed quantifier-rank classification to their line graphs: line-graph vertices represent original edges, and translating a formula changes quantifier resources. The exact three-class double-line Johnson statement was not located in the inspected sources; exhaustive priority is not claimed.

## Limitations
The theorem concerns only pure graph first-order sentences through quantifier rank three. It does not classify higher ranks, counting logic, named coordinate relations, arbitrary Johnson scheme relations, or general line graphs. The source comparison does not amount to exhaustive historical-priority certification. Independent mathematical validation has not been performed.

## References
1. O. Pikhurko, H. Veith, O. Verbitsky, “The First Order Definability of Graphs: Upper Bounds for Quantifier Rank,” 2003, arXiv:math/0311041, https://arxiv.org/abs/math/0311041 (first public version dated 2003-11-04).
2. H. J. Broersma and H. J. Veldman, “3-Connected line graphs of triangular graphs are panconnected and 1-hamiltonian,” *Journal of Graph Theory* 11 (1987), 399–407, DOI:10.1002/jgt.3190110314, https://ris.utwente.nl/ws/files/6879652/Broersma87three.pdf.
3. B. G. Benediktsson, *Model-Theoretic Methods for Algorithmically Tame Graph Classes*, PhD thesis (2022), Section 5 (Johnson-graph first-order methods; distinct structure and questions).
