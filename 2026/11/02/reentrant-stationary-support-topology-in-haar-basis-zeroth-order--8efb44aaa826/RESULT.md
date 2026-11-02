# Reentrant stationary-support topology in Haar-basis zeroth-order descent

## Finding

Consider the full-basis, forward finite-difference descent method specified below on an isotropic quadratic. Its unique stationary distribution has **exactly one of three support geometries**—a closed ball, a closed annulus with a genuine central hole, or a sphere—depending sharply on the normalized constant learning rate. In every dimension at least two, the support sequence as the rate increases is

\[
\text{ball}\ \longrightarrow\ \text{annulus}\ \longrightarrow\ \text{sphere}\ \longrightarrow\ \text{annulus}\ \longrightarrow\ \text{ball},
\]

with transitions at \(\gamma=1/2,1,3/2\). Its stationary mean-square error is smooth across all three thresholds, and the outer support radius does not shrink as the learning rate decreases to zero.

**Theorem.** Let \(d\ge2\), \(\lambda,\delta>0\), and \(0<\gamma:=\alpha\lambda<2\). For independent Haar orthogonal matrices \(U_n\), let their columns be \(u_{n,1},\dots,u_{n,d}\). Apply

\[
X_{n+1}=X_n-\alpha\sum_{i=1}^{d}
\frac{f(X_n+\delta u_{n,i})-f(X_n)}{\delta}\,u_{n,i},
\qquad f(x)=\frac\lambda2\|x\|_2^2.
\]

The transition kernel has a unique invariant probability \(\mu_\gamma\), and from any initial distribution with finite second moment the iterates converge in quadratic Wasserstein distance at factor at most \(|1-\gamma|\) per update. Put

\[
q=|1-\gamma|,\qquad a=\frac{\gamma\delta\sqrt d}{2},\qquad
R=\frac a{1-q},\qquad r=\frac a{1-q}\max\{0,1-2q\}.
\]

Its **full topological support** is precisely

\[
\operatorname{supp}(\mu_\gamma)=
\{x\in\mathbb R^d:r\le\|x\|_2\le R\}.
\]

Thus the support is a ball for \(0<\gamma\le1/2\) and \(3/2\le\gamma<2\), an annulus with positive inner radius for \(1/2<\gamma<1\) and \(1<\gamma<3/2\), and the sphere of radius \(\delta\sqrt d/2\) at \(\gamma=1\). For \(\gamma\ne1\), the stationary measure is absolutely continuous with respect to Lebesgue measure; at \(\gamma=1\), it is the uniform measure on that sphere. In every case,

\[
\mathbb E_{\mu_\gamma}X=0,\qquad
\mathbb E_{\mu_\gamma}\|X\|_2^2
=\frac{d\gamma\delta^2}{4(2-\gamma)}.
\]

In particular, for every \(0<\gamma\le1\), \(R=\delta\sqrt d/2\), even though \(\mathbb E\|X\|_2^2\to0\) as \(\gamma\downarrow0\). For \(1/2<\gamma<1\), the exact excluded radius is \(r=\delta\sqrt d(2\gamma-1)/2\). No statement about dimension one is intended.

## Assumptions and scope

All arithmetic is exact. The objective is the centered isotropic quadratic on \(\mathbb R^d\) for arbitrary integer \(d\ge2\). Function values are noiseless. At each iteration, the same positive forward-difference distance \(\delta\) is used along all \(d\) orthonormal columns of a **fresh independent Haar matrix**; the entire batch is used once. The step \(\alpha\) and \(\delta\) do not decay. The initial condition is arbitrary and independent of the future basis draws, with finite second moment for the stated Wasserstein bound. The contraction range is strictly \(0<\alpha\lambda<2\).

This is a specific specialization of structured zeroth-order gradient descent; it is not a theorem for arbitrary anisotropic quadratics, partial bases, discrete sign-only bases, noisy function evaluations, or one-dimensional direction sets.

## Proof

**1. Exact reduction.** Expand a directional difference of the quadratic:

\[
\frac{f(x+\delta u)-f(x)}\delta
=\lambda\langle x,u\rangle+\frac{\lambda\delta}{2}
\quad(\|u\|_2=1).
\]

Since \(\sum_i u_{n,i}u_{n,i}^{\mathsf T}=I\), the estimated gradient is exactly

\[
\lambda X_n+\frac{\lambda\delta}{2}
\sum_{i=1}^d u_{n,i}.
\]

The vector \(\sum_i u_{n,i}=U_n(1,\dots,1)^{\mathsf T}\) has norm \(\sqrt d\) and uniform direction on the unit sphere. Therefore the recursion has exactly the same transition law as

\[
X_{n+1}=(1-\gamma)X_n-aV_n,
\]

where \(V_n\) are independent, uniform on \(S^{d-1}\), and \(a=\gamma\delta\sqrt d/2\). The minus sign and, for negative \(1-\gamma\), any alternating signs may be absorbed into independent rotationally uniform \(V_n\).

**2. Existence, uniqueness, and moments.** Write \(b=1-\gamma\), so \(|b|=q<1\). The series

\[
Y=-a\sum_{j=0}^{\infty}b^jV_j
\]

converges absolutely almost surely. Its law is invariant by peeling off the first summand. Synchronous coupling of two trajectories using the same fresh \(V_n\) gives distance \(q^n\) times the initial distance; consequently

