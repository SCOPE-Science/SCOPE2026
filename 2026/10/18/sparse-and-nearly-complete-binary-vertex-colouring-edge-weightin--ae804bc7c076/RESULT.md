# Sparse and nearly complete binary vertex-colouring edge-weightings of bicliques

## Finding

Let \(G=K_{m,n}\) have distinguished, labelled bipartition classes \(L\) and \(R\), where \(1\le m\le n\). A **proper binary edge-weighting** is a map \(w:E(G)\to\{0,1\}\) such that the incident sums \(\sigma_w(u)=\sum_{e\ni u}w(e)\) and \(\sigma_w(v)\) differ at the ends of **every original edge** \(uv\in E(G)\), including an edge receiving weight zero. Let \(f_{m,n}(k)\) count these weightings with exactly \(k\) weight-one edges.

For \(m\ge2\), define
\[
 A_{m,n}=m!\,[x^m](e^x-x)^n
 =\sum_{j=0}^{\min(m,n)}(-1)^j\binom nj(m)_j(n-j)^{m-j},
\]
with \((m)_j=m!/(m-j)!\) and \(0^0=1\). This is a nonnegative integer: the number of functions from the labelled \(m\)-element class to the labelled \(n\)-element class with no fibre of size one.

**Theorem (complete two-ended support classification).**

1. If \(m=n=1\), no proper binary weighting exists. If \(m=1<n\), a weighting is proper exactly when its number of weight-one edges is at least two; thus \(f_{1,n}(k)=\binom nk\) for \(2\le k\le n\), and zero otherwise.
2. For \(2\le m<n\), the minimum support is \(m\), its number of labelled minimizers is \(f_{m,n}(m)=A_{m,n}\), and its maximum support is \(mn\), attained uniquely by the all-one weighting. Every minimizer is a disjoint union of stars centered in \(R\), each star having at least two leaves in \(L\); isolated vertices are allowed in \(R\).
3. For \(m=n=q\ge2\), the minimum and maximum support sizes are \(q\) and \(q^2-q\), respectively. Each extremal layer has \(2A_{q,q}\) labelled weightings. The minimum supports are exactly the star forests just described and their reversals with the two bipartition classes interchanged. Every maximum support is the edge-complement of a minimum support. In fact the whole support polynomial is reciprocal: \(f_{q,q}(k)=f_{q,q}(q^2-k)\) for every integer \(k\).
4. If \(2\le m<n\) and \(n=m+1\), the all-one weighting is isolated from below by a sharp **three-edge gap**: 
\[
 f_{m,m+1}(m(m+1)-1)=f_{m,m+1}(m(m+1)-2)=0,
 \qquad f_{m,m+1}(m(m+1)-3)=m\binom{m+1}{3}.
\]
Every weighting in this first nontrivial layer comes from turning precisely three edges incident with one vertex of \(L\) from one to zero. If \(n\ge m+2\), then \(f_{m,n}(mn-1)=mn\): every single-edge deletion from the all-one weighting is proper.

Up to automorphism of \(K_{m,n}\), every minimum-support weighting for \(m\ge2\) is classified by an integer partition \(\lambda\vdash m\) whose parts are all at least two; for a balanced biclique the two possible star-center sides belong to the same orbit. If \(\lambda\) has \(t\) parts and \(a_s\) parts equal to \(s\), then its labelled multiplicity is
\[
 (1+\mathbf{1}_{\{m=n\}})\,
 \frac{(n)_t\,m!}{\left(\prod_{i=1}^t\lambda_i!\right)
 \left(\prod_{s\ge2}a_s!\right)}.
\]
Consequently, the number of minimum-support automorphism orbits equals the number of partitions of \(m\) without parts one (including the appropriate one-part partition). The scalar minimum/maximum endpoints are included to state the enumerative classification; their existence is not asserted to be previously unknown.

## Assumptions and scope

All graphs are finite, simple, labelled, complete bipartite graphs with \(1\le m\le n\). The weights \(0\) and \(1\) are distinguished, the induced vertex colours are **sums**, not products, and their inequality is required across **all** edges of the original biclique, not just across the positive-weight subgraph. A support is a subset of its \(mn\) labelled edges. The orbit statement uses the full graph automorphism group and therefore permits exchange of parts only when \(m=n\). The coefficient formula uses formal power series over \(\mathbb{Q}\); no analytic convergence is needed.

## Proof

