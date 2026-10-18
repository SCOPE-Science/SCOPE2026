# A sharp small-aperture correction for three-mode least-squares projection

## Finding
Let \(0<h<\pi\), let \(\mu_h(dt)=dt/(2h)\) on \([-h,h]\), and let \(P_h\) be the \(L^2(\mu_h)\)-orthogonal projection onto the three-dimensional real (or complex) space \(\operatorname{span}\{1,\cos t,\sin t\}\). The same operator acts on \(L^1(\mu_h)\) and \(L^\infty(\mu_h)\) through its bounded integral kernel. There exists \(h_0>0\) such that for every \(0<h<h_0\) its pointwise Lebesgue function has precisely two global maximizers, at \(t=\pm h\), and
\[
\boxed{\|P_h\|_{L^1\to L^1}=\|P_h\|_{L^\infty\to L^\infty}=1+\frac{12\sqrt6}{25}-\frac{387\sqrt6}{21875}h^2+O(h^4).}
\]
The coefficient of \(h^2\) is strictly negative. The leading term is the endpoint Lebesgue constant for quadratic Legendre least-squares projection on \([-1,1]\); the nonzero second term measures the first departure of the three-mode curved trigonometric space from that polynomial model.

## Assumptions and scope
The interval is symmetric, the measure is uniform and normalized, and the projection has exactly the three modes \(1,\cos t,\sin t\). The aperture \(h\) tends to zero while the approximation-space dimension stays fixed. The endpoint statement holds for all sufficiently small positive \(h\), without a numerical claim about the maximal admissible \(h_0\). No assertion is made about higher Fourier bandwidth, asymmetric arcs, or discrete least squares.

## Proof
Write \(x=t/h\) and \(y=s/h\), with \(x,y\in[-1,1]\). Define
\[
 a_h=\frac{\sin h}{h},\qquad
 b_h=\frac12+\frac{\sin(2h)}{4h},\qquad
 c_h=\frac12-\frac{\sin(2h)}{4h}.
\]
Orthogonality of the constant, centered cosine, and sine gives the exact reproducing kernel relative to \(dy/2\):
\[
 K_h(x,y)=1+\frac{(\cos(hx)-a_h)(\cos(hy)-a_h)}{b_h-a_h^2}
 +\frac{\sin(hx)\sin(hy)}{c_h}.
\]
For \(h>0\) sufficiently small, both denominators are positive because the three generators are linearly independent. This symmetric real kernel defines the projection on either endpoint space. Its Lebesgue function is \(\Lambda_h(x)=\frac12\int_{-1}^1|K_h(x,y)|\,dy\), so the \(L^\infty\) norm is \(\max_x\Lambda_h(x)\). Symmetry of the kernel and duality give the same \(L^1\) norm.

Taylor expansion after cancellation of the apparent zero denominators is uniform with all fixed derivatives on the compact square. Its leading kernel is
\[
 K_0(x,y)=1+3xy+\frac54(3x^2-1)(3y^2-1),
\]
namely the degree-two Legendre reproducing kernel with normalized uniform measure. At \(x=1\),
\[
 K_0(1,y)=\frac32(5y^2+2y-1),\quad
 r_{\pm}=\frac{-1\pm\sqrt6}{5}.
\]
The kernel is negative precisely between \(r_-\) and \(r_+\). Its mean is one; therefore
\[
 \Lambda_0(1)=1-\int_{r_-}^{r_+}K_0(1,y)\,dy
 =1+\frac{12\sqrt6}{25}=:L_*.
\]

We now prove that \(x=\pm1\) are the only maximizers of \(\Lambda_0\), with a strict separation away from the ends. By Cauchy--Schwarz and the reproducing identity,
\[
 \Lambda_0(x)\le\sqrt{K_0(x,x)},\qquad
 K_0(x,x)=\frac94-\frac92x^2+\frac{45}{4}x^4.
\]
On \(0\le x\le21/25\), the diagonal maximum is attained at \(x=0\) or \(x=21/25\), and elementary substitution gives \(\sqrt{K_0(x,x)}<L_*\) throughout. For \(21/25\le x\le1\), the quadratic \(K_0(x,\cdot)\) is positive at \(y=\pm1\) and has two simple roots \(u_-(x)<0<u_+(x)\) in \((-1,1)\). Write their midpoint and half-width as
\[
 m(x)=-\frac{2x}{5(3x^2-1)},\qquad
 d(x)=\frac{\sqrt{3(25x^4-22x^2+5)}}{5(3x^2-1)}.
\]
Because the kernel integrates to one, differentiation of its negative-region formula cancels the moving-root boundary terms and yields
\[
 \Lambda_0'(x)=-2d(x)\left[3m(x)+\frac{15x}{2}(3m(x)^2+d(x)^2-1)\right].
\]
Direct simplification makes the bracket
\[
 -\frac{9x(5x^2-2x-1)(5x^2+2x-1)}{5(3x^2-1)^2}<0
\]
throughout \([21/25,1]\). Thus \(\Lambda_0\) increases strictly there. By reflection, its only maximizers are \(\pm1\).

