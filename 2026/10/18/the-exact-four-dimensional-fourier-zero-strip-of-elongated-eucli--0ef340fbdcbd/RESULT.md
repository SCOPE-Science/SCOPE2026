# The exact four-dimensional Fourier-zero strip of elongated Euclidean bipyramids

## Finding
Let
\[
\Omega_{\alpha,4}=\{(x,y)\in\mathbb R\times\mathbb R^3:|x|+\alpha\|y\|_2<1\},\qquad \alpha>0,
\]
and let \(\kappa(\Omega)\) be the Euclidean distance to the nearest real zero of the Fourier transform of the indicator of \(\Omega\). Write \(u\in\mathbb R\) for the axial Fourier coordinate and \(s=\|\eta\|_2/\alpha\) for the rescaled transverse Fourier radius.

**Theorem.** The four-dimensional bipyramid Fourier transform is strictly positive for all \(u\in\mathbb R\) and \(0\le s<\pi\). At the sharp boundary \(s=\pi\), its zeros are exactly
\[
(u,s)=(\pm(2k+1)\pi,\pi),\qquad k=1,2,3,\ldots .
\]
Consequently, for every \(\alpha>0\),
\[
\boxed{\ \pi\alpha<\kappa(\Omega_{\alpha,4})<\pi\sqrt{\alpha^2+9}\ },
\]
and the exact leading slope, previously defined only by an infimum over a two-variable zero set, is
\[
\boxed{\ \lim_{\alpha\to\infty}\kappa(\Omega_{\alpha,4})/\alpha=\pi\ }.
\]
More precisely, as \(\alpha\to\infty\),
\[
\boxed{\ \kappa(\Omega_{\alpha,4})^2
=\pi^2\alpha^2+9\pi^2-\frac{36\pi^2}{\alpha^2}+O(\alpha^{-4})\ }.
\]
Up to reflection of the axial coordinate and arbitrary direction of the transverse vector, a nearest zero has frequencies
\[
|u_\alpha|=3\pi-\frac{12\pi}{\alpha^2}+O(\alpha^{-4}),
\qquad
\frac{\|\eta_\alpha\|_2}{\alpha}=\pi+\frac{18\pi}{\alpha^4}+O(\alpha^{-6}).
\]
The positive-axis nearest-zero branch is uniquely determined for all sufficiently large \(\alpha\).

An explicit sufficient equal-volume-ball counterexample threshold follows:
\[
\kappa(\Omega_{\alpha,4})>\kappa(\Omega_{\alpha,4}^*)
\quad\text{whenever}\quad
\alpha>\frac{3j_{2,1}^4}{4\pi^3}=16.826118761\ldots,
\]
where \(j_{2,1}\) is the first positive zero of the Bessel function \(J_2\) and \(\Omega_{\alpha,4}^*\) is the equal-volume Euclidean ball. The stated threshold is sufficient, not claimed necessary.

## Assumptions and scope
The body is the four-dimensional *solid* double cone with Euclidean three-ball cross sections, with arbitrary real \(\alpha>0\). Use the Fourier convention
\[
\widehat{\chi_\Omega}(\xi)=\int_\Omega e^{i\langle\xi,z\rangle}\,dz,
\qquad
\kappa(\Omega)=\min\{\|\xi\|_2:\widehat{\chi_\Omega}(\xi)=0,\ \xi\in\mathbb R^4\}.
\]
The real zero set is nonempty by the elementary nonemptiness result for centrally symmetric bodies of positive finite volume (see the motivating source, Proposition 1.1), is closed, and its distance to the origin is attained. All statements concern real Fourier zeros, not complex zeros.

## Proof
**1. Exact Fourier profile and removable resonances.** Integrate each three-ball transverse section using the elementary radial transform
\[
\int_{\|y\|\le r} e^{i\eta\cdot y}\,dy
=\frac{4\pi}{\|\eta\|^3}
\bigl(\sin(r\|\eta\|)-r\|\eta\|\cos(r\|\eta\|)\bigr).
\]
After \(x\mapsto|x|\) and \(s=\|\eta\|/\alpha\), the Fourier transform for \(s>0\) equals \(8\pi\alpha^{-3}s^{-3}F(u,s)\), where
\[
F(u,s)=\int_0^1\cos(ux)
\bigl(\sin(s(1-x))-s(1-x)\cos(s(1-x))\bigr)\,dx.
\]
Elementary integration, valid away from \(u=\pm s\), gives
\[
F(u,s)=\frac{s^2N(u,s)}{(s^2-u^2)^2},\quad
N(u,s)=(u^2-s^2)\sin s+2s(\cos u-\cos s).
\tag{1}
\]
At the removable resonances \(u=\pm s\), direct integration or taking the limit gives
\[
F(\pm s,s)=\frac{\sin s-s\cos s}{4}.
\tag{2}
\]
The expression in (2) is strictly positive for \(0<s\le\pi\), since \(s\mapsto\sin s-s\cos s\) has derivative \(s\sin s>0\) on \((0,\pi)\) and is \(\pi\) at the endpoint. At \(s=0\), the Fourier transform is a positive constant times
\[
I_3(u)=\int_0^1(1-x)^3\cos(ux)\,dx
=\frac{3\bigl(u^2+2\cos u-2\bigr)}{u^4}\quad(u\ne0),
\]
with \(I_3(0)=1/4\). Because \(u^2>4\sin^2(u/2)\) for \(u\ne0\), this is strictly positive.

