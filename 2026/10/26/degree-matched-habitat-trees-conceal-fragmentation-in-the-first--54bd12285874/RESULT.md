# Degree-matched habitat trees conceal fragmentation in the first two moments, but not the third

## Finding

Let \(T\) and \(U\) be finite simple trees on the same \(n\ge 2\) vertices and with the same degree multiset. Retain every vertex independently with probability \(p\in(0,1)\), and let \(C_T\) be the number of connected components of the induced subgraph on retained vertices, with \(C_T=0\) for the empty subgraph. Define the component-count probability generating function \(H_T(p,z)=\mathbb E[z^{C_T}]\), and let
\[
L(T)=\sum_{\{u,v\}\in E(T)}(\deg_T(u)-1)(\deg_T(v)-1),
\]
which counts the unoriented paths of exactly three edges.

**Theorem.** For every such pair and every \(0<p<1\):

1. The means and variances of \(C_T\) and \(C_U\) are identical.
2. Their third cumulants satisfy the exact all-order identity
   \[
   \kappa_3(C_T)-\kappa_3(C_U)=-6\bigl(L(T)-L(U)\bigr)p^4(1-p)^2.
   \]
   In particular, unequal three-edge-path counts force opposite, nonzero differences in their unstandardized third centered moments at **every** interior survival probability.
3. The polynomial difference \(H_T(p,z)-H_U(p,z)\) is divisible over \(\mathbb Z[p,z]\) by \(p^4(1-p)^2z(z-1)^3\).
4. Six vertices are the least size admitting such a degree-matched pair with differing fragmentation laws. Up to tree isomorphism, its degree class has precisely two members: the three-armed spiders of arm lengths \((3,1,1)\) and \((2,2,1)\), here denoted \(A\) and \(B\). They satisfy
   \[
   H_A(p,z)-H_B(p,z)=p^4(1-p)^2z(z-1)^3,
   \qquad
   \kappa_3(C_A)-\kappa_3(C_B)=6p^4(1-p)^2>0.
   \]

## Assumptions and scope

The habitat network is a finite connected acyclic undirected graph. Patch survival is independent and homogeneous, with \(p\) the survival probability and \(q=1-p\). The statistic \(C_T\) includes single-patch components and is zero when no patch survives. The first two moments and third cumulant are **unconditional**, not conditioned on survival of at least one patch. Degree matching refers to equality of multisets, not labeled degree sequences. The result concerns every integer \(n\ge2\) and every real \(0<p<1\), without an asymptotic regime.

For a tree with \(m=n-1\) edges, let
\[
W(T)=\sum_{v\in V(T)}\binom{\deg_T(v)}2,
\qquad
S_3(T)=\sum_{v\in V(T)}\binom{\deg_T(v)}3.
\]
These counts depend only on the degree multiset. By contrast, \(L(T)\) generally does not.

## Proof

**1. Components as surviving vertices minus surviving edges.** Write \(X_v\) for the independent Bernoulli survival indicators and \(Y_{uv}=X_uX_v\) for each edge. Every induced subgraph of a tree is a forest, so, identically for every outcome,
\[
C_T=S-E,\qquad S=\sum_v X_v,\qquad E=\sum_{\{u,v\}\in E(T)}Y_{uv}.
\]
Consequently \(\mathbb E C_T=np-mp^2\). The variance expands using \(\operatorname{Var}(S)=npq\), \(\operatorname{Var}(E)=m(p^2-p^4)+2W(T)(p^3-p^4)\), and \(\operatorname{Cov}(S,E)=2mp^2q\). Thus
\[
\operatorname{Var}(C_T)=npq+m(p^2-p^4)+2W(T)(p^3-p^4)-4mp^2q.
\]
The formula uses only \(n\) and the degree multiset. It proves the first assertion and also ensures equality of the first two factorial moments.

**2. Where the third moment first detects arrangement.** Expand \(\mathbb E(S-E)^3\). The terms \(\mathbb E S^3\), \(\mathbb E S^2E\), and \(\mathbb E SE^2\) are determined by \(n,m,W(T)\): any selection of at most two (possibly repeated) edges has only the adjacent and disjoint intersection types, whose numbers are \(W(T)\) and \(\binom m2-W(T)\). Adding one or two independently indexed vertex indicators to those edge products changes their expectations only according to the number of vertices already covered, not their position. Therefore every difference between degree-matched trees in their third raw component moments comes from \(-\mathbb E E^3\).

For three distinct edges the possible induced edge configurations are: a three-star on four vertices, a three-edge path on four vertices, an adjacent two-edge wedge plus a disjoint edge on five vertices, and three mutually disjoint edges on six vertices. The respective counts are
\[
S_3(T),\quad L(T),\quad W(T)(m-2)-3S_3(T)-2L(T),\quad
\binom m3-W(T)(m-2)+2S_3(T)+L(T).
\]
Here the third count follows by extending each two-edge wedge with one of the other \(m-2\) edges and subtracting triples counted three times for a star or twice for a path; the last count is the remainder. The probabilities that all endpoint indicators of such a triple equal one are respectively \(p^4,p^4,p^5,p^6\). Hence, between degree-matched trees, the difference in \(\mathbb E E^3\) is
\[
6\bigl(L(T)-L(U)\bigr)(p^4-2p^5+p^6)
=6\bigl(L(T)-L(U)\bigr)p^4q^2.
\]
The factor \(6\) counts permutations of distinct edges in the cube. Repeated-edge terms involve at most two edges and cancel. The equality of first and second moments means the difference in third raw moments equals the difference in third cumulants, proving assertion 2.

