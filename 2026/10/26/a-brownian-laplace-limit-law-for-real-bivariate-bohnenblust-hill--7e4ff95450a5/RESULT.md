# A Brownian Laplace limit law for real bivariate Bohnenblust–Hille ratios

## Finding

Let \(m\geq2\), \(q_m=2m/(m+1)\), and let \(a=(a_0,\ldots,a_m)\) be uniformly distributed on the Euclidean unit sphere of \(\mathbb R^{m+1}\). For the real homogeneous polynomial
\[
P_{m,a}(x,y)=\sum_{j=0}^{m}a_jx^{m-j}y^j,
\]
define its real Bohnenblust–Hille coefficient ratio by
\[
R_m(a)=\frac{(\sum_{j=0}^{m}|a_j|^{q_m})^{1/q_m}}{\max_{|x|,|y|\leq1}|P_{m,a}(x,y)|}.
\]
Let \(W_+\) and \(W_-\) be **independent** standard real Brownian motions on \([0,1]\). For \(\sigma\in\{+,-\}\) and \(s\in[0,\infty)\), put
\[
U_\sigma(s)=\int_0^1 e^{-su}\,dW_\sigma(u),\qquad
V_\sigma(s)=\int_0^1e^{-s(1-u)}\,dW_\sigma(u).
\]
The stochastic integrals have continuous versions extending to \(s=\infty\), where both are zero. Define
\[
M=\max_{\sigma\in\{+,-\}}\sup_{0\leq s\leq\infty}\max\{|U_\sigma(s)|,|V_\sigma(s)|\}.
\]
Then \(0<M<\infty\) almost surely and
\[
\boxed{R_m\ \xrightarrow[m\to\infty]{\mathrm{law}}\ M^{-1}.}
\]
Moreover, the limiting distribution has full support \((0,\infty)\): it is not a deterministic constant. This supplies an explicit Gaussian-process limit law at fixed real dimension two, where previously known estimates guarantee order-one tightness rather than a limiting distribution.

## Assumptions and scope

All coefficients, variables, and Brownian motions are real. The coefficient sphere carries rotation-invariant normalized surface probability; the polynomial sup norm is taken on the real square \([-1,1]^2\). Degrees tend to infinity with the number of variables fixed at two. The first-public paper motivating the ratio appeared September 24, 2026. The result makes no claim for the complex polydisc, dimensions greater than two, or arbitrary non-Gaussian coefficient ensembles.

## Proof

**1. Gaussian replacement and the exact boundary reduction.** Let \(g_0,\ldots,g_m\) be independent standard normal variables. Since \(g/\|g\|_2\) is uniform on the coefficient sphere and \(R_m\) is homogeneous of degree zero, \(R_m(g)\) and \(R_m(a)\) have identical laws. By homogeneity of the degree-\(m\) polynomial, its maximum absolute value on \([-1,1]^2\) occurs on the boundary, and changing the sign of a coordinate only introduces a global degree-dependent sign after reparametrization. Thus, **exactly**,
\[
\|P_{m,g}\|_{\infty,\mathbb R}=
\max_{-1\leq t\leq1}\max\left\{\left|\sum_{j=0}^{m}g_jt^j\right|,\left|\sum_{j=0}^{m}g_jt^{m-j}\right|\right\}.
\]
Writing \(t=\sigma e^{-s/m}\) with \(\sigma\in\{1,-1\}\) and \(s\in[0,\infty]\) splits this maximum into four weighted-sum paths. For the reverse negative path an irrelevant factor \((-1)^m\) disappears inside absolute values.

**2. The coefficient numerator has limit one after square-root normalization.** Because \(q_m\to2\) and \(q_m\in[4/3,2)\), uniform fourth-moment domination and Chebyshev's inequality show
\[
\frac1{m+1}\sum_{j=0}^{m}|g_j|^{q_m}
-\mathbb E|g_0|^{q_m}\xrightarrow{\mathbb P}0,
\qquad \mathbb E|g_0|^{q_m}\longrightarrow1.
\]
Also \((m+1)^{1/q_m}/\sqrt m\to1\), because \(1/q_m-1/2=1/(2m)\). Consequently
\[
\frac{\|g\|_{q_m}}{\sqrt m}\xrightarrow{\mathbb P}1.
\]

**3. Two independent limiting noises, retaining time-reversal dependence.** For \(\sigma\in\{1,-1\}\), let \(Z_m^\sigma\) be the piecewise-linear interpolation on \([0,1]\) of
\[
Z_m^\sigma(k/m)=m^{-1/2}\sum_{j=0}^{k-1}\sigma^jg_j,
\qquad 0\leq k\leq m.
\]
These are jointly centered Gaussian polygonal processes. Their same-sign covariance converges to \(\min(u,v)\); their cross-sign covariance is bounded in absolute value at mesh times by \(1/m\), since every alternating partial sum has magnitude at most one. Gaussian finite-dimensional convergence and the fourth-moment tightness bound for increments give, jointly in \(C([0,1])^2\),
\[
(Z_m^+,Z_m^-)\ \Longrightarrow\ (W_+,W_-),
\]
with independent standard Brownian limits. Interpolation errors in the cross-covariance vanish uniformly.

