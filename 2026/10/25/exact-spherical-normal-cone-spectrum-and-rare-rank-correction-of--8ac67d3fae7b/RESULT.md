# Exact spherical normal-cone spectrum and rare-rank correction of two-row matching polytopes

## Finding
For every integer \(n\ge2\), let \(P_n\) be the convex hull in \(\mathbb R^{2\times n}\), with its ambient Frobenius Euclidean metric, of all zero-one matrices containing at most one nonzero entry in each row and each column. A uniformly random unit direction exposes exactly one vertex almost surely. Write \(\omega_{n,r}\) for the spherical normal-cone angle of any specified vertex containing exactly \(r\in\{0,1,2\}\) ones. Define \(\varphi(t)=e^{-t^2/2}/\sqrt{2\pi}\), \(\Phi(t)=\int_{-\infty}^t\varphi(s)\,ds\), and
\[
B_n=\int_0^\infty\!\varphi(t)\Phi(t)^{n-1}J(t)\,dt,\qquad J(t)=\frac{e^{t^2/4}\operatorname{erfc}(t/2)}{2\sqrt 2}=\frac1{\sqrt{2\pi}}\int_0^\infty e^{-ty-y^2}\,dy.
\]
Then the **entire vertex-angle spectrum**, including multiplicities, is
\[
\boxed{\omega_{n,0}=2^{-2n}\ (1\ \text{vertex}),\quad
\omega_{n,1}=2^{1-n}\left(\frac{1-2^{-n}}{2n}+B_n\right)\ (2n\ \text{vertices}),\quad
\omega_{n,2}=\frac{1-\omega_{n,0}-2n\omega_{n,1}}{n(n-1)}\ (n(n-1)\ \text{vertices}).}
\]
In particular the total spherical angle of the rank-one layer exhibits the **sharp extreme-value correction**
\[
\boxed{\Pr\{\operatorname{rank}(V_n)=1\}=2^{1-n}\left(1+\frac1{\sqrt{\pi\log n}}+o((\log n)^{-1/2})\right),\quad n\to\infty.}
\]
Here \(V_n\) is the vertex selected by the random direction. The zero vertex has probability \(2^{-2n}\); hence the same displayed correction describes the probability that the exposed matching is not of maximum cardinality.

## Assumptions and scope
The polytope is the standard two-row rectangular partial-permutation (complete bipartite matching, or doubly substochastic) polytope \(\operatorname{PPerm}(2,n)\), not its lower-dimensional partial-permutohedron projection. No affine renormalization or altered inner product is used. All \(2n\) ambient coordinates of the direction are independent standard normals before division by their Euclidean length. Because a linear functional has the same maximizer under positive scalar multiplication, this Gaussian direction agrees with Haar-uniform direction on the unit sphere. We consider \(n\ge2\), and ties have spherical measure zero because different vertices define different linear forms.

## Proof
**1. Vertex types and their symmetries.** Every permitted zero-one partial-permutation matrix is a vertex: the coordinate objective assigning weight \(1\) to its occupied cells and weight \(-2\) to every other cell exposes it uniquely (the all-zero matrix is exposed by an all-negative objective). There are \(1\), \(2n\), and \(n(n-1)\) such matrices of ranks zero, one, and two. Permuting the columns and swapping the rows acts by ambient orthogonal transformations transitively on each rank orbit, so its members have the same angular measure.

**2. The zero vertex.** Let \(G=(G_{ij})\) have independent \(N(0,1)\) entries. The all-zero matrix is uniquely optimal exactly when every coordinate \(G_{ij}<0\). Its probability is \(2^{-2n}\).

**3. Exact rank-one angular measure.** Fix the vertex with its single one at row one, column one. Set \(x=G_{11}\), \(y=G_{21}\), \(X_j=G_{1j}\), \(Y_j=G_{2j}\) for \(2\le j\le n\). Comparing against every feasible singleton and every feasible two-edge matching shows that this fixed vertex is uniquely optimal precisely when
\[
x>0,\qquad y<x,\qquad Y_j<0,\qquad X_j<\min\{x,x-y\}\quad(2\le j\le n).
\]
Necessity follows by comparing respectively with the zero vertex, the opposite-row singleton at column one, the two-edge matching extending the target using column \(j\), and the singleton or two-edge matching using \(X_j\). For sufficiency, these inequalities bound all singletons by \(x\), all pairs using column one by \(x\), and all pairs using neither entry of column one by \(x\) because \(X_i<x\) and \(Y_j<0\). Equality cases have probability zero.

