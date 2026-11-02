# Domination polynomials of full edge subdivisions and their induced-matching minima

## Finding

For **every finite undirected simple graph**, including graphs with multiple components or isolated vertices, the ordinary domination polynomial of its full one-edge subdivision has a vertex-subset formula. The smallest exponent is also determined by the maximum induced matching size of the original graph. More precisely, for notation defined below,

\[
\boxed{D_{S(G)}(z)=\sum_{W\subseteq V} z^{n-|W|+e_W}(1+z)^{q_W}\prod_{v\in I_W}\left((1+z)^{d_v}-1\right).}
\]

\[
\boxed{\gamma(S(G))=n-\nu_s(G).}
\]

Every minimum dominating set is classified by an induced forest of the original graph, as stated precisely below; the formulas count *sets*, not perfect matchings or weighted covers.

## Assumptions and scope

The graph \(G=(V,E)\) is finite, simple, undirected, and may be disconnected; write \(n=|V|\), \(m=|E|\). Its full subdivision \(S(G)\) has original vertices \(V\) and a distinct degree-two subdivision vertex \(s_e\) for every edge \(e\in E\); the neighbors of \(s_{uv}\) are exactly \(u,v\), and no original vertices are adjacent. A dominating set includes each vertex itself when determining which vertices are dominated.

The ordinary domination polynomial is \(D_H(z)=\sum_{D\subseteq V(H):\,D\text{ dominating}}z^{|D|}\). For each \(W\subseteq V\), define \(e_W=|E(G[W])|\), \(I_W=\{v\in W:\deg_{G[W]}(v)=0\}\), \(d_v=\deg_G(v)\), and \(q_W=m-e_W-\sum_{v\in I_W}d_v\). The induced matching number \(\nu_s(G)\) is the largest number of disjoint edges whose union of endpoints induces exactly those edges. An empty graph has \(\nu_s(G)=0\). Empty products equal one. The factor for a vertex with \(d_v=0\) is zero, as required.

## Proof

**1. Exact partition by omitted original vertices.** Fix a dominating set \(D\) of \(S(G)\), and put \(W=V\setminus(D\cap V)\). Every edge \(uv\in E(G[W])\) has both originals absent, so \(s_{uv}\in D\) is forced. Any \(v\in W\setminus I_W\) is already dominated by one of those forced subdivision vertices. An isolated vertex \(v\in I_W\) has no forced incident subdivision vertex and must instead choose a *nonempty* subset of its \(d_v\) incident subdivision vertices. The associated edge stars are pairwise disjoint for distinct vertices of \(I_W\), and they are disjoint from \(E(G[W])\); an edge with both endpoints in \(W\) cannot meet an isolated vertex of \(G[W]\). Finally, every subdivision vertex corresponding to an edge outside these forced and locally selected stars has at least one selected original endpoint, so its membership in \(D\) is free. Exactly \(q_W\ge0\) such subdivision vertices remain. Hence, fixing \(W\), the weighted sum of valid \(D\)'s is precisely

\[
z^{n-|W|+e_W}(1+z)^{q_W}\prod_{v\in I_W}\left((1+z)^{d_v}-1\right).
\]

Distinct omitted-original subsets are disjoint counting classes, so summing over \(W\subseteq V\) proves the full polynomial identity.

**2. Sharp domination number.** For each fixed \(W\) with a feasible dominating set, the minimum possible number of selected vertices is \(n-|W|+e_W+|I_W|\). Let \(H_1,\ldots,H_c\) denote the nontrivial connected components of \(G[W]\). Removing isolated vertices gives

\[
|W|-e_W-|I_W|=\sum_{j=1}^{c}(|V(H_j)|-|E(H_j)|)\le c.
\]

Each nontrivial component contains an edge. Taking one edge from each yields an **induced matching of \(G\)**, because no edge of \(G\) joins distinct components of the *induced* graph \(G[W]\). Thus \(c\le\nu_s(G)\). Every dominating set therefore has at least \(n-\nu_s(G)\) vertices. Conversely, let \(M\) be a maximum induced matching and let \(W\) be its \(2\nu_s(G)\) endpoints. Select all original vertices outside \(W\) and the \(\nu_s(G)\) subdivision vertices corresponding to the edges of \(M\). This dominates every vertex and has \(n-\nu_s(G)\) elements. The same construction works for the empty matching in an edgeless graph.

**3. Classification and count of all minima.** Equality throughout the preceding bounds requires exactly \(\nu_s(G)\) nontrivial components of \(G[W]\), and \(|E(H_j)|=|V(H_j)|-1\) in every one: each must be a tree. No original isolated vertex of degree zero can be omitted. Conversely, any \(W\) with those properties yields a minimum dominating set by selecting all originals outside \(W\), all subdivision vertices from \(E(G[W])\), and exactly one incident boundary subdivision vertex for each \(v\in I_W\). None of the other subdivision vertices is selected. These are *all* minima, since selecting extra subdivision vertices or more than one boundary vertex increases the cardinality. Each choice of \(W\) contributes \(\prod_{v\in I_W}d_v\) distinct minimum sets, without duplication, because \(W\) is uniquely recovered from the dominating set. Thus

\[
\boxed{N_{\min}(G)=\sum_{\substack{W\subseteq V,\;G[W]\text{ forest},\\c_+(G[W])=\nu_s(G),\;d_v>0\ (v\in I_W)}}\ \prod_{v\in I_W}d_v,}
\]

