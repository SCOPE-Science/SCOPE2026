# Exact two-scale exponential covariance domination on the two-sphere

## Finding
Let \(\mathbb S^2\) be the unit sphere with angular distance \(\theta(x,y)=\arccos(x\cdot y)\). For arbitrary \(a,b>0\) and \(\lambda\in\mathbb R\), the isotropic kernel
\[
K_{a,b,\lambda}(x,y)=e^{-a\theta(x,y)}-\lambda e^{-b\theta(x,y)}
\]
is positive semidefinite for every finite set of spherical sites exactly when \(\lambda\le\Lambda(a,b)\), with
\[
\Lambda(a,b)=\begin{cases}
\displaystyle\frac{(1+e^{-\pi a})(b^2+1)}{(1+e^{-\pi b})(a^2+1)},&a>b,\\[6pt]
\displaystyle\frac{a(1-e^{-\pi a})}{b(1-e^{-\pi b})},&a<b,\\[6pt]
1,&a=b.
\end{cases}
\]
When \(a\ne b\), this kernel remains **strictly positive definite** at \(\lambda=\Lambda(a,b)\). At \(a=b\), it is strictly positive definite exactly when \(\lambda<1\), and is identically zero at \(\lambda=1\). For \(a>b\) the sharp obstruction is spherical-harmonic degree zero. For \(a<b\) it is a limit of even degrees tending to infinity; no finite-degree coefficient vanishes at the sharp boundary.

## Assumptions and scope
Positive semidefiniteness means that \(\sum_{i,j=1}^N c_i\overline{c_j} K(x_i,x_j)\ge0\) for all \(N\ge1\), all \(x_i\in\mathbb S^2\), and complex \(c_i\). Strict positive definiteness means strict inequality for every nonzero coefficient vector attached to pairwise distinct points. The parameters \(a,b\) are arbitrary *positive* real numbers, while \(\lambda\) may be any real number. The result concerns the geodesic metric on the two-sphere only; it does not claim the same bound in other dimensions or in Euclidean distance.

## Proof
Write \(P_n\) for the ordinary Legendre polynomial normalized by \(P_n(1)=1\), and define for \(c>0\)
\[
I_n(c)=\int_0^\pi e^{-ct}P_n(\cos t)\sin t\,dt,\qquad n\in\{0,1,\ldots\}.
\]
The degree-\(n\) Schoenberg coefficient of \(e^{-c\theta}\) is \((2n+1)I_n(c)/2\). The Schoenberg criterion therefore gives positivity exactly when \(I_n(a)-\lambda I_n(b)\ge0\) for **every** integer \(n\ge0\).

**An exact two-step recurrence.** Put \(g_n(t)=\sin t\,P_n(\cos t)\). The standard Legendre identities
\[
(2n+3)P_{n+1}(u)=P'_{n+2}(u)-P'_n(u),\qquad
(2n+3)uP_{n+1}(u)=(n+2)P_{n+2}(u)+(n+1)P_n(u)
\]
imply on differentiating \(g_n\) that
\[
g_{n+2}''(t)+(n+3)^2g_{n+2}(t)=g_n''(t)+n^2g_n(t).
\]
The endpoint values are \(g_n(0)=g_n(\pi)=0\), \(g_n'(0)=1\), and \(g_n'(\pi)=(-1)^{n+1}\). Integrating twice by parts gives
\[
\int_0^\pi e^{-ct}g_n''(t)\,dt
=c^2I_n(c)-1-(-1)^n e^{-\pi c}.
\]
Since the latter boundary term is the same for indices \(n\) and \(n+2\), the identity above yields
\[
\boxed{I_{n+2}(c)=\frac{c^2+n^2}{c^2+(n+3)^2}I_n(c).}
\]
Direct integration gives the strictly positive bases
\[
I_0(c)=\frac{1+e^{-\pi c}}{1+c^2},\qquad I_1(c)=\frac{1-e^{-\pi c}}{4+c^2}.
\]
Thus **all** Legendre coefficients are strictly positive for each individual exponential.

**Monotonicity of the two-scale ratio.** Put \(R_n=I_n(a)/I_n(b)\). The recurrence implies
\[
\frac{R_{n+2}}{R_n}-1
=\frac{(a^2-b^2)\bigl((n+3)^2-n^2\bigr)}{(b^2+n^2)(a^2+(n+3)^2)}.
\]
Therefore both parity subsequences of \(R_n\) increase strictly when \(a>b\) and decrease strictly when \(a<b\). If \(a>b\), direct comparison of the two base expressions yields \(R_0<R_1\): indeed \((1+e^{-\pi a})/(1+e^{-\pi b})<1\), whereas \((1-e^{-\pi a})/(1-e^{-\pi b})>1\), and \((b^2+1)/(a^2+1)<(b^2+4)/(a^2+4)\). Hence \(\inf_{n\ge0}R_n=R_0\), and equality is realized only at degree zero.

