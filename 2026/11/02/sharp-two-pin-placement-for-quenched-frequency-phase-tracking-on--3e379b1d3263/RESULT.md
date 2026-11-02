# Sharp two-pin placement for quenched-frequency phase tracking on a path

## Finding

Fix a path with \(N\ge3\) vertices and two pinned reference-phase vertices \(1\le i<j\le N\). The unpinned vertices obey linear phase tracking with independent, time-independent, mean-zero intrinsic-frequency offsets of common variance \(\sigma^2>0\). The normalized expected squared reference-phase error has the **exact all-size form**

\[
\mathcal E_N(i,j):=\frac{\kappa^2}{\sigma^2}\mathbb E\|\theta^*\|_2^2
=B(i-1)+J(j-i-1)+B(N-j),
\]

where

\[
B(n)=\frac{n(n+1)(n^2+n+1)}6,
\qquad
J(n)=\frac{2(n+1)^4+5(n+1)^2-7}{180}.
\]

Both formulas include \(n=0\). For every fixed middle gap \(m=j-i-1\), all minimizers must balance the two exterior gaps, differing in length by at most one. Consequently, for every integer \(N\ge3\), the complete optimal cost is given by the exact one-dimensional finite minimum

\[
\mathcal E_N^*=
\min_{0\le m\le N-2}
\left\{B\left(\left\lfloor\frac{N-2-m}{2}\right\rfloor\right)
+B\left(\left\lceil\frac{N-2-m}{2}\right\rceil\right)+J(m)\right\}.
\]

Every optimal pair is obtained from a minimizing \(m\) and balanced outer gaps; the two possible placements are reflections. Writing \(q=\sqrt[3]{15}\), **every sequence of optimal pairs** satisfies

\[
\frac{i_N}{N}\longrightarrow\frac1{2+q},\qquad
\frac{j_N}{N}\longrightarrow1-\frac1{2+q},
\qquad
\frac{\mathcal E_N^*}{N^4}\longrightarrow\frac1{6(2+q)^3}.
\]

Thus the optimal interior unpinned gap is asymptotically \(\sqrt[3]{15}\) times either exterior unpinned gap. The result is for *reference-phase tracking of quenched frequency disorder*, not the rotation-invariant Kuramoto order parameter or a white-in-time noise coherence metric.

## Assumptions and scope

Let \(P_N\) be the unit-edge-weight path on \(\{1,\dots,N\}\). Pin precisely two distinct vertices \(i,j\) to phase zero, with all other (free) vertices following

\[
\dot\theta_F(t)=\omega_F-\kappa L_F\theta_F(t),\qquad \kappa>0.
\]

Here \(L_F\) is the **principal grounded Laplacian** of the full path (original full-graph degrees retained), and \(\omega_u\) for free \(u\) are independent, identically distributed, with \(\mathbb E\omega_u=0\), \(\mathbb E\omega_u^2=\sigma^2\in(0,\infty)\). They remain fixed in time; no Gaussian assumption is needed. The pinned phases and their noise are both zero. The equilibrium \(\theta^*=\kappa^{-1}L_F^{-1}\omega_F\) is unique because each free component meets a pinned vertex. Norms sum **absolute squared deviations from the fixed zero reference** over all free vertices, not deviations from the free population's sample mean.

This is an exact theorem about the linear grounded-oscillator system. It describes the leading small-phase dynamics of the infinite-reset-rate limit in subsystem-reset Kuramoto models, but it does **not** assert an exact finite-reset-rate or nonlinear-Kuramoto optimum.

## Proof

**1. Reduction to a squared Green operator.** The matrix \(L_F\) is symmetric positive definite. From \(\mathbb E[\omega_F\omega_F^T]=\sigma^2 I\),

\[
\frac{\kappa^2}{\sigma^2}\mathbb E\|\theta^*\|_2^2
=\operatorname{tr}(L_F^{-1}I L_F^{-1})=\operatorname{tr}(L_F^{-2}).
\]

This is different from \(\operatorname{tr}(L_F^{-1})\), the objective for temporally white forcing, and from \(\operatorname{tr}(L_F^{-1}PL_F^{-1})\) with a centering projector \(P\).

**2. Three independent pinned-path intervals.** Write \(a=i-1\), \(m=j-i-1\), \(b=N-j\). Then \(a,m,b\ge0\) and \(a+m+b=N-2\). Removing the pinned rows and columns divides \(L_F\) into three blocks: a left segment of length \(a\) with one pinned end and one free end; a middle segment of length \(m\) with two pinned ends; and a right segment of length \(b\) with one pinned end and one free end. For a one-pinned-end block of size \(n\), number vertices starting at the pinned end, and its inverse Green kernel is

\[
G^{\rm DN}_{pq}=\min(p,q),\qquad 1\le p,q\le n.
\]

For a two-pinned-end block of length \(n\), its inverse is

\[
G^{\rm DD}_{pq}=\frac{\min(p,q)\left(n+1-\max(p,q)\right)}{n+1}.
\]

Both formulas are checked by multiplication by the relevant tridiagonal Laplacian, including the Neumann/free-end diagonal of one. Taking squared Frobenius norms and using elementary finite power sums yields

\[
\|G^{\rm DN}\|_F^2=\sum_{k=1}^n k^2(2(n-k)+1)=\frac{n(n+1)(n^2+n+1)}6=B(n),
\]

