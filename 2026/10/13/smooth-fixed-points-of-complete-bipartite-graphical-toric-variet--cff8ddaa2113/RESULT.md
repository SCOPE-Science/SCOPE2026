# Smooth fixed points of complete-bipartite graphical toric varieties: an exact enumerator

## Finding

For integers \(a,b\ge2\), let \(G=K_{a,b}\) have disjoint labeled color classes \(A\) and \(B\) of sizes \(a\) and \(b\). Let \(X_{a,b}\) be the normal projective toric variety associated with the normal fan of its graphical zonotope. Write \(S(a,b)\) for the number of **smooth torus-fixed points**. Put \((q)_r=q!/(q-r)!\) for \(0\le r\le q\).

Every torus-fixed point is indexed by a unique acyclic orientation \(\omega\). Successively remove all current sources of \(\omega\), obtaining nonempty monochromatic layers \(B_1,\ldots,B_k\) alternating between \(A\) and \(B\). For \(a,b\ge2\), the point is smooth, equivalently locally \(\mathbb Q\)-factorial, exactly when all strictly interior layers are singletons. Such an orientation necessarily has at least four layers.

Its complete two-parameter enumerator is

\[
S(a,b)=2\sum_{r=2}^{\min(a,b)}(a)_{r-1}(b)_{r-1}
+\mathbf 1_{a>b}(a)_{b-1}b!\bigl(2^{a-b+1}-2\bigr)
+\mathbf 1_{b>a}(b)_{a-1}a!\bigl(2^{b-a+1}-2\bigr),
\]
where the indicator notation has its usual meaning. Equivalently, the bivariate exponential generating function is

\[
\sum_{a,b\ge2}\frac{S(a,b)}{a!b!}x^a y^b
=\frac{xy}{1-xy}\left(
2(e^x-1)(e^y-1)
+x(e^y-1)^2+y(e^x-1)^2\right).
\]
In the balanced case one obtains

\[
S(m,m)=2(m!)^2\sum_{j=1}^{m-1}\frac1{(j!)^2},\qquad
\lim_{m\to\infty}\frac{S(m,m)}{(m!)^2}
=2\sum_{j=1}^{\infty}\frac1{(j!)^2}.
\]

