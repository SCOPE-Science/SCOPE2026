# Exact open-independent locating codes of rectangular rook graphs

## Finding

Let \(m,n\ge 2\) be integers. The rectangular rook graph \(R_{m,n}=K_m\square K_n\) has vertex set \([m]\times[n]\), with two different cells adjacent precisely when they share a row or a column. A set \(S\) is an **open-independent open-locating-dominating code** if all sets \(N(v)\cap S\), for \(v\in V(R_{m,n})\), are nonempty and pairwise distinct, and each \(s\in S\) has exactly one neighbor inside \(S\).

Identify cells with the edges of the complete bipartite graph \(K_{m,n}\). Then \(S\) is such a code **if and only if** its selected edges form vertex-disjoint two-edge paths, in one of exactly three configurations:

1. The paths cover every original vertex of \(K_{m,n}\).
2. They cover every original vertex except one on the \(n\)-vertex side, and every path is centered on the \(m\)-vertex side. Necessarily \(n=2m+1\).
3. They cover every original vertex except one on the \(m\)-vertex side, and every path is centered on the \(n\)-vertex side. Necessarily \(m=2n+1\).

In the spanning case define integers
\[
a=\frac{2m-n}{3},\qquad b=\frac{2n-m}{3}.
\]
Here \(a\) is the number of paths centered in the \(n\)-vertex part and \(b\) is the number centered in the \(m\)-vertex part. Let \(C_{m,n}\) be the number of labeled codes. Exactly one of the following mutually exclusive cases can occur:
\[
C_{m,n}=\begin{cases}
\dfrac{m!n!}{2^{a+b}a!b!},&a,b\in\mathbb Z_{\ge0},\\[4pt]
\dfrac{n!}{2^m},&n=2m+1,\\[4pt]
\dfrac{m!}{2^n},&m=2n+1,\\[4pt]
0,&\text{otherwise}.
\end{cases}
\]
Every code that exists has exactly \(2\lfloor(m+n)/3\rfloor\) cells; consequently its complete cardinality generating polynomial is either zero or the single monomial
\[
C_{m,n}\,z^{2\lfloor(m+n)/3\rfloor}.
\]
In particular, the square board \(R_{q,q}\), for \(q\ge2\), admits a code exactly when \(q\equiv0\pmod 3\); in that case it has
\[
\frac{(q!)^2}{2^{2q/3}\big((q/3)!\big)^2}
\]
possible codes, each containing \(4q/3\) selected cells.

## Assumptions and scope

All graphs are finite, simple, and undirected; cells are labeled. The open neighborhood \(N(v)\) excludes \(v\) itself, and the distinct-signature requirement applies to **all** vertices, including selected vertices. The term two-edge path means a copy of \(P_3\) with three original vertices and two selected edges. The classification concerns open-independent open-locating-dominating sets, not merely open locating codes and not ordinary identifying codes using closed neighborhoods. The theorem is for all integer parameters \(m,n\ge2\); it makes no assertion about optimal codes without the open-independence restriction.

## Proof

**1. Selected components.** Regard the selected cells \(S\) as an edge set \(F\) of \(K_{m,n}\). A cell corresponding to an edge \(e\) has as selected rook neighbors exactly the other edges of \(F\) sharing an endpoint with \(e\). The code condition therefore says that every edge of \(F\) meets exactly one other edge of \(F\). The nonempty edge-connected components of \(F\) must be disjoint two-edge paths, with disjoint original-vertex supports. Indeed, the two edges incident in one such pair cannot meet a third selected edge, and pairs cannot share original vertices.

For each original vertex \(x\) of \(K_{m,n}\), let \(E_F(x)\) denote the set of selected edges incident with \(x\). At the two leaves of a selected path with edges \(e,f\), these sets are respectively \(\{e\}\) and \(\{f\}\); at its center the set is \(\{e,f\}\). Unused vertices have the empty set. For an unselected cell represented by an edge \(xy\), its code signature is precisely \(E_F(x)\cup E_F(y)\). For a selected cell, its signature is the singleton consisting of its paired selected edge.

**2. At most one unused original vertex.** Suppose two original vertices in different bipartition sides are unused. Their connecting edge has empty signature, contradicting open domination. Suppose instead distinct unused vertices \(x,y\) lie on one side. Taking any vertex \(w\) on the other side, the two distinct cells \(xw\) and \(yw\) both have signature \(E_F(w)\), contradicting location. Thus at most one original vertex can be unused.

**3. Orientation with one unused vertex.** If the unique unused vertex \(w\) lies in the \(n\)-vertex side, consider any selected two-edge path centered in that same side, with leaf \(x\) in the \(m\)-vertex side and selected edge \(e\) incident to \(x\). The unselected edge \(xw\) has the singleton signature \(\{e\}\), identical to the signature of the selected edge paired with \(e\). This is impossible. Therefore every selected path must be centered in the \(m\)-vertex side, using one such vertex and two vertices of the other side. All \(m\) left-side vertices are then centers, and precisely \(2m\) right-side vertices are used; hence \(n=2m+1\). The opposite orientation is symmetric. If no vertex is unused, the paths span all \(m+n\) vertices.

