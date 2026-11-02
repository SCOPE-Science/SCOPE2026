# Wheel spanning-tree exchange centers and complementary-tree census

## Finding

**Theorem.** For every integer \(m\ge3\), let \(W_{m+1}\) have hub \(h\) and rim vertices \(v_0,\ldots,v_{m-1}\), with edges \(v_iv_{i+1}\) (indices modulo \(m\)) and \(hv_i\). Let \(\mathcal T(W_{m+1})\) be the unrestricted spanning-tree **single-edge exchange graph**: each vertex is a spanning tree, and two distinct trees are adjacent precisely when they differ in one removed and one inserted edge.

For a tree \(T\), write \(H_T=(V(W_{m+1}),E(W_{m+1})\setminus E(T))\), including isolated vertices, and write \(\beta(H_T)=|E(H_T)|-|V(H_T)|+c(H_T)\) for its cycle rank. Then every eccentricity satisfies the exact formula

\[
\operatorname{ecc}_{\mathcal T}(T)=m-\beta(H_T).
\]

Consequently,

\[
\operatorname{rad}(\mathcal T(W_{m+1}))=m-\lfloor m/3\rfloor=\lceil2m/3\rceil,
\qquad
\operatorname{diam}(\mathcal T(W_{m+1}))=m.
\]

A tree is central exactly when its edge complement contains \(\lfloor m/3\rfloor\) independent cycles. A tree is peripheral exactly when its edge complement is itself a spanning tree. The number of peripheral trees is precisely

\[
\boxed{2^{m+1}-4},
\]

and the number of **unordered complementary pairs of spanning trees** is \(2^m-2\). The claim concerns labelled edges and distinct spanning-tree edge sets; no graph-isomorphism quotient is taken.

## Assumptions and scope

The rim has length \(m\ge3\). The exchange graph permits **every** single-edge exchange yielding a spanning tree, not only exchanges that traverse triangles or other prescribed fundamental cycles. The complement \(H_T\) uses the edges absent from \(T\) **within the wheel**, not the complement of the wheel in a complete graph. It has exactly \(m\) edges on exactly \(m+1\) vertices. Its isolated vertices count toward \(c(H_T)\).

The radius/diameter apply to this connected basis-exchange graph and hence involve graph distances between spanning trees, not distances between vertices of the underlying wheel. The two complementary trees in a pair are regarded as unordered only for the final pair count.

## Proof

**1. Exchange distance and complement rank.** If \(T,U\) are spanning trees of any connected graph having \(n\) vertices, then the unrestricted exchange distance is \(|E(U)\setminus E(T)|=(n-1)-|E(T)\cap E(U)|\). The lower bound follows because one exchange inserts at most one required edge. For the matching upper bound, insert any edge of \(U\setminus T\): its fundamental cycle in \(T\) contains an edge outside \(U\), since \(U\) is acyclic. Removing that edge never loses an edge of \(T\cap U\). Repeat until \(U\) is obtained.

Fix \(T\) and put \(H_T=G-E(T)\). The largest possible intersection of a spanning tree \(U\) with \(H_T\) is the graphic-matroid rank of \(H_T\), namely \(|V(G)|-c(H_T)\). Indeed, the intersection is necessarily a forest; conversely, a spanning forest of \(H_T\) can always be extended to a spanning tree of the connected graph \(G\). For the wheel, this maximum equals \(m+1-c(H_T)\), and therefore \(\operatorname{ecc}(T)=m+1-c(H_T)\). Since \(|E(H_T)|=m\) and \(|V(H_T)|=m+1\), we have \(\beta(H_T)=c(H_T)-1\). This proves the formula \(\operatorname{ecc}(T)=m-\beta(H_T)\).

**2. Bounding wheel cotree cycles.** Because \(T\) spans every rim vertex and the wheel has rim degree three, every rim vertex has degree at most two in \(H_T\). Every cycle not containing the hub must be the complete rim cycle. Every other cycle contains the hub and consists of two spokes joined by a nonempty rim path. Two distinct cycles of \(H_T\) cannot share a rim vertex: at a rim vertex of degree two the incident cycle edges are forced, and propagation along their rim path shows that any two such cycles coincide. Thus all distinct cycles are edge-disjoint and can intersect only at the hub. If the rim itself is a cycle, there are no spokes in \(H_T\), so that cycle is the only one. In every case the cycle rank equals the number of these distinct cycles. Every cycle contains at least three edges, and \(H_T\) has \(m\) edges. Hence \(\beta(H_T)\le\lfloor m/3\rfloor\).

**3. Attaining the bound and finding the radius.** Write \(m=3q+r\), where \(q\ge1\) and \(r\in\{0,1,2\}\). With rim vertices indexed from \(0\) to \(m-1\), choose \(H\) to consist of the \(q\) disjoint-edge hub triangles on rim pairs \((v_{3j},v_{3j+1})\), for \(0\le j<q\): each triangle uses the rim edge \(v_{3j}v_{3j+1}\) and the two corresponding spokes. Add the \(r\) spokes at \(v_{3q},\ldots,v_{3q+r-1}\). Then \(H\) contains exactly \(m\) edges and exactly \(q\) independent cycles.

The complement \(T=E(W_{m+1})\setminus E(H)\) is a spanning tree. Indeed, after deleting the \(q\) selected rim edges, the retained rim edges form exactly \(q\) path components, and each path contains exactly one retained spoke, at \(v_{3j+2}\) for \(0\le j<q\). Thus those rim paths are joined into a tree through the hub. The bound is attained, so the radius is \(m-q=\lceil2m/3\rceil\). The center characterization follows directly from the eccentricity identity.

