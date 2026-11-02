# Sharp geometry and stability of periodic Fock observation stripes

## Finding

For every \(L>0\) and \(0<w<L\), put \(\mathbb T_L=\mathbb R/L\mathbb Z\). Let \(E\subset\mathbb T_L\) be measurable with length \(|E|=w\), and let \(\Omega_E=\{z\in\mathbb C:\operatorname{Re}z\bmod L\in E\}\). On normalized analytic Bargmann–Fock space, define its sharp squared observation constants by
\[
 A(E)\|F\|^2\le\int_{\Omega_E}|F(z)|^2e^{-\pi|z|^2}\,dA(z)\le B(E)\|F\|^2
 \quad\text{for every }F\in\mathcal F_\pi.
\]

Define the normalized periodized heat kernel and interval endpoints by
\[
 K_L(x)=\sqrt2\sum_{j\in\mathbb Z}e^{-2\pi(x+jL)^2}
 =\frac1L\sum_{n\in\mathbb Z}e^{-\pi n^2/(2L^2)}e^{2\pi inx/L},
\]
\[
 a_{L,w}=\int_{-w/2}^{w/2}K_L(L/2-x)\,dx,\qquad
 b_{L,w}=\int_{-w/2}^{w/2}K_L(x)\,dx.
\]

Then every such measurable \(E\) obeys the **simultaneously sharp** inequalities
\[
 0<a_{L,w}\le A(E)\le B(E)\le b_{L,w}<1,\qquad
 \frac{B(E)}{A(E)}\le\frac{b_{L,w}}{a_{L,w}}.
\]
Equality in any of the three outer extremal assertions occurs **if and only if** \(E\) is a translate, modulo null sets, of one interval of length \(w\).

There is a quantitative form. Put \(d(E)=\inf_{u\in\mathbb T_L}|E\mathbin\triangle(u+[-w/2,w/2])|\) and \(m=d(E)/2\). For \(0\le m\le\min(w,L-w)\), define
\[
 \Delta_-(m)=2\int_0^{m/2}\!\left[K_L\!\left(\frac{L-w}{2}-s\right)-K_L\!\left(\frac{L-w}{2}+s\right)\right]ds,
\]
\[
 \Delta_+(m)=2\int_0^{m/2}\!\left[K_L\!\left(\frac w2-s\right)-K_L\!\left(\frac w2+s\right)\right]ds.
\]
For all \(E\),
\[
 A(E)\ge a_{L,w}+\Delta_-(m),\qquad
 B(E)\le b_{L,w}-\Delta_+(m).
\]
Each modulus is strictly positive for \(m>0\), with
\[
 \Delta_-(m)=-\frac12K_L'\!\left(\frac{L-w}{2}\right)m^2+O(m^4),\quad
 \Delta_+(m)=-\frac12K_L'\!\left(\frac w2\right)m^2+O(m^4).
\]
These are explicit valid stability moduli, not asserted to be the globally best moduli at fixed symmetric-difference distance.

Fix \(0<\rho<1\). In the sparse-period limit \(L\to\infty\) and \(w=\rho L\),
\[
 a_{L,\rho L}\sim\frac{\sqrt2}{\pi(1-\rho)L}\exp\!\left[-\frac\pi2(1-\rho)^2L^2\right],\qquad b_{L,\rho L}\to1.
\]
Thus the worst possible observation condition ratio has the sharp reciprocal asymptotic. At fixed \(L,\rho\), let \(E_M\) consist of \(M\) equally spaced centered intervals, each of length \(\rho L/M\). As integer \(M\to\infty\),
\[
 A(E_M)=\rho-\frac{2\sin(\pi\rho)}\pi e^{-\pi M^2/(2L^2)}+O_{L,\rho}(e^{-2\pi M^2/L^2}),
\]
\[
 B(E_M)=\rho+\frac{2\sin(\pi\rho)}\pi e^{-\pi M^2/(2L^2)}+O_{L,\rho}(e^{-2\pi M^2/L^2}).
\]
Consequently, \(\sup_E A(E)=\inf_E B(E)=\rho\) and \(\inf_E B(E)/A(E)=1\), with no optimizer for \(0<\rho<1\).

## Assumptions and scope

The Fock space is \(\mathcal F_\pi=\{F\text{ entire}:\|F\|^2=\int_{\mathbb C}|F(z)|^2e^{-\pi|z|^2}\,dA(z)<\infty\}\), with planar Lebesgue area. All measurable sets on \(\mathbb T_L\) are identified modulo null sets. Bounds concern squared Hilbert norms, not their square roots. Period \(L\) and width \(w\) are arbitrary positive real parameters satisfying \(0<w<L\). No regularity or finite-component assumption is placed on \(E\).

