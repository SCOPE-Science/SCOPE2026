# Quartic entropy curvature in the minimal two-harmonic doubling-map deformation

## Finding

Let \(D(x)=2x\pmod 1\) on the circle \(\mathbb R/\mathbb Z\). For real \(a,b\), put
\[
u_{a,b}(x)=\frac{a\sin(2\pi x)+b\cos(2\pi x)}{4\pi},\qquad
v_{a,b}(x)=u_{a,b}(2x)-2u_{a,b}(x),\qquad
T_{\varepsilon,a,b}(x)=2x+\varepsilon v_{a,b}(x)\pmod1.
\]
For sufficiently small real \(\varepsilon\), denote by \(\mu_{\varepsilon,a,b}\) the unique absolutely continuous invariant probability of this expanding degree-two map and by
\[
\lambda(\varepsilon,a,b)=\int\log T'_{\varepsilon,a,b}\,d\mu_{\varepsilon,a,b}
\]
its stationary Lyapunov exponent, also its metric entropy. **For every fixed real pair \((a,b)\)**,
\[
\boxed{\displaystyle
\lambda(\varepsilon,a,b)=\log 2-
\frac{(a^2+b^2)(9a^2+5b^2)}{128}\,\varepsilon^4
+O_{a,b}(|\varepsilon|^5).}
\]
In particular the first three derivatives at zero vanish; if \((a,b)\ne(0,0)\), the first nonzero derivative is fourth order and strictly negative. For unit pure sine versus unit pure cosine, the quartic loss has the exact anisotropy ratio \(9:5\).

The family is **exactly the two-dimensional zero-quadratic-response kernel** within the real, zero-mean, degree-at-most-two trigonometric perturbations of doubling. More precisely, for
\[
w(x)=A\sin(2\pi x)+B\cos(2\pi x)+C\sin(4\pi x)+E\cos(4\pi x)
\]
and \(F_t(x)=2x+t w(x)\pmod1\), whose Lyapunov exponent is computed with respect to its own absolutely continuous invariant probability,
\[
\lambda(F_t)=\log2-\frac{\pi^2}{4}\big((A+2C)^2+(B+2E)^2\big)t^2+O_w(|t|^3).
\]
Consequently its quadratic loss vanishes exactly when \(C=-A/2\) and \(E=-B/2\); no nonzero one-harmonic zero-mean direction has this degeneracy.

## Assumptions and scope

All functions are functions on the unit circle, and Fourier coefficients use \(\widehat g(k)=\int_0^1g(x)e^{-2\pi\mathrm{i}kx}\,dx\). The small parameter is real, and \(a,b\) are fixed during the limit \(\varepsilon\to0\). Writing \(r=\sqrt{a^2+b^2}\), the explicit sufficient condition \(|\varepsilon|r<1/4\) ensures \(T'_{\varepsilon,a,b}>1\), because \(\|v'_{a,b}\|_\infty\le4r\). The same condition ensures that \(H_\varepsilon(x)=x+\varepsilon u_{a,b}(x)\) is an orientation-preserving smooth circle diffeomorphism. For \(r=0\), the map is exactly doubling and the formula holds identically. The error constant is not asserted uniform for unbounded \((a,b)\); no finite-parameter exact equality is asserted beyond the asymptotic expansion.

## Proof

