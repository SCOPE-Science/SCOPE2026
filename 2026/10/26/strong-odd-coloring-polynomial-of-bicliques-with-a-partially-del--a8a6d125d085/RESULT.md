# Strong odd coloring polynomial of bicliques with a partially deleted matching

## Finding
Let \(G_{p,q,t}\) be obtained from \(K_{p,q}\) by deleting exactly \(t\) pairwise disjoint edges, where \(p,q\ge2\) and \(1\le t<\min(p,q)\). Every strong odd coloring has a unique color-class partition of the following form: the matched endpoints belonging to each deleted edge are singleton classes on their respective sides, except that the two corresponding singleton classes may be merged; and the remaining \(p-t\) and \(q-t\) vertices, separately on each side, partition into nonempty **odd-cardinality** classes. Conversely, every partition of this form is a strong odd coloring.

Write \(S_{\mathrm{odd}}(u,k)\) for the number of partitions of a labeled \(u\)-element set into \(k\) nonempty odd-cardinality blocks. Let \((Q)_d=Q(Q-1)\cdots(Q-d+1)\) for \(d\ge1\) and \((Q)_0=1\). The number \(\Phi_{p,q,t}(Q)\) of proper strong odd colorings by a palette of \(Q\) named colors, allowing unused colors, satisfies, for every integer \(Q\ge0\),
\[
\boxed{\Phi_{p,q,t}(Q)=\sum_{k=0}^{p-t}\sum_{\ell=0}^{q-t}
 S_{\mathrm{odd}}(p-t,k)S_{\mathrm{odd}}(q-t,\ell)
 \sum_{j=0}^{t}\binom tj (Q)_{2t+k+\ell-j}.}
\]
This is a polynomial identity in \(Q\). Equivalently, the number of *unlabeled* valid color partitions into exactly \(d\) classes is
\[
 u_d=\sum_{k=0}^{p-t}\sum_{\ell=0}^{q-t}\sum_{j=0}^{t}
 \mathbf1_{\{d=2t+k+\ell-j\}}\binom tj
 S_{\mathrm{odd}}(p-t,k)S_{\mathrm{odd}}(q-t,\ell),
\]
so \(\Phi_{p,q,t}(Q)=\sum_d u_d(Q)_d\).

With \(\varepsilon(u)=1\) when positive \(u\) is odd and \(\varepsilon(u)=2\) when positive \(u\) is even, the strong odd chromatic number is
\[
\boxed{\chi_{\mathrm{so}}(G_{p,q,t})=t+\varepsilon(p-t)+\varepsilon(q-t).}
\]
The number of optimal unlabeled partitions is \(c(p-t)c(q-t)\), where \(c(u)=1\) for odd \(u\) and \(c(u)=2^{u-2}\) for even \(u\). The number of optimal named colorings with \(\chi_{\mathrm{so}}\) available colors is therefore \(\chi_{\mathrm{so}}!c(p-t)c(q-t)\).

## Assumptions and scope
All graphs are finite, simple, and undirected. Fix labeled bipartition classes \(A=\{a_1,\ldots,a_p\}\) and \(B=\{b_1,\ldots,b_q\}\), and delete \(a_i b_i\) exactly when \(1\le i\le t\). The strict inequality \(t<\min(p,q)\) ensures **at least one unmatched vertex in each class**; this hypothesis is essential to the structural proof. A strong odd coloring is a proper vertex coloring such that for each vertex and for each color appearing in its open neighborhood, the number of neighbors carrying that color is odd. Colors are counted as named unless explicitly described as unnamed color classes. All symbols \(p,q,t,Q\) range over integers in the domains displayed above. Binomial coefficients and Stirling numbers have their standard combinatorial interpretations, and \(S_{\mathrm{odd}}(0,0)=1\).

## Proof
**1. Parity constraints on the two sides.** Every unmatched vertex of \(A\) is adjacent to every vertex in \(B\). Thus the strong odd condition at any such vertex requires **each nonempty color class within \(B\) to have odd cardinality**. Symmetrically, every nonempty color class within \(A\) has odd cardinality, because \(B\) contains an unmatched vertex.

For each deleted-edge index \(i\le t\), let \(C_i\) be the vertices of \(B\) colored like \(b_i\). The preceding observation makes \(|C_i|\) odd. If \(|C_i|\ge3\), vertex \(a_i\) has exactly \(|C_i|-1\) neighbors of that color: all of \(C_i\) except \(b_i\). This is a positive even number, forbidden by the strong odd condition. Consequently \(b_i\) is a singleton within its own side's color partition. Interchanging the sides, \(a_i\) is likewise a singleton in \(A\). All classes contained in the unmatched portions of the two sides have odd sizes, and conversely any such within-side partition makes every appearing neighborhood color have odd multiplicity or zero at every vertex: at unmatched vertices, the side classes are odd; at matched vertices, a deleted partner's singleton class contributes zero and every other class contributes its full odd size.

