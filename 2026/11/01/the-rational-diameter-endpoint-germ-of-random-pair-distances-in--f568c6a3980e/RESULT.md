# The rational diameter-endpoint germ of random-pair distances in regular simplices

## Finding
Let \(d\geq4\) be an integer, let \(K\subset\mathbb R^d\) be a regular Euclidean \(d\)-simplex of edge length \(\ell>0\), and let \(X,Y\) be independent volume-uniform points of \(K\). Define the near-diameter probability
\[
F_d(t)=\Pr\{\|X-Y\|_2\geq\ell(1-t)\},\qquad 0<t<1.
\]
Then \(F_d\) has a **convergent, explicitly computable power series at \(t=0\)** whose coefficients are rational. In particular,
\[
\boxed{F_d(t)=\frac{d(d+1)2^{2d-2}(d!)^2}{(2d)!}\,t^{2d}\left[1+\frac{3(d-1)}{2d+1}\,t+O_d(t^2)\right].}
\]
The leading constant is strictly positive, and the displayed first relative correction is exact. In the first dimension not covered by the classical triangle/tetrahedron correlation formulas,
\[
\boxed{F_4(t)=\frac{128}{7}t^8\left(1+t+\frac{34}{15}t^2+O(t^3)\right).}
\]
A constructive description of **all** coefficients follows. Put \(m=2d\), fix distinct indices \(i,j\in\{0,\dots,d\}\), and write \(f_0,\ldots,f_d\) for the standard orthonormal basis of \(\mathbb R^{d+1}\). Form the \(m\) vectors
\[
c_{a,k}=\frac{f_k-f_i}{1+\mathbf1_{\{k=j\}}}\quad(k\ne i),\qquad
c_{b,l}=\frac{f_j-f_l}{1+\mathbf1_{\{l=i\}}}\quad(l\ne j).
\]
Let \(\Theta=(\Theta_1,\ldots,\Theta_m)\) be uniform on the standard \((m-1)\)-simplex (the Dirichlet law with all parameters equal to one), index the displayed vectors by \(c_1,\ldots,c_m\), and set
\[
Q(\Theta)=\frac12\left\|\sum_{r=1}^{m}\Theta_r c_r\right\|_2^2.
\]
There is a \(t_0(d)>0\) such that for every \(0<t<t_0(d)\), with \(s=2t-t^2\), the following series converges absolutely and equals the exact probability:
\[
\boxed{F_d(t)=\frac{d(d+1)(d!)^2}{4(2d)!}
\sum_{k=0}^{\infty}
\frac{m}{m+k}\binom{m+2k-1}{k}
\mathbb E\bigl[Q(\Theta)^k\bigr]s^{m+k}.}
\]
Every moment of \(Q\) is rational and obtainable by finite polynomial expansion and the identity
\[
\mathbb E\left[\prod_{r=1}^{m}\Theta_r^{\alpha_r}\right]
=\frac{(m-1)!\prod_{r=1}^{m}\alpha_r!}{(m-1+\sum_r\alpha_r)!},\qquad\alpha_r\in\mathbb Z_{\geq0}.
\]
Thus the formula provides a positive-coefficient rational series in the squared-distance deficit \(s\), and a rational Taylor series in the distance deficit \(t\). The theorem concerns **two independent points**, not the dependent pairwise distances among a common sample of points.

## Assumptions and scope
The dimension \(d\ge4\) is fixed while \(t\downarrow0\). The distribution is the normalized \(d\)-dimensional Lebesgue measure on the full simplex, not surface measure. The edge length \(\ell\) is arbitrary and cancels from the normalized event. All boundary inequality choices have probability zero. No uniform-in-\(d\) remainder estimate is asserted. The all-order series holds on an unspecified but nonempty dimension-dependent interval only; no global distribution formula is claimed.

