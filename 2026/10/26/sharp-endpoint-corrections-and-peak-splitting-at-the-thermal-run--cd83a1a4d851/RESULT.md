# Sharp endpoint corrections and peak splitting at the thermal run-and-tumble transition

## Finding

Consider a harmonically trapped one-dimensional run-and-tumble particle with independent thermal diffusion. The Gaussian-convolution stationary density and its implicit shape-transition equation are established in earlier literature, particularly Guéneau, Majumdar and Schehr (2026), Section V.1.1, and are **not** new here. The quantitative refinement proved below is that its critical thermal variance has an explicit *first* correction at perfect persistence and a previously unresolved *logarithm-of-logarithm plus constant* correction near the disappearance of the active phase. The positive-density peaks also separate from the origin with a sharp coefficient of three in squared dimensionless distance.

Write \(a=\gamma/k\in(0,1)\), \(t=Dk/v^2\), with switching rate \(\gamma\), harmonic relaxation rate \(k\), propulsion speed \(v\), and thermal diffusion coefficient \(D\). Let \(t_c(a)\) be the unique positive critical thermal variance, characterized by the previously known vanishing central curvature. Define
\[
 c_0=e^{1/2}\sqrt{2\pi}\operatorname{erf}(1/\sqrt2)=2.821372269284896\ldots.
\]
Then
\[
 t_c(a)=1-c_0a+O(a^2)\qquad (a\downarrow0).
\]
Writing \(\delta=1-a\downarrow0\), \(L=\log(1/\delta)\), and \(\lambda_c=1/[2t_c(1-\delta)]\),
\[
 \lambda_c=L+\tfrac32\log L+\log(2/\sqrt\pi)+o(1).
\]
At each fixed \(a\in(0,1)\), the only stationary maxima for \(t<t_c(a)\) lie at two symmetric locations \(\pm m_a(t)\), and
\[
 m_a(t)^2=3[t_c(a)-t]+O_a([t_c(a)-t]^2)\qquad(t\uparrow t_c(a)).
\]
The mode is unique at the origin for \(t\ge t_c(a)\); it is also unique for all \(t>0\) when \(a\ge1\). The leading limits \(t_c(a)\to1\) as \(a\to0\), and \(t_c(a)\sim1/[2\log(1/(1-a))]\) as \(a\uparrow1\), as well as the implicit central-curvature equation, are previously known.

## Assumptions and scope

The physical stochastic equation is \(dX_s=(-kX_s+v\sigma_s)\,ds+\sqrt{2D}\,dW_s\), with \(k,v,D,\gamma>0\), independent standard Brownian motion \(W\), and a symmetric two-state telegraph process \(\sigma\in\{-1,+1\}\) changing sign at Poisson rate \(\gamma\). Its stationary normalized position is \(Z=kX/v=U+\sqrt tG\), where \(G\sim N(0,1)\) is independent of \(U\), and \(U\) has previously known density
\[
 f_a(u)=\frac{\Gamma(a+1/2)}{\sqrt\pi\Gamma(a)}(1-u^2)^{a-1}\boldsymbol1_{|u|<1}.
\]
The exact Gaussian convolution \(p_{a,t}=f_a*\varphi_t\) and original implicit curvature threshold are assumptions from prior results, or follow directly by conditioning on the independent Ornstein–Uhlenbeck component. All limits above hold with the other physical parameters fixed as specified. The finite-rate peak distance in original units is \((v/k)m_a(t)\).

## Proof

