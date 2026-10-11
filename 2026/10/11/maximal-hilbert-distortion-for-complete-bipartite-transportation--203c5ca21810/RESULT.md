# Maximal Hilbert distortion for complete-bipartite transportation spaces

## Finding

For every pair of integers \(m,n\geq 3\), give the complete bipartite graph \(K_{m,n}\) unit edge lengths and its vertices the shortest-path metric. Its real Lipschitz-free (transportation-cost) Banach space has dimension \(d=m+n-1\) and satisfies the exact formula

\[
 d_{\mathrm{BM}}\bigl(\mathcal F_{\mathbb R}(K_{m,n}),\ell_2^{d}(\mathbb R)\bigr)=\sqrt{m+n-1}=\sqrt d.
\]

Thus this family attains the maximal possible real Euclidean Banach–Mazur distance in every one of its dimensions. The equality already holds in the non-Hanner regime \(m,n\geq3\); no choice of a differently oriented Euclidean ellipsoid improves the displayed constant.

## Assumptions and scope

A Lipschitz potential consists of real numbers \(x_i\), \(1\leq i\leq m\), assigned to the first bipartition class and \(y_j\), \(1\leq j\leq n\), assigned to the second, modulo addition of one common constant. The norm on the Lipschitz dual of \(\mathcal F_{\mathbb R}(K_{m,n})\) is

\[
 L(x,y)=\max_{1\leq i\leq m,\,1\leq j\leq n}|x_i-y_j|.
\]

Indeed every cross-part distance is one, and every same-part distance is two; the cross-edge Lipschitz inequalities imply the remaining inequalities. Write

\[
 \bar x=\frac1m\sum_i x_i,\quad \bar y=\frac1n\sum_j y_j,\quad
 h=\bar x-\bar y,\quad u_i=x_i-\bar x,\quad v_j=y_j-\bar y.
\]

These are independent coordinates on the quotient, subject to \(\sum_i u_i=\sum_j v_j=0\). Consider the Euclidean quadratic form

\[
 Q_0(x,y)=h^2+\frac1m\sum_i u_i^2+\frac1n\sum_j v_j^2.
\]

Banach–Mazur distance is the infimum, over positive-definite real quadratic forms \(Q\) on the quotient, of the square root of

\[
 \frac{\max\{Q(z):L(z)=1\}}{\min\{Q(z):L(z)=1\}}.
\]

Since a finite-dimensional norm and its dual have the same Euclidean Banach–Mazur distance, it suffices to evaluate this expression on the Lipschitz dual.

## Proof

**1. All vertices of the Lipschitz polytope.** Let \(B=\{z:L(z)\leq1\}\), a bounded polytope in the quotient. An edge joining first-class vertex \(i\) to second-class vertex \(j\) is *tight* at \(z\) when \(|x_i-y_j|=1\). The tight-edge subgraph is connected exactly when \(z\) is a vertex of \(B\): if disconnected, distinct tight components can be shifted by sufficiently small independent constants; if connected, a spanning tree of tight-edge equalities determines all potentials modulo a common constant.

Along a tight edge the difference of its endpoint values is \(\pm1\). Connectivity implies that any two values in the same part differ by an even integer. The cross-edge inequalities ensure that the range of values in either part is at most two. If the first part is nonconstant, its values must be two numbers differing by exactly two. Every value in the second part must then equal their midpoint, hence the second part is constant. The symmetric argument applies if the second part is nonconstant. If both parts are constant, their difference must be \(\pm1\) for the tight graph to be connected.

Consequently, after translating potentials, the vertices are exactly the two constant-class choices with difference \(\pm1\), together with potentials having one class identically zero and the other class taking only values \(\pm1\) with both signs present. Conversely each listed potential has every cross edge tight and is a vertex.

**2. A matching Euclidean comparison.** At either constant-class vertex, \(Q_0=1\). At a vertex with \(x_i\in\{-1,1\}\) and all \(y_j=0\), the identity

\[
 \frac1m\sum_i(x_i-\bar x)^2=1-\bar x^2
\]

implies \(Q_0=1\); similarly for the other class. Since \(Q_0\) is convex, its maximum on \(B\) is one. Therefore \(Q_0\leq L^2\) everywhere.

For the linear functional \(\Delta_{ij}(z)=x_i-y_j=h+u_i-v_j\), its squared dual norm relative to \(Q_0\) is

\[
 \|\Delta_{ij}\|_{Q_0,*}^2=1+(m-1)+(n-1)=d.
\]

Here, for example, the functional \(u\mapsto u_i\) has squared dual norm \(m-1\) on the zero-sum left subspace equipped with \(m^{-1}\sum_i u_i^2\). Cauchy–Schwarz consequently gives \(L^2\leq d Q_0\). Both extremes occur: \(Q_0=L^2=1\) at any vertex, whereas choosing \(h=1\),

\[
 (u_1,u_2,\ldots,u_m)=(m-1,-1,\ldots,-1),\qquad
 (v_1,v_2,\ldots,v_n)=(-(n-1),1,\ldots,1)
\]

produces \(Q_0=d\) and \(L=d\), and scaling to \(L=1\) produces \(Q_0=1/d\). Thus the squared distortion of \(Q_0\) is exactly \(d\).

