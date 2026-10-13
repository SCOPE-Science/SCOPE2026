# Planar coincidence theorem for optimal randomized Kaczmarz sampling

## Finding

For any finite collection of nonzero real row vectors spanning \(\mathbb R^2\), consider the consistent linear system \(Ax=b\) and randomized Kaczmarz iterations whose row indices are sampled independently using any freely chosen probability vector \(p\), including zero sampling probabilities. Normalize the row vectors to unit normals \(u_i=(a_i,b_i)\). Associate the points
\[
 z_i=(a_i^2-b_i^2,2a_i b_i)\in\mathbb R^2,
 \qquad r=\operatorname{dist}\bigl(0,\operatorname{conv}\{z_1,\ldots,z_m\}\bigr).
\]
The frame-spanning assumption gives \(0\le r<1\). Define the worst-initialization annealed mean-square factor
\[
 \Gamma(p)=\lim_{k\to\infty}
 \left(\sup_{\|e_0\|_2=1}\mathbb E_p\|e_k\|_2^2\right)^{1/k},
 \qquad e_k=x_k-x_*.
\]
The limit exists and the exact minimum is
\[
 \boxed{\min_{p_i\ge0,\ \sum_i p_i=1}\Gamma(p)=\frac{1+r^2}{2}.}
\]
Moreover, its complete set of minimizers is precisely the set of minimizers of the previously studied *one-step worst-case* contraction \(\sup_{\|e_0\|=1}\mathbb E_p\|e_1\|_2^2\), whose minimum equals \((1+r)/2\). In particular:

- If \(r=0\), the optimal distributions are **exactly** those with \(\sum_i p_i z_i=0\). For every such distribution, every deterministic initial error, and every integer \(k\ge0\),
  \[
  \mathbb E_p\|e_k\|_2^2=2^{-k}\|e_0\|_2^2.
  \]
  At least one optimal distribution uses at most three row directions.
- If \(0<r<1\), the \(z_i\) lie in a unique shortest circular arc of length less than \(\pi\), bounded by two distinct extreme points \(z_a,z_b\). Every optimal distribution places total probability \(1/2\) on each of those two directions and zero on all other directions; duplicate copies of the same direction may split its assigned mass. Writing \(v_j=(-b_j,a_j)\), \(\gamma=(1+r^2)/2\), then for all deterministic \(e_0\in\mathbb R^2\) and integers \(k\ge1\),
  \[
  \mathbb E_p\|e_k\|_2^2
    =\frac{(v_a^\top e_0)^2+(v_b^\top e_0)^2}{2}\,\gamma^{k-1}.
  \]
  The prefactor is positive whenever \(e_0\ne0\).

Thus no nonlinear semidefinite optimization is required for the optimal **annealed** sampling rule in the real plane. It coincides with the optimizer of the older one-step eigenvalue bound, although the optimal **rates** \((1+r^2)/2\) and \((1+r)/2\) differ strictly when \(0<r<1\).

## Assumptions and scope

Let \(m\ge2\), let each row of \(A\in\mathbb R^{m\times2}\) be nonzero, and assume \(\operatorname{rank}(A)=2\) and \(b=Ax_*\) for some \(x_*\in\mathbb R^2\). Independent row selections \(I_0,I_1,\ldots\) all have the same distribution \(\Pr(I_k=i)=p_i\), with arbitrary \(p_i\ge0\) summing to one. Each step is the standard *unrelaxed* orthogonal projection
\[
 e_{k+1}=P_{I_k}e_k,\quad P_i=I_2-u_i u_i^\top=v_i v_i^\top,
 \quad u_i=\frac{A_{i,:}^\top}{\|A_{i,:}\|_2},\quad v_i=(-u_{i,2},u_{i,1}).
\]
The theorem is about optimizing the expectation of the squared Euclidean error, not almost-sure or typical-trajectory exponents. Opposite unit normals represent the same row direction. Zero probabilities are permitted; the optimal support always still spans the plane. Here \(\operatorname{conv}\) is the ordinary finite convex hull, and \(r\) is Euclidean distance.

## Proof