**1. Universal quadratic response at doubling.** For a smooth mean-zero periodic \(w\), let \(F_t(x)=2x+t w(x)\pmod1\), let \(P_t\) be its Perron--Frobenius operator with respect to Lebesgue measure, and let \(h_t\) be its normalized invariant density. On smooth functions,
\[
P_0\phi(x)=\frac12\left(\phi(x/2)+\phi((x+1)/2)\right).
\]
Transfer-operator perturbation for smooth uniformly expanding circle maps gives the required five derivatives of the normalized invariant density and Lyapunov functional near \(t=0\). In particular \(h_0=1\). Differentiate the weak identity
\[
\int \psi(x)(P_t\phi)(x)\,dx=\int\psi(2x+t w(x))\phi(x)\,dx
\]
at zero and integrate by parts. One obtains
\[
\left.\frac{d}{dt}P_t1\right|_{0}=-\frac12P_0w',\qquad
h'_0=-\frac12\sum_{j=1}^{\infty}P_0^j w',
\]
where the series converges on zero-mean smooth functions (and terminates for a trigonometric polynomial). Expanding the logarithm and using \(\int h_t=1\) gives
\[
\left.\frac{d}{dt}\lambda(F_t)\right|_0=0,\qquad
\lambda(F_t)=\log2-\frac{t^2}{8}\left(\int(w')^2+2\sum_{j=1}^{\infty}\int w'P_0^j w'\right)+O_w(|t|^3).
\]
The parenthesized quantity is the Green--Kubo asymptotic variance
\[
\sigma_D^2(g)=\lim_{n\to\infty}\frac1n\int\left(\sum_{k=0}^{n-1}g(D^k x)\right)^2dx,
\qquad g=w',\quad\int g=0.
\]
The equality follows by expanding the square, using invariance of Lebesgue measure and exponential decay of correlations for trigonometric polynomials. All quantities here are finite and explicit.

**2. Minimal Fourier null space.** For a real trigonometric polynomial \(g\) with zero mean, the doubling map sends Fourier frequencies \(m\) along the disjoint towers \(m,2m,4m,\ldots\), with \(m\) odd. Direct orthogonality gives
\[
\sigma_D^2(g)=2\sum_{m\ge1\atop m\ \mathrm{odd}}
\left|\sum_{j\ge0}\widehat g(2^jm)\right|^2.
\]
All sums are finite for the polynomials in this theorem. When \(g=w'\) has frequencies only \(1,2\), this reduces to
\[
\sigma_D^2(w')=2\pi^2\big((A+2C)^2+(B+2E)^2\big).
\]
Substituting into the previous expansion proves the claimed full two-harmonic quadratic formula and its kernel characterization. The kernel is exactly \(w=v_{a,b}\) for suitable \(a,b\), since \(v=u\circ D-2u\) and \(u\) is a first-harmonic trigonometric polynomial.

**3. Removing the first-order perturbation by conjugacy.** Fix \(a,b\). Let \(H_\varepsilon(x)=x+\varepsilon u(x)\), with \(u=u_{a,b}\) and \(v=u\circ D-2u\). Taylor expansion in \(C^5\) yields
\[
T_\varepsilon(H_\varepsilon(x))
=2x+\varepsilon u(2x)+\varepsilon^2u(x)v'(x)+O_{C^5}(|\varepsilon|^3).
\]
It follows, by applying the smooth inverse of \(H_\varepsilon\), that
\[
S_\varepsilon:=H_\varepsilon^{-1}\circ T_\varepsilon\circ H_\varepsilon
=D+\varepsilon^2 f+O_{C^5}(|\varepsilon|^3),\qquad f=u v'.
\]
The invariant absolutely continuous measures are conjugate, and the difference between their logarithmic derivative observables is a smooth coboundary. Hence \(\lambda(S_\varepsilon)=\lambda(T_\varepsilon)\). The universal first derivative of \(\lambda\) at \(D\) vanishes in **every** perturbation direction. Its second differential, from Step 1, is \(-\sigma_D^2(f')/4\). Taylor expansion with the \(O(\varepsilon^3)\) remainder therefore yields
\[
\lambda(T_\varepsilon)=\log2-\frac{\varepsilon^4}{8}\sigma_D^2(f')+O_{a,b}(|\varepsilon|^5).
\]
There is no hidden cubic contribution: the conjugated map begins at order \(\varepsilon^2\) and the Lyapunov functional has zero first derivative at doubling.

**4. Exact fourth-order coefficient.** Write \(z=b-\mathrm{i}a\). Direct differentiation and multiplication of the trigonometric polynomials \(u\) and \(v'\) gives for \(f'= (u v')'\):
\[
\widehat{f'}(1)=-\frac{a^2+b^2}{8},\qquad
\widehat{f'}(2)=\frac{z^2}{4},\qquad
\widehat{f'}(3)=-\frac{3z^2}{8}.
\]
The negative Fourier coefficients are their complex conjugates; all other coefficients vanish. Consequently the dyadic tower formula gives
\[
\sigma_D^2(f')=2\left(\left|\widehat{f'}(1)+\widehat{f'}(2)\right|^2+
\left|\widehat{f'}(3)\right|^2\right)
=\frac{(a^2+b^2)(9a^2+5b^2)}{16}.
\]
Substitution in Step 3 proves the boxed quartic expansion and strict positivity for every nonzero \((a,b)\). This completes the proof.

## Verification

The standalone `verify_quartic.py` checks the exact Fourier-polynomial identity, the four calibration pairs \((a,b)=(1,0),(0,1),(1,1),(0,0)\), and the two-harmonic kernel using symbolic algebra. A separate numerical stationary-density iteration over 32768 grid points and 42 transfer iterations gave, at \(\varepsilon=0.08\), normalized observed losses approximately \(0.070806\), \(0.039551\), and \(0.224855\) for \((a,b)=(-1,0),(0,1),(1,1)\), versus the proved limiting coefficients \(9/128\), \(5/128\), and \(7/32\). These numerical computations are **not** proof of the asymptotics; the proof is the operator expansion, conjugacy and exact Fourier calculation above. The difference is compatible with higher-order terms and numerical discretization; no error certificate is asserted for the numerical method.

## Relationship to prior work

Pollicott and Vytnova (arXiv:2201.04752, first posted January 13, 2022) give rigorous transfer-operator/pressure bounds for Lyapunov exponents of expanding maps and examples including a Lanford family. The present theorem supplies a different, explicit **degenerate fourth-order perturbation coefficient** and a complete minimal-harmonic null-space description; neither is stated in their inspected source.

De la Llave, Shub and Simó (2008, DOI below) investigate a **single first-harmonic** perturbation with an additive rotation parameter, comparing average and maximal entropy with a reference integral. Their complete author-hosted article has different map parameters and no two-harmonic first-order conjugacy cancellation or the reported coefficient. Galatolo and Pollicott (arXiv:1603.07762, 2016) develop first-order invariant-density response and optimization, including Fourier analysis of doubling; their object is first-order density change, not fourth-order entropy along the null space. These earlier methods, linear response and smooth conjugacy invariance are established ingredients rather than new claims.

## Limitations

The result is local in the perturbation parameter for fixed finite \((a,b)\). It does not quantify a uniform remainder as the harmonic amplitudes grow, and it does not provide finite-amplitude entropy bounds or classify all smooth infinite-Fourier perturbations. Its novelty is assessed against the inspected literature and mathematical-index searches; absence from the inspected sources does not establish universal publication priority. An independent audit has not been performed.

## References

1. M. Pollicott and P. Vytnova, *Accurate bounds on Lyapunov exponents for expanding maps of the interval*, arXiv:2201.04752 (first version January 13, 2022), *Communications in Mathematical Physics* 397 (2023), 485–502, DOI:10.1007/s00220-022-04495-7. Full article: https://link.springer.com/article/10.1007/s00220-022-04495-7.
2. R. de la Llave, M. Shub, and C. Simó, *Entropy estimates for a family of expanding maps of the circle*, *Discrete and Continuous Dynamical Systems B* 10 (2008), 597–608, DOI:10.3934/dcdsb.2008.10.597. Author-hosted full article: https://profshub.github.io/articles/2008-Entropy_estimates_for_a_family_of_expanding_maps_of_the_circle.pdf.
3. S. Galatolo and M. Pollicott, *Controlling the statistical properties of expanding maps*, arXiv:1603.07762 (2016), *Nonlinearity* 30 (2017), 2737–2751. Author-hosted full article: https://warwick.ac.uk/fac/sci/maths/people/staff/mark_pollicott/p3/linear-revised2.pdf.
