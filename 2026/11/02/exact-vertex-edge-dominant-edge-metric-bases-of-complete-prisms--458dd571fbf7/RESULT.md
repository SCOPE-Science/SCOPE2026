# Exact vertex-edge dominant edge-metric bases of complete prisms

## Finding

Let \(H_n=K_n\square K_2\), where \(n\ge2\). A vertex set \(S\) is an *edge resolving set* if, for any two distinct edges \(e,f\), some \(s\in S\) satisfies \(d(s,e)\ne d(s,f)\), where \(d(s,uv)=\min\{d(s,u),d(s,v)\}\). It is also *vertex-edge dominating* if every edge \(e\) satisfies \(d(s,e)\le1\) for at least one \(s\in S\). A set satisfying both requirements is a vertex-edge dominant edge resolving set, and its minimum size is denoted \(\gamma_{emd}(H_n)\).

**Theorem.** For every integer \(n\ge2\),
\[
\gamma_{emd}(H_n)=\operatorname{edim}(H_n)=
\begin{cases}n,&2\le n\le6,\\ n-1,&n\ge7.\end{cases}
\]
All minimum sets are classified as follows. Let \(x_i,y_i\) be the two vertices in matched column \(i\), with \(1\le i\le n\).

- For \(n\ge7\), exactly one matched column is empty, every other column contributes exactly one selected vertex, and at least three selected vertices lie in each clique layer.
- For \(2\le n\le6\), either one matched column is empty, a different matched column contributes both endpoints, and every remaining column contributes exactly one endpoint; or every column contributes exactly one endpoint, with the following layer restrictions: for \(n\le4\), the entire selection lies in a single clique layer, while for \(n=5,6\), either the entire selection lies in one layer or both layers contain at least two selected vertices.

All selected vertex sets are labeled (no quotient by graph automorphisms). Their number \(M_n\) is
\[
M_n=\begin{cases}
 n(n-1)2^{n-2}+2,&2\le n\le4,\\
 n(n-1)2^{n-2}+2^n-2n,&n=5,6,\\
 n\displaystyle\sum_{j=3}^{n-4}\binom{n-1}{j},&n\ge7.
\end{cases}
\]
In the last case, equivalently \(M_n=n[2^{n-1}-2-2(n-1)-2\binom{n-1}{2}]\). In particular, the minimum drops from \(n\) to \(n-1\) exactly at \(n=7\).

## Assumptions and scope

All graphs are simple, finite, and undirected. The two clique layers are labeled \(X=\{x_1,\ldots,x_n\}\) and \(Y=\{y_1,\ldots,y_n\}\); the only cross-layer edges are the matching edges \(m_i=x_iy_i\). Write \(x_I=x_ix_j\) and \(y_I=y_iy_j\) for any two-element index set \(I=\{i,j\}\). A selected set \(S\) determines index sets \(A=\{i:x_i\in S\}\), \(B=\{i:y_i\in S\}\), and support \(T=A\cup B\). A *missing column* is an index outside \(T\); a *doubled column* lies in \(A\cap B\). The theorem covers all integer orders \(n\ge2\) including \(H_2\cong C_4\).

## Proof

**1. Edge-distance comparison.** Cartesian distances give \(d(x_k,y_j)=1+\mathbf 1_{k\ne j}\) and \(d(x_k,x_j)=\mathbf 1_{k\ne j}\). Thus for any two-element \(I\),
\[
\begin{aligned}
d(x_k,m_i)&=d(y_k,m_i)=\mathbf1_{k\ne i},\\
d(x_k,x_I)&=\mathbf1_{k\notin I},&d(y_k,x_I)&=1+\mathbf1_{k\notin I},\\
d(y_k,y_I)&=\mathbf1_{k\notin I},&d(x_k,y_I)&=1+\mathbf1_{k\notin I}.
\end{aligned}
\]
Consequently, for two distinct two-element index sets \(I,J\), the horizontal edges \(x_I,x_J\) (and likewise \(y_I,y_J\)) are indistinguishable precisely when \(T\cap(I\triangle J)=\varnothing\). Two matching edges \(m_i,m_j\) are indistinguishable precisely when \(T\cap\{i,j\}=\varnothing\). A horizontal edge \(x_I\) and matching edge \(m_h\) are indistinguishable precisely when
\[
A\cap(I\triangle\{h\})=\varnothing
\quad\text{and}\quad B\subseteq I\setminus\{h\}.
\tag{1}
\]
The criterion for \(y_I,m_h\) interchanges \(A,B\). Finally, \(x_I\) and \(y_J\) are indistinguishable precisely when
\[
A\subseteq J\setminus I\quad\text{and}\quad B\subseteq I\setminus J.
\tag{2}
\]
These are all possible unordered edge-type comparisons and follow directly by substituting the displayed edge distances. Their hypotheses are necessary *and* sufficient.

