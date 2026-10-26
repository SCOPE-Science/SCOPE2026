# Exact thermal unimodality threshold for a harmonically trapped run-and-tumble particle

## Finding

Let \(X_t\) solve
\[
 dX_t=(-\kappa X_t+vS_t)\,dt+\sqrt{2D}\,dW_t,
\]
where \(\kappa,v,D>0\), \(W\) is standard Brownian motion, and the independent symmetric telegraph state \(S_t\in\{-1,1\}\) flips at rate \(\lambda>0\) in either direction. Write \(a=\lambda/\kappa\), \(\tau=D\kappa/v^2\), and \(Y=\kappa X/v\) in the stationary law. For \(0<a<1\) there exists exactly one number \(\tau_c(a)>0\) such that the stationary density of \(Y\) has exactly two symmetric strict modes when \(0<\tau<\tau_c(a)\), and exactly one mode, at zero, when \(\tau\ge\tau_c(a)\). At equality the central mode is quartically flat: its second derivative vanishes and its fourth derivative is strictly negative. For \(a\ge1\), the density has exactly one mode for every \(\tau>0\).

Specifically, define \(z_c(a)>0\) as the unique positive solution of
\[
 {}_1F_1\!\left(\frac12;a+\frac12;-z\right)
 -\frac{z}{a+\frac12}{}_1F_1\!\left(\frac32;a+\frac32;-z\right)=0.
\]
Then \(\tau_c(a)=1/(2z_c(a))\) and
\[
 \lim_{a\downarrow0}\tau_c(a)=1,
 \qquad \lim_{a\uparrow1}\tau_c(a)=0.
\]
For example \(\tau_c(1/2)=0.316464340348\ldots\). This locates the complete thermal shape transition, including its uniqueness, rather than merely the athermal threshold.

## Assumptions and scope

The environment is a stationary irreducible two-state continuous-time Markov chain with independent Brownian forcing; the potential is harmonic, the propulsion speed is fixed, and the temperature parameter satisfies \(D>0\). Modes mean local maxima of the smooth stationary *position* density, and strict modes are isolated local maxima. Both switching directions have the same rate \(\lambda\). All assertions cover every \(a,\tau>0\); no finite discretization or numerical approximation is assumed in the theorem. The claim is for one-time stationary distributions, not dynamical relaxation.

## Proof

**1. Exact stationary decomposition.** Write the two-sided stationary solution as
\[
 X_0=v\!\int_{-\infty}^0 e^{\kappa s} S_s\,ds
       +\sqrt{2D}\!\int_{-\infty}^0 e^{\kappa s}\,dW_s.
\]
The second independent term is normal with variance \(D/\kappa\). For the dimensionless first term \(U\), stationarity of the two telegraph component densities and zero total current give \(\rho_+-\rho_-=u(\rho_++\rho_-)\) and
\[
 \frac{d}{du}[(1-u^2)f(u)]=-2au f(u).
\]
Normalization yields
\[
 f_a(u)=\frac{(1-u^2)^{a-1}}{\mathrm B(1/2,a)}\,\mathbf1_{(-1,1)}(u).
\]
Thus \(Y\overset d=U_a+\sqrt\tau G\) with independent \(G\sim N(0,1)\); its smooth density is \(p_{a,\tau}=f_a*\varphi_\tau\).