**1. A unique crossing of central curvature.** Let \(Y=U^2\sim\operatorname{Beta}(1/2,a)\). Put \(\lambda=1/(2t)\) and
\[
 F_a(\lambda)=\int_0^1 y^{-1/2}(1-y)^{a-1}e^{-\lambda y}\,dy,
 \quad H_a(\lambda)=-2\lambda F_a'(\lambda)-F_a(\lambda).
\]
The sign of \(p_{a,t}''(0)\) is the sign of \(H_a(1/(2t))\). The function \(F_a\) obeys the Kummer equation
\[
 \lambda F_a''+(a+1/2+\lambda)F_a'+F_a/2=0,
\]
obtained by integrating the derivative of \(y^{1/2}(1-y)^ae^{-\lambda y}\). Every zero \(\lambda_*\) of \(H_a\) is transverse, since
\[
 H_a'(\lambda_*)=2(a-1)F_a'(\lambda_*)>0\quad(0<a<1).
\]
Further, \(H_a(0)=-F_a(0)<0\), and the Laplace endpoint expansion gives
\[
 H_a(\lambda)=\sqrt\pi(1-a)\lambda^{-3/2}+O_a(\lambda^{-5/2})>0
\]
for large \(\lambda\). Thus precisely one zero occurs: every zero crosses upward and cannot cross back. For \(a\ge1\), the athermal beta density is unimodal (uniform at \(a=1\)), and its Gaussian convolution is strictly decreasing for positive positions, so no bimodality occurs.

