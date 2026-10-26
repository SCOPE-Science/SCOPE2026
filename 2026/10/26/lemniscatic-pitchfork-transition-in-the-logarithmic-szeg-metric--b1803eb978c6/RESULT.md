# Lemniscatic pitchfork transition in the logarithmic Szegő metric of an annulus

## Finding

Consider the ordinary Euclidean-boundary-arclength Hardy space on the annulus \(A_q=\{z:q<|z|<1\}\), where \(0<q<1\). Put \(h=-\log q\) and \(u=\log(|z|/\sqrt q)\in(-h/2,h/2)\). The squared logarithmic infinitesimal projective Szegő metric is
\[
M_h(u):=|z|^2\partial_z\partial_{\bar z}\log S_q(z,z).
\]
Let \(K(m)=\int_0^{\pi/2}(1-m\sin^2t)^{-1/2}\,dt\) and let \(m\in(0,1)\) be the unique elliptic parameter satisfying
\[
h=\pi\frac{K(1-m)}{K(m)}.
\]
Define \(C_h(u)=\operatorname{cn}(2iK(m)u/\pi\mid m)\), with \(\operatorname{cn}(\cdot\mid m)\) the Jacobi cosine with *parameter* \(m\), rather than modulus \(\sqrt m\). Then for every \(u\in(-h/2,h/2)\),
\[
\boxed{M_h(u)=\frac{K(m)^2}{\pi^2}\left(mC_h(u)^2+\frac{1-m}{C_h(u)^2}\right).}
\]
Its global minimizing set has the following exhaustive phase diagram.

* If \(0<h\le\pi\), the unique minimizing logarithmic radius is \(u=0\); the minimum is \(K(m)^2/\pi^2\). Thus there is exactly one minimizing circle, \(|z|=\sqrt q\).
* If \(h>\pi\), the minimum is attained at exactly two logarithmic radii \(u=\pm u_*\), where \(u_*\in(0,h/2)\) is uniquely determined by \(C_h(u_*)^4=(1-m)/m\). The minimum is \(2K(m)^2\sqrt{m(1-m)}/\pi^2\). The corresponding radii \(r_\pm=\sqrt q\,e^{\pm u_*}\) obey \(r_-r_+=q\); the central circle becomes a strict local maximum.

The two minimizing circles can be located without numerical optimization:
\[
u_* =\frac{\pi}{2K(m)}F\!\left(\arccos\left((m/(1-m))^{1/4}\right)\Bigm|1-m\right),
\]
where \(F(\phi\mid p)=\int_0^{\phi}(1-p\sin^2t)^{-1/2}\,dt\). At the transition \(h=\pi\) (equivalently \(q=e^{-\pi}\), \(m=1/2\)), the unique center minimum is quartically flat:
\[
M_\pi(u)=\frac{K(1/2)^2}{\pi^2}+\frac{8K(1/2)^6}{\pi^6}u^4+O(u^6),\quad u\to0.
\]
All minimizing points in the annulus are precisely the circles stated above, including arbitrary angular coordinate.

## Assumptions and scope

Use unnormalized Euclidean arclength \(|d\zeta|\) on *both* boundary circles. For Laurent monomials, \(\|z^n\|_{H^2(\partial A_q)}^2=2\pi(1+q^{2n+1})\). Hence the reproducing kernel is
\[
S_q(z,w)=\frac{1}{2\pi}\sum_{n\in\mathbb Z}\frac{(z\bar w)^n}{1+q^{2n+1}},\qquad z,w\in A_q.
\]
The series and every interior derivative converge normally. Multiplication of the kernel by a positive constant does not affect \(M_h\). This result classifies *logarithmic-coordinate* metric minima, not minima of the Euclidean-area zero density \(M_h(u)/(\pi|z|^2)\), which is a different problem. The coefficient \(M_h\) multiplies \(du^2+d\theta^2\) in the pulled-back Kähler metric \(\partial\bar\partial\log S_q\) in the cylindrical coordinate \(u+i\theta\). If the projective distance is normalized as \(\rho_S(z,w)^2=1-|S_q(z,w)|/\sqrt{S_q(z,z)S_q(w,w)}\), then its local squared-distance expansion is \(\rho_S(z,z+\delta)^2=\tfrac12\partial_z\partial_{\bar z}\log S_q(z,z)|\delta|^2+o(|\delta|^2)\); this uniform factor of two does not change the minimizing circles.

