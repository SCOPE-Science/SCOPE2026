# Exact boundary-hull area and sharp shape ordering for arbitrary triangles

## Finding
For every nondegenerate Euclidean triangle \(T\), let \(s_1,s_2,s_3>0\) be its side lengths, \(p_i=s_i/(s_1+s_2+s_3)\), and \(A=\operatorname{area}(T)\). For every integer \(n\ge3\), choose \(n\) independent points uniformly by boundary arclength, let \(H_n\) be their convex hull and write \(Q_n=\mathbb E[\operatorname{area}(H_n)]/A\). Then
\[
Q_n=1-\frac{1-\sum_{i=1}^3(1-p_i)^{n+2}+\sum_{i=1}^3p_i^{n+2}}{(n+1)(n+2)p_1p_2p_3}.
\]
Equivalently, for independent \(U_i\sim\operatorname{Unif}[0,1]\),
\[
1-Q_n=n\,\mathbb E\bigl[(p_1U_1+p_2U_2+p_3U_3)^{n-1}\bigr].
\]
The missing-area fraction is a **strictly Schur-convex** function of \((p_1,p_2,p_3)\). The complete sharp range is
\[
\frac{n-3+2^{2-n}}{n+1}<Q_n\le 1-\frac{27[1-3(2/3)^{n+2}+3(1/3)^{n+2}]}{(n+1)(n+2)}.
\]
The upper equality holds exactly for equilateral triangles. The lower endpoint is unattained and approached when the side proportions tend, in any order, to \((1/2,1/2,0)\). In particular, \(Q_3=\frac14(1-\sum_i p_i^2)\), and \(Q_3=1/6\) for an equilateral triangle.

For fixed \(T\), \(\lim_{n\to\infty}n^2(1-Q_n)=1/(p_1p_2p_3)\). For any sequence of nondegenerate triangles whose smallest side proportion \(q_n\) satisfies \(nq_n\to\tau\in[0,\infty)\),
\[
\lim_{n\to\infty}n(1-Q_n)=4\int_0^1e^{-\tau(1-u)}\,du=
\begin{cases}4(1-e^{-\tau})/\tau,&\tau>0,\\4,&\tau=0.\end{cases}
\]
Thus fixed-shape quadratic decay crosses over to linear decay for thin triangles.

## Assumptions and scope
Uniform means independent sampling from the probability measure \(ds/(s_1+s_2+s_3)\) on the three line segments. A nondegenerate triangle has \(p_i>0\), \(\sum p_i=1\), and every \(p_i<1/2\); conversely these conditions characterize its side-length proportions. Area is ordinary two-dimensional Euclidean area; the finite-sample result holds for every integer \(n\ge3\). The limits concern independent samples at each \(n\), not coupled sample paths.

## Proof
**1. Conditional hull area.** Let \(M_i\) count samples on side \(i\); the count vector is multinomial with parameters \(n\) and \(p\). Conditional on \(M_i=m_i>0\), the mean normalized distance from either endpoint of side \(i\) to the nearest sampled point on that side is \(1/(m_i+1)\), by the minimum order statistic of independent uniform variables. Different sides are conditionally independent. The hull boundary is composed of the extreme sampled positions on occupied sides. Decomposing the uncovered region into the triangles adjoining the three original vertices (or using the corresponding two-side quadrilateral when one side is empty) gives the exact conditional identity
\[
\frac{\mathbb E[\operatorname{area}(H_n)\mid M=m]}{A}=1-\sum_{i:m_i>0}\frac1{(m_j+1)(m_k+1)},
\]
where \(\{i,j,k\}=\{1,2,3\}\). This identity also covers one occupied side, giving zero area, and two occupied sides, giving \((m_jm_k-1)/((m_j+1)(m_k+1))\). For three occupied sides it subtracts the three disjoint corner triangles.

