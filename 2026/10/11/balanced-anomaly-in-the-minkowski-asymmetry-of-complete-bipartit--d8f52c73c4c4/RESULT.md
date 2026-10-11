# Balanced anomaly in the Minkowski asymmetry of complete-bipartite spanning-tree polytopes

## Finding
For every pair of integers \(p,q\ge2\), let \(K_{p,q}\) have vertex parts of sizes \(p\) and \(q\), and define the spanning-tree polytope
\[
P_{p,q}=\operatorname{conv}\{\mathbf1_T:T\subseteq E(K_{p,q})\text{ is a spanning tree}\}\subset\mathbb R^{pq}.
\]
Its Minkowski asymmetry is exactly
\[
s(P_{p,q})=\max\left\{p-1,q-1,\frac{(p-1)(q-1)(p+q-1)}{p^2-2p+q^2-2q+1}\right\}.
\]
Equivalently, if \(p\ne q\), then \(s(P_{p,q})=\max\{p,q\}-1\), while for balanced parts \(p=q=r\ge2\),
\[
s(P_{r,r})=\frac{(2r-1)(r-1)^2}{2r^2-4r+1}>r-1.
\]
A minimizing Minkowski center in every case is the uniform edge vector \(c=t\mathbf1_{pq}\), where \(t=(p+q-1)/(pq)\). In the balanced case the exact excess \(s(P_{r,r})-(r-1)=r(r-1)/(2r^2-4r+1)\) tends to \(1/2\). The interior-subgraph constraint ties with the boundary constraint when the part sizes differ by exactly one. No assertion is made about uniqueness or the complete set of minimizing centers.

## Assumptions and scope
The parameters \(p,q\) are integers at least two. All containment statements are taken in the affine hull of \(P_{p,q}\), namely \(x(E)=p+q-1\). For a compact convex set \(P\) of positive affine dimension, define
\[
s(P)=\min\{\lambda\ge1:\exists c\in\operatorname{aff}(P)\text{ with }c-P\subseteq\lambda(P-c)\}.
\]
The graph \(K_{p,q}\) is connected, and its spanning-tree polytope has dimension \(pq-1\). The proof uses the standard nonredundant-or-redundant spanning-tree inequalities, not a classification of facets.

## Proof
**1. Reduction to the uniform center.** For fixed \(\lambda\), the set of \(c\) satisfying \(c-P_{p,q}\subseteq\lambda(P_{p,q}-c)\) is convex: equivalently, for every \(x\in P_{p,q}\), the condition \((1+\lambda)c-x\in\lambda P_{p,q}\) holds; taking a convex combination of feasible centers preserves this condition. The feasible-center set is invariant under the automorphism group \(S_p\times S_q\), which permutes all \(pq\) edges transitively. Averaging any minimizing center over this group therefore gives a minimizing center with all coordinates equal. The affine equation \(c(E)=p+q-1\) forces \(c=t\mathbf1\) with \(t=(p+q-1)/(pq)\). Thus it suffices to calculate the reflection factor at this specific center.

**2. Exact reflection test.** Suppose an inequality \(L(x)\le u\) is valid on \(P_{p,q}\), and put \(\ell=\min_{x\in P_{p,q}}L(x)\). For a center \(c\) with \(L(c)<u\), the reflection containment holds for this inequality if and only if
\[
\lambda\ge\frac{L(c)-\ell}{u-L(c)}.
\]
The standard spanning-tree-polytope description comprises \(x_e\ge0\), the affine equality \(x(E)=p+q-1\), and \(x(E(S))\le |S|-1\) for each proper vertex subset \(S\) of size at least two. Here \(E(S)\) consists of the edges having both ends in \(S\).

For the nonnegativity inequalities, \(\max_T x_e=1\) and \(\min_T x_e=0\), so the required factor is \((1-t)/t=(p-1)(q-1)/(p+q-1)\), no larger than either \(p-1\) or \(q-1\).

For \(S\), write \(a=|S\cap V_p|\) and \(b=|S\cap V_q|\). Subsets with \(ab=0\) give only vacuous inequalities. For \(a,b\ge1\) with \((a,b)\ne(p,q)\), the upper bound is \(u=a+b-1\), and the uniform center has \(L(c)=tab\). The minimum number of internal edges among spanning trees is
\[
\ell(a,b)=\begin{cases}
0,&a<p,\ b<q,\\
b,&a=p,\ b<q,\\
a,&a<p,\ b=q.
\end{cases}
\]
Indeed, after deleting all \(ab\) edges between the chosen vertices, the remaining graph is connected in the first case; in the second it has a connected component and precisely \(b\) isolated right-side vertices; in the third it has one connected component and \(a\) isolated left-side vertices. To form a spanning tree one must and can add exactly the number of edges equal to the number of resulting components minus one. This proves the minima without an optimization assumption.