The constraints on the \(Y_j\) contribute \(2^{-(n-1)}\). Integrating \(y\le0\) gives \(\tfrac12\int_0^\infty\varphi(x)\Phi(x)^{n-1}\,dx\), and integrating \(0<y<x\) gives \(\int_{x>y>0}\varphi(x)\varphi(y)\Phi(x-y)^{n-1}\,dx\,dy\). Substitute \(t=x-y\) and use
\[
\varphi(t+y)\varphi(y)=\varphi(t)\,(2\pi)^{-1/2}\exp(-ty-y^2)
\]
to obtain the integral \(B_n\). Because \(\Phi'(x)=\varphi(x)\), the first integral is \((1-2^{-n})/n\). Completing the square in the inner integral yields the stated complementary-error-function expression for \(J\), and hence the exact rank-one angle.

**4. Rank-two angular measure.** Each Gaussian direction has exactly one maximizer among all vertices almost surely. Since the three rank orbits partition the vertex set, their total angular measures sum to one. Solving for the rank-two angle gives the formula without requiring another integration.

**5. Sharp asymptotics.** Let \(M_n=\max\{G_1,\ldots,G_n\}\) for independent standard Gaussians. Its density is \(n\varphi(t)\Phi(t)^{n-1}\); therefore
\[
nB_n=\mathbb E[J(M_n)\mathbf1_{\{M_n>0\}}].
\]
The positive decreasing function \(J\) satisfies \(J(t)\sim1/(\sqrt{2\pi}\,t)\) as \(t\to\infty\), by substituting \(u=ty\) in its defining integral and using dominated convergence. Put \(b_n=\sqrt{2\log n}\). Standard Gaussian tail estimates show that for every fixed \(\varepsilon\in(0,1)\),
\[
\Pr\{M_n<(1-\varepsilon)b_n\}\le\exp\{-c_\varepsilon n^{\,1-(1-\varepsilon)^2}/\sqrt{\log n}\},\qquad
\Pr\{M_n>(1+\varepsilon)b_n\}\to0,
\]
for sufficiently large \(n\), with \(c_\varepsilon>0\). Since \(J(0)<\infty\) and \(J\) is decreasing, sandwiching its expectation on the typical interval between \(J((1+\varepsilon)b_n)\) and \(J((1-\varepsilon)b_n)\), then letting \(\varepsilon\downarrow0\), yields
\[
nB_n\sim\frac1{2\sqrt{\pi\log n}}.
\]
Finally the exact formula gives
\[
2n\omega_{n,1}=2^{1-n}\bigl(1-2^{-n}+2nB_n\bigr)
=2^{1-n}\left(1+\frac{1+o(1)}{\sqrt{\pi\log n}}\right),
\]
which is the claimed asymptotic. Adding \(\omega_{n,0}\) changes it by a relatively exponentially small quantity.

## Verification
The accompanying standalone `check_angles.py` evaluates the exact one-dimensional integral using `scipy.integrate.quad`, checks angular normalization, and independently enumerates all matching vertices to simulate Gaussian optimization for dimensions \(2\le n\le8\). The checker uses 50,000 samples per dimension up to five and 120,000 for dimensions six through eight, asserting simulation discrepancy below a six-standard-error envelope plus numerical tolerance. It also evaluates the normalized asymptotic correction at \(n=10,50,100,1000\). To replay, install Python 3, NumPy and SciPy and execute `python check_angles.py`. The infinite theorem is proved analytically above; numerical experiments are corroboration, not proof.

## Relationship to prior work
Heuer and Striker's *Partial permutation and alternating sign matrix polytopes*, first publicly posted December 17, 2020 (arXiv:2012.09901), §2.1 and §3, records the vertices, facets and rectangular matching-polytope realization; its two-row theorem concerns normalized volume and Ehrhart enumeration rather than Euclidean spherical normal-cone angles. The present result is an exact rank-resolved *ambient* angle spectrum and a sharp high-dimensional rare-rank correction. Independent established generic Gaussian-order-statistic estimates underlie the asymptotic calculation; the novelty claim concerns their geometric synthesis for this object, not these elementary probabilistic tools. Related work on the Löwner/John ellipsoids, graph matching adjacency, and partial permutohedra addresses different invariants or a distinct projection and does not supply the displayed angles from its stated conclusions.

## Limitations
These angles depend on the ambient Frobenius Euclidean structure and do not transfer unchanged to projected partial permutohedra, fixed-cardinality matching faces, or non-isotropic directions. The asymptotic fixes the number of rows at two and lets only the number of columns diverge; no rate is claimed beyond the displayed little-o error. Gaussian simulation is finite and cannot establish priority or correctness of the infinite limit. Independent mathematical review has not been performed. Equivalences buried in less-indexed probability literature remain a residual originality risk.

## References
1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, version 1 dated 2020-12-17; accessible full text version 3 (2022-03-08), https://arxiv.org/html/2012.09901v3 ; *SIAM Journal on Discrete Mathematics* 36(4) (2022), 2863–2888, DOI 10.1137/21M1417958.
2. Standard Gaussian maximum-order-statistic identity: \(\Pr\{M_n\le t\}=\Phi(t)^n\). Its necessary consequences are derived in the proof above, without relying on an additional specialized theorem.