**2. Sharp all-axial-frequency positivity.** On \([0,\pi^2]\), put \(h(t)=\cos\sqrt t\). Its derivatives for \(t>0\), with \(z=\sqrt t\), are
\[
h'(t)=-\frac{\sin z}{2z},\qquad
h''(t)=\frac{\sin z-z\cos z}{4z^3}>0\quad(0<z<\pi).
\]
The last inequality follows by differentiation of \(\sin z-z\cos z\), whose derivative \(z\sin z\) is positive. Fix \(0<s<\pi\) and let \(\ell_s(t)\) be the tangent line to \(h\) at \(t=s^2\). Strict convexity gives \(h(t)>\ell_s(t)\) for \(0\le t\le\pi^2\), \(t\ne s^2\). For \(t>\pi^2\), because \(h'(s^2)<0\) and \(\ell_s(\pi^2)<h(\pi^2)=-1\), one has \(\ell_s(t)<-1\le h(t)\). Thus \(h(t)>\ell_s(t)\) for all \(t\ge0\), \(t\ne s^2\).

The numerator in (1) is exactly the tangent-line deficit:
\[
N(u,s)=2s\bigl(h(u^2)-\ell_s(u^2)\bigr).
\]
It follows that \(F(u,s)>0\) for every \(u\ne\pm s\) and \(0<s<\pi\); the remaining resonances and \(s=0\) were covered in step 1. For \(s=\pi\), the numerator becomes \(N(u,\pi)=2\pi(1+\cos u)\). Hence its zeros away from resonances occur exactly at the odd multiples of \(\pi\). The apparent points \(u=\pm\pi\) are *not* zeros, because (2) gives \(F(\pm\pi,\pi)=\pi/4>0\). The first actual boundary zeros are therefore \(u=\pm3\pi\), establishing sharpness of the strip and identifying the least transverse zero radius as \(\pi\).

**3. Bounds, limiting slope and strict finite-parameter upper bound.** Every real Fourier zero has \(s\ge\pi\), and a zero at \((u,s)=(3\pi,\pi)\) exists. Hence
\[
\pi\alpha\le\kappa(\Omega_{\alpha,4})\le\pi\sqrt{\alpha^2+9}.
\tag{3}
\]
The first inequality is strict for any finite \(\alpha\): an equality-achieving zero would have both \(s=\pi\) and \(u=0\), but \(F(0,\pi)>0\). Dividing (3) by \(\alpha\) proves the limiting slope. To see the upper inequality is strict, use the local zero curve described in step 4: moving \(u\) slightly left of \(3\pi\) changes \(u^2\) linearly downward and \(s^2\) only quadratically upward. Thus a nearby actual zero has smaller squared norm than \(\pi^2(\alpha^2+9)\), for every fixed finite \(\alpha\).

**4. The nearest-zero asymptotics.** The first derivatives of \(N\) at \((u_0,s_0)=(3\pi,\pi)\) obey
\[
N(u_0,s_0)=0,\quad N_u(u_0,s_0)=0,\quad
N_s(u_0,s_0)=-8\pi^2,\quad N_{uu}(u_0,s_0)=2\pi.
\]
The analytic implicit-function theorem therefore supplies the unique local zero curve \(s=\sigma(u)\), with
\[
\sigma(3\pi)=\pi,\quad\sigma'(3\pi)=0,\quad
\sigma''(3\pi)=\frac1{4\pi},
\]
and so
\[
\sigma(u)=\pi+\frac{(u-3\pi)^2}{8\pi}+O((u-3\pi)^3).
\tag{4}
\]
Take an arbitrary nearest zero of \(\Omega_{\alpha,4}\). The bound (3) forces \(|u|\le3\pi\), \(\pi\le s\le\pi\sqrt{1+9/\alpha^2}\). Therefore any subsequential limit as \(\alpha\to\infty\) has \(s=\pi\), \(|u|\le3\pi\), and \(F(u,\pi)=0\). Step 2 forces \(u=\pm3\pi\). By evenness we may assume \(u>0\); the nearest zero must then lie on (4) for all sufficiently large \(\alpha\).

Put \(\varepsilon=\alpha^{-2}\). Minimizing the squared norm along the curve is equivalent to minimizing \(\sigma(u)^2+\varepsilon u^2\). Its derivative is \(2\sigma\sigma'+2\varepsilon u\), with strictly positive second derivative near \((u,\varepsilon)=(3\pi,0)\), because \(2\sigma(3\pi)\sigma''(3\pi)=1/2\). Hence its unique local, and thereby positive-axis global, minimum is analytic in \(\varepsilon\) and satisfies
\[
u_\alpha=3\pi-12\pi\varepsilon+O(\varepsilon^2),\qquad
s_\alpha=\sigma(u_\alpha)=\pi+18\pi\varepsilon^2+O(\varepsilon^3).
\]
Substituting in \(u_\alpha^2+\alpha^2s_\alpha^2\) gives
\[
\kappa(\Omega_{\alpha,4})^2
=\pi^2\alpha^2+9\pi^2-36\pi^2\alpha^{-2}+O(\alpha^{-4}).
\]
The negative-axis minimizing branch follows by symmetry, and transverse directions are arbitrary owing to rotational invariance in \(\mathbb R^3\).

**5. The explicit equal-volume-ball threshold.** Since \(\operatorname{vol}_4(\Omega_{\alpha,4})=2\pi/(3\alpha^3)\), the equal-volume ball has Fourier-zero distance
\[
\kappa(\Omega_{\alpha,4}^*)
=j_{2,1}\left(\frac{3\pi}{4}\right)^{1/4}\alpha^{3/4}.
\]
The strict inequality \(\kappa(\Omega_{\alpha,4})>\pi\alpha\) and elementary rearrangement establish the displayed sufficient threshold \(3j_{2,1}^4/(4\pi^3)\). No assertion about its necessity is made.

## Verification
The standalone `checks/fourier4_checker.py` symbolically verifies the closed integral (1), both resonance values, and the implicit derivatives at \((3\pi,\pi)\). It compares 35 positive cosine-transform integrals with quadrature and evaluates three large-parameter stationary zeros as independent numerical cross-checks. Execute it with Python 3, SymPy and mpmath installed:

`python checks/fourier4_checker.py`

The all-frequency positivity theorem and nearest-zero expansion are proved analytically above. Finite quadrature samples do not prove a uniform zero-free strip or global minimality.

## Relationship to prior work
Gómez-Serrano, Levitin, Platt and Polterovich introduced these elongated Euclidean bipyramids and proved a positive but unspecified transverse zero-free strip in every dimension at least three. Their source gives a linear lower bound, not the sharp four-dimensional strip or a second-order nearest-zero expansion.

The published note *A Pólya–Bessel zero-free strip for Fourier bipyramids* proves an explicit lower bound in every dimension involving the first zero of a Bessel combination. Its four-dimensional constant is strictly below \(\pi\): the relevant convexity mechanism changes sign before \(\pi\). It does not locate a Fourier zero at the strip boundary or establish sharpness.

The published *Exact leading slope of Fourier-zero distance for elongated bipyramids* proves in every dimension that the slope equals an infimum over the fixed rescaled zero set, but explicitly does **not** calculate that infimum or establish its attainment. Here the previously unresolved four-dimensional coefficient is evaluated as \(\pi\), the boundary zeros are classified, and the next asymptotic term is computed. A separate published dimension-three certified strip of width two concerns a different transverse dimension and gives no implication for this result.

## Limitations
The exact strip and expansion are specific to four-dimensional Euclidean bipyramids. The finite-\(\alpha\) global nearest-zero location is not classified for every parameter, though its large-\(\alpha\) position is determined. The equal-volume-ball threshold is sufficient and may be nonoptimal. The literature comparison includes the original manuscript and the closest accessible published records; older unindexed accounts of four-dimensional cone Fourier transforms could still contain an equivalent identity or implication.

## References
1. J. Gómez-Serrano, M. Levitin, D. Platt, I. Polterovich, *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, arXiv:2609.10517v1, September 9, 2026, especially §2. https://arxiv.org/pdf/2609.10517
2. *A Pólya–Bessel zero-free strip for Fourier bipyramids*, published research record 2026/9/18/SCOPE-polya-bessel-zero-free-strip-for-fourier-bipyramids--72c1da0f9bb0, https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-polya-bessel-zero-free-strip-for-fourier-bipyramids--72c1da0f9bb0
3. *Exact leading slope of Fourier-zero distance for elongated bipyramids*, published research record 2026/10/11/SCOPE-exact-leading-slope-of-fourier-zero-distance-for-elongated-bipyr--328d6e388fdc, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-leading-slope-of-fourier-zero-distance-for-elongated-bipyr--328d6e388fdc
4. *A rationally certified width-two Fourier zero-free strip for three-dimensional bipyramids*, published research record 2026/10/11/SCOPE-a-rationally-certified-width-two-fourier-zero-free-strip-for-thr--7d5ef01cc46e, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-rationally-certified-width-two-fourier-zero-free-strip-for-thr--7d5ef01cc46e
