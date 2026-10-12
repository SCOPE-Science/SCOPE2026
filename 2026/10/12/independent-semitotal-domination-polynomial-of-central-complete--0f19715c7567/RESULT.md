# Independent semitotal domination polynomial of central complete multipartite graphs

## Finding

Let \(G=K_{n_1,\ldots,n_r}\), where \(r\ge2\) and all part sizes \(n_i\ge1\). Its central graph \(C(G)\) is obtained by subdividing every edge once and connecting every originally nonadjacent pair. An independent semitotal dominating set is independent, dominating, and has for each selected vertex another selected vertex at graph distance exactly two.

Count these sets by cardinality and by their selected original vertices:
\[
J_G(z,w)=\sum_{D\in\mathrm{IST}(C(G))}z^{|D|}w^{|D\cap V(G)|}.
\]
For a support \(S\subseteq[r]\), put \(a_i(S)=n_i-\mathbf1_{i\in S}\), \(q(S)=\sum_i a_i(S)\), \(B_i(S)=\sum_{j\ne i}a_j(S)\), and \(e(S)=\sum_{i<j}a_i(S)a_j(S)\). Call \(S\) admissible precisely when all three conditions hold:

1. \(B_i(S)\ge1\) for every \(i\notin S\).
2. If \(S=\{i\}\), then \(a_i(S)\ge1\) and \(B_i(S)\ge1\).
3. If \(q(S)=2\) and the two residual vertices belong to different parts \(i,j\), then \(S\cap\{i,j\}\ne\varnothing\).

**Theorem.** The complete bivariate distribution is
\[
\boxed{J_G(z,w)=\sum_{S\text{ admissible}}
 \left(\prod_{i\in S}n_i\right)z^{|S|+e(S)}w^{|S|}.}
\]
More precisely, every feasible set has one unique form: select exactly one original vertex from every part indexed by \(S\), then select every subdivision vertex whose two original endpoints were not selected. No other vertices may be selected.

When every \(n_i\ge2\), every support is admissible, and hence
\[
J_G(z,w)=\sum_{S\subseteq[r]}\left(\prod_{i\in S}n_i\right)z^{|S|+e(S)}w^{|S|},
\qquad J_G(1,1)=\prod_i(1+n_i).
\]
For \(r\ge3\) with all \(n_i\ge2\), the minimum size is \(r+\sum_{i<j}(n_i-1)(n_j-1)\), realized by exactly \(\prod_i n_i\) sets. For \(r=2\), writing the part sizes \(a,b\ge2\), the minimum is \(2+(a-1)(b-1)\); there are precisely \(ab+a\mathbf1_{a=2}+b\mathbf1_{b=2}\) minima.

At the singleton boundary \(G=K_m\), for \(m\ge2\),
\[
J_{K_m}(z,1)=z^m+\mathbf1_{m\ge3}z^{\binom m2}
+\sum_{t=2}^{m-3}\binom mt z^{t+\binom{m-t}{2}},
\]
where the sum is empty if its upper limit is below two. Thus for \(m=4\) the only minimum set has size four; for \(m=3\) and every \(m\ge5\), the minimum size is \(m\) and the number of minimum sets is \(1+\binom m3\).

## Assumptions and scope

All graphs are finite, simple, and undirected. The \(r\) partite classes are labelled, each of positive size, and \(r\ge2\). Distances are computed in the entire central graph, not in the chosen set. The definition above permits \(K_2\) and includes singleton parts. The polynomial counts labelled vertex subsets, not graph-isomorphism types. \(\mathbf1_P\) denotes the indicator of proposition \(P\). An empty product is one and an empty sum is zero.

## Proof

Write \(X=D\cap V(G)\). Distinct original vertices are adjacent in \(C(G)\) precisely when they belonged to one part of \(G\). Thus independence requires at most one vertex from each part; write \(S\) for those parts. A subdivision vertex belonging to an original edge \(uv\) is adjacent only to \(u\) and \(v\). If neither endpoint was selected, domination forces that subdivision vertex into \(D\); if either endpoint was selected, independence excludes it. Consequently \(D\) is uniquely determined by \(X\): it consists of \(X\) and all subdivision vertices indexed by edges of \(G-X\). This immediately gives \(|D|=|S|+e(S)\) and multiplicity \(\prod_{i\in S}n_i\).

Every unselected original vertex in a selected part is dominated by the selected original of its part. For a part \(i\notin S\), an unselected original vertex sees no chosen original, so it is dominated exactly when it is incident to some edge of \(G-X\). This is equivalent to \(B_i(S)\ge1\), establishing condition 1 as necessary and sufficient for domination once the forced template is fixed.