**4. A uniform summation-by-parts map, including both boundary layers.** For a continuous path \(z\) starting at zero define
\[
\Phi_s(z)=e^{-s}z(1)+s\int_0^1e^{-su}z(u)\,du,
\qquad \widehat z(u)=z(1)-z(1-u).
\]
The integrand mass is \(1-e^{-s}\), so \(z\mapsto(s\mapsto\Phi_s(z))\) is \(1\)-Lipschitz from the uniform norm into \(C([0,\infty])\), where \(\Phi_\infty(z)=z(0)=0\). The reversed map \(z\mapsto\Phi_s(\widehat z)\) is likewise continuous. Integration by parts identifies \(\Phi_s(W)\) with \(\int_0^1e^{-su}\,dW(u)\) and \(\Phi_s(\widehat W)\) with \(\int_0^1e^{-s(1-u)}\,dW(u)\).

For the forward discrete path set \(b_j=m^{-1/2}\sigma^jg_j\) and \(S_k=\sum_{j<k}b_j\). Direct Abel summation gives, with \(t=e^{-s/m}\),
\[
\sum_{j=0}^m b_jt^j=t^mS_{m+1}+\sum_{k=1}^m(t^{k-1}-t^k)S_k.
\]
But \(t^m=e^{-s}\) and \(t^{k-1}-t^k=\int_{(k-1)/m}^{k/m}se^{-su}\,du\). Comparing this exact identity to \(\Phi_s(Z_m^\sigma)\) yields, uniformly over **all** \(0\leq s\leq\infty\),
\[
\left|\sum_{j=0}^m b_je^{-sj/m}-\Phi_s(Z_m^\sigma)\right|
\leq |b_m|+\omega_{Z_m^\sigma}(1/m)
\leq 3\max_{0\leq j\leq m}|g_j|/\sqrt m.
\]
The right side converges to zero in probability by a Gaussian union bound. For the reversed coefficient sequence \(b_m,\ldots,b_0\), its cumulative-sum polygon differs uniformly by at most \(2\max_j|b_j|\) from \(\widehat Z_m^\sigma\), so the same conclusion holds for the reverse paths. These estimates exclude any unexamined small-\(t\) or large-\(s\) tails.

The continuous mapping theorem now gives joint convergence of all four sign/forward–reverse paths to \((U_+,V_+,U_-,V_-)\) in \(C([0,\infty])^4\). Taking the joint maximum of absolute suprema, which is continuous under the uniform norm, proves \(\|P_{m,g}\|_{\infty,\mathbb R}/\sqrt m\Longrightarrow M\).

**5. Division and full support.** The paths are bounded since \(|\Phi_s(z)|\leq\|z\|_\infty\); hence \(M<\infty\) almost surely. At \(s=0\), \(U_+(0)=W_+(1)\), so \(M>0\) almost surely. Slutsky's theorem and continuity of division on positive denominators give the announced convergence. Finally, \(M\) depends continuously on the two Brownian sample paths. Wiener measure has full support on the continuous paths starting at zero. On the deterministic pair \((z_+(u),z_-(u))=(cu,0)\), with arbitrary \(c>0\), the maximum is exactly \(c\). Thus every positive value belongs to the support of \(M\), and every positive value belongs to the support of \(M^{-1}\). In particular the limit cannot be a point mass. \(\square\)

## Verification

The finite-dimensional reduction, Abel identity, and alternating covariance estimate can be reproduced with the standalone `CHECK.py` script. Its numerical tests cover finite examples only. The infinite-dimensional convergence is proved analytically by the joint Gaussian invariance principle, uniformly controlled Abel summation, and continuous mapping, not by simulation. The Gaussian-process limit has explicit covariance: within one sign, \(\operatorname{Cov}(U(s),U(t))=(1-e^{-(s+t)})/(s+t)\) with its continuous value at zero; and \(\operatorname{Cov}(U(s),V(t))=\int_0^1e^{-su-t(1-u)}\,du\). Different signs are independent.

## Relationship to prior work

Pellegrino and Teixeira, *Typical Bohnenblust–Hille Ratios* (arXiv:2609.31779, first posted September 24, 2026), Theorem D and Section 7.2, establish that in every fixed real dimension the ratio is bounded above and below in probability by dimension-dependent positive constants; Lemma 7.2 identifies the Gaussian coefficient numerator scale. The finding here supplies the complete nonconstant distributional limit specifically in real dimension two and identifies the four coupled boundary profiles. Their complex-case Theorem C concerns a different scalar field and a vanishing deterministic rescaling. Work on real anisotropic Bohnenblust–Hille constants studies extremal constants, not the random spherical coefficient law. Classical weak-convergence principles for Gaussian partial sums underlie the proof, but by themselves do not identify this coefficient-to-supremum ratio or its reflected and parity-decoupled profiles.

## Limitations

The limit distribution is specified by a compact Gaussian-process supremum; no elementary cumulative-distribution formula, sharp tail expansion, or extension to real dimension three or higher is asserted. Its exact priority against unindexed literature on boundary-scaled Kac polynomials remains a separate literature risk. Numerical checks do not establish the limiting theorem. The derivation uses Gaussian representation of uniform spherical measure, so no assertion is made for non-Gaussian random coefficient directions.

## References

1. Daniel M. Pellegrino and Eduardo V. Teixeira, *Typical Bohnenblust–Hille Ratios*, arXiv:2609.31779 (first submitted 2026-09-24), Theorem D and Section 7.2, https://arxiv.org/abs/2609.31779 and https://arxiv.org/html/2609.31779.
2. Daniel Núñez-Alarcón et al., *The Geometry of Real Anisotropic Bohnenblust–Hille Constants*, arXiv:2609.04143 (2026), https://arxiv.org/abs/2609.04143; comparison concerns extremal rather than random-direction constants.
3. W. Feller, *An Introduction to Probability Theory and Its Applications*, Vol. II, the functional central limit/invariance principle (standard background, not a claimed new theorem).
