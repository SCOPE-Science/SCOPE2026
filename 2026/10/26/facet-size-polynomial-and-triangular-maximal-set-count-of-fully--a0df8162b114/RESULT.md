# Facet-size polynomial and triangular maximal-set count of fully whiskered paths

## Finding
Let \(m\ge2\), and let \(T(\mathbf t)\) be formed from the path \(v_1\cdots v_m\) by attaching \(t_i\ge1\) distinct leaves to each \(v_i\). An edge-general-position set contains no three edges on a single geodesic. A *facet* is an edge-general-position set maximal under inclusion, not necessarily of maximum cardinality. Define
\[
T_0=\sum_{i=1}^m t_i,\qquad L_i=\sum_{h=1}^{i}t_h,\qquad R_i=\sum_{h=i+1}^{m}t_h,\qquad M_{ij}=\sum_{h=i+1}^{j}t_h.
\]
The polynomial enumerating **all inclusion-maximal** edge-general-position subsets by their sizes is
\[
\boxed{\mathcal F_{\mathbf t}(z)=z^{T_0}+z\sum_{i=1}^{m-1}\bigl(z^{L_i}+z^{R_i}\bigr)+z^2\sum_{1\le i<j\le m-1}z^{M_{ij}}.}
\]
In particular, the number of facets is
\[
\boxed{\mathcal F_{\mathbf t}(1)=\frac{m(m+1)}2,}
\]
**independently of the numbers of attached leaves**. If \(m\ge3\), the minimum size of an inclusion-maximal edge-general-position set (the lower edge-general-position number) is exactly
\[
\boxed{\min\left\{t_1+1,\ t_m+1,\ 2+\min_{2\le i\le m-1}t_i\right\}.}
\]
For \(m=2\), it is \(\min\{t_1+1,t_2+1,t_1+t_2\}\). The maximum feasible cardinality is \(T_0\), as also follows from the previously established maximum formula for arbitrary trees. For \(m\ge3\) and \(t_i=r\ge1\), the facet sizes include both \(r+1\) and \(mr\); their difference can grow without bound although there are always just \(m(m+1)/2\) facets.

## Assumptions and scope
All graphs are finite simple undirected graphs. The path vertices and all attached leaves are distinct; in particular \(t_i\) are positive integers, not merely nonnegative. Write \(e_i=v_iv_{i+1}\) for the spine edge at position \(i\), with \(1\le i<m\), and \(P_i\) for the set of \(t_i\) pendant edges at \(v_i\). For any indices \(a\le b\), write \(P_{[a,b]}=\bigcup_{h=a}^bP_h\). Empty unions are empty. A geodesic in a tree is its unique path between its endpoints. Each facet is counted once as a labeled edge subset.

## Proof
**Path classification.** Every tree geodesic contains at most two pendant edges. If a feasible set contains at least three spine edges, those three lie on a common geodesic joining the two ends of the spine, which is forbidden. Therefore every feasible set has zero, one, or two chosen spine edges.

With no chosen spine edge, *every* pendant-edge subset is feasible. Suppose the only chosen spine edge is \(e_i\). If one chosen pendant edge is attached on the left side \(P_{[1,i]}\) and another on the right side \(P_{[i+1,m]}\), the geodesic between the two leaves passes through all three selected edges. Hence all chosen pendants must be on one side of \(e_i\). Conversely, with them confined to one side, a geodesic crosses \(e_i\) at most once and uses at most one of those pendant edges on its left/right end. Consequently no geodesic has three selected edges.

Suppose exactly two spine edges \(e_i,e_j\), with \(i<j\), are selected. A selected pendant attached at position \(h\le i\) or \(h\ge j+1\), together with \(e_i,e_j\), lies on the geodesic from its leaf to the opposite endpoint of the spine. These positions are forbidden. Conversely, all selected pendants attached at positions \(i+1\le h\le j\) are compatible, because a geodesic containing both selected spine edges cannot visit any such pendant leaf, while a path containing one such pendant edge cannot contain both chosen spine edges. This proves the three disjoint forms of feasible sets.

**Facet classification.** Put \(P=\bigcup_{h=1}^mP_h\). The maximal feasible sets are exactly:

1. \(P\), with no spine edge;
2. \(\{e_i\}\cup P_{[1,i]}\) and \(\{e_i\}\cup P_{[i+1,m]}\), for each \(1\le i<m\);
3. \(\{e_i,e_j\}\cup P_{[i+1,j]}\), for each \(1\le i<j<m\).