## Proof

**1. Reduction to the hyperbolic-secant lattice.** Since \(q=e^{-h}\), the kernel diagonal admits
\[
2\pi S_q(z,z)=\frac{e^{h/2-u}}2 Z_h(u),\qquad
Z_h(u)=\sum_{n\in\mathbb Z}\frac{e^{2u(n+1/2)}}{\cosh(h(n+1/2))}.
\]
For radial functions, the identity \(|z|^2\partial_z\partial_{\bar z}=(1/4)\partial_u^2\) holds. The additive linear term \(h/2-u\) in the log kernel has zero second derivative, so
\[
M_h(u)=\tfrac14\bigl(\log Z_h(u)\bigr)''.
\]

**2. Exact elliptic representation.** The nome \(Q=e^{-h}\) is exactly the Jacobi nome for the parameter \(m\) above. The classical Jacobi-cosine Fourier series (DLMF 22.11.2, with modulus \(\sqrt m\)) is
\[
\operatorname{cn}(v\mid m)=\frac{2\pi}{\sqrt m K(m)}\sum_{j\ge0}\frac{Q^{j+1/2}}{1+Q^{2j+1}}\cos\!\left(\frac{(2j+1)\pi v}{2K(m)}\right).
\]
Substitute \(v=2iK(m)u/\pi\) and use \(Q^{j+1/2}/(1+Q^{2j+1})=1/(2\cosh(h(j+1/2)))\). Pairing positive and negative half-integers yields the exact, normally convergent identity
\[
Z_h(u)=\frac{2\sqrt m K(m)}\pi C_h(u).
\]
The imaginary transformation gives \(C_h(u)=1/\operatorname{cn}(2K(m)u/\pi\mid1-m)\). Because \(2K(m)(h/2)/\pi=K(1-m)\), \(C_h\) is even, strictly increasing from \(1\) to \(+\infty\) on \([0,h/2)\), and positive there.

