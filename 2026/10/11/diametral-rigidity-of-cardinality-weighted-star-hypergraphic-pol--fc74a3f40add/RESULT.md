# Diametral rigidity of cardinality-weighted star hypergraphic polytopes

## Finding

Let \(r\ge2\) be an integer, \(e_0,e_1,\ldots,e_r\) the standard basis of \(\mathbb R^{r+1}\), and \(\Delta_I=\operatorname{conv}\{e_i:i\in I\}\). For real weights \(w_1>0\) and \(w_h\ge0\) for \(2\le h\le r\), define the cardinality-weighted star hypergraphic polytope
\[
P_r(w)=\sum_{\varnothing\ne S\subseteq[r]}w_{|S|}\Delta_{\{0\}\cup S}.
\]
Put, for \(1\le j\le r\),
\[
a_j=\sum_{h=1}^r w_h\binom{r-j}{h-1},\quad
T=\sum_{h=1}^r\binom rh w_h=\sum_{j=1}^r a_j,
\]
where out-of-range binomial coefficients vanish. Then the exact squared ambient Euclidean diameter is
\[
\boxed{\operatorname{diam}_2(P_r(w))^2=T^2+\sum_{j=1}^r a_j^2.}
\]
Every diametral unordered vertex pair, and no other pair, has the form
\[
\boxed{\left\{T e_0,\;\sum_{j=1}^r a_j e_{\pi(j)}\right\}},\qquad\pi\in\mathfrak S_r.
\]
Thus the number of distinct diameter pairs is the number of distinct permutations of the multiset \(\{a_1,\ldots,a_r\}\). It is exactly \(r!\) whenever \(w_2>0\), and exactly one when \(w_h=0\) for all \(h\ge2\).

For the \(m\)-graph polytope of a star on \(r+1\) vertices, set \(w_h=1\) for \(1\le h\le m\), otherwise zero, with \(1\le m\le r\), ignoring the common singleton translation. Then
\[
\operatorname{diam}_2^2=\left(\sum_{h=1}^m\binom rh\right)^2+\sum_{j=1}^r\left(\sum_{t=0}^{m-1}\binom{r-j}{t}\right)^2.
\]
Its diametral-pair count jumps from one at \(m=1\) to \(r!\) for every \(2\le m\le r\). In particular,
\[
\begin{aligned}
D_{r,1}^2&=r(r+1),\\
D_{r,2}^2&=\left(\frac{r(r+1)}2\right)^2+\frac{r(r+1)(2r+1)}6,\\
D_{r,r}^2&=(2^r-1)^2+\frac{4^r-1}{3}.
\end{aligned}
\]

## Assumptions and scope

Distances are measured in the inherited standard Euclidean metric of \(\mathbb R^{r+1}\), restricted to the affine hyperplane \(\sum_{i=0}^r x_i=T\). A common translation does not affect the result. The theorem assumes cardinality-dependent nonnegative simplex coefficients, with positive edge weight. It does not concern shortest-path distances in the polytope graph or Euclidean distance after deleting the hub coordinate.

## Proof

**Vertex reconstruction.** Maximizing a generic linear functional on the Minkowski sum means selecting its unique maximizer from every positively weighted coordinate simplex. Subtract a constant so the hub coefficient is zero. Suppose precisely \(s\) leaves have positive coefficients; list these leaves in decreasing order \(\pi(1),\ldots,\pi(s)\). All remaining leaf coefficients are negative. A hyperedge consisting of the hub and \(h\) leaves contributes to the first positive leaf it contains, or to the hub if it has no positive leaf. Exactly \(\binom{r-j}{h-1}\) subsets of \(h\) leaves select the positive leaf \(\pi(j)\): they must contain it, avoid the preceding \(j-1\) positive leaves, and choose their other members among the remaining \(r-j\) leaves. Hence every vertex has the form
\[
v_{s,\pi}=\left(T-\sum_{j=1}^s a_j\right)e_0+\sum_{j=1}^s a_j e_{\pi(j)},\qquad0\le s\le r.
\]
Conversely, making the indicated \(s\) leaf coefficients positive and strictly decreasing, and the others negative, exposes the stated vertex. Coincident descriptions are allowed when some weights coincide. By the hockey-stick identity, \(\sum_{j=1}^r\binom{r-j}{h-1}=\binom rh\), yielding \(T=\sum_j a_j\). Since \(w_1>0\), every \(a_j\ge w_1>0\), so \(\sum_{j\le s}a_j=T\) holds precisely when \(s=r\).