**3. Universal divisibility of the generating-function difference.** For each vertex subset \(A\), let \(c_T(A)\) be its number of induced components. Then
\[
H_T(p,z)=\sum_{A\subseteq V(T)}p^{|A|}q^{n-|A|}z^{c_T(A)}.
\]
The distributions of induced component counts from subsets of at most three vertices depend only on \(n,m,W\). For three retained vertices, the only possibility with two retained edges is a two-edge wedge; these occur \(W\) times. The one-edge and zero-edge cases are then fixed by \(m(n-2)\) total edge-with-third-vertex incidences and \(\binom n3\) total triples. Thus the difference is divisible by \(p^4\).

For zero deleted vertices, each tree contributes the one-component full tree. For exactly one deleted vertex \(v\), a tree splits into \(\deg(v)\) components. Equality of the degree multisets therefore makes the terms with zero or one deleted vertex identical, so the difference is divisible by \(q^2=(1-p)^2\). The coefficient of \(z^0\) is always the probability of the empty retained set, \(q^n\), and so cancels: the difference has factor \(z\). Finally, equality of the normalized total probabilities and the first two factorial moments says that the difference and its first two \(z\)-derivatives vanish at \(z=1\); hence \((z-1)^3\) is a factor. These four factors are pairwise coprime in \(\mathbb Q[p,z]\); by monic polynomial division and primitive-content arithmetic, the product divides the integer-coefficient difference in \(\mathbb Z[p,z]\).

**4. Sharpness and explicit pair.** All trees on at most five vertices are determined by their degree multisets, as seen directly from the possible degree sequences or from the exhaustive generation in the verification program. At six vertices the only degree multiset admitting two nonisomorphic trees is \((1,1,1,2,2,3)\): the two degree-two vertices may extend the same arm or two distinct arms of the unique degree-three vertex. Choose edges
\[
E(A)=\{01,12,23,04,05\},\qquad E(B)=\{01,12,03,34,05\}.
\]
The three-edge-path counts are \(L(A)=3\) and \(L(B)=4\). Enumeration of the \(2^6\) retained vertex subsets gives no difference except in the four-retained-vertex coefficients, where the differences at component counts \(1,2,3,4\) are respectively \(-1,3,-3,1\). Therefore
\[
H_A(p,z)-H_B(p,z)=p^4q^2(-z+3z^2-3z^3+z^4)=p^4q^2z(z-1)^3.
\]
The third-cumulant difference then follows both by differentiation and from assertion 2. This pair establishes the smallest-order threshold.

## Verification

The included reproducible program `verify.py` uses only the Python standard library. It generates labeled trees through Prüfer sequences, groups their canonical isomorphism types for \(2\le n\le6\), compares all degree-matched classes, and enumerates all vertex survival subsets using integers. The class counts are \(1,1,2,3,6\) for sizes \(2\) through \(6\); there is exactly one nonisomorphic degree-matched pair, at size \(6\). The program verifies equality of the first two component factorial-moment polynomials, the predicted third-factorial-moment difference, and every coefficient of the stated six-vertex generating-function difference. The exact program output is in `certificate.json`.

Finite checks are confirmatory. The identities for unbounded tree order and continuous \(p\) follow from the preceding combinatorial proof, not enumeration.

## Relationship to prior work

Urban and Keitt (2001) established the ecological use of graph representations of habitat connectivity. Tittmann, Averbouch, and Makowsky (2008) introduced the general induced-subgraph component polynomial, of which the present probability generating function is a specialization after normalizing vertex-selection weights. Their general polynomial provides a framework and is **not** represented as new here. Liao and Hou (2013) investigated information recovered from that polynomial, including a four-vertex-path count for regular bipartite graphs; their cited result has different graph assumptions and does not establish the present degree-matched tree cumulant law. Allard et al. (2015) treated component-size distributions in percolation on finite graphs, not this exact count-of-components moment comparison. The present claim concerns the all-order third-cumulant difference, universal generating-function divisibility, and the sharp minimal degree-matched ecological-tree example.

## Limitations

The results require independent homogeneous vertex survival on trees and **unconditional** connected-component counts. They do not hold by assertion for graphs with cycles, correlated patch loss, unequal patch probabilities, a statistic conditioned on nonempty survival, or empirical distributions estimated from finite field data. A third moment is generally sensitive to estimation noise. The checked literature may not exhaust all earlier graph-polynomial or ecological-reliability terminology; no independent originality audit has been performed.

## References

- D. Urban and T. Keitt (2001), *Landscape Connectivity: A Graph-Theoretic Perspective*, Ecology 82, 1205–1218. DOI: 10.1890/0012-9658(2001)082[1205:LCAGTP]2.0.CO;2. Public online date: 2001-05-01.
- P. Tittmann, I. Averbouch, and J. A. Makowsky (2008), *The Enumeration of Vertex Induced Subgraphs with Respect to the Number of Components*, arXiv:0812.4147, public preprint 2008-12-22. https://arxiv.org/abs/0812.4147.
- S. Liao and Y. Hou (2013), *Note on the Subgraph Component Polynomial*, arXiv:1311.6856, public preprint 2013-11-27. https://arxiv.org/abs/1311.6856.
- A. Allard et al. (2015), *General and exact approach to percolation on random graphs*, arXiv:1509.01207, public preprint 2015-09-03. https://arxiv.org/abs/1509.01207.