## Proof

**1. Exact Fock multiplier, with normalization.** Let \(g(t)=2^{1/4}e^{-\pi t^2}\), so \(\|g\|_{L^2(\mathbb R)}=1\). The unitary Bargmann transform is
\[
 (\mathcal B f)(z)=2^{1/4}\int_{\mathbb R} f(t)e^{2\pi tz-\pi t^2-\pi z^2/2}\,dt.
\]
The standard Bargmann/STFT identity identifies \(e^{-\pi|z|^2}|\mathcal Bf(z)|^2\) with the squared Gaussian STFT at \((\operatorname{Re}z,\pm\operatorname{Im}z)\). By Plancherel in its frequency coordinate, for each real \(x\),
\[
 \int_{\mathbb R}|(\mathcal Bf)(x+iy)|^2e^{-\pi(x^2+y^2)}dy
 =\int_{\mathbb R}|f(t)|^2\sqrt2 e^{-2\pi(t-x)^2}\,dt.
\]
Tonelli's theorem and periodicity therefore give the *exact* multiplier identity
\[
 \int_{\Omega_E}|F(z)|^2e^{-\pi|z|^2}\,dA(z)
 =\int_{\mathbb R}|(\mathcal B^{-1}F)(t)|^2 H_E(t)\,dt,
 \quad H_E(t)=\int_E K_L(t-x)\,dx.
\]
The Gaussian series converges absolutely together with all derivatives; Poisson summation gives its displayed Fourier expansion. Hence \(A(E)=\min_{t\in\mathbb T_L}H_E(t)\) and \(B(E)=\max_{t\in\mathbb T_L}H_E(t)\) exactly.

**2. Strict circular heat-kernel monotonicity.** Write \(q=e^{-\pi/(2L^2)}\). Poisson summation also yields \(LK_L(x)=\vartheta_3(\pi x/L,q)\). Jacobi's triple-product identity gives, for \(0<\theta<\pi/2\),
\[
 \frac{d}{d\theta}\log\vartheta_3(\theta,q)
 =-4\sin(2\theta)\sum_{j=1}^{\infty}
 \frac{q^{2j-1}}{1+2q^{2j-1}\cos(2\theta)+q^{4j-2}}<0.
\]
The denominator equals \(|1+q^{2j-1}e^{2i\theta}|^2\). Thus \(K_L\) is symmetric and strictly decreasing as geodesic distance from \(0\) increases from \(0\) to \(L/2\). In particular its only maximum and minimum modulo \(L\) are at \(0\) and \(L/2\).

