# Two-harmonic circle exponentials: the sharp positive-type cone and infinite spectral obstructions

## Finding
Let \(1\le p<q\) be integers, \(a,b\in\mathbb R\), and let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). Define the stationary, unit-diagonal kernel
\[
K_{p,q;a,b}(x,y)=\exp\!\bigl(a[\cos(p(x-y))-1]+b[\cos(q(x-y))-1]\bigr).
\]
Then \(K_{p,q;a,b}\) is positive semidefinite on **every** finite set of circle sites if and only if
\[
\boxed{a\ge0\quad\text{and}\quad b\ge0.}
\]
If either parameter is negative, the stationary profile has **infinitely many strictly negative Fourier coefficients** (not merely one negative finite Gram eigenvalue).

For the admissible, nonconstant kernels, write \(S=\{p:a>0\}\cup\{q:b>0\}\), and let \(d=\gcd S\). The Fourier coefficients are strictly positive exactly at indices divisible by \(d\). Accordingly, the kernel is strictly positive definite on every finite set of distinct sites **modulo the period \(2\pi/d\)**. As a kernel on the full circle it is strictly positive definite exactly if \(d=1\). If \(a=b=0\), it is the constant-one rank-one kernel.

## Assumptions and scope
The claim concerns all integers \(1\le p<q\), all real parameters \(a,b\), and arbitrary finite configurations (not just equally spaced grids). Positive semidefiniteness is defined by \(\sum_{j,k=1}^m\overline{v_j}v_kK(x_j,x_k)\ge0\) for all \(m\ge1\), sites \(x_j\in\mathbb T\), and complex weights \(v_j\). Strict positivity refers to distinct sites, with the displayed quotient-circle qualification. The Fourier coefficient convention is \(\widehat f(n)=(2\pi)^{-1}\int_0^{2\pi}f(t)e^{-int}\,dt\).

## Proof
**1. Laurent model and the spectral criterion.** Put
\[
\Phi(z)=\exp\!\left[\frac a2(z^p+z^{-p})+\frac b2(z^q+z^{-q})\right]
=\sum_{n\in\mathbb Z}c_nz^n,\qquad z\ne0.
\]
The Laurent series converges absolutely and uniformly on every compact annulus. Its real symmetric coefficients satisfy \(c_{-n}=c_n\in\mathbb R\). On the unit circle, the unnormalized profile is \(\Phi(e^{it})\), and the kernel profile is \(e^{-a-b}\Phi(e^{it})\). The positive scalar \(e^{-a-b}\) cannot change coefficient signs. The Fourier criterion for continuous functions of positive type on the compact abelian circle group says that the kernel is positive semidefinite on all finite configurations if and only if \(c_n\ge0\) for all integers \(n\).

**2. Sufficiency and exact support.** For \(a,b\ge0\), the modified-Bessel expansion
\[
e^{t\cos\theta}=\sum_{k\in\mathbb Z}I_{|k|}(t)e^{ik\theta},
\quad I_m(t)=\sum_{j=0}^\infty\frac{(t/2)^{2j+m}}{j!(j+m)!}
\]
gives
\[
c_n=\sum_{pu+qv=n}I_{|u|}(a)I_{|v|}(b)\ge0.
\]
For \(t>0\), every \(I_m(t)>0\); for \(t=0\), only \(I_0(0)=1\) is nonzero. Consequently, if both parameters are positive, \(c_n>0\) precisely for \(n\in\gcd(p,q)\mathbb Z\), because every such integer has an integral Bézout representation \(pu+qv=n\). With exactly one positive parameter, the support is the associated frequency lattice. With both zero, only \(c_0\) survives.

**3. Nonnegativity cannot survive any negative coefficient: the infinite-negativity lemma.** Suppose, aiming for contradiction, that only finitely many Laurent coefficients \(c_n\) are negative. Define the finite Laurent polynomial \(P(z)=\sum_{c_n<0}(-c_n)z^n\). It has nonnegative coefficients. Then \(G(z)=\Phi(z)+P(z)\) has nonnegative Laurent coefficients at **every** index. For each \(r>0\) and real \(\theta\), absolute convergence and the triangle inequality imply
\[
|G(re^{i\theta})|\le G(r)=\Phi(r)+P(r),\qquad
|\Phi(re^{i\theta})|\le\Phi(r)+2P(r). \tag{1}
\]
Here \(\Phi(r)>0\), \(P(r)\ge0\), and \(P(r)\) has at most polynomial growth as \(r\to\infty\).

If \(b<0\), choose \(\theta=\pi/q\). Because \(p<q\), the leading growth rates as \(r\to\infty\) are
\[
\log|\Phi(re^{i\theta})|=\frac{|b|}{2}r^q+O(r^p),\qquad
\log\Phi(r)=-\frac{|b|}{2}r^q+O(r^p).
\]
Thus the left side of (1) grows superpolynomially, while its right side grows at most polynomially, contradicting (1). This conclusion holds regardless of the sign of \(a\).

