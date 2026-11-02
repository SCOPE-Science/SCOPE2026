# A sharp Rayleigh transition and finite chord test for almost-equal random circle quadrature

## Finding

Let \(m\ge3\) distinct sample points \(z_j=(\cos\Theta_j,\sin\Theta_j)\) lie on the unit circle and not all on a common line. Define the minimal relative deviation from uniform weights needed to integrate the first Fourier harmonics exactly by
\[
T_m=\min\left\{t\ge0:\ \sum_{j=1}^m w_j=1,\ \sum_{j=1}^m w_jz_j=0,\ \left|mw_j-1\right|\le t\text{ for all }j\right\}.
\]
Writing \(S_m=\sum_jz_j\), \(n_{ij}=R_{\pi/2}(z_i-z_j)\), and \(p_{k,ij}=n_{ij}\cdot z_k\), the *exact finite-node formula* is
\[
\boxed{T_m=\max_{1\le i<j\le m}\frac{|n_{ij}\cdot S_m|}{\sum_{k=1}^m|p_{k,ij}-\operatorname{med}(p_{1,ij},\dots,p_{m,ij})|}.}
\]
Here any median can be used. In particular, for every \(t\in[0,1)\), there is an exact quadrature rule with **strictly positive** weights in \([(1-t)/m,(1+t)/m]\) if and only if \(T_m\le t\).

For independent uniformly distributed \(\Theta_j\in[0,2\pi)\), the same statistic obeys the *sharp asymptotic law*
\[
\boxed{\frac{mT_m}{\|S_m\|_2}\longrightarrow\frac\pi2\quad\text{almost surely},\qquad
\lim_{m\to\infty}\mathbb P\!\left(T_m\le\frac c{\sqrt m}\right)=1-\exp\!\left(-\frac{4c^2}{\pi^2}\right),\quad c\ge0.}
\]
The ratio is interpreted on the almost-sure event \(S_m\ne0\) for all \(m\). This is an exact success-probability transition for near-equal, positive quadrature on the space \(\operatorname{span}\{1,\cos\theta,\sin\theta\}\).

## Assumptions and scope

The finite identity assumes only \(m\ge3\), pairwise distinct points on the Euclidean unit circle, and noncollinearity. For random nodes these conditions hold almost surely. There are no regular-grid, separation, or conditioning assumptions. The weights are real during the minimization; a prescribed relative tolerance less than one automatically makes them strictly positive. The sampling law is i.i.d. normalized arc measure; \(\Theta_j\) are coupled as the first \(m\) terms of one infinite i.i.d. sequence for almost-sure assertions.

## Proof

**1. Reduce exact integration to a centered zonotope.** Put \(v_j=mw_j-1\). The three quadrature constraints are equivalent to
\[
\sum_{j=1}^m v_j=0,\qquad \sum_{j=1}^m v_jz_j=-S_m,
\]
while \(|v_j|\le t\). Define the closed centrally symmetric convex body
\[
K_m=\left\{\sum_{j=1}^m v_jz_j:\ -1\le v_j\le1,\ \sum_jv_j=0\right\}\subset\mathbb R^2.
\]
Since the sampled points are not collinear, the map from the zero-sum hyperplane to \(\mathbb R^2\) is surjective, so \(K_m\) has nonempty interior. Consequently \(T_m\) is the Minkowski gauge of \(S_m\) with respect to \(K_m\).

**2. Compute the dual support function.** For every unit vector \(u\), linear-programming duality for the equality \(\sum_jv_j=0\) yields
\[
h_{K_m}(u)=\max_{\substack{|v_j|\le1\\\sum v_j=0}}\sum_jv_j(u\cdot z_j)
=\min_{a\in\mathbb R}\sum_{j=1}^m|u\cdot z_j-a|.
\]
The minimum occurs at any median. It is strictly positive for all \(u\in S^1\), because a zero value would mean every sampled point has the same projection onto \(u\), contradicting noncollinearity. By separation of convex bodies,
\[
T_m=\max_{u\in S^1}\frac{|u\cdot S_m|}{h_{K_m}(u)}.
\]

**3. Reduce the continuum maximum to chord normals.** Between successive directions at which two projected values \(u\cdot z_i\) and \(u\cdot z_j\) coincide, their strict ordering is fixed. In each such angular chamber the median-centered absolute-deviation sum is a *linear functional* of the vector \(u\), because it is a fixed signed sum of the projections (this remains true for even \(m\)). Thus the ratio is the absolute value of one linear trigonometric expression divided by a strictly positive linear trigonometric expression. On any chamber the derivative of the unsigned ratio with respect to angle has constant sign, or vanishes identically. The maximum of its absolute value therefore occurs at a chamber endpoint. Those endpoints are precisely the directions orthogonal to the chords \(z_i-z_j\). Taking all pairs gives the finite formula. This also covers an identically zero numerator, when \(T_m=0\).