**1. Exact second-moment operator and its spectrum.** On the real vector space \(\mathrm{Sym}_2\) of symmetric \(2\times2\) matrices use the Frobenius inner product \(\langle C,D\rangle_F=\operatorname{tr}(CD)\). Define the positive, self-adjoint linear operator
\[
 \mathcal T_p(C)=\sum_i p_i P_i C P_i
   =\sum_i p_i\langle P_i,C\rangle_F P_i.
\]
The covariance satisfies \(\mathbb E[e_k e_k^\top]=\mathcal T_p^k(e_0e_0^\top)\). Let \(B:\mathbb R^m\to\mathrm{Sym}_2\) send the \(i\)-th standard basis vector to \(\sqrt{p_i}P_i\). Then \(\mathcal T_p=BB^*\), and its nonzero eigenvalues equal those of \(K_p=B^*B\), with entries
\[
 (K_p)_{ij}=\sqrt{p_ip_j}\langle P_i,P_j\rangle_F
   =\sqrt{p_ip_j}(u_i^\top u_j)^2.
\]
Therefore \(\rho(\mathcal T_p)=\lambda_{\max}(K_p)\ge0\). This also identifies the worst-initialization exponential factor: self-adjointness gives
\[
 \sup_{\|e_0\|_2=1}\mathbb E\|e_k\|_2^2
 =\lambda_{\max}\!\left(\mathcal T_p^k(I_2)\right).
\]
An eigenvector for the largest eigenvalue of the entrywise nonnegative matrix \(K_p\) may be chosen entrywise nonnegative. Its image under \(B\) is a nonzero positive-semidefinite eigenmatrix of \(\mathcal T_p\), with strictly positive trace. Consequently \(I_2\) has a nonzero projection onto the maximal-eigenvalue eigenspace, and the displayed worst-initialization factor has limit \(\rho(\mathcal T_p)\). The conclusion also holds when some probabilities vanish or when the top eigenvalue is multiple. (The spanning assumption ensures the optimal rate is strictly less than one, but is not needed for this spectral reduction.)

**2. A universal lower bound.** The unit vector \(q=(\sqrt{p_1},\ldots,\sqrt{p_m})\) gives the Rayleigh estimate
\[
 \Gamma(p)=\lambda_{\max}(K_p)\ge q^\top K_pq
 =\sum_{i,j}p_ip_j(u_i^\top u_j)^2.
\]
By elementary double-angle algebra, \(2(u_i^\top u_j)^2-1=z_i^\top z_j\). Thus if \(s(p)=\sum_i p_i z_i\),
\[
 \boxed{\Gamma(p)\ge\tfrac12(1+\|s(p)\|_2^2)
                  \ge\tfrac12(1+r^2).}\tag{1}
\]
The exact one-step covariance is \(\sum_i p_iP_i\). Its two eigenvalues are \((1\pm\|s(p)\|_2)/2\), so the optimal one-step upper contraction is \((1+r)/2\), attained exactly when \(s(p)\) is the unique nearest point of the convex hull to the origin.

**3. The zero-distance case.** If \(r=0\), a probability vector with \(s(p)=0\) exists by the definition of convex hull. The doubled-angle identity yields \(\sum_i p_i u_i u_i^\top=I_2/2\), hence \(\sum_i p_i P_i=I_2/2\). Conditional on \(e_k\),
\[
 \mathbb E\big[\|e_{k+1}\|_2^2\mid e_k\big]
 =e_k^\top\left(\sum_i p_iP_i\right)e_k
 =\tfrac12\|e_k\|_2^2.
\]
Iterating proves the claimed exact finite-time identity and \(\Gamma(p)=1/2\). Conversely, equality in the minimum forces \(s(p)=0\) by (1). Planar Carathéodory's theorem guarantees a representing convex combination involving at most three points. This is a statement about directions, so repeated parallel rows may share mass.

**4. Positive-distance geometry.** If \(r>0\), strict separation of \(0\) from the finite convex hull means all the \(z_i\) lie in an open semicircle of the unit circle. After taking their arguments cyclically, exactly one gap between successive distinct points has length \(G>\pi\); the complementary occupied arc has length \(\Delta=2\pi-G<\pi\). Call its endpoints \(z_a,z_b\). Let \(w\) be the unit vector pointing through the midpoint of that short arc. Every sampled point satisfies
\[
 w^\top z_i\ge\cos(\Delta/2)>0,
\]
with equality only at the two extreme doubled-angle directions. Every convex combination therefore has Euclidean norm at least \(\cos(\Delta/2)\). Equality is attained at \((z_a+z_b)/2\), where the transverse components cancel. Thus the unique closest point is \((z_a+z_b)/2\), and
\[
 r=\cos(\Delta/2)=|u_a^\top u_b|.
\]
The representation of this closest point by the available \(z_i\) is uniquely the half-and-half mixture of the endpoints, apart from splitting probability across duplicate directions: the supporting-line equality forbids interior points, and transverse cancellation forces equal endpoint masses.

**5. Sharpness, all-initialization rate and uniqueness.** For this half-and-half selection, the nonzero block of \(K_p\) is
\[
 \tfrac12\begin{pmatrix}1&r^2\\r^2&1\end{pmatrix},
\]
whose maximum eigenvalue is \((1+r^2)/2\). This attains (1). Every alternative minimizer must also attain the distance bound in (1), so Step 4 proves the asserted complete characterization. After its first projection the error is parallel to one of \(v_a,v_b\). Given either direction, the next independently selected projection preserves its squared norm with conditional average factor \(\tfrac12(1+(v_a^\top v_b)^2)=(1+r^2)/2\). The exact expression for \(\mathbb E\|e_k\|_2^2\) follows by induction from the first-step identity. Since \(u_a,u_b\) are not parallel, neither are \(v_a,v_b\); the prefactor is strictly positive for every nonzero \(e_0\). Combining Steps 2–5 proves that the annealed and one-step optimum probability sets coincide in every case.

