# Critical quartic Bessel gaps and the logarithmic circle stability form

## Finding

Write \(J_k\) for the ordinary Bessel function of the first kind of integer order \(k\geq0\). The *matched-cutoff critical modal gap* is
\[
D_k=\lim_{R\to\infty}\int_0^R r\bigl(J_0(r)^4-J_k(r)^4\bigr)\,dr.
\]
Although the two separate integrals diverge, each gap exists as the stated ordinary improper limit and has the exact value
\[
\boxed{D_k=\frac{2}{\pi^2}\sum_{j=1}^{k}\frac1{2j-1}
=\frac2{\pi^2}\left(H_{2k}-\frac12H_k\right)},\qquad k\geq0,
\]
with the empty sum and \(H_0\) equal to zero. Hence \(D_0=0\), the sequence is strictly increasing, and
\[
D_k=\frac{\log k+2\log2+\gamma}{\pi^2}+O(k^{-2})\quad(k\to\infty).
\]
Here \(\gamma\) is Euler's constant.

For \(q>4\) define the convergent modal moments
\[
I_k(q)=\int_0^\infty |J_k(r)|^q r\,dr.
\]
For every **fixed** \(k\geq1\), as \(\varepsilon=q-4\downarrow0\),
\[
I_k(4+\varepsilon)=\frac3{\pi^2\varepsilon}+O_k(1),\qquad
\lim_{\varepsilon\downarrow0}\bigl(I_0(4+\varepsilon)-I_k(4+\varepsilon)\bigr)=D_k.
\]
In the unnormalized arclength and Fourier-transform convention of the cited mixed-norm extension work, define the pure-mode quadratic deficit
\[
W_q(k)=(2\pi)^2\bigl(I_0(q)^{2/q}-I_k(q)^{2/q}\bigr).
\]
Its exact first-order critical law is
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{W_{4+\varepsilon}(k)}{\sqrt\varepsilon}
=\frac{4\pi}{\sqrt3}\sum_{j=1}^{k}\frac1{2j-1}}.
\]
For every **fixed finite bandwidth** \(K\geq1\), there exists \(\varepsilon_K>0\) such that whenever \(4<q<4+\varepsilon_K\), the least nonzero modal gap among \(1\leq k\leq K\) is attained **uniquely** at degree one; its sharp constant has the limiting value \(4\pi/\sqrt3\) after division by \(\sqrt{q-4}\). This finite-band statement makes no assertion that degree one is the global nonzero maximizer for all harmonics at a common exponent.

The entire critical gap sequence is the spectrum of a canonical positive logarithmic quadratic form. For \(f\in L^2(\mathbb S^1)\), let \(P_k\) project onto the usual integer Fourier character \(e^{ik\theta}\), with \(k\in\mathbb Z\). On the domain
\[
\mathcal D=\left\{f:\sum_{k\in\mathbb Z}\log(2+|k|)\|P_k f\|_2^2<\infty\right\}
\]
put
\[
\mathcal Q(f)=\sum_{k\in\mathbb Z}D_{|k|}\|P_kf\|_2^2.
\]
Writing \(T_t=e^{-t|\partial_\theta|}\) for the circle Poisson semigroup, one has the exact representation
\[
\boxed{\mathcal Q(f)=\frac1{\pi^2}\int_0^\infty
\frac{e^{-t/2}}{1-e^{-t}}\bigl(\|f\|_2^2-\langle T_tf,f\rangle\bigr)\,dt.}
\]
Both sides may be \(+\infty\) for a general \(L^2\) function. The optimal critical Poincaré bound is
\[
\boxed{\mathcal Q(f)\geq\frac2{\pi^2}\|f-P_0f\|_2^2},
\]
with equality exactly when the Fourier support of \(f\) lies in degrees \(0,1,-1\). On trigonometric polynomials the form is also exactly the limit of the finite-mode spectral differences \(I_0(q)-I_{|k|}(q)\) applied diagonally.

## Assumptions and scope

All Bessel orders are integers and all radial integrals use \(r\,dr\). The divergence is canceled with a *common radial cutoff* before passing to infinity; no separate critical fourth moments are assigned finite values. The \(q\downarrow4\) limits fix the mode \(k\) first, and the finite-band assertion fixes \(K\). The circle carries unnormalized arclength \(d\theta\); the Fourier transform is \(\widehat{f\sigma}(x)=\int_{\mathbb S^1}e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega)\). The mixed norm is \(L^q((0,\infty),r\,dr;L^2(\mathbb S^1))\). The formula for \(W_q(k)\) is expressed in that normalization, and \(P_0\) is the projection onto constants. The full untruncated optimal stability coefficient at general \(q>4\) is not claimed here.

