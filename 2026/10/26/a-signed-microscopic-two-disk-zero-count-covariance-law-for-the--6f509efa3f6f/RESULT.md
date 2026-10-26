# A signed microscopic two-disk zero-count covariance law for the planar Gaussian entire function

## Finding
Let \(F(z)=\sum_{j=0}^{\infty}\xi_j z^j/\sqrt{j!}\), with independent standard circular complex Gaussian coefficients, and let \(N(r)\) be its number of zeros, with multiplicity, in \(\{|z|<r\}\). Define, for \(d>0\),
\[
K(d)=\frac{\operatorname{Li}_{3/2}(e^{-d^2})-2d^2\operatorname{Li}_{1/2}(e^{-d^2})}{4\sqrt\pi},
\qquad K(0)=\frac{\zeta(3/2)}{4\sqrt\pi}.
\]
For every \(A<\infty\), uniformly over real \(a,b\in[-A,A]\),
\[
\frac{\operatorname{Cov}(N(R+a),N(R+b))}{R}
=K(|a-b|)+O_A(R^{-1}),\qquad R\longrightarrow\infty.
\]
There is precisely one \(d_*\in(0,1/\sqrt2)\) for which \(K(d_*)=0\), numerically \(d_*=0.54676907543845\ldots\). The function \(K\) is positive on \([0,d_*)\), negative on \((d_*,\infty)\), and vanishes only at \(d_*\). Consequently, although the disks are nested, their zero counts have strictly negative covariance for every fixed radial gap greater than \(d_*\) and all sufficiently large radii. The assertions at \(d=0\) use the continuous extension and recover the known one-circle variance coefficient.

## Assumptions and scope
The independent \(\xi_j\) have complex density \(\pi^{-1}e^{-|z|^2}\). The Gaussian series converges almost surely to an entire function. Zero counts are unconditioned and count multiplicities. Radii are positive; the asymptotic uses \(R>A\). The offsets \(a,b\) remain in a fixed bounded interval as \(R\to\infty\). The polylogarithm is \(\operatorname{Li}_{s}(q)=\sum_{k\ge1}q^k/k^s\) for \(0<q<1\). Only the products \(d^2\operatorname{Li}_{1/2}(e^{-d^2})\) are used at \(d=0\), with continuous limit zero. Covariances are real ordinary second moments, not a statement about any limiting joint distribution.

## Proof
**1. A Gaussian logarithm covariance identity.** If \(X,Y\) are jointly standard circular complex Gaussians, and \(q=|\mathbb E[X\overline Y]|^2\), then
\[
\operatorname{Cov}(\log|X|,\log|Y|)
=\frac14\sum_{k\ge1}\frac{q^k}{k^2}
=\frac14\operatorname{Li}_2(q).
\]
For completeness, the orthonormal Laguerre polynomials \(L_k\) for the exponential probability density on \([0,\infty)\) satisfy
\(\mathbb E[\log|X| L_k(|X|^2)]=-1/(2k)\) for \(k\ge1\), while Gaussian pairings imply \(\mathbb E[L_j(|X|^2)L_k(|Y|^2)]=\mathbf1_{j=k}q^k\). The \(L^2\) Laguerre expansion and Parseval give the displayed identity, including the endpoint \(q=1\) by convergence.

**2. Exact finite-radius covariance.** Let \(J(r)=(2\pi)^{-1}\int_0^{2\pi}\log|F(re^{i\theta})|\,d\theta\), where the usual local-integrability convention applies at boundary zeros. Jensen's formula gives \(rJ'(r)=N(r)\) away from the zero radii. The normalized Fock kernel is
\[
\frac{\mathbb E[F(z)\overline{F(w)}]}{\sqrt{\mathbb E|F(z)|^2\mathbb E|F(w)|^2}}
=\exp\!\left(z\overline w-\frac{|z|^2+|w|^2}{2}\right).
\]
The squared magnitude on the circles of radii \(r,s\), at angular difference \(\theta\), equals \(e^{-(r-s)^2-2rs(1-\cos\theta)}\). The preceding identity, Fubini, and the angular Bessel representation yield
\[
\operatorname{Cov}(J(r),J(s))
=\frac14\sum_{k=1}^{\infty}\frac{e^{-k(r^2+s^2)}}{k^2}I_0(2krs),
\]
where \(I_\nu\) denotes the modified Bessel function. The mixed radial derivative and the identities \(I_0'=I_1\), \(I_1'=I_0-I_1/x\) give the exact identity
\[
\boxed{\operatorname{Cov}(N(r),N(s))
=rs\sum_{k=1}^{\infty}e^{-k(r^2+s^2)}
\left(2rs I_0(2krs)-(r^2+s^2)I_1(2krs)\right).}
\]
For distinct radii the differentiation is justified by uniform convergence on compact separated radial pairs. At equal radii the differentiated summand is \(O(k^{-3/2})\); continuity of the count covariance in \(L^2\), or the same convergent differentiated series, extends the identity to \(r=s\).

