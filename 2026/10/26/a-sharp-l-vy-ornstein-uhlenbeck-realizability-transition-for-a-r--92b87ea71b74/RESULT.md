# A sharp Lévy–Ornstein–Uhlenbeck realizability transition for a randomly switched harmonic trap

## Finding

Let \(\rho_\alpha\) be the normalized stationary position law of the symmetric on/off harmonic-trap diffusion defined below. Its known characteristic function admits a previously unexhibited Lévy–Khintchine decomposition. **For every \(\alpha>0\), this stationary law is infinitely divisible**, with Gaussian variance one and symmetric Lévy density
\[
\nu_\alpha(x)=\frac{(1+\alpha/2)e^{-\sqrt\alpha |x|}-e^{-\sqrt{2\alpha}|x|}}{|x|},\quad x\ne0.
\]
More specifically, it is a convolution of an independent standard Gaussian, a symmetric variance-gamma random variable of shape \(\alpha/2\), and a finite-activity symmetric compound-Poisson random variable with **rate \(\log2\)** and density
\[
f_\alpha(x)=\frac{e^{-\sqrt\alpha|x|}-e^{-\sqrt{2\alpha}|x|}}{|x|\log2},\qquad x\ne0.
\]
The same stationary marginal is **self-decomposable, equivalently a stationary marginal of a constant-rate Lévy-driven Ornstein–Uhlenbeck process, if and only if**
\[
\boxed{\alpha\ge\alpha_c:=2(\sqrt2-1).}
\]
In that range it admits an explicit Ornstein–Uhlenbeck surrogate driven by independent Brownian motion and a symmetric compound-Poisson process with rate exactly \(\alpha\); the positive jump density is
\[
j_\alpha(x)=\frac{\sqrt\alpha}{\alpha}\left[(1+\alpha/2)e^{-\sqrt\alpha|x|}-\sqrt2 e^{-\sqrt{2\alpha}|x|}\right].
\]
For \(0<\alpha<\alpha_c\), infinite divisibility survives but no constant-rate Lévy-driven Ornstein–Uhlenbeck process can have the same stationary one-time distribution.

## Assumptions and scope

Consider a one-dimensional Brownian particle whose harmonic trap switches between an on state (harmonic restoring force) and an off state (free Brownian diffusion), each switching at an equal strictly positive Poisson rate. Rescale position so that the on-state Fokker–Planck drift is \(\partial_z(z\rho_+)\) and the diffusion coefficient in either state equals one. Let \(\alpha>0\) be the resulting dimensionless switching rate. The stationary conditional, state-weighted densities obey
\[
0=\partial_z(z\rho_+)+\partial_z^2\rho_++\alpha(\rho_--\rho_+),\qquad
0=\partial_z^2\rho_-+\alpha(\rho_+-\rho_-).
\]
Because switching is symmetric, each stationary switching state has probability \(1/2\); thus the position marginal is \(\rho_++\rho_-\). All probability laws and Lévy measures below concern this one-dimensional marginal and the full range \(\alpha\in(0,\infty)\). The Ornstein–Uhlenbeck construction reproduces **the stationary marginal only**, not the physical switched diffusion's correlations or path law.

## Proof

**1. Identify the exact marginal from the stationary equations.** Define \(F_\pm(q)=\int_{\mathbb R}e^{iqz}\rho_\pm(z)\,dz\), including the state probabilities. The two Fourier equations are
\[
-qF_+'-q^2F_++\alpha(F_--F_+)=0,
\qquad-q^2F_-+\alpha(F_+-F_-)=0.
\]
The second equation gives \(F_-=\alpha F_+/(\alpha+q^2)\). With \(F_+(0)=1/2\), substitution and integration of the first equation yield
\[
F_+(q)=\tfrac12 e^{-q^2/2}(1+q^2/\alpha)^{-\alpha/2},\quad
F_-(q)=\frac{\alpha F_+(q)}{\alpha+q^2}.
\]
Consequently the normalized stationary marginal has exactly the characteristic function derived for this model in the source paper,
\[
\phi_\alpha(q)=e^{-q^2/2}
\left(1+\frac{q^2}{2\alpha}\right)
\left(1+\frac{q^2}{\alpha}\right)^{-(1+\alpha/2)}.
\tag{1}
\]

**2. Show infinite divisibility and identify the jumps.** For any \(c>0\), the elementary Frullani identity is
\[
\int_{\mathbb R}(\cos(qx)-1)\frac{e^{-c|x|}}{|x|}\,dx
=-\log(1+q^2/c^2).
\tag{2}
\]
Taking the logarithm in (1), applying (2) with \(c=\sqrt\alpha,\sqrt{2\alpha}\), gives
\[
\log\phi_\alpha(q)=-q^2/2+
\int_{\mathbb R}(\cos(qx)-1)\nu_\alpha(x)\,dx.
\tag{3}
\]
The Lévy density is strictly positive because \(1+\alpha/2>1\) and \(\sqrt{2\alpha}>\sqrt\alpha\). It is integrable against \(\min(1,x^2)\) (its near-zero singularity is of order \(1/|x|\), and its tails are exponential). Thus (3) is a genuine Lévy–Khintchine representation for **all** \(\alpha>0\).

To obtain the stated probabilistic splitting, separate (1) into
\[
\phi_\alpha(q)=e^{-q^2/2}
(1+q^2/\alpha)^{-\alpha/2}
\frac{1+q^2/(2\alpha)}{1+q^2/\alpha}.
\]
The middle factor is a centered variance-gamma characteristic function. By (2), the logarithm of the last factor equals
\[
\int_{\mathbb R}(\cos(qx)-1)
\frac{e^{-\sqrt\alpha|x|}-e^{-\sqrt{2\alpha}|x|}}{|x|}\,dx.
\]
Frullani's integral further gives the total mass of this positive measure as
\[
2\int_0^\infty\frac{e^{-\sqrt\alpha x}-e^{-\sqrt{2\alpha}x}}x\,dx=\log2,
\]
proving the rate and density of the independent compound-Poisson component.