**2. Exact averaging.** For each \(i\), use \(1/(m_j+1)(m_k+1)=\int_0^1\int_0^1x^{m_j}y^{m_k}\,dx\,dy\). The multinomial theorem implies
\[
\mathbb E\frac{\mathbf1_{\{M_i>0\}}}{(M_j+1)(M_k+1)}=\int_0^1\int_0^1[(p_i+p_jx+p_ky)^n-(p_jx+p_ky)^n]\,dx\,dy.
\]
Integrating two powers yields, for \(N=n+2\), the expression
\[
\frac{1-\sum_{r=1}^3(1-p_r)^N+\sum_{r=1}^3p_r^N}{N(N-1)p_jp_k}.
\]
Summing over \(i\), and using \(\sum_i1/(p_jp_k)=1/(p_1p_2p_3)\), proves the displayed exact formula. The numerator is the threefold finite difference \(\Delta_{p_1}\Delta_{p_2}\Delta_{p_3}(z^N)|_{z=0}\), so the fundamental theorem of calculus applied three times yields
\[
\frac{1-\sum(1-p_i)^N+\sum p_i^N}{p_1p_2p_3}
=N(N-1)(N-2)\int_{[0,1]^3}(p\cdot u)^{N-3}\,du,
\]
which proves the cubical-moment formula.

**3. Sharp shape ordering.** Because \(n-1\ge2\), the function \(t\mapsto t^{n-1}\) is strictly convex on \((0,1)\). Therefore \(\Phi_n(p)=\mathbb E(p\cdot U)^{n-1}\) is symmetric and strictly convex under every nontrivial averaging of two unequal coordinates: fix their sum and interchange the two i.i.d. nonconstant uniform variables to obtain strict Jensen inequality. This makes \(\Phi_n\) strictly Schur-convex. Among triangle proportions, \((1/3,1/3,1/3)\) is majorized by every \(p\), while every \(p\) is majorized by \((1/2,1/2,0)\). These vectors give the claimed upper equality and strict lower limit, respectively. Substitution in the exact formula gives the two endpoints.

**4. Two asymptotic regimes.** At fixed positive \(p\), all terms involving \(p_i^{n+2}\) and \((1-p_i)^{n+2}\) tend exponentially to zero, proving the quadratic limit. In the thin regime, relabel so \(p_3=q_n\). Triangle inequalities imply \(p_1,p_2\to1/2\). In the cubical integral use \(U_1=1-s/n\), \(U_2=1-t/n\); then
\[
n(1-Q_n)=\int_0^n\!\int_0^n\!\int_0^1
\left[1-\frac{p_1s+p_2t}{n}-p_3(1-u)\right]^{n-1}\,du\,ds\,dt.
\]
The integrand converges to \(e^{-(s+t)/2-\tau(1-u)}\), and for all sufficiently large \(n\) it is dominated by \(e^{-(s+t)/3}\). Dominated convergence gives \(4\int_0^1e^{-\tau(1-u)}du\), including \(\tau=0\).

## Verification
The standalone checker `checks/triangle_boundary_hull_checker.py` compares exact rational multinomial enumeration with the closed expression for six nondegenerate side-proportion triples, checks sharp endpoints, independently simulates genuine Euclidean boundary-point convex hulls of four triangles, and evaluates the cubical moment by Gauss–Legendre quadrature. Run `python checks/triangle_boundary_hull_checker.py` (Python 3 with NumPy). Every test passed; the analytic arguments, not finite checks, justify the all-\(n\) statements.

## Relationship to prior work
Reitzner, Schütt and Werner study random convex hulls sampled from boundaries of simple polytopes and prove general asymptotic missing-volume results. Their main statements do not supply the finite-\(n\) triangle shape formula, strict Schur-convex ordering, equality cases, or thin-triangle scaling law. Interior-sampled polygon convex-hull results, including Efron's classical framework, concern a different sampling measure. Boundary-hull calculations on parallelograms concern a distinct shape family and do not imply the triangle classification.

## Limitations
Only arclength-uniform independent boundary sampling from a nondegenerate Euclidean triangle is covered; neither interior sampling nor arbitrary polygons are classified by this theorem. The lower sharp bound is an infimum over degenerating triangles. The thin-regime limit assumes the stated scaling of the smallest side proportion. Historical priority remains provisional pending wider literature scrutiny.

## References
1. M. Reitzner, C. Schütt and E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first posted 2019-11-14); Discrete & Computational Geometry 69 (2023), 453–504, doi:10.1007/s00454-022-00460-2.
2. B. Efron, *The convex hull of a random set of points*, Biometrika 52 (1965), 331–343, doi:10.1093/biomet/52.3-4.331 (general random-hull framework, different sampling details).