**4. Uniform law of large numbers for the support functions.** Set
\[
H_m(u)=\min_{a\in[-1,1]}\sum_j|u\cdot z_j-a|.
\]
The restricted interval is sufficient because all projections lie in \([-1,1]\). The family \((z,u,a)\mapsto|u\cdot z-a|\), indexed by the compact set \(S^1\times[-1,1]\), is bounded and uniformly Lipschitz in \((u,a)\). A finite-net argument and the scalar strong law therefore give uniform almost-sure convergence of its empirical means. Rotational invariance makes the population objective \(\mathbb E|\cos\Theta-a|\) independent of \(u\); it has a median at \(a=0\) and minimum \(\mathbb E|\cos\Theta|=2/\pi\). Thus
\[
\sup_{u\in S^1}\left|\frac{H_m(u)}m-\frac2\pi\right|\longrightarrow0\qquad\text{almost surely}.
\]
From the dual formula, taking the direction \(u=S_m/\|S_m\|_2\) for the lower bound and using the largest possible numerator for the upper bound, the uniform convergence yields \(mT_m/\|S_m\|_2\to\pi/2\) almost surely.

**5. Limiting success probability.** By the multivariate central limit theorem,
\[
\frac{S_m}{\sqrt m}\Longrightarrow N\!\left(0,\frac12I_2\right).
\]
Hence \(\sqrt m\,T_m\Longrightarrow(\pi/(2\sqrt2))\sqrt{G_1^2+G_2^2}\), where \(G_1,G_2\) are independent standard normal variables. The radial standard-normal tail is \(\mathbb P(G_1^2+G_2^2>r^2)=e^{-r^2/2}\), giving the stated distribution function. All its continuity points include each \(c\ge0\). For any fixed \(c\), the threshold \(c/\sqrt m\) is below one once \(m\) is large enough, so the success event corresponds to *strictly positive* exact quadrature weights.

## Verification

The included standalone `verify.py` computes the finite chord-normal formula and independently solves the primal linear program using HiGHS via SciPy for 204 seeded nondegenerate random samples, with 1e-7-scale agreement. It also checks a regular-triangle zero-deviation case and empirical support-function normalizers at 36 directions for a separate large sample, for **241 passing finite checks**. Run `python verify.py` with Python 3.10+, NumPy, and SciPy. These computations do not certify the infinite limit, which follows from Steps 4–5.

## Relationship to prior work

Neumayer, Schäfer, and Ullrich (2026), arXiv:2610.32699v1, introduce the general random-node weight-adaptation framework, and their Corollary 2.13 gives a nonsharp high-probability sufficient sample size for an arbitrary fixed relative weight box. The result here specializes to the lowest nontrivial trigonometric space but determines the **exact minimal finite-sample box width**, a **finite chord-based deterministic test**, and the **nondegenerate asymptotic probability law and constant** in the critical \(m^{-1/2}\) window. The general existence theorem does not state these quantities. Wendel's classic random convex-hull theorem concerns unconstrained positive weights and does not determine closeness to equal weights. Range-restricted calibration is also studied outside this Fourier setting, but no identified source settles the stated sharp circular law.

## Limitations

The deterministic formula exploits the two-dimensional geometry of first Fourier harmonics and is not asserted for additional harmonics, higher-dimensional spheres, arbitrary nonuniform sampling densities, or near-equality in other norms. For tolerances \(t\ge1\), feasible weights in the box need not be positive. The formula gives exact mathematical values in real arithmetic; a floating-point implementation is not a validated exact-arithmetic certificate. The asymptotic formula supplies a limiting probability, not a finite-sample error bound or an optimality statement about runtime. Priority outside the inspected sources and the available research records remains subject to independent specialist review.

## References

1. S. Neumayer, M. Schäfer, T. Ullrich, *Random nodes with positive weights: Richter–Tchakaloff rules and optimal positive quadrature*, arXiv:2610.32699v1 (first posted 2026-10-23), especially Corollary 2.13. https://arxiv.org/html/2610.32699v1
2. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica **11** (1962), 109–112. https://doi.org/10.7146/math.scand.a-10655
3. *A global optimisation approach to range-restricted survey calibration*, Statistics and Computing (2018). https://discovery.ucl.ac.uk/id/eprint/10067066/
