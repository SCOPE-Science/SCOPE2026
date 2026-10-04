# Dissociation polynomial and all maximal dissociation sets of generalized windmills
## Finding
For integers \(n,m\ge2\), let \(W_{n,m}=K_1\vee nK_m\), with center \(c\) and clique blades \(B_1,\ldots,B_n\). A set \(S\subseteq V(W_{n,m})\) is a dissociation set exactly when either \(c\notin S\) and \(|S\cap B_i|\le2\) for every \(i\), or \(c\in S\) and \(|S\setminus\{c\}|\le1\). Hence its dissociation polynomial is \[D_{W_{n,m}}(z)=\left(1+mz+\binom{m}{2}z^2\right)^n+z+nmz^2.\] Consequently \(|\mathcal D(W_{n,m})|=(1+m+\binom{m}{2})^n+1+nm\) and \(\operatorname{diss}(W_{n,m})=2n\). Moreover, the maximal dissociation sets are exactly the \(nm\) center-plus-one-outer-vertex sets of size \(2\) and the \(\binom{m}{2}^n\) center-free sets choosing exactly two vertices from every blade, of size \(2n\). Thus the lower and upper maximal-dissociation numbers are \(2\) and \(2n\), respectively.

## Assumptions and scope
All graphs are finite, simple, and undirected. For integers \(n,m\ge2\), define the generalized windmill
\[
W_{n,m}=K_1\vee nK_m.
\]
Thus \(W_{n,m}\) has one central vertex \(c\) and \(n\) pairwise disjoint clique blades \(B_1,\ldots,B_n\), each of order \(m\), with \(c\) adjacent to every blade vertex and no edges between distinct blades.

A dissociation set is a vertex set \(S\) for which the induced graph \(W_{n,m}[S]\) has maximum degree at most \(1\). The dissociation polynomial is
\[
D_G(z)=\sum_{S\in\mathcal D(G)} z^{|S|}.
\]
A dissociation set is maximal if it is inclusion-maximal among dissociation sets.

## Proof
Suppose first that \(c\notin S\). Distinct blades are anticomplete to one another, while each blade induces a clique. Therefore the induced degree of every selected vertex in \(B_i\) is \(|S\cap B_i|-1\). Hence \(S\) is a dissociation set exactly when
\[
|S\cap B_i|\le2
\]
for every blade. The contribution of one blade to the generating polynomial is
\[
1+mz+\binom{m}{2}z^2,
\]
and independence of the blade choices gives
\[
\left(1+mz+\binom{m}{2}z^2\right)^n
\]
for all center-free dissociation sets.

Now suppose that \(c\in S\). The center is adjacent to every outer vertex, so its degree in the induced graph is \(|S\setminus\{c\}|\). Thus dissociation requires
\[
|S\setminus\{c\}|\le1.
\]
Conversely, the center alone and the center together with any one outer vertex both induce maximum degree at most one. These cases contribute
\[
z+nmz^2.
\]
Adding the disjoint center-free and center-containing families proves
\[
D_{W_{n,m}}(z)=\left(1+mz+\binom{m}{2}z^2\right)^n+z+nmz^2.
\]

Setting \(z=1\) gives the exact number of dissociation sets. The largest exponent in the first term is \(2n\), realized by choosing two vertices from every blade; center-containing sets have size at most two. Since \(n\ge2\), this proves
\[
\operatorname{diss}(W_{n,m})=2n.
\]

For maximality, a center-containing dissociation set is maximal exactly when it consists of \(c\) and one outer vertex: the center alone can be enlarged once, while any center-plus-one set cannot accept a second outer vertex. There are \(nm\) such sets.

A center-free dissociation set is maximal exactly when every blade contributes exactly two vertices. If some blade contributes fewer than two, another vertex from that blade can be added. If every blade contributes two, no outer vertex can be added, and adding the center would give the center induced degree \(2n>1\). Hence the center-free maximal sets are exactly the \(\binom{m}{2}^n\) choices of two vertices in each blade, all of size \(2n\). Therefore the two possible maximal-set sizes are \(2\) and \(2n\).

## Verification
The included checker constructs the graphs directly from their adjacency lists and independently tests every vertex subset by computing induced degrees. It compares this direct test with the structural classification, accumulates every coefficient of the dissociation polynomial, and separately tests inclusion-maximality by attempting every one-vertex extension.

The exhaustive range contains every parameter pair \(n,m\ge2\) with \(1+nm\le18\) among the tested bounds. All polynomial coefficients, total counts, maximum sizes, maximal-set sizes, and maximal-set multiplicities agree with the theorem.

## Relationship to prior work
The 2023 paper “Counting the number of dissociation sets in cubic graphs” defines the dissociation polynomial and proves an extremal theorem for cubic graphs. Its full text states that the polynomial counts all dissociation sets by cardinality and lists MSC 05A17, 05C31, and 05C69. The paper studies cubic graphs via an occupancy argument; generalized windmills with \(n,m\ge2\) are not cubic because their center has degree \(nm\). Full-text searches of that paper found no occurrence of “windmill” or “friendship.”

Earlier dissociation-set literature studies maximum and minimum maximal dissociation sets and their algorithmic complexity, but the targeted literature searches did not locate a generalized-windmill formula, a friendship-graph dissociation polynomial, or the two-level maximal-set classification above.

A separate recent result gives the general-position polynomial of the same generalized-windmill family. General-position sets obey a geodesic condition rather than the induced-maximum-degree condition defining dissociation sets, so that polynomial does not imply the present one.

## Limitations
The theorem is restricted to the standard generalized windmills \(K_1\vee nK_m\) with \(n,m\ge2\). It does not address generalized windmills with several central vertices or Dutch windmills built from longer cycles. The exhaustive computation is finite corroboration only; the arbitrary-parameter theorem follows from the exact structural proof. Literature search cannot exclude a differently phrased or non-indexed exact formula.

## References
1. J. Tu, J. Xiao, R. Lang, “Counting the number of dissociation sets in cubic graphs,” AIMS Mathematics 8(5) (2023), 10021–10032, DOI 10.3934/math.2023507.
2. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon, F. Werner, “The complexity of dissociation set problems in graphs,” Discrete Applied Mathematics 159(13) (2011), 1352–1366, DOI 10.1016/j.dam.2011.04.023.
3. O. I. Duginov, B. M. Kuskova, D. S. Malyshev, N. A. Shur, “Structural and algorithmic properties of maximal dissociating sets in graphs,” Proceedings of the Steklov Institute of Mathematics / related journal publication (2022), as indexed by the Institute of Mathematics and Mechanics.