**2. Universal lower bound and edge domination.** If two columns \(i,j\) are missing, the matching edges \(m_i,m_j\) have identical distance vectors. Hence every edge resolving set has at most one missing column and therefore at least \(n-1\) vertices. Conversely, every edge resolving set in this graph automatically vertex-edge dominates: for a horizontal edge in layer \(X\), if any \(x_k\) is selected then its distance to this edge is at most one; if no \(x_k\) is selected, at least one of the two edge indices must occur in \(B\), since at most one column is missing, and its selected \(y\)-vertex has distance one. The same argument holds for layer \(Y\). Every selected vertex has distance at most one from every matching edge \(m_i\). Thus the two minimum parameters and their minimum bases coincide.

**3. The \(n-1\) case.** Equality in the lower bound forces one missing column \(h\), exactly one selected endpoint from every other column, and no doubled column: \(A\cap B=\varnothing\) and \(A\cup B=[n]\setminus\{h\}\).

If \(B=\varnothing\), choose any \(a\in A\). Formula (1) shows that \(x_{\{h,a\}}\) and \(m_a\) collide. If \(B=\{b\}\), the pair \(x_{\{h,b\}},m_h\) collides. If \(B=\{b,c\}\), the pair \(x_{\{b,c\}},m_h\) collides. By symmetry, \(|A|\le2\) is likewise impossible. Therefore an \(n-1\)-vertex edge resolving set must have \(|A|,|B|\ge3\), which requires \(n\ge7\).

Conversely, assume one missing column, no doubled column, and \(|A|,|B|\ge3\). The support misses just one index, so any two matching edges and any two distinct horizontal edges in one layer are distinguished: \(|I\triangle J|\ge2\) for distinct two-element \(I,J\). Condition (1) fails because its second requirement would place at least three indices of \(B\) inside a set of size at most two; its reversed version fails similarly for \(A\). Condition (2) fails because its two right-hand sets each have cardinality at most two. Thus all edges are distinguished, and by Step 2 every edge is also vertex-edge dominated. This proves the \(n\ge7\) classification and, because the lower bound is attained, the asserted minimum.

**4. All \(n\)-vertex bases when \(n\le6\).** Selecting all \(x_i\) is edge resolving by the criteria in Step 1, so \(\gamma_{emd}(H_n)\le n\); the nonexistence of \(n-1\)-vertex bases from Step 3 then proves equality. A size-\(n\) set with at most one missing column must be either (i) a transversal with one selected endpoint in every column, or (ii) one missing column and one doubled column with every other column singly occupied.

In (ii), any mixed horizontal-layer comparison (2) is distinguished by the vertex chosen in both layers of the doubled column, since that index cannot simultaneously lie in \(J\setminus I\) and \(I\setminus J\). Formula (1) and its reversal cannot hold because the doubled-column vertex in both layers would require that index simultaneously to belong and not belong to \(I\). The same-type comparisons are distinguished because just one column is missing. Hence every such set works.