**6. Finite algorithm.** Compute normalized rows and their doubled-angle points; sort their arguments modulo \(2\pi\). If the maximum cyclic argument gap \(G\) does not exceed \(\pi\), choose any convex representation of the origin (with at most three points). Otherwise choose half the probability mass on each endpoint of the complementary short arc. Then \(r=0\) in the former case and \(r=-\cos(G/2)>0\) in the latter. Sorting takes \(O(m\log m)\) comparisons; a planar convex-hull or small linear-feasibility calculation handles the first case. This procedure does not require solving the general lifted semidefinite program.

## Verification

The standalone finite checker `verify_planar_rk.py` is bundled in the same package. It uses only Python's standard library and produces `VERIFY_OK 789 exact/geometry checks`. It checks \(588\) exact-fraction finite-time identities across \(21\) pairs, four deterministic errors, and seven nonzero horizons; \(36\) exact isotropic-frame identities; \(50\) rational moment identities; \(49\) deterministic arc/segment geometry checks; and \(66\) exact comparisons for the three-row directional example. [Total: \(789\) checks.] The tests do not replace the proof for arbitrary real row angles and arbitrarily long horizons.

In one three-row example, \(u_1=(1,0)\), \(u_2=(3/5,4/5)\), and \(u_3=(4/5,3/5)\). The optimal distribution is \(p=(1/2,1/2,0)\). It has \(r=3/5\), exact annealed factor \(17/25\), and optimal one-step upper factor \(4/5\). The third row lies strictly inside the relevant doubled-angle arc and receives zero mass. In another example \(u_1=(1,0)\), \(u_2=(3/5,4/5)\), \(u_3=(3/5,-4/5)\); \(p=(7/32,25/64,25/64)\) yields \(\sum_i p_i z_i=0\) and exactly \(2^{-k}\) mean-square contraction for all initial vectors and iterations.

## Relationship to prior work

Strohmer and Vershynin (2007 preprint) proved expected exponential convergence of randomized Kaczmarz under row-norm sampling; their general theory does not solve optimized row selection in the real plane. Dai, Soltanalian and Pelckmans (2014 preprint) introduced a convex semidefinite formulation of optimized one-step worst-case Kaczmarz contraction. Their objective is the eigenvalue bound, not the exact annealed exponent. Agaskar, Wang and Lu (2014) derived exact lifted mean-square dynamics and formulated the *general* annealed-exponent sampling problem as a semidefinite program; that formulation and the associated exponent are **prior art**. The current planar result supplies a closed-form optimal value, a complete characterization of all optimal distributions, at-most-three-direction support, and a proof that the exact-rate optimizer coincides with the earlier one-step optimizer specifically in real dimension two. The latter coincidence cannot be assumed from the general convex programs: the two objective functions are distinct. Wang, Agaskar and Lu (2015) studied exact mean-square behavior for inconsistent systems, a different regime.

## Limitations

The conclusion is limited to finite, nonzero row pools spanning the **real** plane, a consistent system, independent identically distributed row choices, the standard orthogonal projection step, and nonnegative probabilities that may be zero. It does not optimize adaptive or without-replacement sampling, relaxed projections, noisy/inconsistent systems, individual trajectories, or the quenched exponent. The support-sparsity guarantee is specific to the two-dimensional geometry, not an assertion for arbitrary dimensions. The formulas for the optimized rate are exact mathematical equalities; finite rational experiments alone would not establish them. The literature comparison does not rule out an undiscovered equivalent closed-form planar statement in specialized optimal-design literature.

## References

1. T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, first arXiv version 2007-02-08, arXiv:math/0702226v1. https://arxiv.org/abs/math/0702226
2. L. Dai, M. Soltanalian and K. Pelckmans, *On the Randomized Kaczmarz Algorithm*, arXiv:1402.2863v1, 2014-02-12. https://arxiv.org/pdf/1402.2863
3. A. Agaskar, C. Wang and Y. M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, GlobalSIP 2014, DOI:10.1109/GlobalSIP.2014.7032145. Author-archived full text: https://dash.harvard.edu/server/api/core/bitstreams/7312037d-8b4a-6bd4-e053-0100007fdf3b/content
4. C. Wang, A. Agaskar and Y. M. Lu, *Randomized Kaczmarz Algorithm for Inconsistent Linear Systems: An Exact MSE Analysis*, arXiv:1502.00190v1, 2015-02-01. https://arxiv.org/pdf/1502.00190
