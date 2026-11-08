# A largest-part law for Euclidean inballs of complete-multipartite symmetric edge polytopes

## Finding

Let \(k\ge 3\), let \(m_1,\ldots,m_k\) be positive integers, and put \(N=\sum_i m_i\ge3\), \(L=\max_i m_i\), and \(h=|\{i:m_i=L\}|\). Consider the complete multipartite graph \(G=K_{m_1,\ldots,m_k}\) on \([N]\) and its **canonical intrinsic Euclidean symmetric-edge polytope**
\[
P_G=\operatorname{conv}\{\pm(e_u-e_v):uv\in E(G)\}\subset H=\{x\in\mathbb R^N:\sum_i x_i=0\}.
\]
Define the rational quantities
\[
B=\frac{\lfloor N^2/4\rfloor}{N},\qquad T=L-\frac{L\bmod2}{N},\qquad M=\max\{B,T\}.
\]
Then the maximum Euclidean inscribed-ball radius is
\[
\boxed{\rho(P_G)=M^{-1/2}.}
\]
In particular, **the inradius depends only on the total number of vertices and the size of the largest independent part**, and not on the remaining part-size profile.

The origin is an incenter. The affine dimension of the **entire set of centers of radius-\(\rho(P_G)\) balls** is precisely
\[
\boxed{
\dim\mathcal I(P_G)=
\begin{cases}
0,& B\ge T,\\
N-1-h(L-1),& T>B\ \text{and}\ L\ \text{even},\\
\max\{0,N-hL-1\},& T>B\ \text{and}\ L\ \text{odd}.
\end{cases}}
\]
The center set is a bounded convex polytope having the origin in its relative interior.

For completeness, the **exact number of facets tangent to the origin-centered maximal ball** also follows. Define
\[
C_B=\begin{cases}\binom N{N/2},&N\text{ even},\\2\binom N{(N-1)/2},&N\text{ odd},\end{cases}\quad
C_T=\begin{cases}h\binom L{L/2},&L\text{ even},\\2h\binom L{(L-1)/2},&L\text{ odd}.\end{cases}
\]
The number is \(\mathbf1_{B\ge T}C_B+\mathbf1_{L\ge2,\,T\ge B}C_T\). The two contact types are disjoint. A tie gives both types, except when all parts are singletons, in which case only binary contacts exist. For example, \(K_{2,2,2}\) has incenter dimension \(2\); \(K_{2,2,2,2}\) has a unique incenter and exactly \(78\) tangent facets; and \(K_{3,3,3}\) has a unique incenter and \(18\) tangent facets. For \(K_{2a,2a-1,2a-1}\), \(a\ge2\), the optimal-center dimension is \(4a-2\), and is therefore unbounded.

## Assumptions and scope

All edges are unweighted, all parts nonempty, and the ambient inner product is inherited from the ordinary \(\mathbb R^N\) coordinates restricted to \(H\). No coordinate deletion or nonorthogonal lattice projection is used to measure distances. The polar \(Q=P_G^{\circ}\) is formed **inside \(H\)** with respect to this inner product:
\[
Q=\{y\in H:\ |y_u-y_v|\le1\text{ for all }uv\in E(G)\}.
\]
The graph is connected, so \(Q\) is bounded and full-dimensional in \(H\). The incenter locus is \(\mathcal I(P_G)=\{c\in H:B_H(c,\rho(P_G))\subseteq P_G\}\), where \(B_H\) denotes an intrinsic Euclidean ball.

## Proof

**1. Polarity and integral extremes.** Since \(P_G=-P_G\), if a radius-\(r\) ball centered at \(c\) is contained in \(P_G\), so is its image centered at \(-c\); averaging the two balls shows the origin-centered radius-\(r\) ball is also contained. Thus the global inradius equals the origin-centered inradius. By polarity,
\[
\rho(P_G)^{-2}=\max_{y\in Q}\|y\|_2^2.
\]
The strictly convex squared norm has all its maximizers among vertices of \(Q\). Fix a vertex \(y\) and choose one coordinate as an additive gauge value \(0\). The active tight-edge constraints \(y_u-y_v=\pm1\) have rank \(N-1\), because this is a vertex modulo constants. They contain a spanning tree; propagating along that tree shows all coordinate values are integers. The graph diameter is at most two, so after subtracting the minimum, each integer value lies in \(\{0,1,2\}\). If both \(0\) and \(2\) occur, they can occur only within a **single part**: opposite endpoints in different parts would violate an edge inequality. All vertices outside that part then have value \(1\).

**2. Two possible squared-norm shells.** For a binary labeling with \(j\) ones and \(N-j\) zeros, the squared norm after centering is exactly \(j(N-j)/N\le B\). Any balanced binary labeling is feasible, so this bound is attained as a feasible point of \(Q\).

For a three-level labeling, let \(a,b\ge1\) count respectively zeros and twos in its unique exceptional part of size \(m\); all other coordinates are one and at most \(m-a-b\) coordinates of that part remain one. Translation by one and orthogonal centering give
\[
\|y\|_2^2=(a+b)-\frac{(b-a)^2}{N}.
\]
For any fixed \(t=a+b\le m\), this expression is at most \(t-(t\bmod2)/N\), maximized at the most balanced choice of \(a,b\). As a function of integer \(t\ge2\), the latter is strictly increasing for \(N\ge3\). Thus the bound is at most \(m-(m\bmod2)/N\le T\). Conversely, when \(L\ge2\), choose the largest part, label half of its vertices zero and half two as evenly as possible, and label all outside vertices one. This is feasible and attains \(T\). When \(L=1\) there are no three-level labelings, but \(T=1-1/N\le B\). Since the squared norm is convex on the polytope, the maximum is exactly \(M=\max\{B,T\}\). This proves the radius formula.

