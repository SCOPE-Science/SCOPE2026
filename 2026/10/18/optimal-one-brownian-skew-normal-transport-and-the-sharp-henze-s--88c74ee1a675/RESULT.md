# Optimal one-Brownian skew-normal transport and the sharp Henze strong-error penalty

## Finding
Let \(\phi,\Phi\) be the standard normal density and distribution function, respectively, and let \(Z,E\) be independent standard normals. For a real skew parameter \(a\), write
\[
F_a(y)=\int_{-\infty}^{y}2\phi(t)\Phi(at)\,dt,\qquad Q_a(z)=F_a^{-1}(\Phi(z)),\qquad m=\sqrt{2/\pi}.
\]
The increasing Brownian-quantile coupling \(Q_a(Z)\) and the usual independent-auxiliary-normal coupling \(H_a=(Z+a|E|)/\sqrt{1+a^2}\) have the same skew-normal marginal law. Among all couplings of that law with a standard normal, \((Z,Q_a(Z))\) uniquely minimizes expected squared displacement. For every \(a\ne0\), its displacement is strictly smaller than that of \((Z,H_a)\).

The quantile coupling also satisfies the exact sensitivity identity
\[
\partial_a Q_a(z)=\frac{\phi(aQ_a(z))}{(1+a^2)\Phi(aQ_a(z))},
\]
and the global quantitative bound
\[
\bigl\|Q_a(Z)-Z-ma\bigr\|_{L^2}\le \tfrac12 a^2+\tfrac m3|a|^3. \tag{1}
\]
Consequently, defining \(R_Q(a)=\mathbb E[(Q_a(Z)-Z)^2]\) and \(R_H(a)=\mathbb E[(H_a-Z)^2]\),
\[
R_Q(a)=\tfrac2\pi a^2+O(|a|^3),\qquad R_H(a)=2\left(1-\frac1{\sqrt{1+a^2}}\right)=a^2+O(a^4),
\]
so that
\[
\lim_{a\to0,\,a\ne0}\frac{R_H(a)}{R_Q(a)}=\frac\pi2.
\]
This gives a sharp leading factor \(2/\pi\) in the squared Brownian-displacement cost of quantile sampling relative to the two-normal construction, while preserving the same one-step numerical transition distribution.

## Assumptions and scope
The statements above hold for every real \(a\) and standard normals \(Z,E\). For a scalar stochastic differential equation, consider a fixed state \(x\), drift \(b=b(x)\in\mathbb R\), strictly positive diffusion \(\sigma=\sigma(x)>0\), and time step \(h>0\). In the skew-normal step construction of the cited numerical paper, use \(a=\sqrt{\pi/2}\,\sqrt h\,b/\sigma\) and define two numerical increments
\[
\Delta_Q=\sigma\sqrt h\,Q_a(Z),\qquad \Delta_H=\sigma\sqrt h\,H_a.
\]
Then \(\Delta_Q\) and \(\Delta_H\) have identical conditional one-step distributions, and if \(b\ne0\), their squared deviations from the *unshifted* Brownian increment satisfy
\[
\mathbb E[(\Delta_Q-\sigma\sqrt h\,Z)^2]=b^2h^2+o(h^2),\qquad
\mathbb E[(\Delta_H-\sigma\sqrt h\,Z)^2]=\tfrac\pi2 b^2h^2+o(h^2).
\]
Here the comparator is explicitly the unshifted Brownian increment, not the exact solution increment of the SDE; no global strong convergence rate is inferred. For \(b=0\), both deviations vanish identically.

## Proof
**Distributional equality.** The characteristic representation \((Z+a|E|)/\sqrt{1+a^2}\) has density \(2\phi(y)\Phi(ay)\), as seen by conditioning a bivariate normal vector on a half-space, or by direct integration. The map \(Q_a\) is strictly increasing and sends a standard normal to the same law by the probability-integral transform. Also, by the normal symmetry \(\Phi(ay)+\Phi(-ay)=1\), every even moment of the skew-normal density agrees with the corresponding standard-normal moment. In particular \(\mathbb E[Q_a(Z)^2]=1\), for all real \(a\).

**Sharp quadratic transport.** For any \(z_1<z_2\) and \(y_1<y_2\), uncrossing a reversed pair improves the sum of the two quadratic costs by \(2(z_2-z_1)(y_2-y_1)>0\). The one-dimensional increasing rearrangement is therefore the unique quadratic-cost minimizing coupling of two atomless laws. For \(a\ne0\), conditional on \(Z\), the variable \(H_a\) still has nondegenerate randomness from \(|E|\), whereas \(Q_a(Z)\) is a deterministic increasing function. Thus the two-normal coupling is not optimal; its expected squared cost is strictly higher. Because \(\mathbb E[ZH_a]=1/\sqrt{1+a^2}\) and both second moments equal one,
\[
R_H(a)=2\left(1-(1+a^2)^{-1/2}\right).
\]

