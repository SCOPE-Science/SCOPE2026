# Exact finite-sample area and sharp shape order for boundary-random triangles

## Finding
Let \(T\) be a nondegenerate Euclidean triangle of area \(A>0\), side lengths \(a,b,c>0\), and perimeter \(L=a+b+c\). Independently sample \(N\ge3\) points uniformly with respect to Euclidean arclength on \(\partial T\), and let \(H_N\) be their convex hull. Set \(p=a/L\), \(q=b/L\), \(r=c/L\), and \(m=N+2\). Then the **exact finite-sample normalized expected area** is
\[
\frac{\mathbb E[\operatorname{area}(H_N)]}{A}
=1-N\int_{[0,1]^3}(pu+qv+rw)^{N-1}\,du\,dv\,dw
=1-\frac{1-(1-p)^m-(1-q)^m-(1-r)^m+p^m+q^m+r^m}{m(m-1)pqr}.
\]
For every fixed \(N\ge3\), this quantity is strictly Schur-concave in the three normalized side lengths. Therefore, among **all nondegenerate triangles**, it is uniquely maximized by the equilateral triangle, with exact maximum
\[
U_N=1-\frac{3^{N+2}-3\cdot2^{N+2}+3}{(N+1)(N+2)3^{N-1}}.
\]
Its sharp infimum, **not attained by any nondegenerate triangle**, is
\[
L_N=1-\frac{4-2^{2-N}}{N+1},
\]
which is approached exactly in normalized side-length space, up to permutation, by the degenerate limit \((p,q,r)\to(1/2,1/2,0)\). In particular, \(L_3=1/8\) and \(U_3=1/6\).

## Assumptions and scope
Uniform arclength sampling means every point chooses side \(i\) with probability its Euclidean length divided by \(L\), and conditional on that side chooses a uniform position along it. The points are independent and repetitions have probability zero. The hull of one or two points is assigned area zero (the formula also holds for \(N=1,2\), though strict shape ordering is asserted only for \(N\ge3\)). All side lengths obey the strict triangle inequalities, equivalently \(p,q,r>0\), \(p+q+r=1\), and \(\max(p,q,r)<1/2\). Limits toward degenerate triangles refer to ratios of areas **before** taking the geometric degeneration; no normalized area is defined for an actually degenerate triangle.

## Proof
**1. Conditional area from side counts.** Index the three sides cyclically by \(0,1,2\), and write \(K_i\) for the number of sampled points on side \(i\). Then \((K_0,K_1,K_2)\) is multinomial with parameters \(N;(p,q,r)\). Conditional on \(K_i=k_i>0\), the expected fractions of side \(i\) omitted next to either endpoint are each \(1/(k_i+1)\); this is the elementary expectation of the minimum, or of one minus the maximum, among \(k_i\) independent uniform points on \([0,1]\). Positions on different sides are independent conditional on counts.

When all three sides are occupied, the complement \(T\setminus H_N\) comprises exactly three disjoint vertex triangles. The triangle at the common endpoint of sides \(i,j\) has area \(A\) times the product of its two omitted side fractions. Consequently, the conditional normalized mean area is \(1-\sum_{\{i,j\}}[(k_i+1)(k_j+1)]^{-1}\), where the sum covers all three unordered side pairs.

When exactly two sides \(i,j\) are occupied, they meet at one vertex. A direct shoelace calculation for the quadrilateral bounded by their two extreme sample points on each side (with coincident extremes permitted) gives the conditional normalized mean \(1-(k_i+1)^{-1}-(k_j+1)^{-1}\). This remains correct when one side has only one point. If exactly one side is occupied, the hull has zero area. These three cases combine into the **single exact conditional identity**
\[
\mathbb E\!\left[\frac{\operatorname{area}(H_N)}A\,\middle|\,(K_i)=(k_i)\right]
=1-\sum_{\{i,j,k\}=\{0,1,2\}}
\frac{\mathbf1_{\{k_k>0\}}}{(k_i+1)(k_j+1)}.
\]
Each unordered pair \(\{i,j\}\) appears exactly once, and \(k\) denotes the remaining side. In the one-occupied-side case the sole nonzero term equals \(1\), so the formula covers all occupancy patterns.

**2. Multinomial evaluation.** For \(p,q,r>0\) summing to \(1\), use \((k+1)^{-1}=\int_0^1 t^k\,dt\) and the multinomial generating function to obtain
\[
\begin{aligned}
F_N(p,q;r)&:=\mathbb E\frac{\mathbf1_{\{K_r>0\}}}{(K_p+1)(K_q+1)}\\
&=\int_0^1\!\int_0^1[(px+qy+r)^N-(px+qy)^N]dx\,dy\\
&=\frac{B_m(p,q,r)}{m(m-1)pq},
\end{aligned}
\]
where
\[
B_m(p,q,r)=1-(p+q)^m-(q+r)^m-(r+p)^m+p^m+q^m+r^m.
\]
The numerator is invariant under permuting \(p,q,r\). Summing \(F_N\) over the three unordered pairs and using \(1/(pq)+1/(qr)+1/(rp)=(p+q+r)/(pqr)=1/(pqr)\) gives the asserted closed form.