**The large-degree boundary.** Iterating the recurrence gives the exact products
\[
I_{2m}(c)=(1+e^{-\pi c})\frac{\prod_{j=0}^{m-1}(c^2+4j^2)}{\prod_{j=0}^{m}(c^2+(2j+1)^2)},
\]
\[
I_{2m+1}(c)=(1-e^{-\pi c})\frac{\prod_{j=0}^{m-1}(c^2+(2j+1)^2)}{\prod_{j=1}^{m+1}(c^2+4j^2)}.
\]
Using the Wallis product and the standard Euler products
\[
\prod_{j=1}^{\infty}\left(1+\frac{c^2}{4j^2}\right)=\frac{\sinh(\pi c/2)}{\pi c/2},\qquad
\prod_{j=0}^{\infty}\left(1+\frac{c^2}{(2j+1)^2}\right)=\cosh(\pi c/2),
\]
one obtains the fully normalized endpoint asymptotics
\[
\lim_{m\to\infty}(2m)^3I_{2m}(c)=c(1-e^{-\pi c}),\qquad
\lim_{m\to\infty}(2m+1)^3I_{2m+1}(c)=c(1+e^{-\pi c}).
\]
In particular, when \(a<b\), the even limiting ratio \(a(1-e^{-\pi a})/[b(1-e^{-\pi b})]\) is strictly smaller than the odd limiting ratio \(a(1+e^{-\pi a})/[b(1+e^{-\pi b})]\). Both parity sequences strictly decrease, so the former is \(\inf_{n\ge0}R_n\) but no finite \(R_n\) attains this infimum.

Finally, the Schoenberg criterion reduces the complete parameter problem to \(\lambda\le\inf_{n\ge0}R_n\), producing the displayed formulas and converses. The standard strict-positive-definiteness criterion on \(\mathbb S^2\) applies because both even and odd indices have infinitely many **strictly positive** Schoenberg coefficients, even at either sharp boundary for \(a\ne b\). If \(a=b\), the kernel is \((1-\lambda)e^{-a\theta}\), giving the stated degeneracy at equality. No finite experiment is used to establish the infinite sign conditions.

## Verification
A standalone `check.py` evaluates the original defining Legendre integrals at \(45\)-digit precision and compares them against the analytic recurrence for three positive scales and degrees \(0\) through \(11\). The largest absolute discrepancy obtained was approximately \(5.48\times10^{-48}\). It also checks the formula against the first \(30\) coefficient ratios for two parameter pairs in the opposite order regimes. These tests are **supplementary checks**; the full assertion follows from the recurrence, monotonicity, Euler-product limits, and exact Schoenberg criterion above. To reproduce, install Python and `mpmath`, then execute `python check.py` beside this file.

## Relationship to prior work
Gneiting (arXiv:1111.7077, originally public 2011-11-30) documents Schoenberg's spectral characterization and positivity of individual geodesic exponential kernels across spheres. Fiedler (arXiv:1303.6856) provides relations among Schoenberg coefficients across dimensions. Feragen, Lauze and Hauberg (arXiv:1411.0296) discuss geodesic exponential kernels and geometric constraints. The exact **signed comparison of two distinct geodesic exponential scales on \(\mathbb S^2\)**, including its low-frequency versus high-even-frequency transition and endpoint strictness, is not implied by positivity of each exponential separately. A bounded source and indexed-record comparison did not identify this exact three-parameter criterion; this is not a proof of priority or exhaustive uniqueness.

## Limitations
The result is restricted to \(\mathbb S^2\), positive scales, and real signed coefficient \(\lambda\). It does not provide the corresponding parameter regions for \(\mathbb S^d\) with \(d\ne2\), nor certify priority against every unindexed or inaccessible publication. The verification code samples finitely many coefficients and is not a replacement for the infinite analytic proof. No independent scientific audit has been performed.

## References
Gneiting, T., *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077 (first posted 2011-11-30), https://arxiv.org/abs/1111.7077.

Fiedler, J., *From Fourier to Gegenbauer: Dimension walks on spheres*, arXiv:1303.6856 (first posted 2013-03-27), https://arxiv.org/abs/1303.6856.

Feragen, A., Lauze, F., and Hauberg, S., *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296 (first posted 2014-11-02), https://arxiv.org/abs/1411.0296.