**3. Curvature identity.** The Jacobi differential equation in the imaginary argument yields
\[
C_h''=\alpha^2[(1-2m)C_h+2m C_h^3],\qquad \alpha=2K(m)/\pi.
\]
Its first integral, fixed by \(C_h(0)=1\), \(C_h'(0)=0\), is
\[
(C_h')^2=\alpha^2(C_h^2-1)(mC_h^2+1-m).
\]
Consequently
\[
(\log C_h)''=\alpha^2\left(mC_h^2+(1-m)C_h^{-2}\right).
\]
Combining this with step 1 and \(Z_h\propto C_h\) proves the boxed metric formula.

**4. Global optimizer and sharp threshold.** Set \(y=C_h(u)^2\). On \(u\in[0,h/2)\), \(y\) runs strictly through \([1,\infty)\). Thus minimizing the metric is exactly minimizing \(f_m(y)=my+(1-m)/y\) over \(y\ge1\). The derivative \(f_m'(y)=m-(1-m)y^{-2}\) has a single zero at \(y_0=\sqrt{(1-m)/m}\). It lies in the allowed range iff \(m\le1/2\), with equality corresponding to the center. When \(m<1/2\), this gives one positive \(u_*\) and its negative, and \(f_m(y_0)=2\sqrt{m(1-m)}\). When \(m\ge1/2\), \(f_m\) is strictly increasing for \(y>1\), yielding the unique center minimum. At \(m<1/2\) the center is a strict local maximum since \(C_h(u)=1+(\alpha^2/2)u^2+O(u^4)\) and \(f'_m(1)=2m-1<0\). Because \(K(m)\) is strictly increasing in \(m\), \(K(1-m)/K(m)\) is strictly decreasing, equals \(1\) precisely when \(m=1/2\), and covers \((0,\infty)\). Hence \(m=1/2\) is exactly \(h=\pi\). The elliptic-integral formula follows by inverting \(\operatorname{cn}(2K(m)u/\pi\mid1-m)=(m/(1-m))^{1/4}\).

**5. Degenerate critical point.** At \(m=1/2\), \(C_h(u)^2=1+\alpha^2u^2+O(u^4)\). Consequently \(\frac12[y+y^{-1}]=1+\frac12\alpha^4u^4+O(u^6)\). Multiplication by \(K(m)^2/\pi^2=\alpha^2/4\) gives the stated \(8K(1/2)^6/\pi^6\) quartic coefficient. This coefficient is strictly positive. The proof covers all \(0<q<1\) and all interior radii without a finite cutoff.

## Verification

The included `annular_szego_metric_checker.py` evaluates the metric by two *distinct* formulas: finite truncations of the original half-integer Laurent-series variance and the Jacobi elliptic closed form. At 65-digit arithmetic it checks their agreement for six annuli and multiple logarithmic radii, reciprocal-radius symmetry, the algebraic minimum and its two-radius location, sampled global inequalities, and the quartic coefficient at the critical modulus. It reports 1284 passing numerical assertions when run with Python 3 and `mpmath`. These computations corroborate, but do not establish, the all-annulus theorem; the global proof is the monotone change of variable in step 4.

## Relationship to prior work

Gafai–Murid–Wahid (arXiv:2202.09114, first public 2022-02-18) provide the Euclidean-arclength annular Szegő bilateral and product kernels, establishing the base Hardy model rather than the present metric optimization. Katori–Shirai (arXiv:2008.04177) study the same family of weighted Szegő kernels and give one-point Gaussian zero intensities and two-point phase transitions; they do not state a classification of extrema of the *logarithmic radial metric* or the \(q=e^{-\pi}\) threshold. Krantz–Wójcicki (2021) define Szegő projective distances on domains but do not analyze the annular radial minimizer geometry. The exact Jacobi-cosine Fourier series (DLMF 22.11.2) is a classical input, not claimed as new. The claimed contribution is the explicit metric identity *combined with* the complete global radial minimizer bifurcation, sharp value and quartic threshold law. A disguised consequence in classical elliptic-function literature remains a residual historical-priority risk.

## Limitations

No theorem is claimed for weighted boundary measures differing from Euclidean arclength, noncircular doubly connected domains, Euclidean-density minimizing radii, or geodesic-distance global minimizers. The phase diagram is a classification of the logarithmic coordinate coefficient of an infinitesimal projective metric. The probability-normalized Gaussian zero intensity differs by a standard factor of area and also by \(|z|^{-2}\) if expressed in Euclidean area. The supplied numerical checks are finite corroborations, and historical priority has not been independently established.

## References

1. N. S. Gafai, A. H. M. Murid, N. H. A. A. Wahid, *Infinite Product Representation for the Szegö Kernel for an Annulus*, arXiv:2202.09114 (first posted 18 February 2022), https://arxiv.org/abs/2202.09114; Journal of Function Spaces (2022), doi:10.1155/2022/3763450.
2. M. Katori and T. Shirai, *Zeros of the i.i.d. Gaussian Laurent Series on an Annulus*, arXiv:2008.04177 (10 August 2020); Communications in Mathematical Physics 392 (2022), doi:10.1007/s00220-022-04365-2.
3. S. G. Krantz and P. M. Wójcicki, *On an invariant distance induced by the Szegő Kernel*, Complex Analysis and its Synergies 7 (2021), doi:10.1007/s40627-021-00085-w.
4. NIST Digital Library of Mathematical Functions, §22.11, equation 22.11.2, https://dlmf.nist.gov/22.11.E2.