For a two-vertex color class, \(S(2,b)=b2^b\) for every \(b\ge2\). For \((a,b)=(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\), the respective counts are \(8,24,64,90,312,1472\).

## Assumptions and scope

Work over \(\mathbb C\) with the root lattice \(M=\{(z_i)\in\mathbb Z^{a+b}:\sum_i z_i=0\}\) and dual lattice \(N=\operatorname{Hom}(M,\mathbb Z)\). The graphical zonotope \(Z_G\subset M_{\mathbb R}\) is the Minkowski sum \(\sum_{\{i,j\}\in E(G)}[0,e_i-e_j]\); segment orientation changes only translation and not its normal fan. The torus-fixed-point/acyclic-orientation bijection is canonical. Smoothness and local \(\mathbb Q\)-factoriality are evaluated **only at these fixed points**; no classification of the whole smooth or singular loci is asserted.

## Proof

**1. Canonical alternating layers.** In an acyclic orientation of a complete bipartite graph, all sources lie on one color side: sources of different colors would force their common edge in both directions. Delete all sources and iterate. As long as both sides remain, the source side alternates, since every remaining vertex of the previously active color has an incoming edge from a remaining opposite-color vertex. The resulting ordered sequence of layers is therefore alternating; all its blocks are nonempty, and the orientation is recovered uniquely by directing all edges from earlier blocks to later blocks. Conversely any alternating nonempty monochromatic ordered partition defines an acyclic orientation whose successive source layers are those blocks. This establishes a bijection without overcounting permutations within a monochromatic block.

**2. Facets and smoothness.** The normal cone \(\sigma_\omega\subset N_{\mathbb R}\) is the chamber of inequalities \(t_u\le t_v\) for directed edges \(u\to v\) in \(\omega\). The induced partial order is the transitive closure of these inequalities. The cover relations are **exactly** all \(|B_i||B_{i+1}|\) directed edges between each pair of successive source layers: these edges admit no intermediate vertex, whereas every edge joining nonconsecutive blocks factors through vertices in intermediate alternating layers. Thus the facets of \(\sigma_\omega\) are precisely these covers, and their undirected graph \(H_\omega\) is the union of complete bipartite graphs between consecutive layers.

The graph \(H_\omega\) is connected on \(a+b\) vertices. For two layers it equals \(K_{a,b}\), which contains a four-cycle because \(a,b\ge2\). For at least three layers, if an interior block has two vertices, adjoining any vertices in the immediately preceding and following blocks forms a four-cycle. Conversely, if every interior block is a singleton, \(H_\omega\) is a path with possible leaf-stars attached at the two ends, hence a tree. This gives the asserted criterion. A chamber is simplicial iff its Hasse graph is a tree, by the general cone-poset criterion. In that case the facet linear forms \(e_u-e_v\) on the edges of the tree constitute a \(\mathbb Z\)-basis of \(M\), so the primitive rays of its dual cone form a lattice basis and the associated toric fixed point is smooth. In a non-tree case the cone has more than \(a+b-1\) facets and is nonsimplicial, making the fixed point non-\(\mathbb Q\)-factorial. Hence the criterion is also an integral toric smoothness criterion, not merely a rational simplicity criterion.

**3. Even-length enumeration.** Suppose there are \(2r\ge4\) alternating blocks, starting in \(A\) and ending in \(B\). The \(r-1\) interior blocks of color \(A\) and \(r-1\) of color \(B\) must each contain a single labeled vertex. They can be chosen in \((a)_{r-1}(b)_{r-1}\) ways, and the two end blocks consist of all remaining vertices in their respective colors. These are nonempty exactly when \(2\le r\le\min(a,b)\). Reversing colors doubles the count, giving the sum term.

**4. Odd-length enumeration.** A sequence of \(2r+1\ge5\) blocks beginning and ending in \(A\) must have every one of the \(r\) blocks of color \(B\) singleton, so \(r=b\); the \(b-1\) interior \(A\)-blocks are singleton too. After their labeled choices, \(a-b+1\) vertices remain to be divided between two *ordered, nonempty* endpoint blocks in \(2^{a-b+1}-2\) ways, requiring \(a>b\). This gives \((a)_{b-1}b!(2^{a-b+1}-2)\). The symmetric case starting and ending in \(B\) gives the final term. The cases exhaust all orientations satisfying the smoothness criterion.

**5. Bivariate generating function.** Denote \(A(x)=e^x-1\), \(B(y)=e^y-1\). An endpoint block of the respective color contributes \(A(x)\) or \(B(y)\) to the exponential generating function, while an interior singleton of that color contributes \(x\) or \(y\). Even block lengths contribute \(2A(x)B(y)xy/(1-xy)\). Odd lengths beginning and ending in \(A\), respectively \(B\), contribute \(A(x)^2y/(1-xy)\) and \(B(y)^2x/(1-xy)\). Restricting to \(a,b\ge2\) subtracts the cases having a color class of size one: \(yA(x)^2\) and \(xB(y)^2\). Simplification gives the stated generating function. When \(a=b=m\) the odd-length terms vanish, and reindexing the even sum yields the balanced formula and its convergent limiting series.

## Verification

The standalone standard-library script `verify_graphical_zonotope.py` enumerates every orientation on \(K_{a,b}\) for six parameter pairs. For each acyclic orientation it independently computes the transitive reduction via alternate directed paths, reconstructs source layers, checks the Hasse-cover characterization and tree criterion, and compares the number of smooth points with the formula. The following pairs were checked exhaustively: \((2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\). The script additionally checks the balanced factorial-square identity through \(m=14\). The exact output is embedded in `verify_graphical_zonotope_output.txt`. The unrestricted theorem relies on the proof above, **not** on finite enumeration.

## Relationship to prior work

The known general correspondence between acyclic orientations and graphical-zonotope vertices, and the criterion that a chamber is simplicial iff its associated Hasse poset is a tree, appear explicitly in Postnikov–Reiner–Williams (2006/2007), notably Proposition 3.5 and Section 5. Ardila (2004), in the complete-bipartite arrangement, already describes regions by alternating ordered color blocks and enumerates **all** regions; both facts are used here as established foundational material. Grujić (2016) computes the **total** face polynomial of a graphical zonotope, and Carballosa–Khera–Reyes (2023) enumerate acyclic orientations with other constraints. Those are not the same weighted subset as the smooth fixed points.

The contribution here is the joint, all-parameter **filtered enumeration**: the precise singleton-interior characterization of the smooth chambers, the resulting closed two-parameter integer count, and the bivariate generating function and balanced limit. The generic fan-poset criterion, the general block model, the total vertex counts, and the toric smoothness criterion themselves are **not** claimed as new. This calculation may admit an unindexed previous specialization; the cited literature and searches do not establish one.

## Limitations

The result concerns torus-fixed points, not singular components away from them or the full non-fixed smooth locus. It does not count or classify fixed points of each nonzero local divisor-class-group rank. The proof uses characteristic-zero toric language but the elementary fan arithmetic is integral. Exhaustive computations cover only finite displayed instances. The existence of an equivalent historical count outside the inspected literature is not excluded. Independent mathematical validation has not been performed.

## References

- F. Ardila, *A tropical morphism related to the hyperplane arrangement of the complete bipartite graph*, arXiv:math/0404287, first posted 16 April 2004; Sections 1–2.
- A. Postnikov, V. Reiner, L. Williams, *Faces of generalized permutohedra*, arXiv:math/0609184, first posted 6 September 2006; Proposition 3.5, Corollary 3.7, Section 5.
- V. Grujić, *Counting faces of graphical zonotopes*, arXiv:1604.06931, first posted 23 April 2016; Theorem 1.1 and Sections 2–5.
- J. Carballosa, D. Khera, F. Reyes, *Encoding and Enumerating Acyclic Orientations of Graphs*, arXiv:2303.09021, first posted 2023; complete-bipartite enumeration.