**3. Three competing bounds.** When \(a=p\) and \(1\le b<q\), the exact ratio simplifies to
\[
\frac{tpb-b}{p+b-1-tpb}=\frac{b}{q-b},
\]
whose maximum is \(q-1\), attained at \(b=q-1\). Similarly, \(b=q\) yields the maximum \(p-1\).

For \(1\le a<p\) and \(1\le b<q\), the ratio is
\[
F(a,b)=\frac{tab}{a+b-1-tab}.
\]
The quantity \(ab/(a+b-1)\) is nondecreasing in each positive-integer argument, and \(F\) is increasing as a function of that quantity (its denominator remains positive). Hence its maximum occurs at \(a=p-1\), \(b=q-1\), where direct simplification gives
\[
F(p-1,q-1)=\frac{(p-1)(q-1)(p+q-1)}{p^2-2p+q^2-2q+1}.
\]
The denominator is positive for \(p,q\ge2\), so taking the maximum of the three classes proves the first formula. All bounds are attained by actual spanning-tree incidence vectors in the corresponding support tests; thus none is merely an upper estimate.

**4. Balanced transition.** Write \(D=p^2-2p+q^2-2q+1\). If \(p\ge q\), subtracting the larger boundary bound from the interior bound gives
\[
F(p-1,q-1)-(p-1)=\frac{p(p-1)(q-p+1)}D.
\]
This is positive exactly when \(p=q\), zero exactly when \(p=q+1\), and negative for \(p\ge q+2\). Swapping the two graph parts covers every remaining case and proves the piecewise classification. Substituting \(p=q=r\) and dividing the resulting excess by \(r^2\) yields the limit \(1/2\).

## Verification
The accompanying standard-library-only script `verify.py` enumerates every spanning tree of eight complete-bipartite graphs with side sizes between two and five, independently computes each proper-subset support minimum and maximum by scanning tree-incidence vectors, and compares the largest exact-rational reflection factor with the theorem. It checks eight profiles, 6,762 spanning trees in total, and 1,412,760 vertex-subset/tree comparisons. Invoke `python verify.py`. This finite experiment is not the proof for all \(p,q\); the analytical reduction above establishes the infinite-family statement.

## Relationship to prior work
Pineda-Villavicencio and Schröter study matroid-base-polytope reconstructibility, facet recovery, and basis-exchange graphs; their theorems do not provide an affine Minkowski-asymmetry invariant for the complete-bipartite graphic matroids. Chaourar studies minimal facet descriptions of spanning-tree polytopes, rather than minimum reflection factors. The classical spanning-tree inequality system is the input here, but its known description does not itself evaluate this optimization. The polytope \(P_{p,q}\) is a face of the spanning-tree polytope of the complete graph on \(p+q\) vertices (fixing all same-part edge coordinates to zero), but the asymmetry of a convex body is not determined by the asymmetry of a containing polytope. Search-based comparisons cannot establish priority or global absence of equivalent results.

## Limitations
This theorem computes the asymmetry and exhibits a minimizing center, but does not classify all minimizing centers. It does not extend to arbitrary bipartite graphs. The formula is proved in the canonical edge-incidence realization; Minkowski asymmetry itself is affine invariant. The novelty comparison is bounded by accessible inspected literature and relevant searches, with possible equivalent formulations in geometric optimization or matroid theory. No independent validation or priority certification has been performed.

## References
1. G. Pineda-Villavicencio and B. Schröter, “Reconstructibility of matroid polytopes,” arXiv:2010.10227 (first public 20 October 2020); *SIAM Journal on Discrete Mathematics* 36 (2022), 490–508. https://arxiv.org/abs/2010.10227
2. B. Chaourar, “The facets of the spanning trees polytope,” arXiv:1903.07292 (first public 2019), especially §§2–3. https://arxiv.org/abs/1903.07292
3. R. Zenklusen, *Combinatorial Optimization* lecture notes (2015), §1.5, Theorem 9 (spanning-tree-polytope inequality description). https://ethz.ch/content/dam/ethz/special-interest/math/operations-research/ifor-dam/documents/lecture4.pdf