These statements persist for sufficiently small positive \(h\). On the central closed interval, the strict Cauchy--Schwarz margin survives uniform convergence of \(K_h(x,x)\) to \(K_0(x,x)\), while \(\Lambda_h(1)\to L_*\). On the end interval, the two negative-region roots are simple, lie uniformly inside \((-1,1)\), and depend smoothly on \((h,x)\). The first \(x\)-derivative of the corresponding absolute kernel integral consequently converges uniformly to \(\Lambda_0'(x)>0\). By reflection \(\Lambda_h(-x)=\Lambda_h(x)\), so exactly \(\pm1\) maximize for all \(0<h<h_0\).

For the sharp correction, direct expansion of the exact kernel at its maximizing point gives uniformly for \(y\in[-1,1]\)
\[
 K_h(1,y)=\frac32(5y^2+2y-1)
 -\frac{h^2}{280}(175y^4+140y^3-90y^2-28y-5)+O(h^4).
\]
The two simple roots of the first term move by \(O(h^2)\); their motion makes no contribution at order \(h^2\) because the integrand vanishes at the roots. Also \(\frac12\int_{-1}^1K_h(1,y)\,dy=1\) exactly. Consequently,
\[
 \Lambda_h(1)=L_*+\frac{h^2}{280}\int_{r_-}^{r_+}(175y^4+140y^3-90y^2-28y-5)\,dy+O(h^4)
 =L_*-\frac{387\sqrt6}{21875}h^2+O(h^4).
\]
Even analyticity in \(h\), together with smooth simple-root dependence, supplies the fourth-order remainder. This proves the assertion.

## Verification
The reproducible checker `verification/check_arc.py` performs exact symbolic checks for the limiting kernel, both roots, the two coefficients, and the sign-derivative identity; it independently expands the actual trigonometric Gram kernel through the quadratic term. It also evaluates the two negative-region zeros and the absolute kernel integral to high precision for five nonzero apertures. In the current test, all 25 assertions passed, and the sampled fourth-order normalized residual converged numerically toward approximately \(-0.003010\). These are consistency checks, not substitutes for the uniform analytic arguments and exact integrals above.

## Relationship to prior work
The continuous three-mode projector is the fixed-bandwidth case of Fourier-extension least squares. Huybrechs (2010) develops the polynomial transformation and convergence theory; Adcock--Huybrechs--Martín-Vaquero (2012) studies numerical stability and the finite Fourier-extension Gram matrix; Webb--Coppé--Huybrechs (2018) gives a general prolate-kernel representation and asymptotic Lebesgue-function bounds as the bandwidth grows with extension length fixed. The present result instead fixes three modes and shrinks the physical interval, identifies the exact global endpoint optimizer in that regime, and computes its explicit nonzero second-order norm defect. The classical degree-two Legendre kernel provides the limiting term, not the correction term.

## Limitations
The first permissible aperture \(h_0\) is not optimized or explicitly certified. The sign of the correction only implies strict reduction relative to the limiting value locally, not monotonicity for all apertures. The literature comparison did not uncover an equivalent sharp correction, but general kernel identities and older Fourier-extension treatments remain plausible routes by which it could previously have been derived; independent historical-priority assessment is outstanding. There is no claim of independent certification.

## References
- D. Huybrechs, *On the Fourier Extension of Nonperiodic Functions*, SIAM J. Numer. Anal. 47 (2010), 4326--4355, DOI:10.1137/090752456. Public author-hosted full text: https://people.cs.kuleuven.be/~daan.huybrechs/research/sinum_fourierextension.pdf .
- B. Adcock, D. Huybrechs, J. Martín-Vaquero, *On the numerical stability of Fourier extensions*, arXiv:1206.4111 (first submitted 2012-06-19), https://arxiv.org/abs/1206.4111 .
- M. Webb, V. Coppé, D. Huybrechs, *Pointwise and uniform convergence of Fourier extensions*, arXiv:1811.09527 (first submitted 2018-11-23), https://arxiv.org/abs/1811.09527 .