**2. Exactly two maxima below the crossing.** For \(0<a<1\) regularize the beta density by \(f_{a,\varepsilon}(u)\propto(1+\varepsilon-u^2)^{a-1}\boldsymbol1_{|u|<1}\). Its distributional derivative, in increasing spatial order, has the four signs \(+,-,+,-\), hence three sign changes. Gaussian kernels are strictly totally positive. The variation-diminishing theorem, including multiplicities, bounds the number of zeros of \((f_{a,\varepsilon}*\varphi_t)'\) by three. The analytic convolutions converge locally uniformly as entire functions when \(\varepsilon\downarrow0\); Hurwitz/Rouché transfers that multiplicity bound to \(p_{a,t}'\). Symmetry forces a zero at zero, and for \(x>1\) one has \(p_{a,t}'(x)<0\), directly from the convolution integral. A positive central curvature therefore forces exactly one positive and one negative additional critical point, both strict maxima. Negative central curvature excludes any noncentral maximum, since creating one on each half-axis would require at least five zeros counting multiplicities. At the critical variance the central quartic coefficient is negative by Step 3, so the origin remains the unique maximum. These statements are about the actual density, not a discretization.

**3. The peak-splitting coefficient.** The Gaussian heat identity \(\partial_t p_{a,t}=\tfrac12\partial_{xx}p_{a,t}\) yields \(\partial_t p_{a,t}''(0)=p_{a,t}^{(4)}(0)/2\). Since the sign change of the central curvature as a function of \(t\) is transverse and downward, \(p_{a,t_c}^{(4)}(0)<0\). Even analyticity and the Taylor series of the derivative at \(x=m_a(t)\) give
\[
 0=p_{a,t}''(0)m_a(t)+\frac{p_{a,t_c}^{(4)}(0)}6m_a(t)^3+O_a(|t-t_c|m_a(t)^3+m_a(t)^5),
\]
with \(p_{a,t}''(0)=\frac12p_{a,t_c}^{(4)}(0)(t-t_c)+O_a((t-t_c)^2)\). The simple positive peak obeys \(m_a(t)^2=3(t_c-t)+O_a((t_c-t)^2)\).

**4. Perfect-persistence expansion.** For every smooth \(g\) near \([0,1]\), beta-endpoint concentration gives
\[
 \mathbb E_a[g(Y)]=g(1)+a\int_0^1\frac{y^{-1/2}[g(y)-g(1)]}{1-y}\,dy+O_g(a^2).
\]
Apply this to the known curvature equation \(Q(a,t)=\mathbb E_a[(Y-t)e^{-Y/(2t)}]=0\). At \((a,t)=(0,1)\), \(Q=0\), \(\partial_t Q=-e^{-1/2}\), and
\[
 \partial_a Q=-\int_0^1y^{-1/2}e^{-y/2}\,dy=-\sqrt{2\pi}\operatorname{erf}(1/\sqrt2).
\]
The implicit function theorem yields the stated \(c_0\).

**5. Nearly uniform beta law.** Write \(a=1-\delta\). For \(a=1\), direct integration gives \(H_1(\lambda)=-2e^{-\lambda}\). Uniformly in the balance window \(\lambda=\log(1/\delta)+O(\log\log(1/\delta))\), expansion of \((1-y)^{-\delta}\) and the Laplace method at \(y=0\) give
\[
 H_{1-\delta}(\lambda)=-2e^{-\lambda}+\delta\sqrt\pi\lambda^{-3/2}(1+O(1/\lambda)+O(\delta\log^2\lambda))
 +O(\delta e^{-\lambda}(1+\log\lambda)^2).
\]
The remainders are negligible relative to the two displayed terms in the balancing window, so at the unique zero
\[
 2e^{-\lambda_c}=\delta\sqrt\pi\lambda_c^{-3/2}(1+o(1)).
\]
Taking logarithms and iterating once yields \(\lambda_c=L+\frac32\log L+\log(2/\sqrt\pi)+o(1)\). For completeness, the root is in the stated balance window because evaluating \(H_{1-\delta}\) at \(L\) and \(L+3\log L\) produces opposite signs for sufficiently small \(\delta\), and Step 1 proves uniqueness.

## Verification

Run `python checks/verify.py` with Python, NumPy and SciPy. The independent Gauss–Jacobi quadrature implements the beta distribution directly; a separate hypergeometric implementation checks the central-curvature zero. The executable checks curvature signs, negative critical quartic, local peak splitting, the first persistence correction and the logarithmic critical-layer expression. On the packaged copy 48 deterministic assertions passed. This finite calculation corroborates but cannot prove uniqueness or either asymptotic remainder; those depend on the analytic arguments above.

## Relationship to prior work

Guéneau, Majumdar and Schehr (arXiv:2602.08436v1, Section V.1.1, Eq. 96–97) already derive the **same implicit central-curvature phase boundary**, exhibit the one-dimensional shape transition, and obtain its two *leading* persistence-endpoint limits. Sabhapandit and Majumdar (arXiv:2404.02480v1) consider an exactly equivalent telegraphically driven harmonic-trap center. Sevilla and Meléndez Mora (arXiv:2608.21781v1, Section III) independently give the stationary beta–Gaussian convolution. No claim is made to originality of these inputs, the existence of the crossover, or Gaussian variation diminishing. The new assessed statement consists of the explicit linear correction coefficient, the subleading logarithm-of-logarithm and constant, and their unified exact mode-onset coefficient; this literature comparison is limited by incomplete access to the full 2024 work, which must be checked independently for priority.

## Limitations

These results apply only to one-dimensional independent telegraph switching, linear harmonic confinement and constant additive thermal diffusion. The peak-splitting error constant may depend on fixed \(a\), and the asymptotic claims are not uniform in simultaneous multi-parameter limits. The Gaussian convolution and central-curvature equation were known. A plausible older source for the same process was available only in abstract form; implicit prior coverage of the refinements remains an originality risk. No independent scientific assessment has been performed.

## References

- F. J. Sevilla and J. A. Meléndez Mora, *Nonequilibrium statistics of harmonically trapped run-and-tumble particles: An exact convolution approach*, arXiv:2608.21781v1 (first posted 2026-08-22), Section III.
- M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436v1 (first posted 2026-02-09), Section V.1.1, Eqs. 95–97.
- S. Sabhapandit and S. N. Majumdar, *Noninteracting particles in a harmonic trap with a stochastically driven center*, arXiv:2404.02480v1 (first posted 2024-04-03).
- S. Karlin, *Total Positivity*, Volume I (Stanford University Press, 1968), Gaussian variation-diminishing theory.