**3. Positive integral representation.** The numerator is a third forward difference of \(t\mapsto t^m\) at zero:
\[
B_m(p,q,r)=\Delta_p\Delta_q\Delta_r(t^m)\big|_{t=0}
=m(m-1)(m-2)pqr\int_{[0,1]^3}(pu+qv+rw)^{m-3}\,du\,dv\,dw.
\]
Repeated application of the fundamental theorem of calculus proves this identity, and substituting \(m=N+2\) yields the first displayed formula. There is no limiting approximation here.

**4. Strict shape order and equalities.** For \(N\ge3\), \(f(t)=t^{N-1}\) is strictly convex on \([0,1]\). Put \(G_N(p,q,r)=\mathbb E[f(pU+qV+rW)]\), where \(U,V,W\) are independent uniforms on \([0,1]\). Interchanging \(p,q\) leaves \(G_N\) unchanged. For \(p\ne q\), conditional on the other variable, the two exchanged linear combinations differ by \((p-q)(U-V)\), which is nonzero with probability one. Strict convexity shows that replacing \((p,q)\) by \(((p+q)/2,(p+q)/2)\) **strictly lowers** \(G_N\). Thus the symmetric function \(G_N\) is strictly Schur-convex under majorization (the standard finite sequence of pairwise averaging transfers is sufficient). The normalized expected area \(1-NG_N\) is strictly Schur-concave.

The equal vector \((1/3,1/3,1/3)\) is majorized by every probability triple, giving the unique maximizing triangle. Conversely, every normalized triangle side vector, in decreasing order, is majorized by \((1/2,1/2,0)\): its largest coordinate is strictly below \(1/2\), and the first two coordinates sum to at most \(1\). Strictness gives a larger expected area than at this boundary vector. The latter is approached by nondegenerate triangles with two sides converging to equal positive lengths and the third tending to zero.

**5. Evaluating the sharp endpoints.** At \(p=q=r=1/3\), three elementary integrations give
\[
\int_{[0,1]^3}(u+v+w)^{N-1}\,du\,dv\,dw
=\frac{3^{N+2}-3\cdot2^{N+2}+3}{N(N+1)(N+2)}.
\]
At the limiting vector \((1/2,1/2,0)\), two integrations give
\[
\int_{[0,1]^2}(u+v)^{N-1}\,du\,dv
=\frac{2^{N+1}-2}{N(N+1)}.
\]
Substitution yields \(U_N\) and \(L_N\). Finally, at fixed \(p,q,r>0\), the closed formula shows that \(B_m(p,q,r)=1+O(\lambda^m)\) for \(\lambda=\max\{p,q,r,1-p,1-q,1-r\}<1\), so the normalized mean missed area is \((1+O(\lambda^{N+2}))/((N+1)(N+2)pqr)\).

## Verification
The standalone `checker.py` independently evaluates the area expectation by three algebraically distinct routes: the complete multinomial sum over side occupancies, the inclusion-exclusion closed form, and the multinomial expansion of the three-uniform integral. Exact rational arithmetic checks their equality for \(75\) parameter-and-sample-size combinations. It also checks the two endpoint formulas for \(22\) sample sizes. Direct geometric sampling of points on a \(3\)-\(4\)-\(5\) triangle (using cyclic shoelace area rather than occupancy formulas) agrees with the exact expectations at sample sizes \(3,5,8,15\) within five empirical standard errors. Run `python checker.py` with Python 3 and NumPy available. The general theorem follows from the analytic proof, not from the finite computations.

## Relationship to prior work
Reitzner, Schütt, and Werner study convex hulls of independent uniform boundary samples on polytopes in arbitrary dimension and derive asymptotic expected volume deficits and face counts; see the complete freely available version of *The convex hull of random points on the boundary of a simple polytope* (arXiv:1911.05917, initially public 2019-11-14). In contrast, the present theorem is **exact for every finite sample size** in the triangular planar family and establishes a strict, sharp ordering over all triangle shapes. Its \(N^{-2}\) deficit is consistent with the boundary-polytope phenomenon.

Maesumi's *Triangle Inscribed-Triangle Picking* (arXiv:1804.11007, initially public 2018-04-30) concerns precisely **one uniform point on each of three distinct triangle sides**; its mean area ratio \(1/4\) is the all-three-sides-occupied case with counts \((1,1,1)\) used in Step 1. It does not treat a variable number of independently perimeter-sampled points or classify triangle shapes. Classical exact formulas for uniform *interior* sampling in a triangle involve a different probability law and do not imply this arclength-weighted result.

## Limitations
This result is for **expected Euclidean area normalized by the triangle's own area**, not for expected unnormalized area at fixed perimeter. It neither gives the full distribution of the random hull area nor extends the sharp Schur ordering to polygons with more than three sides. The infimum is a limit and is never realized by a nondegenerate triangle. Independent mathematical validation has not been performed. Published or unindexed equivalent calculations outside the inspected sources remain a bibliographic risk.

## References
1. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917, initially submitted 2019-11-14, later *Discrete & Computational Geometry* 69 (2023), 453–504. https://arxiv.org/html/1911.05917v3
2. A. Maesumi, *Triangle Inscribed-Triangle Picking*, arXiv:1804.11007, initially submitted 2018-04-30, later *College Mathematics Journal* 50 (2019), 364–371. https://arxiv.org/html/1804.11007v1
3. E. W. Weisstein, *Triangle Point Picking*, Wolfram MathWorld (interior sampling; different model). https://mathworld.wolfram.com/TrianglePointPicking.html
