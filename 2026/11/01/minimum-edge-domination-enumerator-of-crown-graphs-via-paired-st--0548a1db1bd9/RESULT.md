# Minimum edge-domination enumerator of crown graphs via paired star forests

## Finding

For every integer \(n\ge2\), let \(\operatorname{Cr}_n\) be the crown graph with bipartition \(\{a_1,\ldots,a_n\}\), \(\{b_1,\ldots,b_n\}\) and edges \(a_i b_j\) exactly when \(i\ne j\). Let
\[
M_n(z)=\sum_{F\subseteq E(\operatorname{Cr}_n)\atop F\text{ inclusion-minimal edge dominating}} z^{|F|}.
\]
The following finite coefficient-extraction formula gives **every coefficient**, for all \(n\ge2\):
\[
\boxed{M_n(z)=\bigl(D_n+2A_n+2B_n\bigr)z^n+nS_{n-1}(z).}
\]
Here \(D_n=\sum_{h=0}^{n}(-1)^h\binom nh(n-h)!\) is the derangement number,
\[
A_n=\sum_{s=2}^{n-2}\binom ns
       \sum_{j=0}^{s}(-1)^{s-j}\binom sj(j-1)^j j^{n-j},
\]
where an empty sum is zero, and
\[
B_n=\begin{cases}
0,&n\le3,\\
n(n-1)\binom{n-2}{2}
 \displaystyle\sum_{h=0}^{n-4}(-1)^h\binom{n-4}{h}(n-2-h)!,&n\ge4.
\end{cases}
\]
The star-forest polynomial \(S_t(z)\) is explicitly determined by
\[
\begin{aligned}
W(x,y,z)&=zxy+x(e^{zy}-1-zy)+y(e^{zx}-1-zx),\\
S_t(z)&=\sum_{j=0}^{t}(-1)^j\binom tj (t-j)!^2
[x^{t-j}y^{t-j}]
\left\{e^{W(x,y,z)}\big[z(e^{zx}+e^{zy}-1)\big]^j\right\}.
\end{aligned}
\]
All exponentials and coefficients here are interpreted as formal power series in \(x,y\) with polynomial coefficients in \(z\); each coefficient is a finite sum. In particular, \(S_1(z)=0\).

Every inclusion-minimal edge dominating set belongs to exactly one of the following mutually exclusive structural types: a perfect matching of \(\operatorname{Cr}_n\); one edge from every vertex on one side, with at least two vertices unused on the other side; one edge from every vertex on one side, with exactly one unused opposite vertex \(j\) and the image of \(j\) having a unique preimage; or a spanning star forest on the remaining \(2(n-1)\) vertices after omitting the matched pair \(a_j,b_j\). In the last type, each tree component is a star, and isolated vertices are disallowed.