**Distance bound.** Take arbitrary vertices \(u=(T-x,U)\), \(v=(T-y,V)\), with leaf vectors \(U,V\in\mathbb R_{\ge0}^r\), \(x=\sum_i U_i\), and \(y=\sum_i V_i\). Interchange endpoints to arrange \(0\le y\le x\le T\), and put \(H=\sum_j a_j^2\). Since each leaf vector is a prefix of the nonnegative weight sequence assigned to distinct coordinates, \(\|U\|_2^2\le H\). Also \(\|V\|_2^2\le y^2\) and \(\langle U,V\rangle\ge0\). Therefore
\[
\begin{aligned}
\|u-v\|_2^2&=(x-y)^2+\|U-V\|_2^2\\
&\le(x-y)^2+H+y^2\\
&\le(T-y)^2+H+y^2\\
&=T^2+H-2y(T-y)\le T^2+H.
\end{aligned}
\]

**Equality and multiplicities.** If \(0<y<T\), the last bound is strict. If \(y=T\), then \(x=T\), and both leaf vectors contain all \(r\ge2\) strictly positive weights, so \(\|V\|_2^2<y^2\); the first bound is strict. Thus equality forces \(y=0\), hence \(v=T e_0\), and then forces \(x=T\), hence \(u=\sum_j a_j e_{\pi(j)}\). Every such pair has squared distance \(T^2+H\), proving the exact value and exhaustive extremizers. Finally Pascal's identity gives
\[
a_j-a_{j+1}=\sum_{h=2}^r w_h\binom{r-j-1}{h-2},\qquad1\le j<r.
\]
This is positive whenever \(w_2>0\), yielding \(r!\) distinct leaf permutations. If only \(w_1\) is positive, all \(a_j=w_1\), yielding one. The binomial sums and three displayed specializations follow by substitution.

## Verification

Run `python3 verify_star_diameter.py` from the directory containing this document. It independently constructs vertices by maximizing each weighted hyperedge, compares the resulting vertex set to the prefix-weight formula, and enumerates all squared distances and equality pairs using exact rational arithmetic for \(r=2,3,4,5\) and 30 weighted cases. It additionally checks 299 instances of the symbolic binomial formulas through \(r=24\). Finite checks are corroboration; the proof above establishes the all-dimensional, all-real-weight claim.

## Relationship to prior work

Pešović and Stojadinović (arXiv:2209.12053v1, Section 2, Definition 2.1) introduced the \(m\)-graph polytopes interpolating from graphical zonotopes to graph associahedra. Their quasisymmetric and face-enumeration results do not evaluate ambient Euclidean diameters or classify all diametral pairs. Their singleton summands translate the displayed star polytope.

Behrend (arXiv:2403.06975v1, Sections 2–3) and Behrend et al. (arXiv:2207.14253v3, Sections 3–4) describe partial permutohedra, related coordinate-simplex sums, face and Ehrhart invariants. Projecting the \(m=2\) star construction to leaf coordinates gives the partial permutohedron with parameters \((r,r)\), but that projection changes distances: the full-coordinate squared distance is the leaf-coordinate squared distance plus \((\sum_i(U_i-V_i))^2\). Hence a known leaf-coordinate Euclidean-diameter formula does not imply the present diameter or its endpoint classification in the natural star embedding. An unidentified broader geometric theorem could still cover this statement.

## Limitations

This theorem does not determine projected Euclidean diameters, arbitrary asymmetric hyperedge coefficients, negative simplex coefficients, intrinsic face metrics, or analogous invariants of general-graph \(m\)-graph polytopes. The literature comparison is not exhaustive, and absence of an equivalent source in searches is not proof of global novelty.

## References

1. M. Pešović and T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053v1 (first public 24 September 2022), https://arxiv.org/html/2209.12053v1.
2. R. E. Behrend, *Ehrhart polynomials of partial permutohedra*, arXiv:2403.06975v1 (2024), https://arxiv.org/html/2403.06975v1.
3. R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris, and E. Insko, *Partial permutohedra*, arXiv:2207.14253v3 (2025 revision of a 2022 preprint), https://arxiv.org/html/2207.14253v3.