**3. All farthest polar vertices and tangencies.** Strict convexity implies every point maximizing the squared norm is a vertex of \(Q\). If \(B\ge T\), every balanced binary feasible labeling achieves the maximum and so defines a facet of \(P_G\). If \(T\ge B\) and \(L\ge2\), every three-level maximizer must select one of the \(h\) largest parts and assign all of its entries the extreme values \(0\) and \(2\), in most nearly equal counts; all outside entries equal one. These are distinct facets (potentials are taken modulo constants), and the binary and three-level types are disjoint. Their counts are respectively \(C_B\) and \(C_T\) as displayed. There are no additional farthest vertices by Step 2. A polar vertex \(y\) has support hyperplane \(\langle x,y\rangle=1\) at distance \(1/\|y\|\) from the origin, which proves the tangency count.

**4. The complete center set and its affine dimension.** At radius \(\rho=M^{-1/2}\), a center \(c\in H\) is admissible exactly when
\[
\langle c,y\rangle+\rho\|y\|\le1\qquad\text{for every vertex }y\text{ of }Q.
\]
Let \(F\) be the set of farthest polar vertices. Because \(F=-F\), all constraints for \(F\) reduce to \(\langle c,y\rangle=0\). Every other vertex inequality is *strict at the origin*, so by finiteness a sufficiently small relative neighborhood of the origin inside \(W=H\cap\operatorname{span}(F)^\perp\) remains feasible. Therefore \(\dim\mathcal I(P_G)=N-1-\dim\operatorname{span}(F)\).

When \(B\ge T\), centered indicator vectors of all balanced subsets span \(H\): swapping one selected and one unselected index gives each root \(e_i-e_j\). Hence the center is unique. If \(T>B\), there are no farthest binary vectors. For even \(L\), farthest vectors have zero sum *within* their distinguished part and vanish outside it; balanced signs span the \((L-1)\)-dimensional within-part zero-sum space. The \(h\) maximal parts give an orthogonal direct sum of dimension \(h(L-1)\), giving the even-case formula.

For odd \(L\), varying the nearly balanced signs within a chosen largest part spans its \((L-1)\)-dimensional zero-sum space, while averaging all these signs yields the additional centered indicator of that part. The resulting contribution has dimension \(L\). For \(h\) maximal parts their centered part-indicators are independent if at least one vertex lies outside those parts; if they exhaust \([N]\), there is exactly their one sum-to-zero relation. Thus the span has dimension \(hL\) when \(N>hL\), and \(N-1\) otherwise, proving the odd-case formula. Since the center set is the intersection of finitely many closed halfspaces and lies in the bounded body \(P_G\), it is a bounded convex polytope. The strict nonactive inequalities prove the claimed relative-interior property.

## Verification

The accompanying standard-library `check_multipartite.py` explicitly enumerates all feasible integer polar potentials taking values in \(\{0,1,2\}\), modulo an additive constant. This exhausts all polar vertices (Step 1), but the enumeration is used only for finite sizes. For every complete multipartite size profile of total order \(3\le N\le7\) with at least three nonempty parts, and six larger representative profiles, it checks the exact rational maximum \(N\max\|y\|^2=\max\{\lfloor N^2/4\rfloor,NL-(L\bmod2)\}\) and computes the exact rational rank of all farthest centered normals. It checks both the inradius and the claimed incenter dimension. Run `python3 check_multipartite.py`; success prints `MULTIPARTITE_EXACT_CHECKS_PASSED`. The universal assertion rests on the preceding analytic proof, not on extrapolating these finite tests.

## Relationship to prior work

Higashitani, Jochemko and Michałek (2018), Theorem 3.1 and Proposition 3.5, give the general facet-normal criterion and a binary/three-level combinatorial classification of the facets of complete-multipartite symmetric edge polytopes, together with facet counts. These earlier facts are not claimed as new. The result here maximizes the **intrinsic Euclidean norms** of those normals and determines the sharp competing radius shells, their parity- and multiplicity-sensitive tangency counts, and the **dimension of every optimal-center locus**. Chen, Davis and Korchevskaia (2021) study facet subgraphs in broader graph classes. Kölbl (2024) studies Ehrhart-polynomial roots of the same multipartite family, not Euclidean inspheres. Related geometric studies of particular graphs do not state this multipartite generalization. The mathematical invariant is not determined by Ehrhart or facet counts alone.

## Limitations

The claim is metric-specific: an arbitrary unimodular change of coordinates need not preserve the radius. No extension to weighted edges or arbitrary graphs is asserted. The exact shape, face lattice, and volume of a positive-dimensional incenter polytope are not determined here; its affine dimension and relative-interior point are. Existing facet-normal classifications are powerful enough to make the metric computation accessible, so historical priority of the evaluated radius and center formulas requires independent assessment. No independent mathematical audit is claimed.

## References

1. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (first posted 2018-07-20), Theorem 3.1 and Proposition 3.5, https://arxiv.org/abs/1807.07678 .
2. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315v1 (first posted 2021-07-26), sections 3–4, https://arxiv.org/abs/2107.12315 .
3. M. Kölbl, *On a Conjecture Concerning the Roots of Ehrhart Polynomials of Symmetric Edge Polytopes from Complete Multipartite Graphs*, arXiv:2404.02136v1 (first posted 2024-04-02), https://arxiv.org/abs/2404.02136 .