For \(n\ge3\), the minimum edge-domination number and exact number of minimum sets are
\[
\boxed{\gamma'(\operatorname{Cr}_n)=n-1,\qquad
\#\{F:|F|=n-1\}=nD_{n-1}.}
\]
For \(n\ge5\), the maximum cardinality of an inclusion-minimal edge dominating set and exact number of such maximum sets are
\[
\boxed{\Gamma'(\operatorname{Cr}_n)=2n-4,\qquad
\#\{F:|F|=2n-4\}=n(n-1).}
\]
The remaining small boundaries are \(M_2(z)=z^2\), \(M_3(z)=3z^2+2z^3\), and \(M_4(z)=8z^3+117z^4\). Thus \(\operatorname{Cr}_n\) is not well-edge-dominated for any \(n\ge3\).

## Assumptions and scope

Graphs are finite, simple, undirected, and labeled as above. An edge dominates itself and every edge sharing an endpoint. An *edge dominating set* dominates all edges; *inclusion-minimal* means removal of any one selected edge destroys domination. This is not the same as an arbitrary maximal matching. The enumerator weights each distinct **edge subset** once, not ordered sequences or isomorphism classes. The main theorem applies to every integer \(n\ge2\), including the disconnected graph \(\operatorname{Cr}_2\). All displayed extreme-size formulas have their stated parameter ranges.

## Proof

**1. Uncovered-vertex criterion.** For any edge set \(F\), let \(U_A\) and \(U_B\) be the vertices on the respective sides incident with no edge of \(F\). An edge is undominated if and only if both its endpoints are uncovered. Thus \(F\) dominates every edge exactly when no \(i\in U_A\), \(j\in U_B\) satisfy \(i\ne j\). There are only three possibilities: at least one uncovered side is empty, or \(U_A=U_B=\{j\}\) for a unique \(j\).

**2. All vertices covered.** Suppose \(U_A=U_B=\varnothing\). After deleting a selected edge, domination fails only if **both** its endpoints become uncovered: if only one vertex becomes uncovered, all other vertices are still covered. Therefore every selected edge has degree one at both ends in the selected-edge graph. Hence \(F\) is a perfect matching, necessarily one of the \(D_n\) derangements.

**3. Exactly one side has uncovered vertices.** Suppose \(U_A=\varnothing\) and \(U_B\ne\varnothing\). Every edge is essential only if its \(A\)-endpoint has selected degree one; otherwise removing it leaves all \(A\)-vertices covered. Thus \(F\) consists of one edge \(a_i b_{f(i)}\) per \(i\), with \(f(i)\ne i\). If at least two \(B\)-vertices are unused, removing any edge uncovers an \(a_i\) adjacent to at least one of them, so minimality holds. If precisely \(b_j\) is unused, removal of the edge from \(a_j\) uncovers \(a_j\), which is not adjacent to \(b_j\); it destroys domination precisely when \(b_{f(j)}\) becomes uncovered as well, i.e. when \(f(j)\) has a unique preimage. All other edges are automatically essential. The case with the two sides reversed is identical.

For an image of size exactly \(s\), inclusion–exclusion over the chosen \(s\) target indices counts fixed-point-free maps onto that image. If \(j\) target indices remain available, each of those \(j\) rows has \(j-1\) possible images and each of the remaining \(n-j\) rows has \(j\), yielding \((j-1)^j j^{n-j}\), hence \(A_n\). For the one-hole case choose the unused value (\(n\) choices), the doubly used target (\(n-1\) choices), and its two source rows avoiding both the hole and that target (\(\binom{n-2}{2}\) choices). The remaining \(n-2\) rows biject onto the remaining \(n-2\) targets, avoiding fixed points on exactly \(n-4\) shared labels. Inclusion–exclusion gives the displayed \(B_n\).

**4. A matched pair uncovered.** If both sides have uncovered vertices, the criterion in step 1 forces \(U_A=U_B=\{j\}\). The selected edges cover all remaining vertices, and every edge touches only vertices with indices different from \(j\). Upon deleting a selected edge, the original unmatched uncovered pair defeats domination as soon as either selected endpoint becomes uncovered; otherwise domination persists. Accordingly, each selected edge must be incident to a selected-degree-one vertex. A finite graph with no isolated vertices and every edge incident to a leaf is precisely a disjoint union of stars. These are the spanning star forests of the induced graph \(\operatorname{Cr}_{n-1}\), with \(n\) choices of the omitted pair. No duplication occurs among the four types.

**5. Star-forest coefficient formula.** On a complete bipartite graph with labeled sides, a spanning star forest has unique decomposition into isolated edges, stars with one \(A\)-center and at least two \(B\)-leaves, and stars with one \(B\)-center and at least two \(A\)-leaves. The two-sort exponential formula gives \(e^{W(x,y,z)}\). Delete the diagonal perfect matching by inclusion–exclusion. When \(j\) prescribed pairwise disjoint diagonal edges must be present, no two can occupy the same star component, since two disjoint edges cannot lie in one star. Each forced edge is either a two-vertex component, or the edge incident to a star center with at least one additional free opposite-side leaf. Its two-sort exponential factor is precisely \(z(e^{zx}+e^{zy}-1)\). The remaining \(t-j\) free vertices on each side form an unrestricted bipartite star forest. Multiplying these factors, extracting coefficients, restoring the free labels with \((t-j)!^2\), and applying \(\sum_j(-1)^j\binom tj\) proves the formula for \(S_t(z)\). Combining steps 2–4 proves the boxed polynomial identity.

**6. Extremal sizes.** Every star forest on \(2t\) nonisolated vertices has at least \(t\) edges; equality forces a perfect matching. For \(t\ge2\), \(\operatorname{Cr}_t\) has exactly \(D_t\) such matchings. With \(n=t+1\), all other types have \(n\) edges, proving the minimum statement for \(n\ge3\). A spanning star forest of \(\operatorname{Cr}_t\), \(t\ge3\), has at least two components: one star has at most \(t\) vertices because no center sees its paired opposite-side vertex. Hence it has at most \(2t-2\) edges. Equality requires two star components of sizes \(t\), whose centers must be the two vertices of one deleted matched pair; there are exactly \(t\) configurations. For \(n\ge5\), this upper size \(2n-4\) exceeds the one-sided and perfect-matching sizes \(n\), giving \(n(n-1)\) maximum configurations. Checking the \(n=2,3,4\) cases by the same classification gives the stated boundary polynomials.

## Verification

The accompanying standalone `verify.py` implements the coefficient formula using exact rational arithmetic, computes edge domination independently from original edge neighborhoods, and checks inclusion-minimality by deleting every selected edge. It exhaustively examines all \(2^{n(n-1)}\) edge subsets for \(n=2,3,4,5\): **1,052,740 subsets altogether**. It independently checks the structural classification for each subset, the full cardinality polynomial, and the star-forest coefficient formula against direct edge-subset enumeration for \(t\le4\); additional exact boundary checks cover \(3\le t\le8\). It reports `VERIFY_OK`. These finite experiments corroborate, but do not substitute for, the all-parameter proof above.

## Relationship to prior work

Bonamy, Defrain, Heinrich, Raymond and Pilipczuk (arXiv:1810.00789, first posted 2018-10-01) established output-sensitive enumeration results for minimal dominating sets in triangle-free and related graph classes; this does not give exact coefficients for edge domination in a particular crown graph. Anderson, Kuenzel and Rall (arXiv:2110.07133, first posted 2021-10-14) investigated well-edge-dominated graphs and proved, among other things, that the **undeleted** balanced complete bipartite graphs are well-edge-dominated. Their inspected paper does not state the crown-family complete minimal-edge-domination enumerator. The present theorem treats a natural deletion of the balancing matching, and distinguishes exact enumeration from algorithms for enumerating all minimal sets. The equivalence of edge domination to vertex domination in the line graph is acknowledged, not claimed as new.

## Limitations

This theorem applies to deletion of a **perfect** matching from a balanced complete bipartite graph, not arbitrary deleted matchings or unbalanced bipartite graphs. Its exact coefficient expression is a finite formal-power-series extraction, not a complexity claim of polynomial-time evaluation in the binary length of \(n\). A previously published equivalent formula expressed via line-graph domination, star forests, or restricted endofunctions could establish some or all of the result; publication priority has not been independently certified. No independent mathematical audit has been performed.

## References

1. M. Bonamy, O. Defrain, M. Heinrich, J.-F. Raymond, M. Pilipczuk, *Enumerating minimal dominating sets in \(K_t\)-free graphs and variants*, arXiv:1810.00789, version 1 posted 2018-10-01, https://arxiv.org/abs/1810.00789.
2. S. E. Anderson, K. Kuenzel, D. F. Rall, *On well-edge-dominated graphs*, arXiv:2110.07133, version 1 posted 2021-10-14, https://arxiv.org/abs/2110.07133.
3. Z. Pan, Y. Yang, X. Li, S.-J. Xu, *The complexity of total edge domination and some related results on trees*, arXiv:1910.02431, version 1 posted 2019-10-06, https://arxiv.org/abs/1910.02431. This concerns total rather than ordinary edge domination and is contextual.