**3. A uniform two-radius asymptotic.** Put \(d=|r-s|\) and \(x=2krs\). The scaled large-argument Bessel expansions, with uniform remainders for \(x\ge x_0>0\), are
\[
e^{-x}I_0(x)=(2\pi x)^{-1/2}\left(1+\frac1{8x}+O(x^{-2})\right),
\quad
e^{-x}I_1(x)=(2\pi x)^{-1/2}\left(1-\frac3{8x}+O(x^{-2})\right).
\]
Subtracting these expansions before multiplying by \(2rs\), one gets
\[
\operatorname{Cov}(N(r),N(s))
=\frac{\sqrt{rs}}{2\sqrt\pi}
\sum_{k\ge1}e^{-kd^2}
\left(\frac1{2k^{3/2}}-\frac{d^2}{k^{1/2}}\right)
+O_A(R^{-1})
\]
for \(r=R+a\), \(s=R+b\), \(|a|,|b|\le A\). Indeed, the absolute error from the subtracted Bessel expansion is bounded by a constant times \((rs)^{-1/2}\sum k^{-5/2}+d^2(rs)^{-1/2}\sum k^{-3/2}\), which is \(O_A(R^{-1})\). Dividing by \(R\), using \(\sqrt{rs}/R=1+O_A(R^{-1})\), and summing both polylogarithmic series proves the claimed \(O_A(R^{-1})\) normalized estimate. The factor \(d^2\sum_{k\ge1}e^{-kd^2}k^{-1/2}\) stays bounded and tends to zero as \(d\downarrow0\); this verifies uniformity through coincident radii.

**4. Uniqueness of the sign reversal.** For \(x>0\) put \(A(x)=\operatorname{Li}_{3/2}(e^{-x})\), \(B(x)=\operatorname{Li}_{1/2}(e^{-x})\), \(C(x)=\operatorname{Li}_{-1/2}(e^{-x})\), and \(g(x)=A(x)-2xB(x)\). Then \(g'(x)=-3B(x)+2xC(x)\). Under the probability weights proportional to \(e^{-kx}\), \(k\ge1\), tilting by the decreasing weight \(k^{-1/2}\) cannot increase the expectation of \(k\). Thus
\[
\frac{C(x)}{B(x)}\le\frac1{1-e^{-x}}.
\]
For \(0<x\le1/2\), the elementary estimate \(1-e^{-x}\ge x-x^2/2\ge3x/4\) gives \(2xC(x)/B(x)\le8/3<3\), hence \(g'(x)<0\). At the lower endpoint, \(g(x)\to\zeta(3/2)>0\), since \(xB(x)\to0\). At \(x=1/2\), the absolutely convergent series
\[
g(x)=\sum_{k\ge1}e^{-kx}k^{-3/2}(1-2kx)
\]
is strictly negative: its first term vanishes and all subsequent terms are negative. For \(x>1/2\), every summand is negative. Therefore exactly one positive zero lies in \((0,1/2)\); setting \(d_*=\sqrt{x_*}\) gives the stated complete sign classification. Uniform covariance convergence implies the eventually positive/negative statements at every fixed gap away from \(d_*\).

## Verification
The accompanying standalone program `check.py` evaluates the exact finite-radius Bessel series using exponentially scaled Bessel functions and an asymptotically controlled zeta-series correction at coincidence, and compares it to the polylogarithmic limit. It also brackets the unique zero and checks both sides of the sign transition. Run `python check.py` with NumPy, SciPy and mpmath installed. All 29 corroborative assertions passed. The infinite-dimensional theorem, uniqueness, and uniform convergence are established by the analytical proof above, not by these finite tests.

## Relationship to prior work
Kiro and Nishry's 2019 preprint analyzes zero-count fluctuations of Gaussian Taylor series and includes the known single-circle planar-Fock leading variance \(\zeta(3/2)R/(4\sqrt\pi)\). Buckley and Sodin analyze Gaussian-entire-function argument increments and their covariance for large homothetically scaled fixed curves; fixed concentric circles are separated at macroscopic distance in that setup. Forrester and Honner give bulk zero correlations and one-disk fluctuation information. Those broad covariance and two-point formulas furnish important antecedents and can in principle be integrated to derive further results; the finding here is the explicit *moving-concentric-circle, bounded-physical-gap* crossover function together with its rigorously unique sign-reversal threshold. No claim is made that the underlying Fock zero process, its two-point correlation, the Gaussian logarithm identity, or the diagonal variance constant is new.

## Limitations
The statement covers the planar Gaussian entire function and concentric disks only. The radial gap is fixed as the common radius diverges; no uniformity is asserted for growing gaps. The sign at the exact critical gap for finite radii is not determined by the leading term. The result is a covariance asymptotic and does not establish a joint central-limit theorem. Related classical pair-correlation and moving-curve asymptotic formulas may contain an equivalent implicit form; historical novelty beyond the inspected references remains subject to broader literature checking.

## References
1. A. Kiro and A. Nishry, *Fluctuations for zeros of Gaussian Taylor series*, arXiv:1911.13051, first posted 2019-11-29. https://arxiv.org/abs/1911.13051
2. J. Buckley and M. Sodin, *Fluctuations of the increment of the argument for the Gaussian entire function*, arXiv:1608.05590, 2016. https://arxiv.org/abs/1608.05590
3. P. J. Forrester and G. Honner, *Exact statistical properties of the zeros of complex random polynomials*, arXiv:cond-mat/9812388, 1998. https://arxiv.org/abs/cond-mat/9812388