**2. Which colors may appear on both sides?** Properness forbids two adjacent vertices from receiving the same color. If a color appears in both bipartition classes, every cross-pair of vertices carrying it must be a missing edge. Since the deleted edges form a matching, such a color class consists of **exactly** \(\{a_i,b_i\}\) for a unique \(i\le t\). Conversely, each of these two-vertex independent classes may be formed by merging the two already-valid singleton classes; at no vertex does the merge combine two positive neighborhood counts, since its endpoints are nonadjacent and the graph's only missing cross-edge incident to either endpoint is their pair. Hence mergers of distinct indices are independent. The classification in the finding follows.

**3. Counting.** Write \(m=p-t\), \(r=q-t\). Independently choose an odd-block set partition of the \(m\) unmatched vertices on side \(A\) into \(k\) classes, in \(S_{\mathrm{odd}}(m,k)\) ways; make an analogous choice on \(B\) into \(\ell\) classes. Before merging, there are \(2t+k+\ell\) color classes, because all \(2t\) matched endpoints are side-singletons. Choose exactly \(j\) of the \(t\) deleted edges for merging, in \(\binom tj\) ways. The result has exactly \(d=2t+k+\ell-j\) color classes. Its partition is uniquely recovered from the colors, so no class partitions are repeated. Labeling these \(d\) distinct classes injectively with colors from a \(Q\)-palette gives \((Q)_d\) proper colorings. Summing proves the formulas.

**4. Minimum colors and multiplicities.** Since \(m,r\ge1\), an odd-block partition of \(u\) nonempty vertices has at least one block if \(u\) is odd, attained uniquely by its single full block, and at least two if \(u\) is even, attained exactly by splitting into two odd blocks. For positive even \(u\), there are \(2^{u-1}\) odd-size subsets and complementary choices give the same unordered two-block partition, yielding \(2^{u-2}\) choices. The class count is minimized only if **every one** of the \(t\) deleted pairs is merged, i.e. \(j=t\), and each unmatched side uses its minimum number of odd blocks. This proves the chromatic number and optimal-multiplicity formulas, with the uniqueness of the choices for odd \(u\).

## Verification
The attached standalone `verify.py` constructs each matching-deleted biclique from graph adjacency, enumerates set partitions by restricted-growth words, and checks the defining proper-coloring and open-neighborhood odd-multiplicity conditions independently of the classification. Across 26 parameter triples with \(2\le p\le q\), \(p\le5\), \(q\le6\), and \(p+q\le10\), it examined 945,707 set partitions and matched every nonzero cardinality coefficient. Another 24 direct tests independently enumerated all named color assignments for palettes of size one through four on six small instances. All checks passed. The source and exact stdout are embedded, and the finite checks are corroboration, not an infinite proof.

## Relationship to prior work
Kwon and Park (arXiv:2401.11653, first publicly submitted 2024-01-22) introduced strong odd coloring and treated sparse graph bounds; their primary MSC is 05C15. Caro, Petruševski, Škrekovski, and Tuza (arXiv:2410.02336, first submitted 2024-10-03) proved general and graph-product results and discussed the small strong odd chromatic number of complete bipartite graphs. Their published statements and the full-text sections examined do not enumerate strong odd colorings after an arbitrary **nonperfect** matching deletion.

The later paper on odd independence (arXiv:2509.20763) gives the color-class/odd-independence connection and discusses half graphs and the perfect-matching-deletion construction in a distinct setting. Separately, an accessible published result determines strong odd chromatic numbers of **odd crown graphs**, for which the deleted matching is *perfect* and no unmatched vertices remain; the present theorem deliberately excludes that endpoint. Its result cannot imply the polynomial here because the argument using unmatched universal vertices does not apply at the crown endpoint. Known results on neighborhood-parity odd colorings solve a weaker, different coloring condition and likewise do not imply these counts. The new claim is the all-palette polynomial, strict partial-matching classification, exact optimum, and optimum multiplicity, not the general coloring definition or prior crown-graph result.

## Limitations
The theorem excludes \(t=0\) and \(t=\min(p,q)\). The argument requires an unmatched universal vertex in **both** bipartition classes, so it does not provide endpoint results or a theorem for arbitrary sets of deleted edges. Earlier literature may contain equivalent formulas under alternative partition terminology; no exhaustive novelty assertion or independent review is implied. The verification script tests finite parameters only.

## References
1. H. Kwon and B. Park, “Strong odd coloring of sparse graphs,” arXiv:2401.11653, submitted 2024-01-22, primary MSC 05C15; https://arxiv.org/abs/2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, “On strong odd colorings of graphs,” arXiv:2410.02336, submitted 2024-10-03; https://arxiv.org/abs/2410.02336.
3. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, “The odd independence number of graphs, I: Foundations and classical classes,” arXiv:2509.20763, submitted 2025-09-25; https://arxiv.org/abs/2509.20763.