where \(c_+(G[W])\) is the number of components containing an edge.

**4. Natural specializations.** When \(G=K_n\) with \(n\ge2\) and \(M=\binom n2\), a set \(W\) of size one contributes \(z^{n-1}((1+z)^M-(1+z)^{M-n+1})\); a set \(W\) of size \(w\ge2\) has no induced isolated vertices. Consequently,

\[
\begin{aligned}
D_{S(K_n)}(z)={}&z^n(1+z)^M+n z^{n-1}\big((1+z)^M-(1+z)^{M-n+1}\big)\\
&+\sum_{w=2}^n\binom nw z^{n-w+\binom w2}(1+z)^{M-\binom w2}.
\end{aligned}
\]

Here the unique nontrivial induced-tree component of \(K_n\) must be an edge, so there are exactly \(\binom n2\) minimum sets. For \(G=K_{a,b}\) with \(a,b\ge1\), every induced forest with one nontrivial component is a star with a singleton side and an arbitrary nonempty opposite-side subset. Counting these, subtracting twice-counted single edges, yields

\[
\gamma(S(K_{a,b}))=a+b-1,\qquad N_{\min}(K_{a,b})=a(2^b-1)+b(2^a-1)-ab.
\]

## Verification

The bundled standard-library-only program `verify.py` independently builds the subdivided graph's adjacency, directly enumerates dominating vertex sets, and compares the entire polynomial with the partition formula. It independently enumerates induced matchings and verifies every minimum dominating set's forest structure and exact multiplicity. It compares complete and complete-bipartite specializations as well. Executing `python3 verify.py` produced:

`VERIFY_OK 56 graphs; 104426 direct vertex subsets tested; arbitrary-graph polynomial, induced-matching minimum, minimum-set formula, complete and bipartite specializations`

The finite checks are corroboration, **not** a substitute for the preceding all-graph proof. As a coefficient example, \(D_{S(K_3)}(z)=3z^2+14z^3+15z^4+6z^5+z^6\).

## Relationship to prior work

The domination polynomial and general reduction/splitting formulas for arbitrary graphs were studied by Kotek, Preen, Simon, Tittmann and Trinks (2012); their results are general graph recurrences, not a stated formula in terms of the original graph's induced vertex subsets for *full edge subdivisions*. Fujita, Kazemnejad and Pahlavsay (first public preprint 2022) studied the domination **number** of central graphs, which differ from full subdivisions by adding edges among originally nonadjacent vertices. For complete roots, the operations coincide, and their scalar value agrees with the specialization here; that scalar value is not claimed as a new discovery. Ko and Shepherd (2003) connect domination and induced matching in bipartite graph algorithms, but their stated simultaneous-cover framework does not give this all-set cardinality polynomial. Babikir, Dettlaff, Henning and Lemańska (2021) examine how many edges must be subdivided to raise an independent domination number, a different invariant. Ahmadi, Vatandoost and Behtoei (2025) address identifying codes of full subdivisions; only their abstract, not their full text, could be inspected. Mahmoodi, Behmaram, Došlić and Asadi (2024) study **dominating induced matchings**, a different condition from taking a maximum (not necessarily dominating) induced matching.

No priority or independence certification is asserted: an older unindexed direct formula or a transformation not identified in inspected sources remains possible.

## Limitations

This is a theorem for one-edge subdivisions of finite *simple* graphs. It does not cover repeated subdivisions, loops, multigraphs, weighted domination, or other domination variants. Its exact polynomial sum has up to \(2^n\) terms, so it is not asserted to be polynomial-time computable for unrestricted input graphs. The known general domination-polynomial recurrences and related matching reductions can be applied algorithmically but do not by themselves establish publication priority of this particular formula. A plausible publisher-hosted 2025 study was inaccessible beyond its abstract.

## References

1. T. Kotek, J. Preen, F. Simon, P. Tittmann, M. Trinks, *Recurrence relations and splitting formulas for the domination polynomial*, Electronic Journal of Combinatorics 19(3), P47 (2012), DOI: 10.37236/2475.
2. S. Fujita, F. Kazemnejad, B. Pahlavsay, *New classification of graphs in view of the domination number of central graphs*, arXiv:2204.10292v1 (20 April 2022), https://arxiv.org/abs/2204.10292.
3. C. W. Ko and F. B. Shepherd, *Bipartite domination and simultaneous matroid covers*, SIAM Journal on Discrete Mathematics 16(4), 517–523 (2003), DOI: 10.1137/S089548019828371X.
4. A. Babikir, M. Dettlaff, M. A. Henning and M. Lemańska, *Independent domination subdivision in graphs*, Graphs and Combinatorics 37, 691–709 (2021), DOI: 10.1007/s00373-020-02269-3.
5. S. Ahmadi, E. Vatandoost and A. Behtoei, *Domination number and identifying code number of the subdivision graphs*, Journal of Algebraic Systems 13(2), 1–11 (2025), DOI: 10.22044/jas.2023.12257.1649.
6. A. Mahmoodi, A. Behmaram, T. Došlić and N. Asadi, *Dominating induced matchings and other graph parameters*, AKCE International Journal of Graphs and Combinatorics 21(3), 261–267 (2024), DOI: 10.1080/09728600.2024.2342310.
