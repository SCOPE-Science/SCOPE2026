# Exact angular coefficient and exponentially accurate perimeter deficit for boundary-sampled polygons

## Finding
Let \(K\) be a nondegenerate convex Euclidean polygon with \(m\ge3\) genuine vertices, no collinear successive edges, and positive perimeter \(L\). Draw \(N\ge3\) points independently from its boundary using normalized arclength and write \(H_N\) for their convex hull. Define the perimeter of a segment to be twice its Euclidean length (the standard continuous intrinsic-volume convention). Let \(\ell_i\) and \(\beta_i\in(0,\pi)\) denote the successive edge lengths and exterior turning angles.

Set
\[h(\beta)=1-\frac{\cos^2(\beta/2)}{\sin(\beta/2)}\operatorname{artanh}(\sin(\beta/2)),\qquad \rho=1-\frac{\min_i\ell_i}{L}.\]
Then the **complete leading mean-perimeter deficit and an exponential finite-sample error bound** are
\[\boxed{\left|\mathbb E\big[\operatorname{Per}(K)-\operatorname{Per}(H_N)\big]-\frac{L}{N+1}\sum_{i=1}^m h(\beta_i)\right|\le m(m+1)L\rho^N.}\]
In particular, \(\lim_{N\to\infty}(N+1)\mathbb E[\operatorname{Per}(K)-\operatorname{Per}(H_N)]/L=\sum_i h(\beta_i)\). Unlike the area deficit, which has inverse-square decay, the perimeter deficit has inverse-linear decay with a logarithmic angular profile.

## Assumptions and scope
All angles are oriented positive exterior turns of a convex polygon with genuine corners. The boundary measure is ordinary Euclidean arclength, not an interior-area distribution, and samples are independent with replacement. Angles \(\beta_i\) need not be equal. A sample of points all on one edge has one-dimensional convex hull; the twice-segment-length convention gives its continuous planar convex-geometric perimeter. The bound holds for every integer \(N\ge3\); no asymptotic-only assumption is used in the bound. The implied limit is taken with the polygon held fixed. The bound does not assert uniformity over families with edge lengths tending to zero.

## Proof
Parameterize the counterclockwise boundary by arclength on a circle of length \(L\). The successive sample points in cyclic order give the hull's perimeter by summing their connecting chord lengths; collinear intermediate sampled points do not affect this sum. Their boundary arc-length increments add to \(L\). Thus the perimeter deficit is the sum over successive sampled pairs of arc length minus chord length; each summand is nonnegative and the total is at most \(L\).

Fix a vertex with exterior turn \(\beta\). Write \(A\) for the arclength distance backwards to the nearest sampled point, and \(B\) forwards to the nearest sampled point, both measured around the entire boundary. For \(N\ge2\), the pair has density
\[f_{A,B}(a,b)=\frac{N(N-1)}{L^2}\left(1-\frac{a+b}{L}\right)^{N-2},\quad a,b>0,\quad a+b<L.\]
Indeed two specified sample points provide the nearest endpoints with the remaining \(N-2\) samples outside the intervening interval. There are \(N(N-1)\) ordered endpoint choices, and integrating the displayed density gives one. Set \(S=A+B\) and \(T=A/(A+B)\). The Jacobian is \(S\); therefore \(T\) is uniform on \([0,1]\), independent of \(S\), and \(\mathbb E S=2L/(N+1)\).

For any \(a,b\ge0\), define a nonnegative virtual corner loss
\[g_\beta(a,b)=a+b-\sqrt{a^2+b^2+2ab\cos\beta}.\]
It is homogeneous of degree one and satisfies \(0\le g_\beta(a,b)\le a+b\). Its expected value over the nearest-neighbor distances is
\[\mathbb E g_\beta(A,B)=\frac{2L}{N+1}\int_0^1\!\left[1-\sqrt{1-4\sin^2(\beta/2)t(1-t)}\right]dt.\]
Write \(s=\sin(\beta/2)\in(0,1)\) and \(c=\cos(\beta/2)\). Substitution \(u=2t-1\) gives
\[\int_0^1\sqrt{1-4s^2t(1-t)}\,dt=\int_0^1\sqrt{c^2+s^2u^2}\,du=\frac12+\frac{c^2}{2s}\operatorname{artanh}(s).\]
(The identity \(\operatorname{arsinh}(s/c)=\operatorname{artanh}(s)\) uses \(c^2=1-s^2\).) Hence \(\mathbb E g_\beta(A,B)=Lh(\beta)/(N+1)\).

Let \(G\) be the event that every polygon edge contains at least one sampled point. On \(G\), each genuine corner is crossed by exactly one sample gap, whose endpoints lie on its two incident edges. Its arc-minus-chord shortfall equals precisely \(g_{\beta_i}(A_i,B_i)\). Any gap internal to a single edge contributes zero. Consequently the actual perimeter deficit on \(G\) equals \(\sum_i g_{\beta_i}(A_i,B_i)\). On the complement, the actual deficit is bounded by \(L\), and the sum of the \(m\) virtual losses is bounded by \(mL\) because each of the \(m\) nearest-neighbor gap lengths is at most \(L\). By the union bound,
\[\mathbb P(G^c)\le\sum_i\left(1-\frac{\ell_i}{L}\right)^N\le m\rho^N.\]
The triangle inequality therefore bounds the expectation of the difference by \(m(m+1)L\rho^N\). Summing the exact virtual loss expectations finishes the proof. The claimed limit follows since \(N\rho^N\to0\).

## Verification
The self-contained `verify_boundary_perimeter.py` samples cyclically ordered boundary points in four convex polygon examples, computes actual hull-chord perimeters, and compares independent Monte Carlo means with the analytic leading expression at sample sizes \(20,50,100,200\). The code passes these supplementary diagnostics. The proof, including the density normalization, integral identity and explicit error bound, is analytic and is not based on simulation. A careful check of the exceptional event with an empty polygon edge is essential; replacing the exponentially small exception by zero would incorrectly claim an exact all-sample formula.

## Relationship to prior work
Har-Peled (2011, arXiv:1111.5340v1) studies random hull complexity for samples uniform **inside** convex bodies; its PDF Sections 1–2 concern different sampling and do not give the angular perimeter coefficient here. Schneider (1988) investigates almost-sure convergence of area, perimeter and Hausdorff distance when samples lie on the boundary of a **smooth** convex body, unlike a fixed polygon with corners. Reitzner–Schütt–Werner (arXiv:1911.05917v3) studies random hulls from boundary samples of simple polytopes and gives expected-facet asymptotics and volume-deficit results, but its stated theorems do not give the present explicit planar perimeter law. The finite-sample area-loss asymptotic for polygonal boundary samples involves a different functional and an inverse-square law; it neither supplies this logarithmic angular perimeter coefficient nor the stated error bound.

## Limitations
No general distribution or variance for the perimeter deficit is asserted. The formula applies to fixed convex polygons with positive side lengths; it is not uniform for polygons approaching a smooth curve as the side count grows. The probability of an empty edge is retained in the bound rather than omitted. This self-review does not constitute independent verification, and equivalently formulated historical results may remain unindexed.

## References
1. S. Har-Peled, *On the Expected Complexity of Random Convex Hulls*, arXiv:1111.5340v1, public 2011-11-22, https://arxiv.org/abs/1111.5340.
2. R. Schneider, *Random approximation of convex sets*, Journal of Microscopy 151 (1988), 211–227, DOI:10.1111/j.1365-2818.1988.tb04682.x.
3. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917v3 (2022); Discrete & Computational Geometry 69 (2023), 453–504, https://arxiv.org/abs/1911.05917.