**2. The central-curvature equation.** Put
\[
 I_a(z)=\int_{-1}^1(1-u^2)^{a-1}e^{-zu^2}\,du
      =\mathrm B(1/2,a)\,{}_1F_1(1/2;a+1/2;-z),\quad
 F_a(z)=I_a(z)+2zI_a'(z).
\]
Differentiating under the integral at \(z=1/(2\tau)\) gives
\[
 p_{a,\tau}''(0)
 =-\frac{F_a(1/(2\tau))}{\tau\sqrt{2\pi\tau}\,\mathrm B(1/2,a)}.
\]
The Kummer equation is
\[
 zI_a''(z)+(z+a+1/2)I_a'(z)+I_a(z)/2=0.
\]
At **every** positive zero \(z_*\) of \(F_a\), the identity \(I_a'=-I_a/(2z_*)\) gives the exact crossing derivative
\[
 F_a'(z_*)=\frac{(a-1)I_a(z_*)}{z_*}.
\]
For \(0<a<1\) this is strictly negative. Also \(F_a(0)=\mathrm B(1/2,a)>0\), while Watson's integral asymptotic gives
\[
 F_a(z)=-\sqrt\pi(1-a)z^{-3/2}(1+O_a(z^{-1}))<0
 \quad(z\longrightarrow\infty).
\]
Existence follows by continuity; uniqueness follows because all zeros are strict downward crossings: two distinct downward crossings would require an intervening upward crossing. Hence precisely one root exists. Its hypergeometric form is the displayed equation in the finding.

**3. Global mode count, not merely a local test.** We use the following elementary consequence of strict total positivity of the exponential kernel. If a compactly supported signed measure has at most \(m\) sign alternations along the real line, its bilateral Laplace transform has at most \(m\) real zeros, counting multiplicities, unless identically zero. For completeness: if there were \(m+1\) zeros (with repeated zeros represented by derivative conditions), take the associated \(m+1\) exponential-polynomial basis functions. A nonzero linear combination can be chosen to vanish at precisely the \(m\) sign-boundaries of the measure; the strict Chebyshev property of ordered exponentials forces these to be its only zeros, all simple. Choosing its sign to match the measure makes its integral strictly positive, while the zero and derivative conditions force that same integral to vanish. This is impossible. The Chebyshev property itself follows from the nonvanishing ordered exponential Vandermonde determinant (or induction by Rolle's theorem after division by the smallest exponential).

For \(0<a<1\), truncate \(f_a\) to \([-1+\epsilon,1-\epsilon]\), keeping its original shape and renormalizing. Its distributional derivative has precisely the sign pattern \(+,-,+,-\) (the first and last signs come from jumps at the cutoff endpoints), i.e. three alternations. After Gaussian convolution, the derivative is an exponential transform of this signed measure times an everywhere-positive Gaussian prefactor, hence has at most three sign alternations on the real line. As \(\epsilon\downarrow0\), the Gaussian-smoothed densities and all derivatives converge locally uniformly; any four alternating positive/negative open intervals in the limit would persist for small \(\epsilon\), a contradiction. Hence the limiting derivative also has at most three sign alternations.

The density is even, and for \(y>1\) its derivative is strictly negative. If \(p''(0)>0\), the derivative is positive immediately to the right of zero and negative beyond one; it therefore has at least one positive-to-negative transition, its negative counterpart, and the central transition. The three-alternation bound forbids any further local maxima: precisely two symmetric strict outer modes and a strict central minimum occur. If \(p''(0)<0\), the derivative is negative near zero and at large positive \(y\). Any positive region on the positive half-line would require two further sign alternations there and, by symmetry, two on the negative half-line, in addition to the central alternation. Five alternations are impossible. Hence zero is the unique strict mode (possible horizontal stationary inflections would not be modes).

At the critical temperature, differentiate \(p''(0)\) with respect to \(\tau\): since \(F_a'(z_c)<0\) and \(d(1/(2\tau))/d\tau<0\), this derivative is strictly negative. The Gaussian heat equation \(\partial_\tau p=\frac12\partial_y^2p\) therefore gives \(p''''(0)<0\). The origin is a quartically flat strict maximum. Its derivative is negative immediately to the right and past the compact active support, so a further positive region would require five sign alternations: no other modes exist. Finally, when \(a\ge1\), \(f_a\) is symmetric unimodal (uniform at equality); its convolution with a centered Gaussian is strictly unimodal. This also follows by writing \(f_a\) as a positive mixture of centered uniform densities and differentiating each Gaussian-smoothed uniform, whose derivative is strictly negative on \((0,\infty)\).

**4. Endpoint limits.** As \(a\downarrow0\), \(U_a\) converges weakly to equally weighted masses at \(\pm1\). At every fixed \(z\ge0\), normalized \(F_a(z)\) tends to \((1-2z)e^{-z}\), which has its unique zero at \(z=1/2\). The strict-crossing result and sign bracketing imply \(z_c(a)\to1/2\), and hence \(\tau_c(a)\to1\). As \(a\uparrow1\), the normalized integrals tend to the uniform law, whose curvature function is \(F_1(z)=2e^{-z}\) **without normalization by its beta integral**, positive for each finite \(z\). Thus \(z_c(a)\to\infty\) by uniqueness and sign bracketing, and \(\tau_c(a)\to0\).

## Verification

A standalone Python program `verify.py` computes the critical root independently by scalar bracketing, checks the Kummer derivative identity against centered differences, evaluates the stationary curvature by independent 160-node Gauss–Jacobi quadrature, and samples modal geometry on both sides of the transition. It also checks both limiting regimes. All 54 implemented checks pass with Python 3, NumPy, and SciPy. These finite numerical tests do not establish the all-parameter assertion, which is proved above. Example roots include \(\tau_c(0.1)=0.766833597220\ldots\), \(\tau_c(0.5)=0.316464340348\ldots\), and \(\tau_c(0.9)=0.119126237496\ldots\).

## Relationship to prior work

Wang et al. (2014) reported harmonic trapping and qualitative two-peak nanoswimmer behavior. García-Millán and Pruessner (2021), Appendix D, provided the exact stationary Hermite-series law and plots varying thermal diffusion. Frydel (2022), Sec. II.A, Eq. (15), already explicitly derived the same beta–Gaussian convolution and discussed thermal destruction of bimodality in a related graphical analysis (the latter figure is in the paper's 2D discussion). These distributional identities and qualitative observations are not claimed as new. The present claim evaluates a unique **global** thermal critical curve for the symmetric 1D process, proves exactly two or one modes everywhere, characterizes the quartic borderline, and proves both endpoint limits by a Kummer crossing identity and an oscillation bound. Sevilla and Meléndez Mora's 2026 arXiv abstract also discusses the convolution and qualitative crossover; its full text could not be inspected, so possible overlapping detailed classifications are an outstanding priority risk. More general theory of Gaussian total positivity is used as a standard tool, not claimed as new.

## Limitations

Only an exactly symmetric two-velocity Markov active particle in a one-dimensional harmonic well with independent additive Gaussian thermal noise is covered; no claims are made for asymmetric flipping, nonharmonic potentials, colored thermal forcing, interacting particles, finite-time modality, or higher-dimensional active motion. The critical curve is specified implicitly rather than in elementary closed form. Independent originality and mathematical checks have not been performed; a relevant 2026 full text remains inaccessible. The numerical mode mesh alone is not an infinite proof.

## References

1. Z. Wang, H.-Y. Chen, Y.-J. Sheng, H.-K. Tsao, *Diffusion, sedimentation equilibrium, and harmonic trapping of run-and-tumble nanoswimmers*, Soft Matter **10** (2014), 3209–3217, DOI: 10.1039/C3SM53163E (first public 2014-01-23).
2. R. García-Millán and G. Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production*, J. Stat. Mech. (2021) 063203, DOI: 10.1088/1742-5468/ac014d; Appendix D.
3. D. Frydel, *Positing the problem of stationary distributions of active particles as third-order differential equation*, Phys. Rev. E **106** (2022) 024121, DOI: 10.1103/PhysRevE.106.024121; Sec. II.A, Eqs. (12), (15).
4. F. J. Sevilla and J. A. Meléndez Mora, *Nonequilibrium statistics of harmonically trapped run-and-tumble particles: An exact convolution approach*, arXiv:2608.21781 (2026); abstract only accessible during this review.
5. S. Karlin, *Total Positivity*, Stanford University Press (1968); classical variation-diminishing/Chebyshev property of the Gaussian and exponential kernels.