**Quantile sensitivity.** Differentiation under the Gaussian integral gives, for all finite \(y,a\),
\[
\partial_a F_a(y)=2\int_{-\infty}^y t\phi(t)\phi(at)\,dt=-\frac{2\phi(y)\phi(ay)}{1+a^2},\qquad
\partial_y F_a(y)=2\phi(y)\Phi(ay)>0.
\]
Implicit differentiation of \(F_a(Q_a(z))=\Phi(z)\) yields the displayed sensitivity formula.

**Quantitative bound.** Define the normal inverse Mills function \(r(t)=\phi(t)/\Phi(t)\). Its derivative is \(r'(t)=-r(t)[t+r(t)]\). If \(N\) is standard normal conditioned on \(N\le t\), its mean is \(-r(t)<t\) and variance is \(1-tr(t)-r(t)^2>0\). Hence \(0<r(t)[t+r(t)]<1\), so \(-1<r'(t)<0\) on \(\mathbb R\); in particular, \(|r(t)-r(0)|\le |t|\) and \(r(0)=m\). The sensitivity identity now implies
\[
|\partial_sQ_s(z)-m|
=\left|\frac{r(sQ_s(z))}{1+s^2}-m\right|
\le |s|\,|Q_s(z)|+m s^2.
\]
Taking \(L^2\) norms, using \(\|Q_s(Z)\|_2=1\), and integrating in \(s\) from zero to \(a\), the Minkowski integral inequality gives (1) for positive and negative \(a\). The argument also justifies interchanging integration with the \(L^2\) norm because the displayed bound is integrable on every bounded parameter interval.

Since \(Q_0(Z)=Z\), bound (1) implies \(\|Q_a(Z)-Z\|_2=m|a|+O(a^2)\) and thus \(R_Q(a)=m^2a^2+O(|a|^3)\). Taylor expanding the exact formula for \(R_H\) proves the ratio \(\pi/2\). Finally, substituting \(a=\sqrt{\pi/2}\sqrt h\,b/\sigma\) and multiplying the two costs by \(\sigma^2h\) gives the scalar-SDE formulas.

## Verification
The included `check_quantile.py` independently evaluates skew-normal normal-quantile transforms with SciPy, Gaussian quadrature, and numerical derivatives. It tests moment preservation, the strict optimal-coupling inequality, the global \(L^2\) envelope, quantile sensitivity, inverse-Mills slopes, small-skew constants, and representative one-step SDE parameters. Run `python check_quantile.py` with Python 3, NumPy, and SciPy. Finite floating-point tests only cross-check, and do not prove, the identities for arbitrary parameters.

## Relationship to prior work
The motivating 2026 skew-symmetric SDE scheme chooses the two-normal skew-normal representation to construct its numerical step and investigate pathwise properties. Its stochastic representation and the skew-normal distribution are not new. Increasing one-dimensional quantile transport is classical: that general theorem already implies minimum quadratic cost, and is expressly **not** claimed as original here. The contribution assessed here is the specific one-Brownian construction for the cited skew-SDE increment, its global parameter-sensitivity envelope, and the sharp \(\pi/2\) discrepancy factor against the actual auxiliary-normal coupling. A preceding unadjusted-Barker work instead studies an earlier skew-symmetric SDE construction. No general numerical cost improvement or pathwise theorem for the full SDE is inferred.

## Limitations
This is a scalar, exact-inverse-CDF, one-step comparison of couplings of a fixed skew-normal transition law. It compares against the *unshifted Brownian driver*, not the exact SDE increment or its drift-corrected Euler counterpart. The claim does not establish superior strong order, global time-horizon errors, multilevel Monte Carlo variance, or wall-clock performance. Computing skew-normal quantiles may be more expensive than drawing an independent standard normal. The source's higher-dimensional construction and nonuniform/skewness-dependent numerical error estimates are outside scope. Standard transport theory covers the optimality component; bibliographic overlap for the combined sensitivity and sharp-penalty statement remains possible.

## References
1. Y. Iguchi, S. Livingstone, G. Vasdekis, and R.-Y. Zhang, *Pathwise skew-symmetric discretisation for SDEs with superlinear drift*, arXiv:2607.17735, first released 2026-07-20. https://arxiv.org/abs/2607.17735
2. Y. Iguchi et al., *Skew-symmetric schemes for stochastic differential equations with non-Lipschitz drift: an unadjusted Barker algorithm*, open-access earlier related numerical-analysis study, arXiv:2405.14373. https://arxiv.org/abs/2502.03421
3. N. Henze, *A probabilistic representation of the skew-normal distribution* (1986), classical normal-mixture representation; bibliographic record checked, primary full text not inspected.
4. F. Santambrogio, *Optimal Transport for Applied Mathematicians* (2015), one-dimensional increasing-rearrangement theorem.
