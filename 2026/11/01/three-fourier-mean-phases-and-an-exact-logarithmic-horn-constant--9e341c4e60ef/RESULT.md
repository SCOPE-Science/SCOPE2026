# Three Fourier-mean phases and an exact logarithmic horn constant for the quartic disk

## Finding

Let \(K=\{(x,y)\in\mathbb R^2:x^4+y^4\le1\}\). Adopt the unnormalised Fourier transform \(\widehat{\mathbf1_K}(\xi)=\int_K e^{-i\langle x,\xi\rangle}\,dx\) and the Fourier \(p\)-mean radial function introduced by Langharst, Manui and Zvavitch:
\[
\rho_p(u)^p=\frac{p}{|K|}\int_0^\infty |\widehat{\mathbf1_K}(tu)|^2t^{p-1}\,dt,
\qquad u\in S^1,\quad p>0.
\]
The integral is permitted to be infinite. Put \(F_pK=\{ru:u\in S^1,0\le r\le\rho_p(u)\}\), interpreting infinite radii as complete rays.

The phase classification is exact:

1. For \(0<p<5/2\), \(F_pK\) is a compact origin-symmetric star body with continuous positive radial function.
2. For \(5/2\le p<3\), it has **infinite radius exactly in the four coordinate directions**, finite radius in all other directions, and **finite planar area** despite being unbounded.
3. For \(p\ge3\), its radius is infinite in every direction, and \(F_pK=\mathbb R^2\).

In particular the Fourier index of this strictly convex, non-\(C^2_+\) body is exactly \(5/2\), strictly between the cube's value \(2\) and the positive-curvature value \(3\). Moreover, the axial divergence has the exact residue
\[
\lim_{p\uparrow5/2}(5/2-p)\rho_p(e_1)^p=5\sqrt\pi.
\]
At the critical exponent, write \(u_\theta=(\cos\theta,\sin\theta)\). Its angular horn has the sharp coefficient
\[
\boxed{\lim_{\theta\to0}\frac{\rho_{5/2}(u_\theta)^{5/2}}{\log(1/|\theta|)}=\frac{20\sqrt\pi}{3}.}
\]
The identical angular law holds at the other three coordinate directions by symmetry. These statements concern the same phase classification and its two quantitative boundary laws, not separate accepted claims.

## Assumptions and scope

All Fourier transforms and integrals use Lebesgue measure, the exponential \(e^{-i\langle x,\xi\rangle}\), and no \(2\pi\) prefactor. The convex body \(K\) is the fixed unit quartic disk, not an arbitrary \(\ell_4\)-affine image unless transformed according to the Fourier-mean covariance. The parameter ranges are exact and include the stated boundary values. At an infinite radial direction, \(F_pK\) is a set rather than a compact star body. Area means two-dimensional Lebesgue measure; an unbounded set can have finite area. No smooth-positively-curved assertion is applied at the four flat points.

## Proof

**1. Axis Fourier asymptotic and its coefficient.** A vertical chord of \(K\) at \(x\in[-1,1]\) has length \(2(1-x^4)^{1/4}\), so
\[
H(t):=\widehat{\mathbf1_K}(t e_1)
=4\int_0^1(1-x^4)^{1/4}\cos(tx)\,dx.
\]
Near \(x=1\), \((1-x^4)^{1/4}=\sqrt2(1-x)^{1/4}(1+O(1-x))\). At \(x=0\) the amplitude extends as an even smooth function, so a smooth cutoff removes that endpoint without leaving an algebraic cosine-transform term. Watson's oscillatory endpoint lemma, obtained by damping and scaling \(s=t(1-x)\), gives
\[
H(t)=4\sqrt2\,\Gamma(5/4)t^{-5/4}\cos(t-5\pi/8)+O(t^{-9/4}). \tag{1}
\]
This estimate can also be checked directly by one integration by parts followed by the standard fractional-power oscillatory integral \(\int_0^\infty s^{1/4}e^{is}\,ds=e^{5\pi i/8}\Gamma(5/4)\), interpreted by Abel damping.

Set \(C=4\sqrt2\,\Gamma(5/4)\). Euler's beta integral gives
\[
|K|=4\frac{\Gamma(5/4)^2}{\Gamma(3/2)}.
\]
Squaring (1), using \(\cos^2 z=(1+\cos2z)/2\), and applying Dirichlet's test to the oscillating part shows that, as \(p\uparrow5/2\),
\[
(5/2-p)\int_1^\infty H(t)^2t^{p-1}\,dt\longrightarrow C^2/2.
\]
The contribution below \(t=1\) vanishes after multiplication by \(5/2-p\). Hence the residue equals \((5/2)C^2/(2|K|)=5\sqrt\pi\). At \(p=5/2\), the nonoscillatory integral diverges logarithmically; for every larger \(p\), it diverges as well.

