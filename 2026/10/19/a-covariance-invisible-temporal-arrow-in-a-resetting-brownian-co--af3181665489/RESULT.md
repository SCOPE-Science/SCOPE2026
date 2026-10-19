# A covariance-invisible temporal arrow in a resetting Brownian comb

## Finding

Let \((X_t,Y_t)\) be the stationary continuous two-dimensional Brownian comb with independent complete Poisson resetting to the origin at rate \(r>0\), vertical diffusivity \(D_y>0\), and backbone diffusivity coefficient \(D_x>0\), as precisely defined below. At every fixed stationary time, the two coordinates are independent and have double-exponential (Laplace) laws. Moreover, all their stationary two-time *ordinary* covariances are those of two independent Ornstein–Uhlenbeck coordinates with relaxation rate \(r\) and matching variances.

Nevertheless, for every positive lag \(t\), the time-oriented fourth-order statistics satisfy the **strict all-lag asymmetry**
\[
\operatorname{Cov}(X_t^2,Y_0^2)<0,
\qquad
\operatorname{Cov}(Y_t^2,X_0^2)=0.
\]
In fact, putting \(u=rt\) and \(F(u)=e^u\operatorname{erfc}(\sqrt u)\), the negative covariance is exactly
\[
\boxed{
\operatorname{Cov}(X_t^2,Y_0^2)=
\frac{2D_x\sqrt{D_y}}{r^{3/2}}e^{-u}
\left[(2u^2-3u+2)F(u)
+\frac{4\sqrt u-2u^{3/2}}{\sqrt\pi}-2\right].
}
\]
Thus the complete one-time stationary position law and every ordinary second-order time covariance fail to reveal this directed coupling, whereas one mixed fourth-order lag does. The bracket is strictly negative for every \(u>0\), despite being zero at \(u=0\). The short- and long-lag limits are
\[
\operatorname{Cov}(X_t^2,Y_0^2)
=-2D_x\sqrt{D_y/r}\,t+O(t^{3/2})
\quad(t\downarrow0),
\]
\[
\operatorname{Cov}(X_t^2,Y_0^2)
\sim-\frac{4D_x\sqrt{D_y}}{r^{3/2}}e^{-rt}
\quad(t\to\infty).
\]

## Assumptions and scope

The state space is the full plane. Between resets, \(Y\) is an ordinary Brownian diffusion with generator \(D_y\partial_{yy}\), and \(X\) moves only through the local time that \(Y\) spends at the backbone \(y=0\). More precisely, if \(L_t^0(Y)\) is symmetric semimartingale local time normalized by
\[
\int_0^t f(Y_s)\,d\langle Y\rangle_s
=\int_{\mathbb R}f(a)L_t^a(Y)\,da,
\]
then, during every uninterrupted excursion from a starting state, the horizontal displacement has the law of
\[
\sqrt{D_x/D_y}\,B_{L_t^0(Y)},
\]
where \(B\) is a standard Brownian motion independent of \(Y\). Independent rate-\(r\) Poisson alarms reset **both** coordinates to \((0,0)\); subsequently independent Brownian noises start a fresh excursion. The equivalent formal generator is
\[
\mathcal L f=D_y\partial_{yy}f+D_x\delta_0(y)\partial_{xx}f
+r\bigl(f(0,0)-f(x,y)\bigr).
\]
The delta coefficient means the local-time construction just given, not an arbitrary distributional convention. The initial law is the unique regenerative stationary law. All parameters are strictly positive. Only nonnegative lags are needed by stationarity. No claim is made for zero resetting, degenerate diffusivity, resetting to a moving location, or a discrete comb with finite lattice spacing.

## Proof

