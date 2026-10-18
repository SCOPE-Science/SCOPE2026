# Sperner and paired-incidence bounds for injective edge coloring of one-subdivisions

## Finding

For a finite simple undirected graph \(G\) containing an edge, write \(S(G)\) for the graph obtained by replacing each edge \(uv\) with a two-edge path \(u z_{uv}v\). Put \(q=\chi(G)\ge2\), and define
\[
L(q)=\min\left\{t\ge2:\binom{t}{\lfloor t/2\rfloor}\ge q\right\}.
\]
Then the injective chromatic index satisfies
\[
\boxed{\lceil\log_2 q\rceil\le\chi'_{\mathrm{inj}}(S(G))\le L(q).}
\]
There is also an independently applicable, stronger paired-incidence construction for complete graphs: for all integers \(t\ge2\) and \(2\le n\le 2\binom{t-1}{\lfloor(t-1)/2\rfloor}\),
\[
\boxed{\chi'_{\mathrm{inj}}(S(K_n))\le t.}
\]
Consequently, for every sequence of graphs whose chromatic numbers tend to infinity,
\[
\frac{\chi'_{\mathrm{inj}}(S(G))}{\log_2\chi(G)}\longrightarrow1,
\]
and, uniformly in this regime,
\[
\chi'_{\mathrm{inj}}(S(G))\le\log_2\chi(G)+\frac12\log_2\log_2\chi(G)+O(1).
\]
For a concrete finite comparison, \(S(K_{12})\) admits an injective five-edge-coloring via the paired construction, while the unrestricted middle-layer construction at five colors accommodates only ten vertex labels.

## Assumptions and scope

All graphs are finite, simple, undirected, and loopless. An injective edge coloring assigns colors to edges such that the first and third edges on any three-edge path (or three-cycle) have distinct colors; equivalently, if two edges share a color, no third, distinct edge joins their endpoints. Here every subdivided graph is bipartite and triangle-free, so checking three-edge paths suffices. A color need not distinguish adjacent edges. No optimality beyond the proved lower bound is claimed at a fixed finite chromatic number; in particular the paired complete-graph bounds are upper bounds, not exact formulas.

## Proof

**1. A directed-incidence representation.** Label an edge \(u z_{uv}\) of \(S(G)\) by the directed arc \(u\to v\) of the bidirected original graph. The outer edges of a three-edge path \(u,z_{uv},v,z_{vw}\), with \(u,v,w\) distinct, correspond to \(u\to v\) and \(v\to w\). Thus an incidence edge coloring is injective if and only if no two consecutive arcs of a directed two-path on three distinct vertices have the same color. This also covers the reversed paths, and there are no triangle constraints in \(S(G)\).

**2. The antichain upper bound.** Fix a proper vertex \(q\)-coloring \(\kappa\) of \(G\). Let \(t=L(q)\), choose \(q\) distinct sets \(A_1,\ldots,A_q\subseteq[t]\), each of cardinality \(\lfloor t/2\rfloor\), and assign \(A(v)=A_{\kappa(v)}\) to each original vertex. For every oriented original edge \(u\to v\), color its corresponding subdivided incidence edge by any member of the nonempty difference \(A(u)\setminus A(v)\); for reproducibility, take the least member. Nonemptiness follows because \(\kappa(u)\ne\kappa(v)\) and distinct equal-sized sets are incomparable.

If \(u\to v\to w\) were a monochromatic directed two-path, its first color would belong to \(A(u)\setminus A(v)\) while its second would belong to \(A(v)\setminus A(w)\). These sets are disjoint. This proves \(\chi'_{\mathrm{inj}}(S(G))\le t\).

**3. A paired improvement on cliques.** Fix \(t\ge2\) and let \(r=t-1\). Form distinct equal-sized subsets \(B_1,\ldots,B_b\subseteq[r]\), where \(b=\binom r{\lfloor r/2\rfloor}\). Begin with \(K_{2b}\) whose vertices are partitioned into pairs \(P_i=\{v_{i,0},v_{i,1}\}\); both members of \(P_i\) carry code \(B_i\). For each original edge internal to \(P_i\), color both subdivided incidences by the new color \(t\). For an original edge directed from pair \(P_i\) to a different pair \(P_j\), color the corresponding incidence with any member of \(B_i\setminus B_j\subseteq[r]\), which is nonempty. Coordinate colors cannot repeat on consecutive arcs because they would have to lie both inside and outside the intermediate pair's code. A consecutive two-path cannot use color \(t\) on both arcs: those arcs would have to represent two distinct edges of the fixed matching \(\{v_{i,0}v_{i,1}\}\), which is impossible at a common middle original vertex. Hence the coloring is injective. Restricting it to any \(n\le2b\) original vertices gives the stated bound. In particular \(t=5\) allows \(2\binom42=12\) vertices.

**4. The universal lower bound.** Suppose \(S(G)\) has an injective edge coloring using \(t\) colors. For a color \(c\), let \(D_c\) be the directed graph on \(V(G)\) containing exactly the arcs whose corresponding subdivided incidences have color \(c\). No directed two-path with three different vertices can occur in \(D_c\). Consequently, if a vertex has both an incoming and an outgoing arc in \(D_c\), then they must go to the same sole neighbor; this gives an isolated reciprocated pair. All other edge-containing components have every vertex a pure source or a pure sink. Therefore, the underlying simple graph \(H_c\) is bipartite (and isolated vertices can be placed arbitrarily). Choose a bipartition \(V(G)=X_c\sqcup Y_c\) of each \(H_c\) (including isolated vertices). Give \(v\) its membership signature of length \(t\). Since every original edge \(uv\) appears in at least one \(H_c\), its endpoints have different signatures. These signatures form a proper vertex coloring of \(G\) with at most \(2^t\) colors. Thus \(t\ge\lceil\log_2\chi(G)\rceil\). This reestablishes the lower bound from Bradshaw–Clow–Xu's Proposition 2.5 independently of the upper construction.

**5. Sharp leading logarithmic coefficient.** The central binomial coefficient satisfies \(\binom{t}{\lfloor t/2\rfloor}=\Theta(2^t/\sqrt t)\), with positive absolute implied constants. Consequently \(L(q)=\log_2 q+\frac12\log_2\log_2 q+O(1)\) as \(q\to\infty\). Combining this upper bound with Step 4 and dividing by \(\log_2 q\) proves the asserted limit.

## Verification

The standalone `verify.py` program constructs both colorings using fixed integer bitsets and checks all ordered directed two-paths in the original graph. Its tests include complete graphs for middle-layer palette sizes from two to eight, paired complete graphs at representative capacities including \(t=5,n=12\), and path/cycle cases on up to thirty vertices. Running `python3 verify.py` reproduces the separately embedded `verification_output.txt`, including `VERIFY_OK`, 16,320 oriented incidences, and 819,942 ordered two-path comparisons. The finite checks verify concrete constructions only; Steps 1–5 constitute the proof for unbounded parameters.

## Relationship to prior work

Bradshaw, Clow and Xu, *Injective edge colorings of degenerate graphs and the oriented chromatic number* (first arXiv posting 2023-08-29), Proposition 2.5, prove the lower bound \(\log_2\chi(G)\) for this exact one-subdivision. Their immediately subsequent remark gives \(2\lceil\log_2\chi(G)\rceil\) as an upper bound. The new middle-layer construction improves the leading factor two to one, with a quantified additive logarithmic correction; the paired construction improves the finite clique capacity of that middle-layer approach. Those quantitative upper statements do not follow from the published lower bound or their factor-two upper bound.

Axenovich, Dörr, Rollin and Ueckerdt, *Induced and Weak Induced Arboricities* (2018), provide the induced-star-forest vocabulary and broader parameter framework, but their inspected definitions and general class statements do not yield these subdivision-specific capacities. Ferdjallah, Kerdjoudj and Raspaud (2019) concern injective edge coloring of sparse graphs primarily via maximum-degree bounds, not this chromatic-number transfer. A particularly relevant paper by Priyamvada and Panda, *Injective edge coloring of some standard graph products* (2023 online/2024 volume, DOI below), explicitly treats subdivision operations; only its abstract was accessible. Its uninspected full text could contain a stronger bound, so the originality comparison with that paper is unresolved at full-document level. The present result must not be represented as independently certified new mathematics.

## Limitations

The individual finite-parameter optima are not determined: the lower and upper bounds can differ by approximately one half the binary logarithm of the binary logarithm of \(q\). No uniqueness of optimal colorings is asserted. The paired improvement is proved for subdivided complete graphs, not an arbitrary graph having the same chromatic number. Historical completeness remains limited by inaccessible relevant primary full text, especially Priyamvada–Panda's subdivision results. No independent scientific audit has been performed.

## References

1. P. Bradshaw, A. Clow and J. Xu, *Injective edge colorings of degenerate graphs and the oriented chromatic number*, arXiv:2308.15654v1 (2023-08-29), Proposition 2.5 and following upper-bound remark. https://arxiv.org/html/2308.15654v1
2. M. Axenovich, P. Dörr, J. Rollin and T. Ueckerdt, *Induced and Weak Induced Arboricities*, arXiv:1803.02152v1 (2018-03-06). https://arxiv.org/html/1803.02152v1
3. B. Ferdjallah, S. Kerdjoudj and A. Raspaud, *Injective edge-coloring of sparse graphs*, arXiv:1907.09838 (2019). https://arxiv.org/abs/1907.09838
4. Priyamvada and B. S. Panda, *Injective edge coloring of some standard graph products*, Discrete Mathematics, Algorithms and Applications 16(4) (2024), Article 2350041; first online May 2023 per publisher-linked bibliographic record. DOI:10.1142/S1793830923500416. Full-text comparison unavailable.