## Proof
**1. Barycentric identity and localization.** Label the vertices \(v_0,\ldots,v_d\). If \(x=\sum p_kv_k\) and \(y=\sum q_kv_k\), with nonnegative barycentric coordinates each summing to one, regularity gives
\[
\frac{\|x-y\|_2^2}{\ell^2}=\frac12\sum_{k=0}^{d}(p_k-q_k)^2.
\]
Indeed, the Gram form of the vertex differences on the zero-sum subspace equals half the Euclidean squared norm of their barycentric coefficients. By strict convexity of the Euclidean norm and the fact that every edge has length \(\ell\), equality \(\|x-y\|_2=\ell\) is attained only at the \(d(d+1)\) ordered pairs \((v_i,v_j)\) with \(i\ne j\). Compactness therefore makes the event \(\|X-Y\|_2\ge\ell(1-t)\), for all sufficiently small \(t\), a disjoint union of local events near those pairs.

**2. Exact local quadratic form.** Fix the pair \((v_i,v_j)\). Set \(p_k=a_k\) for \(k\ne i\), \(p_i=1-\sum_{k\ne i}a_k\), and similarly \(q_l=b_l\) for \(l\ne j\), \(q_j=1-\sum_{l\ne j}b_l\). Direct expansion gives
\[
\frac{\|x-y\|_2^2}{\ell^2}=1-S+Q_0,
\]
where
\[
S=2a_j+2b_i+\sum_{k\notin\{i,j\}}(a_k+b_k),
\]
\[
Q_0=\frac12\left\|\sum_{k\ne i}a_k(f_k-f_i)+\sum_{l\ne j}b_l(f_j-f_l)\right\|_2^2.
\]
Introduce \(z_{a,j}=2a_j\), \(z_{b,i}=2b_i\) and leave all other \(2d-2\) nonnegative variables unchanged. Their Jacobian is \(1/4\), \(S=\sum_{r=1}^{m}z_r\), and \(Q_0=\frac12\|\sum_rc_rz_r\|_2^2\). Uniform barycentric coordinates in each simplex have density \(d!\); hence the pair density before the \(z\)-change is \((d!)^2\).

**3. Radial cone integration.** Put \(z=r\theta\), where \(r=\sum_rz_r\) and \(\theta\) belongs to the standard \((m-1)\)-simplex. Then \(Q_0=r^2Q(\theta)\), and the near-endpoint event is exactly
\[
r-r^2Q(\theta)\le s,\qquad s=2t-t^2.
\]
Restrict to a fixed sufficiently small neighborhood of the ordered vertex pair: uniformly over \(\theta\) the left side is increasing in \(r\), and the original barycentric bounds remain inactive for the radial interval under consideration. By compactness and Step 1 this restriction loses no contribution when \(s\) is small. The unique small positive root is
\[
r_*(s,\theta)=\frac{2s}{1+\sqrt{1-4sQ(\theta)}};
\]
this remains valid when \(Q(\theta)=0\) by continuity. The Jacobian of cone coordinates, or the fact that a standard \(m\)-simplex of total coordinate sum at most \(r\) has volume \(r^m/m!\), yields the **exact** local probability
\[
\frac{(d!)^2}{4m!}\,\mathbb E\bigl[r_*(s,\Theta)^m\bigr].
\]
Each of the \(d(d+1)\) ordered pairs contributes equally by symmetry.

**4. Convergent series.** Because \(Q(\theta)\) is uniformly bounded on a compact simplex, \(r_*(s,\theta)\) is jointly analytic in \(s\) on a uniform neighborhood of zero. The relation \(r=s/(1-Q(\theta)r)\), combined with the Lagrange inversion identity, gives for \(k\ge0\)
\[
[s^{m+k}]r_*(s,\theta)^m
=\frac{m}{m+k}\binom{m+2k-1}{k}Q(\theta)^k.
\]
Uniform convergence permits integration term by term. The preceding local-volume identity now gives the stated all-order formula. Each coefficient is rational by expanding the rational quadratic form \(Q^k\) and applying the explicit Dirichlet monomial moment formula. Since \(Q\ge0\), all coefficients in the \(s\)-series are nonnegative.

