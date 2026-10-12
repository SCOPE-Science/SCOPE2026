# Rank censuses and a sharp regularity criterion for biclique continuous-map monoids

## Finding

Let \(m,n\ge 2\), let \(G=K_{m,n}\) with its two independent vertex parts \(X,Y\), and let \(\operatorname{MR}(G)\) be the monoid of partial self-maps whose inverse image of each vertex or edge simplex is empty or a simplex. An element is *regular* if \(fgf=f\) for some \(g\in\operatorname{MR}(G)\). For a nonempty image contained in a single part, call a fiber *singleton* if it has one element.

**Structural criterion.** A map \(f\in\operatorname{MR}(G)\) is nonregular **if and only if** its image lies in one part and it has at least one singleton fiber whose source belongs to \(X\) and another singleton fiber whose source belongs to \(Y\). Maps whose images meet both parts are always regular. The nonregular ranks are exactly \(2,3,\ldots,\max(m,n)\).

Here are explicit polynomials recording the ranks of all maps, nonregular maps, and idempotents:
\[
H_{m,n}(z)=\sum_{f\in\operatorname{MR}(G)}z^{|\operatorname{im}f|},\qquad
Q_{m,n}(z)=\sum_{f\text{ nonregular}}z^{|\operatorname{im}f|},\qquad
E_{m,n}(z)=\sum_{f^2=f}z^{|\operatorname{im}f|}.
\]
Write \((s)_j=s(s-1)\cdots(s-j+1)\) for \(0\le j\le s\), with \((s)_0=1\), and put \((s)_j=0\) for \(j>s\). Binomial coefficients are zero outside their ordinary range. Define
\[
T_k=\sum_{c=0}^{\min(k,m,n)}\binom{k}{c}(m)_c(n)_c(m+n-2c)_{k-c},
\]
\[
F_k=\sum_{\substack{a,b\ge1\\a+b\le k}}
\frac{k!}{a!b!(k-a-b)!}(m)_{k-b}(n)_{k-a},\qquad
U_k(s)=\sum_{c=0}^{\min(k,s)}\binom{k}{c}(s)_c.
\]
Then the complete rank enumerators are
\[
\boxed{\begin{aligned}
H_{m,n}(z)={}&1+\sum_{k=1}^{\max(m,n)}
\left(\binom mk+\binom nk\right)T_kz^k\\
&+\sum_{a=1}^{m}\sum_{b=1}^{n}\binom ma\binom nb
\left((m)_a(n)_b+(n)_a(m)_b\right)z^{a+b},
\end{aligned}}
\]
\[
\boxed{Q_{m,n}(z)=\sum_{k=2}^{\max(m,n)}
\left(\binom mk+\binom nk\right)F_kz^k,}
\]
\[
\boxed{\begin{aligned}
E_{m,n}(z)={}&1+\sum_{k=1}^{m}\binom mk U_k(n)z^k
+\sum_{k=1}^{n}\binom nk U_k(m)z^k\\
&+\sum_{a=1}^{m}\sum_{b=1}^{n}\binom ma\binom nb z^{a+b}.
\end{aligned}}
\]
The rank enumerator of regular elements is \(H_{m,n}(z)-Q_{m,n}(z)\). In particular, the graph \(K_{2,2}\) has \(169\) maps, of which \(16\) are nonregular and \(36\) are idempotent; \(K_{2,3}\) has respectively \(874,174,86\), and \(K_{3,3}\) has \(4489,756,220\). The singleton-part cases are excluded from the novel scope: their known star-graph specialization is consistent with these formulas.

## Assumptions and scope

Every vertex set is labeled, each part of the biclique has its stated positive size, and partial maps include the empty map. The rank is the number of distinct values in the image, not the size of the domain. The continuity convention uses the *full* inverse image of a simplex: for every singleton vertex and every two-vertex edge in the target graph, that inverse image must be empty, one vertex, or one edge of the source graph. The theorem concerns the full monoid \(\operatorname{MR}(G)\), not only its strict or injective subsemigroups. No assumptions about a field or coefficients occur.

## Proof

**1. Fiber structure.** Each nonempty fiber is a singleton or a cross-part edge. If an image vertex \(u\) has a two-vertex fiber, every neighbor \(v\) of \(u\) must be absent from the image: otherwise the full inverse image of the target edge \(\{u,v\}\) contains at least three vertices. Thus a map whose image meets both sides of \(K_{m,n}\) has only singleton fibers and is injective. For such an image, each pair \(u\in X\), \(v\in Y\) has adjacent representatives under the inverse map; complete bipartiteness forces all representatives of \(X\)-image vertices to lie in one source part and all representatives of \(Y\)-image vertices to lie in the opposite source part. Therefore the partial inverse itself satisfies continuity, so \(f\) is regular.

**2. The exact regularity obstruction for independent images.** Suppose the image \(S\) lies entirely in one part. Since the image has no edges, a fiber decomposition using disjoint singleton vertices and disjoint cross-part edges automatically defines a continuous map. A regularity witness \(g\) with \(fgf=f\), restricted to \(S\), must select one representative from each fiber of \(f\). Conversely, any such continuous section is a regularity witness. Because \(S\) is independent, a section is continuous precisely when its distinct selected representatives constitute an independent subset of the source biclique: representatives from opposite source parts would have an edge with a two-vertex inverse image in the independent set \(S\), violating continuity. Every cross-part two-vertex fiber offers one representative in each source part, whereas a singleton fiber has a forced representative. Hence a continuous section exists exactly when all singleton fibers originate in a single source part (including the case of no singleton fibers). This proves the criterion.

