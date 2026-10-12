# Induced-forest enumerator and extremal component spectrum of rectangular rook graphs

## Finding
For integers \(m,n\ge2\), let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\), with vertices identified with the \(mn\) edges of the complete bipartite graph. Define
\[
\mathcal F_{m,n}(z,w)=\sum_{S\subseteq V(R_{m,n})\, :\, R_{m,n}[S]\text{ is a forest}} z^{|S|}w^{c(R_{m,n}[S])},
\]
where the empty forest has zero components. Then the complete bivariate size-and-component enumerator is given by the coefficient-extraction identity
\[
\boxed{\sum_{m,n\ge0}\mathcal F_{m,n}(z,w)\frac{u^m v^n}{m!n!}
=\exp\!\left(u+v+\frac{wuv\bigl(z+\tfrac12(u+v)z^2\bigr)}{1-uvz^2}\right).}
\]
Here the natural empty-side extension \(\mathcal F_{0,n}=\mathcal F_{m,0}=1\) is used only to make the exponential generating function well formed.

Write \(a=\min(m,n)\) and \(b=\max(m,n)\), with \(a,b\ge2\). The maximum order of an induced forest, and hence the minimum feedback-vertex-set size, are
\[
\alpha_{\rm IF}(R_{m,n})=\min\{a+b-1,2a\},\qquad
\tau_{\rm FVS}(R_{m,n})=mn-\min\{a+b-1,2a\}.
\]
The number \(N_{a,b,k}\) of maximum-order induced forests having exactly \(k\) connected components is *entirely explicit*:
\[
\boxed{\begin{aligned}
N_{a,a,1}&=(a!)^2, &N_{a,a,k}&=0\quad(k\ne1),\\
N_{a,b,k}&=\frac{a!b!}{2^k k!\,(b-a-k)!}\binom{a-1}{k-1}
& &\quad (a<b,\ 1\le k\le\min\{a,b-a\}),
\end{aligned}}
\]
with all other \(N_{a,b,k}\) equal to zero. Consequently *all* minimum feedback vertex sets are complements of these counted configurations. A maximum induced forest is necessarily connected when \(b\le a+1\); disconnected maximum induced forests exist exactly when \(b\ge a+2\).

For instance, \(R_{2,4}\) has 30 maximum induced forests of four vertices: 24 connected ones and six having two components.

## Assumptions and scope
All graphs are finite, simple and undirected; the two bipartition classes of \(K_{m,n}\) are distinguished labeled vertex sets, each of size \(m\) or \(n\). In \(R_{m,n}\), adjacency means sharing a row or a column, equivalently sharing an endpoint in \(K_{m,n}\). The polynomial counts vertex subsets, *not* different traversal orientations of paths. A forest means an acyclic (not necessarily connected) induced subgraph. A feedback vertex set is a vertex set whose deletion leaves an induced forest. The statement holds for every pair of integers \(m,n\ge2\); the generating-function identity also holds formally for \(m,n\ge0\). The formal series is expanded with respect to \(u,v\); its denominator is a unit in the ring of formal power series.

## Proof
**1. Transfer to linear forests.** For a selected vertex subset \(S\subseteq V(R_{m,n})=E(K_{m,n})\), form the spanning edge subgraph \(H_S=(V(K_{m,n}),S)\). If any vertex of \(H_S\) has degree at least three, the three incident edges form a triangle in \(L(H_S)=R_{m,n}[S]\). If \(H_S\) contains any cycle, its consecutive edges form a cycle in its line graph. Hence an induced forest of \(R_{m,n}\) gives a cycle-free \(H_S\) of maximum degree at most two: a disjoint union of paths and isolated vertices. Conversely, the line graph of such a union is a disjoint union of paths, thus a forest. Each nontrivial path component of \(H_S\) contributes exactly one component to \(R_{m,n}[S]\), and its edge count equals the corresponding component's vertex count. This is a bijection of the relevant sets with preserved statistics.

**2. Count the alternating paths.** A bipartite path with opposite-side endpoints has \(r\ge1\) vertices of each bipartition class and \(2r-1\) edges. On any prescribed set of \(r\) labels in each class, the number of undirected alternating paths is \((r!)^2\): orient every path from its endpoint on the first side to its endpoint on the second side. Its contribution to the bivariate labeled exponential generating function, with edge variable \(z\), is \((uv)^r z^{2r-1}\).

A path with both endpoints in the first class has \(r+1\) vertices there and \(r\) in the second, with \(2r\) edges. On fixed labeled vertex sets it has \((r+1)!r!/2\) undirected realizations, because reversing a directed listing fixes the same undirected path and no nontrivial path is equal to its reversal as an ordered list. The contribution is \(u^{r+1}v^r z^{2r}/2\), with a symmetric term for endpoints in the second class. Therefore the connected nontrivial component series is
\[
P(u,v,z)=\sum_{r\ge1}(uv)^rz^{2r-1}
+\frac{u+v}{2}\sum_{r\ge1}(uv)^rz^{2r}
=\frac{uv(z+\tfrac12(u+v)z^2)}{1-uvz^2}.
\]
Unselected original vertices are isolated vertices of \(H_S\), with series \(u+v\) and no \(z,w\) weight. The exponential formula for labeled sets of components now yields \(\exp(u+v+wP(u,v,z))\), proving the asserted enumerator, including the \(S=\varnothing\) constant term and the normalization by \(m!n!\).