**5. First two coefficients.** The vectors \(c_r\) satisfy the exact identities
\[
\sum_{r=1}^{m}\|c_r\|_2^2=4d-3,
\qquad\left\|\sum_{r=1}^{m}c_r\right\|_2^2=2d^2.
\]
Dirichlet second moments \(\mathbb E(\Theta_r\Theta_s)=(1+\mathbf1_{\{r=s\}})/(m(m+1))\) therefore imply
\[
\mathbb E Q(\Theta)=\frac{2d^2+4d-3}{4d(2d+1)}.
\]
The first terms of Step 4 are \(s^m(1+m s\mathbb E Q+O_d(s^2))\), and \(s^m=(2t)^m(1-mt/2+O_d(t^2))\). Thus the relative \(t\)-coefficient is
\[
2m\mathbb E Q-\frac m2=\frac{3(d-1)}{2d+1},
\]
with leading coefficient \(d(d+1)2^{m-2}(d!)^2/m!\), as claimed. For \(d=4\), direct rational integration of the fourth-order Dirichlet monomials gives \(\mathbb E Q=5/16\), \(\mathbb E Q^2=533/5280\). Lagrange inversion has \([s^{m+2}]r_*^m=44Q^2\) at \(m=8\). Substituting \(s=2t-t^2\) yields the stated \(34/15\) quadratic relative coefficient.

## Verification
The accompanying standalone Python program `verify.py` checks the rational vector identities for \(2\le d\le16\), derives the leading and first relative coefficients using exact fractions, confirms the first new-dimensional constant \(128/7\), and independently samples the exact cone-root integral to check its small-deficit slope for dimensions \(4,5,7\). Its stochastic quadrature uses a fixed seed and is diagnostic rather than a proof of the infinite expansion. The analytic localization, uniform root expansion, and Lagrange inversion in the preceding proof provide the infinite-dimensional-parameter argument. All coefficients are computed from the formulas included here; no external data files are needed.

## Relationship to prior work
Sinan Wang's *A Brunn–Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies* (arXiv:2610.01916v1, first posted 2026-10-01) introduces the scale-normalized cumulative distance statistic and analyzes its Brunn–Minkowski and Minkowski-problem structure. Its small-distance expansion does not give the far-diameter endpoint of a regular simplex. The present theorem evaluates that complementary endpoint, for \(d\ge4\), through an explicit all-order local cone integral.

The complete distance-related correlation functions for the regular tetrahedron were already obtained by Salvino Ciccariello (arXiv:1407.2788); explicit planar equilateral-triangle formulas also predate this work. Those dimensions are not claimed as new. Aramyan and Yeranyan (2021) prove a general relation between chord and two-point distance distributions, without an explicit regular high-dimensional simplex endpoint coefficient in the accessible description. Lao's 2010 dissertation treats sample diameters of cubes and even-sided polygons; its different sampling statistic and bodies do not give the claimed pairwise simplex germ. A published mathematical finding on the **difference-body gauge** gives a beta bound with simplex equality, but the gauge is not a constant multiple of Euclidean length on the simplex difference body, so it does not determine these coefficients.

## Limitations
This is a local near-diameter result for **regular** simplices in fixed dimension \(d\ge4\). It neither determines the complete distance distribution at all thresholds nor extends to arbitrary nonregular simplices. The value of the convergence radius is not optimized, and the remainder constants may depend strongly on \(d\). The coefficient formulas depend on an explicit rational moment integral; higher coefficients are algorithmic rather than printed in closed form. The claim is internally checked, not independently audited. Historical priority may be affected by older unindexed integral-geometry treatments or by unavailable complete texts; the absence of a database hit is not proof of uniqueness.

## References
1. S. Wang, *A Brunn–Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies*, arXiv:2610.01916v1 (2026-10-01), https://arxiv.org/html/2610.01916v1.
2. S. Ciccariello, *The correlation functions of the regular tetrahedron and octahedron*, arXiv:1407.2788 (2014), https://arxiv.org/abs/1407.2788.
3. R. Aramyan and D. Yeranyan, *Chord length distribution and the distance between two random points in a convex body in Rn*, General Letters in Mathematics 9 (2021), 74–79, https://doi.org/10.31559/glm2020.9.2.3.
4. W. Lao, *Some weak limit laws for the diameter of random point sets in bounded regions*, doctoral dissertation, Karlsruhe Institute of Technology (2010).
5. J. Zhuang and J. Pan, *The distribution of the distance between two random points in an equilateral triangle*, arXiv:1207.1511 (2012), https://arxiv.org/abs/1207.1511.