Let \(F\subseteq E(K_{m,n})\) be the set of edges of weight one. For \(u\in L\) put \(r_u=\deg_F(u)\), and for \(v\in R\) put \(c_v=\deg_F(v)\). Because every \(uv\) across the bipartition is an edge of the **original graph**, a weighting is proper if and only if
\[
 \{r_u:u\in L\}\cap\{c_v:v\in R\}=\varnothing. \tag{1}
\]
This equivalence includes vertices with zero selected degree and is the basis of every classification below.

If \(m=n=1\), both endpoints have the same sum for any weighting. When \(m=1<n\), let \(k=|F|\). The central vertex has sum \(k\); the leaf sums are zero or one. If \(k=0\), zero occurs on both sides; if \(k=1\), one occurs on both sides. For \(k\ge2\), the central sum is different from every leaf sum. This proves assertion 1 and the binomial counts.

Assume \(2\le m\le n\). If \(|F|<m\), some vertex in each part is not incident with any selected edge, since each selected edge touches at most one vertex in each part; condition (1) fails at zero. Thus \(|F|\ge m\). If \(m<n\) and \(|F|=m\), there is an isolated vertex of \(R\) in \(F\). By (1) every vertex of \(L\) then has positive selected degree. With exactly \(m\) selected edges, every vertex of \(L\) has selected degree one. Hence any vertex of \(R\) used by \(F\) must receive at least two of these edges, or else sum one would occur in both parts. Conversely, every assignment of all \(m\) vertices of \(L\) to vertices of \(R\), with occupied fibres at least two, gives a proper \(m\)-edge support. The exponential formula for labelled disjoint fibres gives the generating coefficient \(A_{m,n}\): each of the \(n\) individually labelled targets receives either no preimages or a set of at least two; its contribution is \(e^x-x\). Expanding \((e^x-x)^n\) by the binomial theorem gives the finite alternating sum above. This proves the minimum-support part of assertion 2.

If \(m=n=q\) and \(|F|=q\), either a zero occurs among the degrees on one side or both sides have all selected degrees one. The latter case is a perfect matching, violating (1). If zero occurs on the right, all left degrees are positive and hence exactly one, yielding the same star-forest family; if zero occurs on the left, interchange sides. The two families are disjoint, as their intersection would again require a perfect matching. Their total count is \(2A_{q,q}\). For equal part sizes, replacing \(F\) by its edge-complement replaces every degree \(d\) on either side with \(q-d\), preserving the inequality in (1). Thus \(f_{q,q}(k)=f_{q,q}(q^2-k)\) for every \(k\), and the maximum-support size and count follow immediately.

When \(m<n\), the all-one weighting has constant incident sum \(n\) on \(L\) and \(m\) on \(R\); it is proper and uniquely uses \(mn\) selected edges. For the high-support gap let \(H=E(K_{m,m+1})\setminus F\) be the set of zero-weight edges, with row/column degrees \(x_u=\deg_H(u)\) and \(y_v=\deg_H(v)\). The sums assigned by \(F\) are \(m+1-x_u\) on \(L\) and \(m-y_v\) on \(R\); therefore (1) is equivalent to
\[
 x_u-y_v\ne1\qquad\text{for every }(u,v)\in L\times R.\tag{2}
\]
If \(|H|=1\), the unique nonzero row degree is one and some column has degree zero, violating (2). If \(|H|=2\), either a row has degree one and an unused column exists (because \(m+1\ge3\)), or both zeros lie in one row, which has degree two while the two affected columns have degree one. Again (2) fails.

Let \(|H|=3\). If a row has degree three, then \(H\) is a three-edge star in \(L\); its row degrees are three and zero and its column degrees are one and zero, so no difference is one. Otherwise, for \(m\ge3\) there is an unused column because \(m+1\ge4\), while the row-degree multiset must contain a one (the possible positive partitions of three without a three are \(2+1\) and \(1+1+1\)). This violates (2). For the remaining case \(m=2\), either an unused column and a row degree one yield the same contradiction, or all three columns have degree one, forcing row degrees \(2,1\); then a row of degree two and a column of degree one violate (2). Thus precisely the claimed three-edge stars are allowed, with \(m\binom{m+1}{3}\) choices. If \(n\ge m+2\), deleting one edge leaves every left weighted sum at least \(n-1\ge m+1\) and every right weighted sum at most \(m\); consequently every such deletion is proper, proving the last assertion.