**2. Uniform finite-type bounds.** Parameterise the boundary near \((1,0)\) as \((f(y),y)\), where \(f(y)=(1-y^4)^{1/4}=1-y^4/4+O(y^8)\). For \(u=(\cos\theta,\sin\theta)\), the divergence theorem turns the local Fourier integral into \(t^{-1}\) times an oscillatory boundary integral with phase \(t(\cos\theta\,f(y)+\sin\theta\,y)\) and smooth nonzero amplitude \(\cos\theta-\sin\theta f'(y)\). All other boundary patches are handled by integrations by parts or ordinary stationary phase.

For some fixed \(\theta_0>0\) and all \(t\ge1\), \(|\theta|\le\theta_0\), these considerations give the uniform quartic finite-type estimate
\[
|\widehat{\mathbf1_K}(t u_\theta)|\le
 C_0 t^{-5/4}(1+|\theta|t^{3/4})^{-1/3}. \tag{2}
\]
Here is a derivation of the two regimes, rather than an appeal to a numerical observation. When \(|\theta|t^{3/4}\le1\), partition the \(y\)-integral near the quartic critical point into \(|y|\lesssim t^{-1/4}\) and dyadic annuli. The central interval is \(O(t^{-1/4})\); on an annulus, the fourth derivative of the phase is bounded away from zero, and the fourth-order van der Corput lemma gives the same scale. When \(|\theta|t^{3/4}\ge1\), the critical point is at \(|y|\asymp|\theta|^{1/3}\); after scaling \(y=|\theta|^{1/3}z\), the effective phase parameter is \(t|\theta|^{4/3}\ge1\), and one-dimensional stationary phase gives an \(O(t^{-1/2}|\theta|^{-1/3})\) boundary integral. Multiplication by \(t^{-1}\) proves (2). A finite symmetric cover of \(\partial K\), and ordinary stationary phase away from its four flat points, also proves the global estimate
\[
\sup_{u\in S^1}|\widehat{\mathbf1_K}(tu)|\le C_1t^{-5/4},\qquad t\ge1. \tag{3}
\]
For every fixed nonaxial direction, each of the two supporting points is smooth with strictly positive curvature, so ordinary stationary phase gives a nonzero leading oscillation
\[
\widehat{\mathbf1_K}(tu)=D(u)t^{-3/2}\cos(th_K(u)-3\pi/4)+O_u(t^{-5/2}),\quad D(u)>0.\tag{4}
\]
The exact phase convention in (4) is immaterial for integrability; the positive amplitude and frequency \(h_K(u)>0\) are essential.

By (3) and dominated convergence, \(\rho_p\) is finite, positive, and continuous for \(p<5/2\). By (1) it is infinite at each axial direction when \(p\ge5/2\). By (4) and the positive mean of the squared cosine, it is finite nonaxially for \(p<3\) and infinite nonaxially for \(p\ge3\). This proves the pointwise three-phase classification.

**3. Critical angular logarithm.** We give the needed two-parameter estimate because simply inserting fixed-direction stationary phase into a shrinking-angle integral would be invalid. On each patch around \((\pm1,0)\), put \(y=t^{-1/4}z\) and \(\mu=\sin\theta\,t^{3/4}\). For bounded \(\mu\), quartic stationary phase with parameter gives, uniformly as \(t\to\infty\),
\[
\widehat{\mathbf1_K}(t u_\theta)
=t^{-5/4}\left[e^{-it\cos\theta}B(\mu)+e^{it\cos\theta}\overline{B(\mu)}+o(1)\right],\tag{5}
\]
where \(B\) is continuous at zero and \(B(0)=\frac C2e^{5\pi i/8}\). Uniformity follows by first cutting the rescaled integral to \(|z|\le R\), applying the Taylor expansion of \(f\) there, and bounding the rescaled tails uniformly by dyadic integration by parts; then let \(R\to\infty\). The same argument gives local differentiability of \(B\). For \(|\mu|\ge1\), the stationary-point scaling from step 2 gives the second factor in (2).

Fix a small \(\eta>0\), and split the defining integral at \(T_\theta=(\eta/|\sin\theta|)^{4/3}\). On \(1\ll t\le T_\theta\), (5) and continuity of \(B\) show that its nonoscillatory squared amplitude is \(2|B(0)|^2+o_\eta(1)+o_t(1)=C^2/2+o_\eta(1)+o_t(1)\). The cross term oscillates with phase \(2t\cos\theta\) and contributes \(o(\log(1/|\theta|))\) by integration by parts (the \(B\)-amplitude has bounded variation at the indicated scale). The interval \(0<t<1\) contributes \(O(1)\). For \(t>T_\theta\), (2) and the substitution \(s=|\theta|t^{3/4}\) yield the uniform bound
\[
\int_{T_\theta}^\infty t^{3/2}|\widehat{\mathbf1_K}(t u_\theta)|^2\,dt
\le C\int_{\eta}^\infty \frac{ds}{s(1+s)^{2/3}}<\infty,\tag{6}
\]
independent of \(\theta\). Since \(\log T_\theta/\log(1/|\theta|)\to4/3\), taking \(\theta\to0\) and then \(\eta\downarrow0\) gives
\[
\lim_{\theta\to0}\frac{\int_0^\infty t^{3/2}|\widehat{\mathbf1_K}(t u_\theta)|^2dt}{\log(1/|\theta|)}
=\frac43\frac{C^2}{2}.
\]
Multiplying by \((5/2)/|K|\) yields \(20\sqrt\pi/3\).

**4. Finite area in the noncompact phase.** For \(p=5/2\), step 3 implies \(\rho_p(u_\theta)^2=O((1+|\log|\theta||)^{4/5})\), locally integrable in \(\theta\). For \(5/2<p<3\), split the \(t\)-integral at \(t\asymp|\theta|^{-4/3}\) in (2) to obtain
\[
\rho_p(u_\theta)^p\le C_p|\theta|^{-\frac43(p-5/2)},\qquad 0<|\theta|\ll1.
\]
Consequently \(\rho_p(u_\theta)^2\le C_p|\theta|^{-\frac8{3p}(p-5/2)}\). Its exponent is strictly less than \(4/9<1\) for \(p<3\). Polar integration \(|F_pK|=\tfrac12\int_{S^1}\rho_p(u)^2\,du\) proves finite area; the four infinite-radius rays have zero planar measure. For \(p\ge3\), step 2 shows \(F_pK=\mathbb R^2\), completing the proof.

## Verification

Run `python verify_fourier_quartic.py` with Python 3 and SciPy. It checks beta/gamma normalizations, the exact axial and angular coefficients, five Fourier axial quadratures against the leading endpoint asymptotic, and symmetry/continuity of three nonaxial projection integrals. The script's numerical assertions are finite checks only. The infinite assertions above rest on the analysis of quartic oscillatory integrals, stationary phase, and polar area integrability. In particular (5)-(6), not any sampling grid, justify the angular constant.

## Relationship to prior work

Langharst–Manui–Zvavitch (2026) introduce \(F_pK\) and its Fourier index, obtain general convexity for \(p\le1\), and identify the Fourier index of a cube and of bodies with everywhere positive \(C^2\) curvature. The quartic disk meets neither of those two curvature classes, and their work does not present the stated three-phase quartic-disk law or its sharp coefficients. Lind's 2022 analysis of \(\ell_q\) balls concerns \(1<q\le2\) and the decay constant near \(q=1\), rather than the quartic flat-point regime \(q=4\). Earlier finite-type stationary-phase theory, including Randol's work, supplies relevant oscillatory methods; the geometric phase diagram and the critical angular coefficient are not asserted to be new oscillatory-analysis machinery. The present result uses those methods for the newer Fourier-mean construction. Historical priority for an equivalent specific critical calculation cannot be excluded.

## Limitations

The claim concerns only the planar quartic disk and the specified Fourier normalization. A change to the \(2\pi\)-Fourier convention rescales the explicit constants. No assertion about the convexity of \(F_pK\) for \(1<p<5/2\) is made. The unbounded bodies in the middle phase have finite Lebesgue area but do not have compact boundary. Independent mathematical audit has not been performed. A historical exact equivalent in unindexed finite-type literature remains possible.

## References

1. D. Langharst, A. Manui, A. Zvavitch, *On the Fourier Mean Bodies of a Convex Body*, arXiv:2601.20117, first submitted 2026-01-27; see Definition 2, Proposition 3, Theorems 5, 6, and Section 5. https://arxiv.org/abs/2601.20117
2. M. Lind, *A remark on the Fourier transform of \(\ell^p\) balls*, arXiv:2208.07837 (2022); see the introduction, Section 2, and main curvature-decay estimate. https://arxiv.org/abs/2208.07837
3. B. Randol, *On the asymptotic behavior of the Fourier transform of the indicator function of a convex set*, Trans. Amer. Math. Soc. 139 (1969), 279–285. https://doi.org/10.1090/S0002-9947-1969-0251450-5
4. L. Brandolini, S. Hofmann, A. Iosevich, *Sharp rate of average decay of the Fourier transform of a bounded set*, Geom. Funct. Anal. 13 (2003), arXiv:math/0303188. https://arxiv.org/abs/math/0303188