**3. All-map count.** Fix an independent image \(S\) of size \(k\). If exactly \(c\) labeled values have paired fibers, choose them in \(\binom{k}{c}\) ways and assign distinct source endpoints in the two parts in \((m)_c(n)_c\) ways. The other \(k-c\) labeled values receive distinct singleton source vertices from the \(m+n-2c\) unused vertices, contributing \((m+n-2c)_{k-c}\). Thus their count is \(T_k\), and there are \(\binom mk+\binom nk\) possible independent image sets. Now fix an image containing \(a\) vertices in \(X\) and \(b\) in \(Y\), with \(a,b\ge1\). By step 1 all fibers are singletons. The representative assignment either preserves or interchanges the bipartition, giving \((m)_a(n)_b+(n)_a(m)_b\) maps for each of the \(\binom ma\binom nb\) such image sets. Finally there is one empty map. These disjoint cases give \(H_{m,n}\).

**4. Nonregular count.** For a fixed independent image of \(k\) labeled vertices, let \(a\) fibers be singleton with source in \(X\), \(b\) singleton with source in \(Y\), and \(c=k-a-b\) paired. The obstruction is exactly \(a,b\ge1\). Assigning these types costs \(k!/(a!b!c!)\), then distinct \(X\) and \(Y\) source vertices can be chosen in \((m)_{a+c}(n)_{b+c}=(m)_{k-b}(n)_{k-a}\) ways. Summing gives \(F_k\); multiplying by the number of independent image sets gives \(Q_{m,n}\). A nonregular map has rank at least two and cannot have rank exceeding the larger part. For every rank from two up to \(\max(m,n)\), take a target image in the larger part, one singleton fiber sourced in the smaller part, and the other singleton fibers sourced in the larger source part; this realizes the obstruction. The rank cutoff is therefore sharp.

**5. Idempotent count.** An idempotent fixes every point of its image. If its image meets both graph parts, it cannot have a paired fiber, so it is the partial identity on the image, with \(\binom ma\binom nb\) possibilities for image part-sizes \(a,b\ge1\). If the image consists of \(k\) vertices in \(X\), then each fixed vertex may additionally receive one unused source from \(Y\), and those extras must be distinct. Choosing exactly \(c\) extras yields \(\binom{k}{c}(n)_c\); summing gives \(U_k(n)\). The case of image in \(Y\) is symmetric. Adding the empty idempotent proves \(E_{m,n}\).

## Verification

Run `python3 verify.py` with Python 3 and no third-party dependencies. The verifier independently enumerates every partial map and checks each vertex and edge preimage directly. It tests regularity by enumerating continuous sections, tests idempotence by explicit evaluation, and compares the observed rank distributions with all three formulas for the seven cases \(K_{1,1},K_{1,2},K_{1,3},K_{1,4},K_{2,2},K_{2,3},K_{3,3}\). For the graphs of order at most four, it additionally searches the entire monoid for a witness to \(fgf=f\), independently confirming the section test. All tests finish with `VERIFY_OK`. Finite enumeration is only corroboration, not a proof for arbitrary sizes; steps 1–5 provide that proof.

## Relationship to prior work

Margolis and Rhodes established the graph-continuity framework and its matching/injective decomposition. Their later treatment gives detailed enumerations for paths and cycles and structural results for strict semigroups on bipartite graphs. The 2020 paper computes the **strict** semigroup on balanced complete bipartite graphs, whose enumerator is not the full-monoid rank enumerator here. The present theorem supplies a **full-monoid**, two-parameter rank-by-rank regularity census and a separate idempotent census for the complete bipartite family; neither the strict counts nor the general fiber decomposition alone states these formulas. A prior star-graph census already covers the \(\min(m,n)=1\) subfamily, explicitly excluded from the novel scope.

## Limitations

The novel claim is limited to complete bipartite graphs with both parts of size at least two. These formulas do not classify arbitrary bipartite graphs, their Krohn–Rhodes complexities, or finer Green-class cardinalities. The proof gives exact labeled counts, not isomorphism classes of the partial maps. The computational checks cover only listed small graphs. Novelty is conditional on available published literature: a differently phrased older biclique enumeration might exist.

## References

1. S. Margolis and J. Rhodes, *The Margolis–Rhodes Monoid of Continuous Functions on a Graph*, arXiv:2609.39370, first version dated 2026-09-30; especially the structural decomposition and Sections 3, 4, and 7 of version 2. https://arxiv.org/abs/2609.39370
2. S. Margolis and J. Rhodes, *Degree 2 Transformation Semigroups as Continuous Maps on Graphs: Foundations and Structure*, arXiv:2005.02606, 2020; particularly Lemma 2.6 and Example 2.11 on the strict balanced biclique semigroup. https://arxiv.org/abs/2005.02606