**3. Maximum size.** Assume \(2\le a\le b\). A linear forest with at most \(a+b\) vertices has at most \(a+b-1\) edges if it has any edge. Every vertex on the smaller bipartition side has degree at most two, giving at most \(2a\) edges. Hence \(|S|\le\min\{a+b-1,2a\}\). If \(a=b\), a spanning alternating Hamilton path has \(2a-1\) edges, attaining the first bound. If \(a<b\), an alternating path beginning and ending in the larger class and using all \(a\) smaller-class vertices has \(2a\) edges, attaining the second. This proves the maximum and, by complementation, the feedback vertex set minimum.

**4. All maximum configurations and their components.** If \(a=b\), a linear forest attaining \(2a-1\) edges must be connected and spanning: it is precisely a Hamilton path with opposite-class endpoints. Orient it from the first class to the second to count \(a!\) permutations of each class, hence \((a!)^2\) possibilities.

If \(a<b\), achieving \(2a\) edges forces *every* smaller-class vertex to have degree exactly two. Consequently every nontrivial component is an alternating path with both endpoints in the larger class. A component containing \(r\ge1\) smaller-class vertices uses \(r+1\) larger-class vertices, has \(2r\) edges, and contributes \(u^r v^{r+1}z^{2r}w/2\) to the component series, after the sides are suitably named. For exactly \(k\) such components, the relevant term is
\[
\frac{w^k}{2^k k!}v^k\left(\frac{uv z^2}{1-uvz^2}\right)^k,
\]
whose \(u^a v^{a+k}z^{2a}w^k\) coefficient is \(\binom{a-1}{k-1}/(2^k k!)\) by the positive-composition identity. The other \(b-a-k\) larger-class vertices are isolated, contributing \(1/(b-a-k)!\) from \(\exp(v)\). Multiplication by \(a!b!\) proves the displayed formula, and the constraints on \(k\) follow from having at least one smaller-side vertex per component and enough larger-side vertices. In particular, \(k\ge2\) is possible exactly when \(a\ge2\) and \(b-a\ge2\), proving the connectivity transition.

## Verification
The supplied standalone standard-library Python script `verify_linearforests.py` computes the displayed exponential generating function using exact rational arithmetic and independently enumerates all edge subsets of \(K_{m,n}\), rejecting degree-three vertices and cycles by disjoint-set union. It checks equality for all nine boards \(2\le m\le n\le5\) with \(m\le4\), including 1,152,848 edge subsets, and checks the extremal component formula in each case. An actual replay produced `VERIFY_OK`. Examples include total extremal counts \(30\) on \(R_{2,4}\), \(540\) on \(R_{3,5}\), and \(1440\) on \(R_{4,5}\). The finite comparisons are computational corroboration and are not used as the proof for all orders.

## Relationship to prior work
Fu and Huang's 1994 paper studies decomposition of complete bipartite edges into path forests of bounded component length, rather than the number of individual path forests. Chappell and Pelsmajer (2013) establish general bounds for maximum induced forests of bounded degree in bounded-treewidth graphs, not this labeled two-parameter enumerator. Novotná et al. (2020, Lemma 3) explicitly use the **known** transfer between induced forests of line graphs and vertex-disjoint paths in the original graph in a computational hardness proof. That structural transfer alone does not give an exact all-sizes component-count polynomial or the distribution of extremal forest components; it is used here as background, not asserted as new. The contributions asserted here are the evaluated exponential generating function specialized to every rectangular rook graph and the sharp all-maximizer component formula.

## Limitations
No claim is made about unrelated graph families, minimum feedback vertex sets beyond these rook graphs, or a new general line-graph/path-forest bijection. Classical labeled-combinatorial component methods are used; an earlier differently indexed explicit formula for this same family remains possible despite the documented searches. The exact finite verification does not independently certify the unrestricted symbolic claim, and no independent external mathematical audit has been performed.

## References
1. H.-L. Fu and K.-C. Huang, *The Linear 2-arboricity of Complete Bipartite Graphs*, Ars Combinatoria **38** (1994), 309–318, publisher date 1994-12-31. https://combinatorialpress.com/ars-articles/volume-038-ars-articles/the-linear-2-arboricity-of-complete-bipartite-graphs/
2. G. G. Chappell and M. J. Pelsmajer, *Maximum Induced Forests in Graphs of Bounded Treewidth*, Electronic Journal of Combinatorics **20** (2013), P8, published 2013-10-28. https://doi.org/10.37236/3826
3. J. Novotná, K. Okrasa, M. Pilipczuk, P. Rzążewski, E. J. van Leeuwen, and B. Walczak, *Subexponential-Time Algorithms for Finding Large Induced Sparse Subgraphs*, Algorithmica **83** (2021), 2634–2650, first online 2020-07-31; Lemma 3. https://doi.org/10.1007/s00453-020-00745-z