**4. Attaining diameter \(m\).** Take a tree \(T\) containing all spokes except \(hv_0\), together with the rim edge \(v_0v_1\). Its complement contains the other \(m-1\) rim edges and the spoke \(hv_0\). These edges form a spanning tree: the rim is a path and the hub is attached at \(v_0\). Hence \(\beta(H_T)=0\) and \(\operatorname{ecc}(T)=m\). The distance formula also bounds every eccentricity above by \(m\), proving the diameter and the peripheral criterion.

**5. Counting peripheral trees via binary rim words.** Color each wheel edge red if it belongs to \(T\), blue if it belongs to \(H_T\). Both color classes must be spanning trees. Consider first the binary cyclic word of the \(m\) rim-edge colors. If it is monochromatic, one color class contains the complete rim cycle, so no split into two trees is possible.

Suppose the rim word is nonconstant. Its monochromatic runs alternate in color, and their number \(2s\) is positive and even. The vertices between consecutive runs (the \(2s\) boundary vertices) are precisely those incident to different rim-edge colors. Any vertex internal to a red rim run has both incident rim edges red, so it is isolated in the blue rim-edge forest; its spoke must be blue. The analogous rule applies to internal vertices of blue runs. For either color, each monochromatic rim run is a path component of that color's rim-edge forest and must have exactly one spoke of that same color to connect it to the hub. All its internal spokes have the opposite color, so the two **boundary** spokes at the ends of each run must have different colors.

The boundary vertices form a cyclic sequence of even length \(2s\); the requirement that consecutive boundary spokes differ has exactly two binary solutions. Every internal spoke is already forced, so **each nonconstant rim word has exactly two spoke-color completions**. Both completions give connected acyclic graphs in each color: each rim run is joined to the hub by one spoke, and isolated vertices in one color have their forced spokes of that color. Each color class therefore forms a spanning tree. There are \(2^m-2\) nonconstant rim words, giving \(2(2^m-2)=2^{m+1}-4\) ordered tree/complement pairs, equivalently distinct peripheral spanning trees. Taking the unordered quotient by swapping colors gives \(2^m-2\) complementary tree pairs. This proves all assertions. \(\square\)

## Verification

The standard-library scripts `verify/verify_wheel_metric.py` and `verify/verify_wheel_complement_count.py` can be run with `python3` from any directory. The first independently enumerates all spanning trees for \(3\le m\le10\), computes complementary component counts, checks the radius/diameter/periphery formulas, and for \(3\le m\le5\) constructs the entire unrestricted exchange graph and checks every pairwise distance by breadth-first search. The second exhaustively tests **every** two-coloring of all \(2m\) edges for \(3\le m\le8\), comparing the cyclic-run construction with all actual complementary-tree decompositions; for \(9\le m\le14\) it verifies each constructive completion directly. Both terminate with `ALL_WHEEL_TREE_METRIC_CHECKS_PASS` and `ALL_WHEEL_COMPLEMENT_CHECKS_PASS`, respectively. These finite checks corroborate, but do not replace, the unrestricted symbolic proof.

For example, the spanning-tree counts for \(m=3,4,5,6,7,8,9,10\) are respectively \(16,45,121,320,841,2205,5776,15125\), while peripheral counts are \(12,28,60,124,252,508,1020,2044\).

## Relationship to prior work

Mahoney, *Tree Graphs and Orthogonal Spanning Tree Decompositions* (2016), develops tree graphs and, in Section 4.2, proves that an acyclic edge complement realizes the maximum possible exchange eccentricity and that a cyclic complement gives a smaller eccentricity. Its broader center criterion is credited here; the present claim specializes to wheels and adds the **exact all-size radius**, full eccentricity formula, central cotree characterization, and exact peripheral census. The dissertation's wheel discussion in its duality section and wheel figures in Appendix B do not give this claimed combination. This comparison concerns the text inspected, not a proof that the entire literature lacks another equivalent formulation.

The total number of wheel spanning trees is classical (Benjamin and Yerger, 2006), so the previously known Lucas-number spanning-tree count is not claimed as new. Likewise, the standard unrestricted matroid basis-exchange distance identity in Proof Step 1 is elementary background, not a new theorem. The present exchange graph differs from constructions that allow only exchanges with a prescribed fundamental cycle such as a hub triangle; those can have the same vertex set but a different adjacency relation.

## Limitations

The theorem concerns the ordinary labelled wheel, all \(m\ge3\), and unrestricted one-edge exchanges only. No claim is made about exact center cardinalities, full eccentricity multiplicities away from the periphery, degree statistics, or restricted exchange models. The archival originality search included the most directly relevant available dissertation and targeted research-record, library and web comparisons; unindexed equivalent results remain a genuine possibility. This is a mathematical proof and reproducible finite check, not an independently audited publication.

## References

- J. R. Mahoney, *Tree Graphs and Orthogonal Spanning Tree Decompositions*, Portland State University dissertation, publication dated May 17, 2016, DOI: `10.15760/etd.2939`; especially Section 4.2, pp. 31–34, and Appendix B.6. Open copy: `https://web.pdx.edu/~caughman/mahoneyDissertation.pdf`.
- A. T. Benjamin and C. R. Yerger, *Combinatorial Interpretations of Spanning Tree Identities*, Bulletin of the Institute of Combinatorics and its Applications **47** (2006), 37–42. Institutional record: `https://scholarship.claremont.edu/hmc_fac_pub/1050/`.