**3. No quadratic form does better.** Let \(Q\) be any positive-definite quadratic form. Scaling it gives \(\max_B Q=1\). If \(aL^2\leq Q\leq L^2\), average \(Q\) under the independent coordinate-permutation group \(S_m\times S_n\). The inequalities persist with the same \(a\), so it suffices to consider invariant forms. Every such form has the shape

\[
 Q=\alpha\sum_i u_i^2+\beta\sum_jv_j^2+\gamma h^2,
 \qquad\alpha,\beta,\gamma>0.
\]

This follows from the absence of invariant linear functionals on either zero-sum coordinate space and the scalar nature of permutation-invariant inner products on them. The constant-class vertices give \(\gamma\leq1\).

Define \(\delta_s=0\) for even integers \(s\) and \(\delta_s=s^{-2}\) for odd integers \(s\). A balanced sign pattern of length \(m\) has mean square \(\delta_m\), so the corresponding vertex gives

\[
 m\alpha(1-\delta_m)+\gamma\delta_m\leq1.
\]

Similarly \(n\beta(1-\delta_n)+\gamma\delta_n\leq1\). Therefore

\[
 \frac{m-1}{m\alpha}\geq
 (m-1)\frac{1-\delta_m}{1-\gamma\delta_m},\qquad
 \frac{n-1}{n\beta}\geq
 (n-1)\frac{1-\delta_n}{1-\gamma\delta_n}.
\]

For \(s\geq3\), put \(c_s=0\) if \(s\) is even and \(c_s=(s+1)^{-1}\) if \(s\) is odd. Since \(0<\gamma\leq1\),

\[
 (s-1)\frac{1-\delta_s}{1-\gamma\delta_s}
 \geq (s-1)-c_s(1-\gamma).
\]

The squared dual norm of a crossing-edge functional under \(Q\) is independent of the chosen edge and equals

\[
 G=\frac1\gamma+\frac{m-1}{m\alpha}+\frac{n-1}{n\beta}.
\]

Using \(\gamma^{-1}-1\geq1-\gamma\) and \(c_m+c_n\leq1/2\) for \(m,n\geq3\), the preceding estimates yield

\[
 G\geq d+(1-\gamma)(1-c_m-c_n)\geq d.
\]

The minimum of \(Q(z)\) subject to the linear constraint \(\Delta_{ij}(z)=1\) equals \(1/G\), by quadratic duality. Since every such \(z\) has \(L(z)\geq1\), dividing a minimizing \(z\) by \(L(z)\) gives \(L=1\) and \(Q\leq1/G\). Hence \(\min_{L=1} Q\leq1/d\), while \(\max_{L=1}Q=1\). Every invariant quadratic form therefore has squared distortion at least \(d\); symmetrization extends this lower bound to every quadratic form.

The explicit \(Q_0\) attains the lower bound, completing the proof for the Lipschitz dual. Finite-dimensional duality gives the asserted distance for the transportation space itself.

## Verification

The standalone standard-library script `verify_complete_bipartite.py` uses exact rational arithmetic. It checks the unit quadratic values at every listed sign-pattern vertex for \(3\leq m,n\leq8\), the explicit lower-ratio witness, and the invariant-form lower certificate at four rational values of \(\gamma\). Running `python verify_complete_bipartite.py` prints `COMPLETE_BIPARTITE_HILBERT_EXACT_OK 6228`. These finite checks are consistency tests; the all-dimensions claim follows from the preceding vertex classification and inequalities, not enumeration.

## Relationship to prior work

Godard's tree-metric work identifies Lipschitz-free spaces for tree geometries, giving the classical cross-polytope benchmark. Dilworth, Kutzarova and Ostrovskii study finite graph transportation spaces and Banach–Mazur comparisons with \(\ell_1\), not the exact Euclidean distance of the present non-tree family. Alexander, Fradelizi, García-Lirola and Zvavitch give the graph-polytope and isometry structure and show that the complete-bipartite *spiderwebs* with a two-vertex part have Hanner free-space balls. Their characterization implies that the connected graphs \(K_{m,n}\) with \(m,n\geq3\) are not of Hanner type, but does not evaluate their distance to a Hilbert space. Exact Hilbert distances previously determined for cycle metrics and equilateral metrics concern different canonical graphs and do not imply this two-parameter family. The graph-wide numerical-index-one property for bipartite metrics is a distinct operator invariant and does not determine Banach–Mazur distance.

## Limitations

This proves an exact real-linear Banach–Mazur distance for unit-edge complete bipartite graphs with both parts at least three vertices. It does not assert the same constant for arbitrary connected bipartite graphs, positive edge weightings, or complex scalar fields, and it does not classify all normed spaces attaining the maximal Hilbert distance. General historical results on maximal-distance polytopes may offer alternative explanations; no independent bibliographic or mathematical audit has been carried out.

## References

1. A. Godard, *Tree metrics and their Lipschitz-free spaces*, arXiv:0904.3178 (first public posting 2009-04-21).
2. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (2018).
3. M. Alexander, M. Fradelizi, L. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first posted 2019; Sections 2, 3 and 5).
4. M. Cúth, M. Doucha and T. Titkos, *Isometries of Lipschitz-free Banach spaces*, J. Lond. Math. Soc. 110 (2024), article e70000, doi:10.1112/jlms.70000 (isometry classification, not a Hilbert-distance result).