In (i), a full layer works. If both layers are nonempty and one has exactly one selected index \(b\), say \(B=\{b\}\), choose any \(a\in A\); formula (1) makes \(x_{\{a,b\}}\) and \(m_a\) collide. When \(n=4\) and \(|A|=|B|=2\), take \(I=B\), \(J=A\); formula (2) makes \(x_I,y_J\) collide. For \(n=5,6\), any remaining mixed-layer transversal has \(|A|,|B|\ge2\). Condition (1) cannot hold: with \(|B|\ge2\), it would force \(I=B\), \(h\notin I\), but then \(h\in A\), contradicting its first requirement; similarly for the reversed criterion. Condition (2) cannot hold because \(A\sqcup B=[n]\) has at least five elements whereas \((J\setminus I)\sqcup(I\setminus J)\) has at most four. Same-type comparisons are automatically distinguished. This completes the low-order classification.

**5. Counting.** For \(n\ge7\), choose the omitted column in \(n\) ways and the \(j\) selected vertices in layer \(X\) among the other \(n-1\) columns, where \(3\le j\le n-4\). This yields the stated sum. For \(2\le n\le6\), the missing-and-doubled class has \(n(n-1)2^{n-2}\) sets: choose the hole, choose the doubled column, then choose one endpoint in each other column. The allowed full transversals number two when \(n\le4\); when \(n=5,6\) they number \(2^n-2n\), obtained by excluding precisely the \(2n\) arrangements with a singleton minority layer. No two classes overlap. The displayed formulas follow. \(\square\)

## Verification

The standalone Python 3 script `verification/check_basis.py` constructs \(K_n\square K_2\) from graph adjacencies, obtains all vertex distances by breadth-first search, constructs all edge–vertex distance vectors, and independently enumerates every candidate vertex subset of the theorem's minimum size for \(2\le n\le11\). It checks both edge resolution and distance-one domination, verifies the exact structural classification for **every** candidate, and compares exact base counts. Execute `python3 verification/check_basis.py`. Successful execution ends with `VERIFY_OK`. This finite check is corroborative; the proof for all orders is the five-step argument above.

## Relationship to prior work

Ikhlaq, Hayat, and Siddiqui introduced vertex-edge dominant edge metric dimension in their paper publicly posted on 2022-11-17 and evaluated it on paths, cycles, complete bipartite graphs, and certain path–path and cycle–path Cartesian products; their examined Cartesian-product results do not classify \(K_n\square K_2\) for arbitrary \(n\). Chandran and Reji (2024, Section 3, Theorem 1) prove the broader inequality \(\operatorname{edim}(G)\le\operatorname{edim}(G\square K_2)\le\operatorname{edim}(G)+1\). Applied to \(G=K_n\), it gives only the interval \([n-1,n]\), not which endpoint occurs or the full set of extremizers. An indexed record on mixed metric dimension of complete prisms gives minimum \(n\) for \(n\ge5\), but mixed resolution additionally distinguishes vertex–vertex and vertex–edge pairs, so its result neither supplies the \(n-1\) edge-only bases nor implies this classification. Exact external publication priority is not independently certified.

## Limitations

The theorem is specific to two complete-graph layers linked by a matching, with \(n\ge2\). It does not address more than two layers, arbitrary clique joins, non-Cartesian prisms, nor mixed metric dimension. The independent audit status is not performed. A summary-level record of closely related mixed metric work was accessible, but its full source was not inspected; relevant unindexed literature could also exist.

## References

1. H. M. Ikhlaq, S. Hayat, H. M. A. Siddiqui, *Unique identification and domination of edges in a graph: The vertex-edge dominant edge metric dimension*, arXiv:2211.09327, originally posted 2022-11-17. https://arxiv.org/abs/2211.09327
2. S. Chandran C. and Reji T., *Edge metric dimension of some Cartesian product of graphs*, Proyecciones 43(3) (2024), 587–611, DOI:10.22199/issn.0717-6279-5770. https://www.scielo.cl/scielo.php?pid=S0716-09172024000300587&script=sci_arttext
3. *Mixed metric bases of complete prisms*, relevant indexed research record: https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-mixed-metric-bases-of-complete-prisms--2c5387cbdbd0