**3. Interval shape classification.** At any fixed observation point \(t\), the strict bathtub principle for the radially decreasing function \(x\mapsto K_L(t-x)\) says that among all \(|E|=w\), the integral \(H_E(t)\) is uniquely maximized by the interval of length \(w\) centered at \(t\), and uniquely minimized by the interval centered at \(t+L/2\). Hence \(a_{L,w}\le H_E(t)\le b_{L,w}\) for every \(t\). For a single interval \(I_w\) centered at zero, differentiation of its convolution gives \(H'_{I_w}(t)=K_L(t+w/2)-K_L(t-w/2)<0\) for \(0<t<L/2\) by strict circle monotonicity. Therefore \(A(I_w)=a_{L,w}\), \(B(I_w)=b_{L,w}\). If either extreme is achieved by any \(E\), equality in the strict bathtub principle at its minimizing or maximizing point forces \(E\) to be a translate of \(I_w\). The condition ratio has the same unique extremizers because its numerator and denominator are separately bounded, strictly for nonintervals.

**4. Quantitative exchanged-mass estimate.** For each fixed \(t\), let \(J_t\) be the minimization interval centered at \(t+L/2\); put \(m_t=|E\triangle J_t|/2\). Then \(|J_t\setminus E|=|E\setminus J_t|=m_t\). At fixed exchanged mass, moving removed points toward the two boundaries *inside* \(J_t\) and added points toward the two boundaries *outside* \(J_t\) produces the smallest possible increase in the convolution. Pairing the boundary layers of length \(m_t/2\) yields exactly \(\Delta_-(m_t)\). For the maximizing interval centered at \(t\), the analogous exchange decreases the integral by at least \(\Delta_+(m_t)\). Both moduli increase strictly with \(m_t\) for \(0<m_t<\min(w,L-w)\) because both bracketed differences are strictly positive by monotonicity of \(K_L\). Since every centered interval is a translate and \(m_t\ge d(E)/2\), taking minima or maxima proves both stated global stability bounds. Taylor expansion at the two smooth interior boundary distances yields their quadratic coefficients; positivity follows from \(K'_L<0\) there.

**5. Period and microstructure limits.** For \(G=L-w\), at the midpoint of the missing gap the integral is the sum of two Gaussian tails from the nearest observed stripes and exponentially smaller further stripes. Its leading term is \(\operatorname{erfc}(\sqrt{\pi/2}\,G)\sim \sqrt2\,e^{-\pi G^2/2}/(\pi G)\). The interval-centered mass tends to one. For \(E_M\), the only nonzero Fourier coefficients of its indicator have indices divisible by \(M\), and its coefficients at index \(kM\), with centered alignment, are \(\sin(\pi k\rho)/(\pi k)\) for \(k\ne0\). Multiplication by the positive Gaussian Fourier coefficients of \(K_L\) gives the exact uniformly convergent cosine series
\[
 H_{E_M}(t)=\rho+2\sum_{k=1}^{\infty}\frac{\sin(\pi k\rho)}{\pi k}
 e^{-\pi k^2M^2/(2L^2)}\cos(2\pi kMt/L).
\]
The first harmonic dominates the remaining terms by \(O_{L,\rho}(e^{-2\pi M^2/L^2})\), yielding both expansions. Since all nonzero Gaussian Fourier coefficients are strictly positive, \(H_E\) cannot be identically \(\rho\) unless \(\mathbf1_E=\rho\) almost everywhere, impossible for a nontrivial binary mask. This proves nonattainment of the homogeneous ideal.

**6. Spectrum and spectral type.** Under the Bargmann unitary the Toeplitz concentration operator is multiplication by the real-analytic, nonconstant, periodic \(H_E\), so its spectrum is its complete range \([A(E),B(E)]\). Analyticity implies only finitely many critical points in a period, while strictly monotone arcs have locally absolutely continuous inverse away from their endpoints. Thus every Lebesgue-null subset of the spectral interval has zero inverse-image measure. The multiplication operator has purely absolutely continuous spectrum and no eigenvalues.

## Verification

Run `python3 check.py` with a standard Python 3 installation. It checks the physical and Fourier representations of the periodic Gaussian, interval extrema, sampled exchange inequalities for disconnected examples, Gaussian-tail asymptotics, and first-harmonic microstripe estimates. The script is supplementary finite numerical evidence, not a replacement for the all-measurable-set proof. Numerical calculations use floating point and explicit tolerances.

## Relationship to prior work

Konate and Orsoni (2021, arXiv:2103.11653) establish quantitative domination inequalities in generalized Fock spaces, with density-dependent rather than exact fixed-shape constants. Jaming and Speckbacher (2019, arXiv:1906.02964) study planar short-time Fourier restriction with broad geometric estimates. Esmeral and Vasilevski (2016) establish the general horizontal-symbol Fock Toeplitz multiplier representation; Arroyo Neri and collaborators (2021) give broader invariant-symbol/poly-Fock multiplier formulas. **The multiplier/diagonalization is known and is not presented as new.** The result here is the paired exact extremal design, equality classification, explicit quantitative interval rigidity, and period/microstructure regimes at prescribed duty fraction. The extremal mechanism uses the classical bathtub principle and Jacobi triple product, so this is a specialized exact theorem rather than a new general rearrangement principle.

## Limitations

The proof is confined to one complex dimension, the standard Gaussian weight, binary vertical observation masks and fixed duty fraction. The stability moduli are valid and explicit, but not shown globally optimal at prescribed translation-invariant symmetric-difference distance. No finite-component assumption is required. Earlier equivalent reductions may exist in work on circle heat-kernel rearrangement or Fock Toeplitz operators; the 2016 article was accessible only in abstract, so historical priority is provisional. No independent validation has been carried out.

## References

1. S. Konate and M.-A. Orsoni, *Sampling constants in generalized Fock spaces* (first posted 2021-03-22), https://arxiv.org/abs/2103.11653.
2. P. Jaming and M. Speckbacher, *Planar sampling sets for the short-time Fourier transform* (first posted 2019-06-07), https://arxiv.org/abs/1906.02964.
3. M. Speckbacher, *Sampling trajectories for the short-time Fourier transform* (first posted 2021-06-02), https://arxiv.org/abs/2106.01018.
4. K. Esmeral and N. Vasilevski, *C*-algebra generated by horizontal Toeplitz operators on the Fock space* (2016), https://doi.org/10.1007/s40590-016-0110-1.
5. Arroyo Neri and collaborators, *Toeplitz Operators with Lagrangian Invariant Symbols Acting on the Poly-Fock Space of C^n* (2021), https://doi.org/10.1155/2021/9919243.
6. Jacobi triple-product identity and Poisson summation (classical identities; used in the indicated normalizations).