**Stationary law and its existing spatial factorization.** Regeneration at independent exponential times gives a unique stationary probability measure \(\pi\), obtained by averaging the no-reset law from \((0,0)\) over an independent exponential age. Its partial Fourier transform in the horizontal variable,
\(\widehat\pi(k,y)=\int e^{ikx}\pi(dx,dy)/dy\), solves
\[
D_y\partial_{yy}\widehat\pi-r\widehat\pi
-D_x k^2\delta_0(y)\widehat\pi(k,0)+r\delta_0(y)=0.
\]
The decaying solution and the derivative jump at the backbone give, with \(\alpha=\sqrt{r/D_y}\),
\[
\widehat\pi(k,y)
=\frac{r e^{-\alpha|y|}}{2D_y\alpha+D_xk^2}
=\frac{\alpha e^{-\alpha|y|}}{2}
\frac1{1+b_x^2k^2},
\qquad
b_x^2=\frac{D_x}{2\sqrt{rD_y}}.
\]
Inverting the characteristic function therefore gives the *product* of two Laplace densities,
\[
\pi(dx\,dy)
=\frac{e^{-|x|/b_x}}{2b_x}
\frac{e^{-|y|/b_y}}{2b_y}\,dx\,dy,
\qquad b_y=\sqrt{D_y/r}=\alpha^{-1}.
\]
Hence \(X_0\) and \(Y_0\) are independent, \(\mathbb E[X_0^2]=D_x/\sqrt{rD_y}\), and \(\mathbb E[Y_0^2]=2D_y/r\). The stationary spatial transform is not asserted as a novelty: it is obtainable by specializing existing comblike resetting solutions [1,2]. Its derivation here fixes the normalization needed for the temporal result.

**Every second-order temporal covariance is deceptively simple.** A time interval of length \(t\) contains no alarm with probability \(e^{-rt}\). On that event, each coordinate is a martingale relative to its initial value. On the complementary event, at least one complete reset makes the endpoint independent of the initial state. Consequently, for all \(t\ge0\),
\[
\operatorname{Cov}(X_t,X_0)=\frac{D_x}{\sqrt{rD_y}}e^{-rt},
\qquad
\operatorname{Cov}(Y_t,Y_0)=\frac{2D_y}{r}e^{-rt},
\]
\[
\operatorname{Cov}(X_t,Y_0)=\operatorname{Cov}(Y_t,X_0)=0.
\]
These are precisely the second-order covariances of a pair of independent stationary Gaussian Ornstein–Uhlenbeck processes with matching coordinate variances and relaxation rate; that comparison concerns covariances only, not their one-time distributions.

**Opposite fourth-order time directions.** The vertical motion is autonomous. Without a reset, conditional on \(Y_0\), its second moment at lag \(t\) is \(Y_0^2+2D_yt\), independent of \(X_0\). After any complete reset the endpoint is also independent of \(X_0\). Since \(X_0^2\) and \(Y_0^2\) are initially independent, this proves
\(\operatorname{Cov}(Y_t^2,X_0^2)=0\) exactly.

For the other time direction, condition first on the same no-alarm event and then on the entire vertical path. The horizontal local-time clock has conditional variance
\(2D_x\int_0^t\delta_0(Y_s)\,ds\). Its stochastic horizontal increments have zero conditional mean. Therefore
\[
\operatorname{Cov}(X_t^2,Y_0^2)
=2D_xe^{-rt}\int_0^t
\operatorname{Cov}_{\pi_y}\bigl(Y^2,p_s(0\mid Y)\bigr)\,ds,
\]
where \(\pi_y(dy)=(\alpha/2)e^{-\alpha|y|}dy\), and the free vertical heat kernel is
\[
p_s(0\mid y)=(4\pi D_ys)^{-1/2}
\exp[-y^2/(4D_ys)].
\]
This identity remains valid at stationary initialization because on an interval with no alarm the increments start from the actual state; reset intervals contribute no initial–final covariance.

For each \(s>0\), the function \(\lvert y\rvert\mapsto y^2\) is strictly increasing and \(\lvert y\rvert\mapsto p_s(0\mid y)\) is strictly decreasing. With independent copies \(R,R'\) of the nondegenerate \(\lvert Y\rvert\), the covariance equals half the expectation of
\((R^2-R'^2)(p_s(0\mid R)-p_s(0\mid R'))\), which is strictly negative. This proves the sign for *every* positive lag without relying on numerics.