\[
\|G^{\rm DD}\|_F^2=
\frac{1}{(n+1)^2}\sum_{p,q=1}^n\min(p,q)^2(n+1-\max(p,q))^2
=\frac{2(n+1)^4+5(n+1)^2-7}{180}=J(n).
\]

The empty-block value is zero. Blockwise addition gives the announced exact formula.

**3. Finite placement reduction.** Fix \(m\) and let \(a+b=N-2-m\). Since \(B(n)\) has positive increasing forward differences (indeed \(B\) is a quartic polynomial with positive coefficients in nonnegative powers of \(n\)), whenever \(a\ge b+2\), moving one free vertex from the longer outer segment to the shorter strictly decreases \(B(a)+B(b)\). Therefore every optimum balances \(a,b\) to within one, proving the stated one-dimensional optimization formula and its complete set of minimizers. No uniqueness of the optimal integer middle gap is required or asserted.

**4. Sharp macroscopic solution.** Uniformly over all nonnegative triples with \(a+m+b=N-2\), polynomial expansion gives

\[
\frac{B(a)+J(m)+B(b)}{N^4}
=\frac16\left(\frac aN\right)^4
+\frac1{90}\left(\frac mN\right)^4
+\frac16\left(\frac bN\right)^4+O(N^{-1}).
\]

Every subsequential limit of the gap fractions lies in the simplex \(x+y+z=1\). The continuous objective \(F(x,z,y)=x^4/6+z^4/90+y^4/6\) is strictly convex on the nonnegative simplex and its unique minimizer lies in the interior: stationarity and symmetry give \(x=y\) and \(z^3=15x^3\), so

\[
x=y=(2+\sqrt[3]{15})^{-1},\qquad z=\sqrt[3]{15}(2+\sqrt[3]{15})^{-1}.
\]

Substitution gives \(F_{\min}=1/[6(2+\sqrt[3]{15})^3]\). Integer gap triples approximating this point exist for all sufficiently large \(N\), so the optimal discrete value converges to this continuous minimum. Every optimal sequence must converge to its unique continuous minimizer. Finally \(i=a+1\) and \(j=N-b\), proving the two pin-location limits.

**5. Distinct from white-in-time disturbances.** If instead \(d\theta_F=-\kappa L_F\theta_Fdt+\sqrt{2D}\,dW_t\), its stationary variance is \((D/\kappa)\operatorname{tr}(L_F^{-1})\). The analogous block costs scale as \(n^2/2\) (outer) and \(n^2/6\) (middle), so two pins asymptotically occupy positions \(N/5\) and \(4N/5\), unlike the quenched-frequency positions above. This comparison is not asserted to be new; it identifies why two established forcing models require different placement choices.

## Verification

The included standalone Python 3 program `verify.py` has no external dependencies and can be run with `python3 verify.py`. It checks exact Green block inverses for lengths up to 20, directly inverts all grounded path matrices and pin pairs through \(N=12\) using rational arithmetic, tests finite balancing over paths through \(N=500\), and checks convergence numerically at seven larger values through \(N=10000\). Its saved output is `PASS 500343 finite checks; exact block identities, path enumeration, optimal gaps and asymptotic consistency`. These are finite checks, not an exhaustive validation of the all-size result; the proof above supplies the universal steps.

## Relationship to prior work

Paramero-Arias and Riascos (2026), `arXiv:2610.21842`, derive the infinite-rate pinned subsystem limit, grounded-Laplacian phase response, and a *centered* Kuramoto order-parameter quadratic form; these statements are prior work. Their spectral analysis concerns general networks and representative complete/complex random networks. The present result selects the different natural, reference-fixed squared tracking loss for a path and solves its two-location discrete and asymptotic optimization. It must not be mistaken for optimization of their rotation-invariant order parameter.

Patterson, McGlohon, and Dyagilev (2016), `arXiv:1604.07094`, and Patterson, Yi, and Zhang (2017), `arXiv:1708.06873`, study one-dimensional leader selection with **temporally white disturbances**, giving \(\frac12\operatorname{tr}(L_F^{-1})\) (up to physical normalization), algorithms and several explicit special-graph results. Those are neither the same forcing law nor the present squared-inverse trace. The path Green kernels and generalized leader-selection framework are standard, not independently claimed discoveries. Novelty is confined to the fully worked quenched-frequency two-pin risk, exact finite reduction, and limiting \(\sqrt[3]{15}\) gap ratio in this reference-phase objective.

## Limitations

The asymptotic conclusion is mathematical for a linear grounded-path model. At fixed coupling and frequency scale, large-path phase magnitudes need not remain small, so nonlinear Kuramoto behavior cannot be inferred uniformly in \(N\). Nor is any finite-rate resetting optimum, a time-dependent fluctuation limit, a robust result for correlated frequency disorder, or an optimality claim for the centered order parameter established. The spectral formulas are exact without Gaussianity but assume frequency independence and equal variance. Mathematical priority remains subject to broader graph-coherence or quenched-response literature not fully exhausted by available searches.

## References

1. K. Paramero-Arias and A. P. Riascos, *Synchronization induced by stochastic subsystem resetting in complex networks*, arXiv:2610.21842 (first submitted 2026-10-15), https://arxiv.org/abs/2610.21842 .
2. S. Patterson, N. McGlohon, and K. Dyagilev, *Optimal k-Leader Selection for Coherence and Convergence Rate in One-Dimensional Networks*, arXiv:1604.07094 (2016), https://arxiv.org/abs/1604.07094 .
3. S. Patterson, Y. Yi, and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (2017), https://arxiv.org/abs/1708.06873 .