**4. Sufficiency.** Conversely, consider any edge collection of one of the three types. The selected edges have distinct singleton signatures, each being the other edge of its path. Any unselected cell joining vertices from two different path components has a signature containing at least one edge label from each component. Labels from different components are disjoint; the component pair, and then the precise endpoint of each component, are recoverable because the local incidence sets \(\{e\},\{f\},\{e,f\}\) are distinct. In the one-unused-vertex cases, each cell incident with that unused vertex meets a center of a path and has the two-label signature \(\{e,f\}\) from just one component. These signatures are distinct from each other and from those involving two components. There are no unselected cells with both endpoints inside one path: the two leaves are in the same part of the bipartition and the center-to-leaf edges are exactly the selected edges. Thus all signatures are nonempty and pairwise distinct, completing the equivalence.

**5. Counting.** In the spanning case let \(a\) paths be centered on the \(n\)-vertex side and \(b\) on the \(m\)-vertex side. Since the paths cover the two parts, necessarily \(m=2a+b\) and \(n=a+2b\), giving the displayed values of \(a,b\). Conversely, nonnegative integral values specify feasible spanning path factors. Choose the \(b\) left centers and \(a\) right centers, then partition and assign their complementary vertices in unordered pairs. The number is
\[
\binom mb\binom na\frac{(2a)!}{2^a}\frac{(2b)!}{2^b}
=\frac{m!n!}{2^{a+b}a!b!}.
\]
If one right vertex is unused, each of the \(m\) left vertices is a center, and an ordered allocation of pairs of distinct right vertices plus the unused one gives \(n!/2^m\). The other case is symmetric. These cases cannot overlap because the spanning case has \(m+n\equiv0\pmod3\), while each one-unused case has \(m+n\equiv1\pmod3\); the two one-unused cases cannot both hold for positive dimensions. Every path contributes exactly two selected edges, proving the uniform cardinality and monomial statements. Taking \(m=n=q\) gives the square-board corollary.

## Verification

The independent Python 3 program `check_rook_old.py` implements the code property directly from row/column adjacency, not from the path-factor characterization. It exhaustively enumerates all subsets of seventeen boards, from \(1\times1\) through \(4\times5\) in the specified test list (including \(3\times6\) and \(4\times4\)). These tests cover **1,501,038 labeled subsets** and compare the direct count with the stated formula for every board. All seventeen comparisons passed. Small one-row boards appear in the tests as extra boundary checks; the theorem itself assumes \(m,n\ge2\). Run `python3 check_rook_old.py` to reproduce. Computation corroborates finite cases; it is not used to infer the theorem for unbounded dimensions.

## Relationship to prior work

Seo and Slater introduced open-independent open-locating domination and proved a sufficient characterization in graphs of girth at least five, together with results for paths, trees, and infinite grids [1]. Rectangular rook graphs have triangles when at least one dimension is three or more, and the remaining \(2\times2\) rook graph has girth four. Thus their high-girth sufficiency theorem does not settle these graphs.

Cappelle, Coelho, Foulds, and Longo studied structural recognition and complexity and proved a necessary local degree condition, as well as classifications for \(P_4\)-tidy graphs and complementary prisms of cographs [2]. The necessary condition alone does not distinguish all code signatures in a rook graph; the \(P_4\)-tidy result can cover very small special cases but provides neither the two-parameter path-packing characterization nor the enumeration above. The general line-graph representation \(R_{m,n}\cong L(K_{m,n})\) is standard. No claim is made to originality of these prior definitions or known special cases.

## Limitations

This result is an exact theorem for this restricted family, not an algorithm for arbitrary graphs. It does not count unconstrained open-locating codes, and a statement about existence of a code does not imply that every minimum unrestricted code is open-independent. Publication-priority searches did not identify a dominating result in the inspected materials, but differently named edge-code or path-factor literature could contain an equivalent classification. Independent mathematical validation remains outstanding.

## References

[1] S. J. Seo and P. J. Slater, *Open-independent, open-locating-dominating sets*, Electronic Journal of Graph Theory and Applications 5(2) (2017), 179–193. DOI: 10.5614/ejgta.2017.5.2.2. Full text: https://www.ejgta.org/index.php/ejgta/article/download/210/pdf_47

[2] M. R. Cappelle, E. Coelho, L. R. Foulds, and H. J. Longo, *Open-independent, open-locating-dominating sets: structural aspects of some classes of graphs*, Discrete Mathematics & Theoretical Computer Science 24:1 (2022), article 5; first public preprint 14 March 2021, arXiv:2103.07972. DOI: 10.46298/dmtcs.8440. Full text: https://arxiv.org/html/2103.07972v4