**3. Determine the sharp self-decomposability threshold.** Write \(\nu_\alpha(x)=k_\alpha(|x|)/|x|\), with
\[
k_\alpha(r)=(1+\alpha/2)e^{-\sqrt\alpha r}-e^{-\sqrt{2\alpha}r},\qquad r>0.
\]
The canonical one-dimensional criterion says that a symmetric infinitely divisible law with Lévy density of this form is self-decomposable exactly when \(k_\alpha\) is nonincreasing; its independent Gaussian component does not affect this condition. Differentiation yields
\[
-k_\alpha'(r)=\sqrt\alpha\left[(1+\alpha/2)e^{-\sqrt\alpha r}-\sqrt2e^{-\sqrt{2\alpha}r}\right].
\tag{4}
\]
After dividing by \(e^{-\sqrt\alpha r}>0\), nonnegativity of (4) for **all** \(r>0\) is equivalent to
\[
1+\alpha/2\ge \sqrt2e^{-(\sqrt2-1)\sqrt\alpha r}\quad\text{for all }r>0,
\]
which is equivalent to \(1+\alpha/2\ge\sqrt2\). Equality still gives \(-k_\alpha'(r)>0\) at every \(r>0\). Below the boundary (4) is negative on an interval immediately to the right of zero, and the criterion rules out self-decomposability.

**4. Construct and delimit the Ornstein–Uhlenbeck surrogate.** If \(\alpha\ge\alpha_c\), set \(h_\alpha(r)=-k_\alpha'(r)\ge0\). This gives a symmetric probability density \(j_\alpha(x)=h_\alpha(|x|)/\alpha\), since
\[
\int_{\mathbb R}h_\alpha(|x|)\,dx=2k_\alpha(0)=\alpha.
\]
Let \(J_t\) be the compound-Poisson process of rate \(\alpha\) with these iid symmetric jumps, and let \(W_t\) be independent standard Brownian motion. The stationary solution of
\[
dU_t=-U_t\,dt+\sqrt2\,dW_t+dJ_t
\tag{5}
\]
has Gaussian variance \(2\int_0^\infty e^{-2s}\,ds=1\), while its jump Lévy density at \(x>0\) equals
\[
\int_0^\infty e^s h_\alpha(e^s x)\,ds
=\frac1x\int_x^\infty h_\alpha(y)\,dy=\frac{k_\alpha(x)}x.
\]
The same formula holds at negative \(x\) by symmetry. Hence its stationary characteristic function is precisely (3). Conversely a stationary law of any Lévy-driven scalar OU model with positive linear restoring coefficient must be self-decomposable; for \(\alpha<\alpha_c\), Step 3 excludes every such representation. This is an existence/nonexistence statement for OU **marginals**, not pathwise equivalence with the switching model.

## Verification

The standalone `check.py` requires Python 3, NumPy, and SciPy. Execute `python check.py` to check the published and conditional Fourier identities, the two stationary Fourier equations, numerical evaluation of (3) against (1), signs of the background driver across the critical threshold, the exact driving-jump rate, the fixed \(\log2\) compound-Poisson intensity, and even-cumulant identities. Independent gamma-variance-mixture samples provide a stochastic consistency check. These computations are finite checks; the universal inequalities and distributional assertions follow from the displayed analytic proof, not from the sample tests.

## Relationship to prior work

Frydel's 2024 on/off-trap paper, arXiv:2407.12213, supplies the physical stochastic model, the stationary Fokker–Planck problem, the characteristic function (1), and a Gaussian-convolution/variance-mixture interpretation. These are **not** claimed as new. The variance-gamma and gamma-remainder constructions are established prior mathematical tools, including Gardini–Sabino–Sasso's 2021 variance-gamma++ work, arXiv:2106.15452. The general canonical self-decomposability criterion and OU equivalence are also classical. The claim here is their exact combination for the on/off-trap marginal, the identified all-parameter infinite divisibility, the independent compound-Poisson factor of rate \(\log2\), the sharp **model-specific** self-decomposability cutoff, and the explicit OU driver of rate \(\alpha\). The earlier constructions do not by themselves state this trap-parameter phase boundary.

## Limitations

No claim is made about temporal correlations or equality in law of the switched diffusion and the OU surrogate. The on/off switching rates are symmetric, diffusion coefficients equal, and the harmonic stiffness is either zero or the normalized positive value. Replacing these assumptions may change the characteristic function and threshold. Independent completeness review and a search of all possible equivalent prior formulations remain outstanding; specifically, related later work on semi-Markovian switching, arXiv:2607.05173, was only partially accessible. Numerical quadrature and simulation do not establish novelty or infinite-dimensional conclusions.

## References

1. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213v1 (first public 2024-07-16); Phys. Rev. E **110**, 024613 (2024), doi:10.1103/PhysRevE.110.024613.
2. A. Gardini, P. Sabino, and E. Sasso, *The Variance Gamma++ Process and Applications to Energy Markets*, arXiv:2106.15452v1 (2021).
3. D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation*, arXiv:2607.05173v1 (2026); cited as a later, only partially inspected related source, not as an input needed for the theorem.
4. W. A. Jurek and W. Vervaat, *An integral representation for self-decomposable Banach space valued random variables*, Z. Wahrscheinlichkeitstheorie verw. Gebiete **62**, 247–262 (1983); used solely for the classical self-decomposability/OU framework.