## Proof

**1. Exact boundary flux.** Fix \(j\geq1\) and abbreviate \(A=J_{j-1}(r)\), \(B=J_j(r)\), and \(U=A^2+B^2\). The standard Bessel differential recurrences give
\[
A'=\frac{j-1}{r}A-B,\qquad B'=A-\frac j r B,
\qquad U'=\frac2r\bigl((j-1)A^2-jB^2\bigr).
\]
Direct differentiation, with no sign assumptions on the Bessel functions, yields the exact identity
\[
\boxed{\left(\frac{r^2U(r)^2}{2}\right)'=(2j-1)r\bigl(J_{j-1}(r)^4-J_j(r)^4\bigr).}
\]
For \(j=1\), the Bessel series gives \(U(0)=1\); for \(j>1\), \(U(0)=0\). Either way \(r^2U(r)^2\to0\) at zero. The fixed-integer-order Hankel asymptotics imply
\[
J_m(r)=\sqrt{\frac2{\pi r}}\Bigl(\cos(r-\tfrac{m\pi}{2}-\tfrac\pi4)+O_m(r^{-1})\Bigr),
\]
so, for adjacent orders, \(U(r)=2/(\pi r)+O_j(r^{-2})\). Thus \(r^2U(r)^2/2\to2/\pi^2\) at infinity. Integration of the boxed derivative gives
\[
\int_0^\infty r\bigl(J_{j-1}^4-J_j^4\bigr)\,dr
=\frac2{\pi^2(2j-1)}.
\]
This is an **improper** integral of a sign-changing function; absolute convergence is not asserted. Telescoping at each finite cutoff and only then taking the limit proves the displayed formula for \(D_k\). Positivity, strict monotonicity, and the harmonic-number expression follow. Standard harmonic-number expansions give \(H_{2k}-H_k/2=(\log k)/2+\log2+\gamma/2+O(k^{-2})\).

**2. The critical limit of finite-exponent moments.** For fixed \(k\) and \(4\leq q\leq5\), the same fixed-order Hankel expansion gives, uniformly at large \(r\),
\[
|J_k(r)|^q r=\left(\frac2\pi\right)^{q/2}r^{1-q/2}
\bigl|\cos(r-\tfrac{k\pi}2-\tfrac\pi4)\bigr|^q
+O_k(r^{-q/2}).
\]
The bounded periodic function \(|\cos u|^q\) has mean \(m(q)=\pi^{-1}\int_0^\pi|\cos u|^qdu\). Its mean-zero remainder has a uniformly bounded periodic primitive for \(q\in[4,5]\), and integration by parts against the decreasing power \(r^{1-q/2}\) bounds its tail by \(O(R^{-1})\) uniformly in \(q\). The error term has an absolutely convergent tail, also uniformly. Since \(m(4)=3/8\), the nonoscillatory part is
\[
\left(\frac2\pi\right)^{q/2}m(q)\frac{R^{2-q/2}}{q/2-2}
=\frac3{\pi^2(q-4)}+O_R(1),
\]
which proves \(I_k(4+\varepsilon)=3/(\pi^2\varepsilon)+O_k(1)\). For the difference between orders \(0\) and \(k\), the two leading cosines have identical period averages. Subtract *before integrating* to cancel the singular mean term. The remaining oscillatory piece has uniformly bounded tails in the above integration-by-parts estimate, and the fixed-order remainder is absolutely integrable. Local dominated convergence then proves \(I_0(q)-I_k(q)\to D_k\).

**3. The square-root law and finite-band stability.** Elementary differentiation of the function \(s\mapsto s^{2/q}\), or the mean-value theorem, gives, for fixed \(k\),
\[
I_0(q)^{2/q}-I_k(q)^{2/q}
=\frac2q\bigl(I_0(q)-I_k(q)\bigr)\,\xi_{k,q}^{2/q-1},
\]
where \(\xi_{k,q}\) lies between the two moments. The preceding estimates give \(\varepsilon\xi_{k,4+\varepsilon}\to3/\pi^2\), hence the claimed value \((4\pi/\sqrt3)\sum_{j=1}^k(2j-1)^{-1}\) after multiplying by \((2\pi)^2\). For each fixed \(K\), the limit is strictly increasing with the mode. Finiteness of the index set makes this strict ordering persistent for all sufficiently small positive \(\varepsilon\). The Fourier–Bessel mode identity and Minkowski's inequality then establish the sharp finite-band deficit bound
\[
(2\pi)^2 I_0(q)^{2/q}\|f\|_2^2
-\|\widehat{f\sigma}\|_{L^q_{\mathrm{rad}}L^2_{\mathrm{ang}}}^2
\geq\min_{1\leq k\leq K}W_q(k)\|f-P_0f\|_2^2
\]
for \(f\) supported on angular Fourier degrees \(|k|\leq K\). A pure degree-one character attains the coefficient. This assertion uses no interchange of the limit with an unbounded index set.

**4. The logarithmic form and its sharp gap.** For integer \(k\geq1\), the elementary Laplace identity gives
\[
\sum_{j=1}^k\frac1{2j-1}
=\frac12\int_0^\infty\frac{e^{-t/2}(1-e^{-kt})}{1-e^{-t}}\,dt.
\]
Insert this into \(D_k\), apply Parseval, and use Tonelli's theorem for the nonnegative spectral summands to obtain the Poisson-semigroup formula. The harmonic-number asymptotic shows \(D_k\asymp\log(2+k)\) for \(k\geq1\), proving that the stated domain is exact. Because \(D_1=2/\pi^2\) and \(D_k>D_1\) for \(k\geq2\), the optimal Poincaré coefficient and every equality case follow immediately. Convergence of diagonal finite-band spectral forms to \(\mathcal Q\) holds for trigonometric polynomials, coefficient by coefficient; an unrestricted nonlinear endpoint convergence assertion is neither needed nor made.

## Verification

`CHECK.py` reproduces the Bessel-flux polynomial identity using symbolic algebra, tests 40 independent finite-radius Bessel quadrature identities against their exact boundary terms, verifies the harmonic-number and semigroup expressions, and probes the strict critical spectral Poincaré inequality for several finite Fourier polynomials. It uses Python, NumPy, SciPy and SymPy. These finite computations check formulas and normalization, not the infinite Hankel asymptotics, which are justified in the proof above. The limit and all equalities in the theorem are analytic arguments.

## Relationship to prior work

Xu, *Sharp radial--angular mixed norm Fourier extension and global stability on spheres* (first publicly posted October 14, 2026), proves for every admissible \(q>4\) that the zeroth Bessel mode dominates the others in dimension two, and expresses the optimal stability coefficient spectrally. Its §3.2 explicitly notes that the individual fourth moments diverge. Its equation (3.65) provides a related positive-power Bessel flux for the first three modes when the exponent is above the critical value; the recurrences used here are classical. The present result instead identifies the **nonvanishing boundary flux at the excluded critical exponent for every integer mode**, evaluates all differences exactly, and obtains the limiting logarithmic spectral form and sharp square-root coefficients. The exact current finite-band result is weaker than claiming a global nonzero-mode order for all \(q>4\); Xu explicitly leaves that global question open for the circle.

Carneiro, Oliveira e Silva and Sousa, *Sharp mixed norm spherical restriction* (2019), established the harmonic-mode reduction and normalization. Ciccone and Sousa, *Global and local maximizers for some Fourier extension estimates on the sphere* (2025), gave modal comparison regions but not this renormalized quartic hierarchy. Standard Bessel recurrences and Hankel expansions are classical, also recorded in the NIST Digital Library of Mathematical Functions. No novelty is claimed for those ingredients alone.

## Limitations

This is a circle, integer-order, matched-cutoff critical result. It does not define an endpoint mixed-norm extension inequality at \(q=4\), where individual modes diverge. The convergence \(I_0(q)-I_k(q)\to D_k\) is for a **fixed** degree, not uniformly over all degrees. The first-degree stability result is only for each separately fixed finite bandwidth \(K\); the unrestricted optimal nonzero mode for all \(q\) near four is not determined. The logarithmic form is a diagonal renormalized spectral object, not a claimed unconditional nonlinear extension limit for arbitrary \(L^2\) input. Its derivation shares a flux ingredient with the motivating paper, so possible previously indexed or unindexed endpoint evaluations remain an originality risk. Independent mathematical validation has not been performed.

## References

1. Z. Xu, *Sharp radial--angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648 (first version, 2026-10-14), https://arxiv.org/abs/2610.19648 . Especially Theorems 1.2--1.3, §3.2, Eq. (3.65), and Remark 3.
2. E. Carneiro, D. Oliveira e Silva, M. Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365 (2019), https://arxiv.org/abs/1710.10365 . Especially Theorem 1 and the Fourier--Bessel decomposition.
3. V. Ciccone and M. Sousa, *Global and local maximizers for some Fourier extension estimates on the sphere*, Journal of Fourier Analysis and Applications **31** (2025), article 70, https://doi.org/10.1007/s00041-025-10201-7 .
4. NIST Digital Library of Mathematical Functions, Chapter 10, §§10.6, 10.17, 10.22, https://dlmf.nist.gov/10 .