**Exact evaluation.** Introduce the dimensionless time \(v=rs\), and \(F(v)=e^v\operatorname{erfc}(\sqrt v)\). Elementary Gaussian–exponential integration gives
\[
\operatorname{Cov}_{\pi_y}(Y^2,p_s(0\mid Y))
=\frac1\alpha\left[(2v^2+v-1)F(v)
-\frac{2v^{3/2}}{\sqrt\pi}\right].
\]
The derivative identity \(F'(v)=F(v)-1/\sqrt{\pi v}\) shows directly that
\[
\begin{split}
\int_0^u\left[(2v^2+v-1)F(v)
-\frac{2v^{3/2}}{\sqrt\pi}\right]dv
={}&(2u^2-3u+2)F(u)\\
&+\frac{4\sqrt u-2u^{3/2}}{\sqrt\pi}-2.
\end{split}
\]
The right side vanishes at zero. Substitution into the covariance integral yields the stated formula with prefactor \(2D_x/(r\alpha)\).

For the small-lag asymptotic, the integrand tends to \(-1\) as \(v\downarrow0\); its next term is \(O(\sqrt v)\). For the long-lag limit, one can use the Laplace resolvent of the vertical heat kernel. For \(z>0\), putting \(a=\sqrt{z/D_y}\),
\[
\int_0^\infty e^{-zs}
\operatorname{Cov}_{\pi_y}(Y^2,p_s(0\mid Y))\,ds
=-\frac{2\alpha+a}{\alpha D_y(\alpha+a)^3}.
\]
The integrand is strictly negative, so monotone convergence as \(z\downarrow0\) gives \(-2/(D_y\alpha^3)=-2/(r\alpha)\). Thus the dimensionless integral approaches \(-2\), giving the exact exponential long-lag constant. All moments and exchanged integrals are justified by the explicit exponentially decaying stationary marginals and nonnegative or integrable absolute conditional expressions.

## Verification

The standalone program `verification/check.py` was run successfully with Python 3, `mpmath`, and `scipy`, completing **66 independent numerical and algebraic checks**. It reconstructs the stationary resolvent boundary jump, compares Gaussian heat-kernel quadrature with the independently evaluated complementary-error-function expression, differentiates its antiderivative, checks the Laplace resolvent, and performs direct time-and-space quadrature at multiple positive parameter sets. These finite checks illustrate and help detect normalization errors; the analytic argument above—not numerical sampling—proves every-lag strictness, uniqueness of the stationary law, and asymptotic assertions.

## Relationship to prior work

Domazetoski et al. [1] analyzed resetting on three-dimensional comblike structures, including exact spatial Fourier–Laplace laws, marginal stationary densities, and mean-square displacements; their Section V explicitly specializes results to the two-dimensional comb. The product stationary law used here follows from those spatial calculations and is **not** claimed as new. Masó-Puigdellosas, Sandev, and Méndez [2] analyzed Markovian and heavy-tailed resetting in comb transport, especially one-time mean-square displacements, but did not evaluate the ordered two-time fourth moment in this theorem. Taźbierski, Metzler, and Magdziarz [3] derived general two-time distribution representations for complete and incomplete renewal resetting, with explicit Brownian and scaled-Brownian examples. Their general representations contain the renewal structure underlying one step of this proof; they do not state the present comb-specific all-lag negative-vs-zero comparison, its local-time mechanism, or the displayed closed form. The result specializes and evaluates general renewal machinery, rather than claiming the renewal principle itself.

## Limitations

The stationary factorization and conventional covariance formulas alone are covered or implied by prior spatial/resetting literature. The assessed claim is their conjunction with the fully evaluated *directed fourth-order* temporal inequality and asymptotics. The model uses infinitely long fingers, singular continuous backbone coupling, complete independent Poisson resetting, and exact stationary sampling. The result does not establish analogous inequalities for discrete combs, finite fingers, fractional vertical motion, partial resetting, or joint multi-time distributions beyond the displayed moments. The analytical proof establishes a property of the mathematical model; no experiment or independent priority review has been performed. As with other specializations of general renewal formulas, an unlocated earlier equivalent evaluation remains a literature-priority risk.

## References

[1] V. Domazetoski, A. Masó-Puigdellosas, T. Sandev, V. Méndez, A. Iomin, and L. Kocarev, *Stochastic resetting on comblike structures*, Physical Review Research **2**, 033027 (2020). First preprint May 23, 2020. DOI: 10.1103/PhysRevResearch.2.033027; arXiv:2005.11575. Lawful open full text: https://webs.uab.cat/vmendez/wp-content/uploads/sites/97/2009/05/115.pdf.

[2] A. Masó-Puigdellosas, T. Sandev, and V. Méndez, *Random Walks on Comb-like Structures under Stochastic Resetting*, Entropy **25**, 1529 (2023). DOI: 10.3390/e25111529. Open full text: https://www.mdpi.com/1099-4300/25/11/1529.

[3] K. Taźbierski, R. Metzler, and M. Magdziarz, *Series representation approach to stochastic processes with complete and incomplete renewal resetting*, New Journal of Physics **27**, 074603 (2025). DOI: 10.1088/1367-2630/adee40. Open full text: https://www.researchgate.net/publication/393582214_Series_representation_approach_to_stochastic_processes_with_complete_and_incomplete_renewal_resetting.