For the orbit statement, the star-forest type is specified by the positive fibre sizes of the map \(L\to R\), which form an integer partition \(\lambda\) into parts of size at least two. Relabelling both sides permutes the leaves and centers arbitrarily, so this partition is a complete orbit invariant when \(m<n\). If \(m=n\), swapping the two parts interchanges the two disjoint star-forest orientations, and produces no additional orbit distinctions. For a fixed \(\lambda\), first partition \(L\) into unlabelled blocks of these sizes in \(m!/\left((\prod_i\lambda_i!)(\prod_s a_s!)\right)\) ways, then inject the \(t\) blocks into the \(n\) labelled potential centers in \((n)_t\) ways. Multiply by two for the two disjoint orientations only in the balanced case. This proves the orbit formula and completes the proof.

## Verification

The standalone standard-library Python program `verify.py` independently tests selected-edge subsets against the literal induced-sum condition (1), rather than using the structural classification as its definition. It completely enumerates all binary matrices for 17 biclique sizes satisfying \(1\le m\le n\le7\) and \(mn\le16\), representing 125,006 binary assignments. It separately exhausts the relevant sparse, dense, and three-deletion slices of \(K_{3,6}\), \(K_{4,5}\), \(K_{5,5}\), and \(K_{5,6}\), comparing 1,200 proper extremal configurations to the formulas. The orbit multiplicities are checked against the independent fibre-occupancy recurrence in 30 parameter settings. All checks pass. Execute with `python3 verify.py` in an ordinary Python 3 environment. No finite check is used as proof of an infinite statement.

## Relationship to prior work

The same vertex-sum notion appears in Lu (2016) and in Aute--Panolan--Philip (2026). The former establishes general existence conditions for proper two-weightings of bipartite graphs; the latter investigates computational complexity, parameterized algorithms, and extension of preassigned weights. Neither of the inspected accessible results gives the exact multiplicities and orbits of minimum-support binary weightings on bicliques or the sharp three-deletion gap for consecutive part sizes.

Bensmail and collaborators (2025), *Graph Irregularity via Edge Deletions*, Theorem 4.2, already show that a balanced biclique requires \(q\) deletions to become locally irregular, while an unbalanced biclique is locally irregular without deletions. Those numerical endpoints are not claimed as new. Their edge-irregulator notion checks degree discrepancies only along **retained edges**, whereas proper binary weighting checks inequalities along **all original edges, including weight-zero edges**. The present result refines the analogous full-graph weighting problem by counting and classifying its extremizers and identifying a sharp gap immediately below the all-one weighting on \(K_{m,m+1}\).

The 2011 paper of Chang, Lu, Wu and Yu establishes existence of additive vertex-colouring edge-weightings for several graph classes, including regular bipartite graphs; existence is not claimed here as new. Further relevant literature includes Madarasi--Simon (2026) on complexity and extension of \(\{a,b\}\)-weightings. See limitations for access qualifications.

## Limitations

This theorem does **not** give every coefficient of the full support polynomial for arbitrary rectangular bicliques; it gives all minimizers, all maximizers, the complete symmetry in the square case, and the first nontrivial high-support layer in the consecutive-size case. The closed minimum counts concern labelled edge weightings, whereas orbit counts identify weightings under graph automorphisms. The 2026 Aute--Panolan--Philip paper's complete text was not accessible through the lawful sources attempted here, so a possible uninspected coverage risk remains; abstract-level comparison alone cannot rule out overlap. Independent mathematical audit and definitive publication-priority verification have not been performed.

## References

1. Shubhada Aute, Fahad Panolan, Geevarghese Philip, *Vertex-Coloring Edge-Weighting: Kernelization and Generalization*, arXiv:2609.27719, first submitted 2026-09-23. https://arxiv.org/abs/2609.27719
2. Hongliang Lu, *Vertex-Coloring Edge-Weighting of Bipartite Graphs with Two Edge Weights*, Discrete Mathematics & Theoretical Computer Science 17:3 (2016), doi:10.46298/dmtcs.2162. https://dmtcs.episciences.org/2162/pdf
3. *Graph Irregularity via Edge Deletions*, arXiv:2511.14514v1 (2025), especially Theorem 4.2. https://arxiv.org/html/2511.14514v1
4. G. J. Chang, C. Lu, J. Wu, Q. Yu, *Vertex-coloring Edge-weightings of Graphs*, Taiwanese Journal of Mathematics 15 (2011), doi:10.11650/twjm/1500406380.
5. Péter Madarasi and Máté Simon, *Complexity, approximation, and extension of proper \(\{a,b\}\)-edge-weightings*, arXiv:2609.31205 (2026). https://arxiv.org/abs/2609.31205