To check maximality, all allowed pendants have been included. In the first form, every spine edge has a selected pendant on each side because all \(t_i\ge1\). In the second form, adding a pendant across \(e_i\) is forbidden; adding any additional spine edge \(e_j\) produces a path containing \(e_i,e_j\) and an already selected pendant in the extreme end bundle (\(P_1\) for the left form, \(P_m\) for the right form). In the third form, adding a pendant outside the interval forces a geodesic through both selected spine edges, and adding any spine edge creates three selected spine edges on the spine geodesic. Therefore all displayed sets are facets.

Every proper feasible set with no spine edge extends to \(P\); with one spine edge extends to at least one set of the second form; and with two spine edges extends to the set of the third form. Thus no other facets exist. Positive bundle sizes make these facets distinct, even when some have equal cardinalities.

The sizes of the three families are \(T_0\), \(1+L_i\) and \(1+R_i\), and \(2+M_{ij}\), giving the stated polynomial. There are respectively \(1\), \(2(m-1)\), and \(\binom{m-1}{2}\) such sets, hence \(1+2(m-1)+\binom{m-1}{2}=m(m+1)/2\).

For \(m\ge3\), the smallest left and right prefix sizes are \(t_1\) and \(t_m\). The smallest interior sum \(M_{ij}\) is attained by an adjacent spine-edge pair around some internal bundle \(t_h\), where \(2\le h\le m-1\). The all-pendant facet has size \(T_0\), which exceeds \(t_1+1\) since \(t_m\ge1\). These observations give the lower formula. The \(m=2\) statement follows directly from the three facets. For \(m\ge3\) and uniform bundles of size \(r\), two one-spine facets have size \(r+1\), while the all-pendant facet has size \(mr\), giving the unbounded width assertion.

**Ancillary complete-set identity.** The preceding classification also independently yields
\[
\mathcal E_{\mathbf t}(z)=(1+z)^{T_0}
+z\sum_{i=1}^{m-1}\left[(1+z)^{L_i}+(1+z)^{R_i}-1\right]
+z^2\sum_{1\le i<j\le m-1}(1+z)^{M_{ij}}.
\]
This identity is included as a check of the classification, **not** as an independent novelty claim: general-tree algorithms for complete edge-general-position counting already exist.

## Verification
The standalone \(\texttt{verify.py}\) independently constructs each test tree, enumerates unique geodesics by graph search, and evaluates the original definition against every selected-edge subset. It separately constructs the proposed three structural families and facets as edge masks, then compares the actual and predicted sets **exactly**, not just their generating polynomials. It exhausts \(60\) positive bundle vectors with \(2\le m\le5\) and \(t_i\in\{1,2\}\), restricted to at most \(14\) graph edges. In total \(135{,}720\) subsets were assessed, with no discrepancy. Run \(\texttt{python3 verify.py}\) from any directory; \(\texttt{verification_output.txt}\) records the expected deterministic output. These finite tests support but do not replace the unrestricted proof.

## Relationship to prior work
Manuel, Prabha and Klavžar introduced edge general position and proved that its **maximum cardinality** on any tree is the number of pendant edges; this known scalar result is not claimed anew [1]. Tian, Klavžar and Tan studied extremal cardinalities and block-graph bounds, not the inclusion-maximal facet distribution here [2]. Existing general-tree polynomial recurrences can compute the number of *all* feasible edge subsets of every size. Their all-set coefficients are not, by themselves, counts of inclusion-maximal sets. The contribution here is the explicit exhaustive **facet** classification, its weighted facet-size enumerator, the triangular count independent of leaf-bundle sizes, and the exact lower facet size on a family with arbitrarily many branching vertices. A classification for spider trees (one branching vertex) is a different and generally incomparable family; this caterpillar result does not claim its special cases as new.

## Limitations
The bundle positivity assumption is essential to this exact facet list: allowing zero-size bundles can merge or destroy putative facets. This result classifies the specified fully whiskered paths, not arbitrary caterpillars or trees. It does not assert uniqueness of the largest facet or compute the facet polynomial for unrestricted trees. Mathematical checking and priority assessment were not independent; unindexed equivalent literature is a residual risk.

## References
1. P. Manuel, R. Prabha, S. Klavžar, “Edge general position problem,” arXiv:2105.04292v1 (first public 10 May 2021), especially Theorem 3.3. https://arxiv.org/html/2105.04292v1
2. J. Tian, S. Klavžar, E. Tan, “Extremal Edge General Position Sets in Some Graphs,” *Graphs and Combinatorics* 40, 40 (2024). arXiv:2302.01587v1; https://doi.org/10.1007/s00373-024-02770-z