If \(b>0\) and \(a<0\), choose \(\theta=2\pi/q\). Then \(\cos(q\theta)=1\) but \(\cos(p\theta)<1\), since \(0<p<q\). Consequently,
\[
\log\frac{|\Phi(re^{i\theta})|}{\Phi(r)}
=\frac{|a|}{2}[1-\cos(2\pi p/q)]r^p+O(r^{-p})\longrightarrow+\infty.
\]
In this case \(\Phi(r)=\exp(br^q/2+O(r^p))\) grows faster than any polynomial, so \(P(r)/\Phi(r)\to0\). After division of (1) by \(\Phi(r)\), the right side tends to one and the left side diverges, again a contradiction.

Finally, if \(b=0\) and \(a<0\), take \(\theta=\pi/p\). Then \(\log|\Phi(re^{i\theta})|=|a|r^p/2+o(r^p)\) and \(\log\Phi(r)=-|a|r^p/2+o(r^p)\), contradicting (1) as in the first case. These cases exhaust every point outside the nonnegative parameter quadrant. Therefore the set of negative Fourier coefficients is infinite whenever \(a<0\) or \(b<0\). This proves necessity and the strengthened spectral obstruction.

**4. Strictness on the exact quotient.** For admissible nonconstant kernels and arbitrary weights,
\[
\sum_{j,k}\overline{v_j}v_k K(x_j,x_k)
=e^{-a-b}\sum_{n\in d\mathbb Z}c_n\left|\sum_j v_je^{inx_j}\right|^2.
\]
Every term is nonnegative and every coefficient on \(d\mathbb Z\) is strictly positive. If this quadratic form vanishes, all moments \(\sum_jv_je^{idkx_j}\) vanish for integers \(k\ge0\). At sites distinct modulo \(2\pi/d\), the first \(m\) such equations form an invertible Vandermonde system in the distinct numbers \(e^{idx_j}\); hence every weight vanishes. Conversely, sites equal modulo \(2\pi/d\) yield identical kernel rows and destroy strict positivity. This establishes the claimed exact quotient criterion.

## Verification
The reproducible standard-Python script `checker.py` checks 48 independent comparisons between Fourier quadrature and the Bessel convolution (maximum error \(1.09\times10^{-15}\)); five finite negative-coefficient examples for signed parameters; a negative \(32\)-site circulant eigenvalue (about \(-5.7128643854\)); two complex-radius growth inequalities; and a positive \(16\)-site spectrum at \(a=1\), \(p=1\), \(q=2\), \(b=-10^{-7}\) (smallest eigenvalue about \(3.18736\times10^{-6}\)). The last experiment illustrates that a **fixed finite grid can appear positive** while the kernel fails global positive definiteness. Numerical checks are supplementary; the infinite-sign and all-configuration statements follow from the proof above.

## Relationship to prior work
Janke and Kleinert (1995, arXiv:hep-lat/9504010v1) examine the same two-harmonic exponential profile at the harmonic pair \((p,q)=(1,2)\) through generalized Bessel weights in a compact lattice model. They discuss lower-order weights and phase-transition mechanisms rather than classifying positive type for all parameter signs and harmonic pairs, or proving infinitely many negative coefficients. Gatto and Jammalamadaka's generalized von Mises density (2007) uses the two-cosine exponential, but pointwise nonnegativity of an angular **density** does not imply positive definiteness as a **stationary kernel**. Gneiting (2011 preprint) describes the general spectral criteria for positive definiteness on spheres, including the circle; that criterion is applied here but does not itself evaluate all mixed-harmonic exponential coefficients. Searches of equivalent Fourier/Bessel formulations and indexed results found related sparse-trigonometric-polynomial extremal problems, which do not imply this parameter classification. These comparisons do not establish historical uniqueness; an unindexed equivalent result remains possible.

## Limitations
The theorem covers precisely two cosine frequencies, with no phase shifts or additional harmonics, on the compact circle group. It does not assert a corresponding characterization for more than two harmonics, arbitrary profiles, or nonstationary kernels. Infinite coefficient negativity supplies existence of finite negative witnesses but gives no uniform upper bound on the number of sites required when a negative parameter is arbitrarily small. The literature comparison is necessarily bounded; independent validation has not been performed.

## References
- W. Janke and H. Kleinert, *Geometrical Origin of Tricritical Points of various U(1) Lattice Models*, arXiv:hep-lat/9504010v1 (first posted April 17, 1995), https://arxiv.org/abs/hep-lat/9504010.
- R. Gatto and S. R. Jammalamadaka, *The generalized von Mises distribution*, *Statistical Methodology* 4 (2007), 341–353, DOI:10.1016/j.stamet.2006.11.003.
- T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077 (first posted November 30, 2011), https://arxiv.org/abs/1111.7077.