We next check the distance-two witnesses. Two chosen originals lie in different parts of \(G\) and therefore have distance two in \(C(G)\), through the subdivision of their joining edge. Thus when \(|S|\ge2\), all chosen originals have witnesses. If \(S=\{i\}\), the unique chosen original is at distance two from a selected subdivision vertex precisely when that edge has one endpoint in its own part (an unchosen original adjacent to it in \(C(G)\)) and one endpoint outside it. Such an edge exists precisely when \(a_i(S)\ge1\) and \(B_i(S)\ge1\); this is condition 2. If \(S\) is empty, there are no originals to test.

Two subdivision vertices are at distance two exactly when their original edges share an endpoint. A chosen subdivision vertex indexed by \(uv\) is at distance two from a chosen original vertex exactly when that vertex belongs to the same part as \(u\) or \(v\). For the residual complete multipartite graph \(G-X\), if there are at least three vertices and at least one edge, every edge shares an endpoint with another edge. Thus all chosen subdivision vertices then have witnesses. When there are exactly two residual vertices in different parts, the sole chosen subdivision vertex has no subdivision witness, but has an original witness precisely when a selected original lies in one of its two endpoint parts. This is condition 3. With fewer than two residual vertices, or two in the same part, there are no chosen subdivision vertices. Therefore the three conditions are together necessary and sufficient, proving the formula.

If every part has size at least two, condition 1 holds because every other part retains at least one vertex; condition 2 holds because the sole selected part retains a vertex and another part remains; and condition 3 is automatic because a two-vertex residual edge can arise only for two parts of size two with both parts selected. This proves the simplified enumerator and the total count.

Adding an omitted part \(i\) to \(S\) changes \(|S|+e(S)\) by \(1-B_i(S)\). If \(r\ge3\) and all sizes are at least two, then \(B_i(S)\ge r-1\ge2\), so a minimizing support must include all parts. When \(r=2\), equality in such an addition occurs only when the other residual part has size one, yielding exactly the extra optimal singleton supports described above. For complete graphs, every part has size one: condition 1 excludes \(|S|=m-1\); condition 2 excludes \(|S|=1\); and condition 3 excludes \(|S|=m-2\), leaving \(S=\varnothing\) for \(m\ge3\), every \(2\le|S|\le m-3\), and \(S=[m]\). Evaluating their exponents gives the stated polynomial. Among its terms, only \(|S|=m-3\) can match the size-\(m\) term when \(m\ge5\), while the stated small cases follow directly.

## Verification

The independent standard-library verifier `verify.py` generates each central graph, computes all-pairs shortest-path distances, and tests independence, domination, and distance-two witnesses directly. It exhaustively compared every subset of the constructed central graph against the formula for 36 part-size profiles, covering 2,272,392 tested subsets; every comparison passed. Four larger profiles were checked on every predicted set without making a claim of exhaustive enumeration of their full powersets. For instance, the formula gives \(J_{K_{2,2,2}}(z,1)=8z^6+12z^7+6z^9+z^{12}\), in agreement with direct enumeration. The universal proof is structural and does not rely on finite tests.

Reproduce using `python3 verify.py`; `verification_output.txt` records the precise output.

## Relationship to prior work

Cabrera-Martínez, López-Carmona, Rios-Villamar, and Serrano-Díaz (2026) study independent semitotal domination numbers of subdivision, middle and central graph operators. Their publicly accessible abstract describes minimum-cardinality formulas, whereas the present claim is the complete size-and-original-support distribution on arbitrary complete multipartite inputs, including singleton transitions. The originating work of the same authors on independent domination of central graphs concerns the weaker condition without distance-two witnesses. Earlier studies treat independent semitotal domination on lexicographic products and other operations. No assertion is made that generic independent domination, or the scalar minimum of the new variant, was first introduced here.

## Limitations

The result covers central graphs of complete multipartite graphs only, not arbitrary central graphs and not other operators. The principal September 2026 preprint could not be inspected in full through available access paths; an equivalent all-set result or stronger structural lemma in its uninspected sections is a residual originality risk. The stated verification is finite, and there has been no independent external audit.

## References

1. A. Cabrera-Martínez, J. L. López-Carmona, I. Rios-Villamar, A. Serrano-Díaz, *On the (independent) semitotal domination in subdivision, middle, and central graphs*, arXiv:2609.33932v1 (first public version September 27, 2026).
2. A. Cabrera-Martínez, J. L. López-Carmona, I. Rios-Villamar, A. Serrano-Díaz, *Independent domination in central graphs*, arXiv:2609.16357v1 (September 14, 2026).
3. B. L. Susada, R. G. Eballe, *Independent semitotal domination in the lexicographic product of graphs*, Advances and Applications in Discrete Mathematics 39 (2023), 237–244, doi:10.17654/0974165823050.
