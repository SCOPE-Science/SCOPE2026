# Subgroup fixed-point homotopy of complete-graph line-clique complexes

## Finding
For every integer \(n\ge4\), put \(X_n=\operatorname{Cl}(L(K_n))\): its vertices are the two-element subsets of \([n]\), and its simplices are pairwise-intersecting families of these two-element subsets. Let \(H\le S_n\) be **any** subgroup acting through relabeling. Denote by \(a\), \(b\), and \(c\) the numbers of its vertex orbits on \([n]\) of cardinalities one, two, and three.

The *geometric* fixed-point space, not merely the subcomplex on individually fixed vertices, has the following complete integral homotopy classification:

\[
|X_n|^H\simeq
\begin{cases}
\text{a discrete space of }b+c\text{ points},&a=0,\\
\left(\bigvee^{\binom{a-1}{3}}S^2\vee\bigvee^{b(a-1)}S^1\right)\ \sqcup\ (\bigsqcup^c\{\mathrm{pt}\}),&a\ge1.
\end{cases}
\]

In the first case \(b+c=0\) means the empty space; in the second, a zero-fold wedge denotes one point. The expression is a homotopy equivalence of ordinary spaces; no equivariant comparison of the full complexes is asserted. The formula applies to *noncyclic* subgroups as well as cyclic subgroups, and longer vertex orbits have no effect.

## Assumptions and scope
All graphs are finite, simple and loopless; \(n\ge4\). For a finite simplicial complex \(X\) with a simplicial \(H\)-action, \(|X|^H\) denotes the common fixed points of all \(h\in H\) in its geometric realization. Fixed points in the interiors of simplices with setwise, but not pointwise, invariant vertices are included. The line graph \(L(K_n)\) has one vertex for each unordered edge \(\{i,j\}\) of \(K_n\), with adjacency exactly when two edges intersect.

The subgroup need not act faithfully, although it is understood as a subgroup of the displayed symmetric group. Orbit counts \(a,b,c\) count whole vertex orbits; for example, a single vertex orbit of size six contributes to none of them.

## Proof
**1. An exact simplicial model of geometric fixed points.** Let \(V\) be the vertices of a finite simplicial \(H\)-complex \(K\). The barycentric coordinates of a point of \(|K|^H\) are constant on each \(H\)-orbit of \(V\). Therefore \(|K|^H\) is canonically homeomorphic to the realization of the complex whose vertices are those \(H\)-orbits \(Q\subseteq V\) that are themselves faces of \(K\), and whose faces are collections \(\{Q_1,\ldots,Q_t\}\) with union \(Q_1\cup\cdots\cup Q_t\) a face of \(K\). To see this, assign to an orbit-vertex its normalized orbit barycenter; conversely, the constant barycentric coordinates recover the unique convex combination of orbit barycenters. These linear maps are inverse on each fixed simplex and agree on overlaps.

Apply the model to \(K=X_n\). Its vertices are edges of \(K_n\), and its faces are edge families in which all pairs intersect.

**2. Classification of possible orbit-vertices.** Any family of at least two distinct pairwise-intersecting edges of a simple graph is either contained in a star or contained in the three edges of a triangle. For completeness, if \(uv\) and \(uw\) are two edges, any further edge meeting both either contains \(u\) or equals \(vw\); if \(vw\) occurs, no fourth distinct edge can meet all three. A single \(H\)-orbit of edges that is a face therefore falls into one of the following cases:

* A star orbit with a unique common center \(v\) fixed by \(H\); its edges join \(v\) to one \(H\)-orbit of other vertices. This includes a single fixed edge joining two fixed vertices, counted in each of its endpoint stars.
* A singleton edge whose endpoints constitute one \(H\)-orbit of size two. There is exactly one such orbit-vertex for each size-two vertex orbit.
* All three edges of a triangle whose three vertices form one \(H\)-orbit of size three. There is exactly one such orbit-vertex for each size-three vertex orbit.

The classification is exhaustive: if a two-edge orbit lies in a star, its center is uniquely determined and hence fixed; if a three-edge orbit is triangular and transitive on its edges, it is transitive on the three triangle vertices. An edge fixed setwise has either two individually fixed endpoints or a size-two orbit. Every size-three vertex orbit acts transitively on the three edges of its complete triangle because its induced transitive subgroup of \(S_3\) is either cyclic of order three or all of \(S_3\).

**3. The fixed complex as a union of elementary pieces.** Let \(F\) be the fixed-orbit simplicial model from Step 1. For every individually fixed vertex \(v\in[n]\), let \(A_v\) be the simplex spanned by all edge-orbit vertices represented by edges incident with \(v\). Every simplex represented by a star lies inside one of these \(A_v\). If \(v\ne w\) are fixed, their intersection is the single fixed-edge orbit \(\{vw\}\), and three different \(A_v\) have empty intersection.

For each set of three fixed vertices \(u,v,w\), the three fixed edge-orbits \(uv,uw,vw\) support an extra filled triangle; its boundary has one edge inside each of \(A_u,A_v,A_w\). For each two-point vertex orbit \(O=\{x,y\}\), there is a vertex \(p_O\) representing the fixed edge \(xy\), and for every fixed \(v\) exactly one extra edge from \(p_O\) to the orbit-vertex representing \(\{vx,vy\}\), already in \(A_v\). No two such extra edges at the same \(p_O\) fill a triangle: their total edge families contain disjoint edges. For each three-point vertex orbit there is one isolated orbit-vertex, coming from its internal triangle; it cannot be joined to any different orbit-vertex. There are no further simplices, by the star-or-triangle classification.