\[
W_2(\nu P^n,\mu_\gamma)
\le q^n W_2(\nu,\mu_\gamma).
\]

Uniqueness among all invariant probability measures also follows without moment assumptions: the transition of any starting point converges weakly to the same series law, and applying invariance to bounded continuous test functions gives equality. Independence and zero means of the sphere increments yield

\[
\mathbb E\|Y\|_2^2
=a^2\sum_{j\ge0}q^{2j}
=\frac{a^2}{1-q^2}
=\frac{d\gamma\delta^2}{4(2-\gamma)}.
\]

**3. The exact support.** For \(q\ge0\), multiplying a uniform sphere vector by a sign does not change its full support. The support is therefore the set of all convergent vector sums with freely selectable directions and lengths \(a,aq,aq^2,\ldots\). It is compact and rotationally invariant. Because \(d\ge2\), the product of direction spheres is connected; its continuous image under the uniformly convergent series is connected. The attainable radii hence form a closed interval.

The largest radius is achieved by aligning all vectors, giving \(R=a/(1-q)\). The polygon inequality in a plane states that vectors of prescribed lengths have minimal possible resultant norm equal to the positive part of the largest length minus the sum of the others. For the first \(N\) lengths, the minimal radius is

\[
m_N=a\max\left\{0,1-\sum_{j=1}^{N-1}q^j\right\}.
\]

This formula is also valid for \(N=1\). The series tail has maximum norm \(aq^N/(1-q)\), so the finite attainable sets converge in Hausdorff distance to the full support. Letting \(N\to\infty\), the minimum radius is

\[
r=a\max\left\{0,1-\frac q{1-q}\right\}
=\frac a{1-q}\max\{0,1-2q\}.
\]

Rotational invariance and connectedness fill every radius between \(r\) and \(R\), establishing the claimed exact ball, annulus, or sphere. Substituting \(q=|1-\gamma|\) gives the two sharp disk thresholds \(\gamma=1/2,3/2\) and the single-sphere case \(\gamma=1\). The outer radius for \(0<\gamma\le1\) simplifies to \(\delta\sqrt d/2\).

**4. Lebesgue regularity.** If \(q>0\), the first two independent sphere increments \(V_0+qV_1\) have an absolutely continuous distribution in \(\mathbb R^d\): the smooth addition map on the product of the two spheres is a submersion whenever the two directions are not parallel, an event of full product surface measure for \(d\ge2\). The area/coarea theorem implies absolute continuity; convolving with the independent remaining series preserves it. If \(q=0\), the invariant law is exactly one Haar-uniform sphere increment. This proves the regularity assertions.

## Verification

Run `python3 verify.py` with a standard-library-only Python 3 environment. The checker performs exact rational identities for the support endpoints, finite-sum polygon radii, truncation errors and stationary second moments; independently evaluates the actual finite-difference formula on random orthonormal bases; and runs illustrative stationary Monte Carlo checks. The infinite-set and distribution statements rely on the proof above, **not** the finite tests. The checker completed 780 exact-rational checks, 750 direct finite-difference checks and five stationary simulation regimes successfully.

## Relationship to prior work

Kozak, Molinari, Rosasco, Tenorio and Villa introduced and analyzed zeroth-order optimization with random orthogonal directions, including full Haar bases and nonvanishing discretization. Their central statements concern convergence, last/best-iterate errors and admissible parameter choices; the inspected full text does not supply an invariant-support classification. Rando, Molinari, Villa and Rosasco analyze the same structured forward-difference estimator under more general stochastic objective assumptions; their principal convergence results use decaying steps or smoothing and do not identify this constant-step geometric stationary phase diagram.

The reduction to a contracting affine random recursion and the polygon inequality are classical mathematical ideas. This finding does **not** claim those general facts are new: the specific all-dimensional translation to the finite-difference algorithm, its three sharp algorithmic transition parameters, exact excluded radii, absolute continuity distinction and nonshrinking-support/vanishing-mean-square separation are the asserted contribution. General iterated-function-system and random-series literature may contain equivalent geometric support statements; that limits priority claims for the geometric step itself.

## Limitations

The statement is exact only for isotropic quadratics, full independent Haar bases, fixed forward differences and the stated stable constant-step range. No high-dimensional practical optimization guarantee, finite-time confidence bound, independent external validation, or claim of novelty for general random-circle/sphere series is made. In dimension one the sphere is disconnected and an analogous full-interval support formula can fail. Boundary rates \(\gamma=0,2\) are outside the theorem. The result does not assert that support alone measures typical optimization accuracy: the exact second moment shows its limitations.

## References

1. D. Kozak, C. Molinari, L. Rosasco, L. Tenorio, S. Villa, *Zeroth order optimization with orthogonal random directions*, arXiv:2107.03941, first posted 2021-07-08. https://arxiv.org/abs/2107.03941
2. M. Rando, C. Molinari, S. Villa, L. Rosasco, *Stochastic Zeroth order Descent with Structured Directions*, arXiv:2206.05124, first posted 2022-06-10. https://arxiv.org/abs/2206.05124
3. T. Banakh, A. Bartoszewicz, M. Filipczak, E. Szymonik, *Topological and measure properties of some self-similar sets*, arXiv:1403.0098 (general finite-alphabet self-similar sumsets, not the stated optimizer). https://arxiv.org/abs/1403.0098