When \(a=0\), no star simplex is present, so only the \(b+c\) isolated vertices remain, proving the first case.

**4. Recovering the attached two-skeleton.** Suppose \(a\ge1\). The union \(A=\bigcup_v A_v\), over the \(a\) fixed vertices, is a good cover by simplices, with pairwise nonempty intersections contractible and all triple intersections empty. Its nerve is the complete graph on these \(a\) vertices, viewed as a one-dimensional simplicial complex. The standard constructive nerve equivalence sends a path inside \(A_v\) joining the common points \(A_v\cap A_u\) and \(A_v\cap A_w\) to the corresponding path through the nerve vertex \(v\). Under this correspondence, the attaching loop of each added triangle from three fixed vertices maps with degree one onto the corresponding three-edge cycle of the complete graph. Hence adding every such triangular two-cell produces, up to homotopy, the complete two-skeleton \(\operatorname{sk}_2\Delta^{a-1}\).

The complex \(\operatorname{sk}_2\Delta^{a-1}\) is contractible for \(a\le3\), and for \(a\ge4\) is homotopy equivalent to \(\bigvee^{\binom{a-1}{3}}S^2\). One explicit proof collapses its maximal spanning cone of all triangles containing a distinguished vertex and then identifies each triangle avoiding that vertex with a two-sphere after quotienting the contractible cone; the number of those triangles is \(\binom{a-1}{3}\). This quotient argument preserves the homotopy type because the cone subcomplex is contractible.

**5. Adding two-point-orbit branches.** For each size-two vertex orbit, attach a new vertex \(p_O\) and \(a\) edges to distinct points, one in each simplex \(A_v\), of the connected complex constructed above. Since no two of these edges belong to a common new two-cell, choosing one connecting edge as a tree edge makes each of the remaining \(a-1\) edges add a free circle. Distinct size-two orbits have disjoint new vertices and no interactions. Thus they contribute exactly \(b(a-1)\) circles, without changing the existing two-sphere summands. The \(c\) size-three orbits supply isolated points. This proves the stated full homotopy classification.

## Verification
The included `verify_fixed_line.py` constructs each tested subgroup from permutations, independently enumerates edge-orbits and all simplices of the resulting geometric fixed-point complex, computes its mod-two boundary ranks, and compares every reduced Betti number against the theorem. It tests representatives of all single-generator cycle types through seven labels (with bounded seven-label cases) and pairs of cycle-type representatives through six labels, a total of 190 subgroup-generated cases. Execute with `python3 verify_fixed_line.py`; it prints `ALL 190 SUBGROUP SAMPLE CASES PASSED` on success. The finite tests are supporting checks only; Steps 1–5 prove the theorem for every \(n\ge4\) and every subgroup, including noncyclic subgroups not sampled.

Two hand checks illustrate the geometry. A four-cycle subgroup acting transitively on four labels has \(a=b=c=0\), so its fixed space is empty. A transposition subgroup on five labels has \((a,b,c)=(3,1,0)\) and fixed space homotopy equivalent to two circles. The trivial subgroup has \((a,b,c)=(n,0,0)\) and recovers the known wedge of \(\binom{n-1}{3}\) two-spheres.

## Relationship to prior work
Goyal, Shukla and Singh (arXiv:2009.12130, first posted 2020-09-25) prove the *ordinary* homotopy equivalence between the clique complex of a line graph and the two-skeleton of the original clique complex (Lemma 3.2), and recall the nonequivariant two-sphere wedge theorem for complete graphs. Neither statement identifies geometric fixed points under arbitrary subgroups of the vertex-permutation group. Ordinary homotopy equivalence is not, in general, an equivariant homotopy equivalence; replacing the present subgroup calculation with that lemma alone would be unjustified. The proof above classifies actual invariant edge-orbit simplices, including orbit-barycenter points invisible in the vertexwise fixed subcomplex.

The result is a fixed-point homotopy classification, stronger in a different direction than a group character or Euler-character formula: it determines connectivity, circle rank and two-sphere rank of every subgroup fixed locus, including the empty case.

## Limitations
This result concerns only complete-graph line-clique complexes and geometric subgroup fixed points. It does not assert an integral \(S_n\)-chain decomposition, a general equivariant equivalence for arbitrary graphs, or classifications for higher nonmatching complexes. The literature comparison cannot exclude an unindexed equivalent result; the original 2020 theorem is closely related and explicitly credited. The test program checks mod-two Betti numbers of finite cases; it is not an independent proof of the integral homotopy statement.

## References
1. S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130v1 (first public posting 2020-09-25); especially Section 3, Lemma 3.2, and the referenced nonequivariant complete-graph theorem. https://arxiv.org/abs/2009.12130 and https://arxiv.org/pdf/2009.12130
2. S. Linusson, J. Shareshian and V. Welker, earlier homotopy work on nonmatching complexes of complete graphs, cited as reference [13] and Theorem 2.1 in Goyal–Shukla–Singh. The source is used only for contextual attribution of the nonequivariant classification.
