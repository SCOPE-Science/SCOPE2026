# Sharp late-absorption tail and a weak-sink extremum for a Lindblad half-line quantum walk

## Finding
Fix an integer initial site \(m\geq1\), hopping scale \(\Omega>0\), and Lindblad boundary loss \(\kappa>0\); put \(\eta=\kappa/\Omega\). Let \(T\) be the absorption time, with \(T=\infty\) on nonabsorbed trajectories. Then, for every fixed set of parameters,
\[
\Pr(t<T<\infty)=\frac{C_m(\eta)}{t^2}+O(t^{-3}),\qquad
C_m(\eta)=\frac{2\eta}{\pi\Omega^2}\frac{m^2+\eta^2(m-1)^2}{(1+\eta^2)^2}>0.
\]
Thus the conditional absorption time has finite positive moments of order strictly below two and infinite moments of order two or above. More sharply,
\[
\mathbb E\big[T^2\mathbf1_{\{T\leq R\}}\big]
=2C_m(\eta)\log(\Omega R)+O(1),\qquad R\longrightarrow\infty.
\]
The dimensionless loss that maximizes the **rare-late-absorption amplitude** \(C_m\) is unique and lies strictly below one:
\[
\eta_m^{\mathrm{tail}}=\begin{cases}
1/\sqrt3,&m=1,\\[3pt]
\displaystyle\left(\frac{\sqrt{9(2m-1)^2+4m^2(m-1)^2}-3(2m-1)}{2(m-1)^2}\right)^{1/2},&m\geq2.
\end{cases}
\]
For \(m\geq2\), \(1/\sqrt3<\eta_m^{\mathrm{tail}}<1\) and \(\eta_m^{\mathrm{tail}}=1-m^{-1}+O(m^{-2})\). At \(\eta=1\) this late-tail amplitude decreases as loss is strengthened, while the total eventual absorption probability increases:
\[
C_m'(1)=\frac{1-2m}{2\pi\Omega^2}<0,
\qquad
\left.\frac{dP_{\mathrm{abs}}(m;\eta)}{d\eta}\right|_{\eta=1}
=\frac2\pi\int_0^1\frac{q^{2m-2}(1-q^2)^2}{(1+q^2)^2}\,dq>0.
\]
Here \(P_{\mathrm{abs}}=\Pr(T<\infty)\). Maximizing late-tail mass is not claimed to be a desirable optimization objective; its opposite local response to overall absorption is the structural observation.

## Assumptions and scope
The Hilbert space is \(\ell^2(\mathbb N)\), with site labels \(1,2,\ldots\). The coherent operator and single sink jump are exactly
\[
H_+=\Omega\sum_{j\geq1}|j\rangle\langle j|-\frac\Omega2\sum_{j\geq1}(|j\rangle\langle j+1|+|j+1\rangle\langle j|),\qquad
L=\sqrt\kappa\,|\emptyset\rangle\langle1|.
\]
The surviving state starts at \(|m\rangle\) and evolves under \(H_{\mathrm{eff}}=H_+-i\kappa|1\rangle\langle1|/2\). Its edge amplitude is \(K_m(t)=\langle1|e^{-iH_{\mathrm{eff}}t}|m\rangle\), and the defective absorption-time density is \(F_m(t)=\kappa|K_m(t)|^2\). These conventions, including the factor of two in the hopping and sink, are essential. The results concern fixed \(m,\eta,\Omega\) as time tends to infinity, not joint large-distance or small-loss limits.

## Proof
**1. Exact boundary transform.** The half-line resolvent in Riberi's model gives
\[
G_m(z):=\langle1|(z-H_{\mathrm{eff}})^{-1}|m\rangle
=-\frac2\Omega\frac{q(z)^m}{1-i\eta q(z)},
\quad
z=\Omega\left(1-\frac{q(z)+q(z)^{-1}}2\right).
\]
Choose the root with \(|q(z)|<1\) for \(\operatorname{Im}z>0\). The causal Laplace transform is \(\widehat K_m(s)=iG_m(is)\), for \(\operatorname{Re}s>0\). The boundary value \(G_m(E+i0)\) is smooth in the band interior and outside the band except at the two band endpoints \(E=0,2\Omega\); importantly \(1-i\eta e^{ik}\ne0\) for \(0\leq k\leq\pi\) and positive \(\eta\). Hence no interior upper-boundary singularity changes the endpoint power law, including \(\eta=1\).

**2. Both branch-edge coefficients.** Define
\[
f(q)=\frac{q^m}{1-i\eta q},\qquad
d_m=f'(1)=\frac{m-i\eta(m-1)}{(1-i\eta)^2},\qquad
f'(-1)=(-1)^{m-1}\overline{d_m}.
\]
On the physical upper branch, with consistent square-root branches,
\[
q(z)=1-\sqrt{-2z/\Omega}+O(z)\ (z\to0),\qquad
q(z)=-1+\sqrt{2(z-2\Omega)/\Omega}+O(z-2\Omega)\ (z\to2\Omega).
\]
Expand \(iG_m(is)=-2if(q(is))/\Omega\) at the corresponding Laplace branch points \(s=0,-2i\Omega\). Inverting each square-root singularity using \(\mathcal L^{-1}(s^{1/2})(t)=-t^{-3/2}/(2\sqrt\pi)\), or equivalently applying the endpoint Fourier lemma to the causal upper-boundary transform, yields
\[
K_m(t)=\sqrt{\frac2\pi}(\Omega t)^{-3/2}
\left[e^{-3\pi i/4}d_m+(-1)^{m-1}e^{3\pi i/4}\overline{d_m}\,e^{-2i\Omega t}\right]
+O(t^{-5/2}).
\]
Here the remainder constant may depend on the fixed parameters. To justify it, partition the energy Fourier integral into neighborhoods of the two endpoints and their smooth complement; the endpoint Puiseux expansions contain only half-integer nonanalytic terms, whose next term is order three-halves, and integration by parts makes the smooth complement superpolynomial. Any isolated decaying pole in the strong-loss representation contributes exponentially and is absorbed in the remainder. No assumption of a continuum of independent loss events is made.

**3. Integrate the flux, including interference.** Multiplying the preceding expansion by its complex conjugate gives
\[
F_m(t)=\frac{2\eta}{\pi\Omega^2 t^3}
\left|e^{-3\pi i/4}d_m+(-1)^{m-1}e^{3\pi i/4}\overline{d_m}\,e^{-2i\Omega t}\right|^2+O(t^{-4}).
\]
The square has constant part \(2|d_m|^2\) and an oscillation at frequency \(2\Omega\). An integration by parts shows that its oscillatory part integrates from \(t\) to infinity to order \(t^{-3}\), while the constant term integrates to \(2\eta|d_m|^2/(\pi\Omega^2t^2)\). Since \(|d_m|^2=[m^2+\eta^2(m-1)^2]/(1+\eta^2)^2\), this is precisely \(C_m(\eta)t^{-2}\), with the stated error.

**4. Moments.** The absorption distribution has positive total mass. Its conditional tail is \(C_m(\eta)/(P_{\mathrm{abs}}t^2)+O(t^{-3})\), proving the sharp conditional fractional-moment threshold by tail integration. Using the density expansion directly, \(t^2F_m(t)=(2C_m)t^{-1}+\text{oscillatory}/t+O(t^{-2})\). The oscillatory integral converges by Dirichlet's test, establishing the precise logarithmic divergence of the truncated defective second moment.

**5. Unique extremum and sign opposition.** Direct differentiation gives
\[
C_m'(\eta)=\frac2{\pi\Omega^2}\frac{m^2-3(2m-1)\eta^2-(m-1)^2\eta^4}{(1+\eta^2)^3}.
\]
The numerator is strictly decreasing in \(\eta^2\geq0\), starts positive, and crosses zero exactly once. It is negative at \(\eta=1\), and is nonnegative at \(\eta=1/\sqrt3\), strictly positive there for \(m\geq2\). Solving the quadratic proves the displayed unique maximizer and its position. Expanding the positive root for large \(m\) yields the stated asymptotic. Finally, Riberi's exact total-absorption formula has a term invariant under \(\eta\leftrightarrow1/\eta\) and a finite-distance term \((2\eta/\pi)\int_0^1q^{2m-2}(1-q^2)/(1+\eta^2q^2)\,dq\). Differentiating at one proves the displayed strictly positive derivative; differentiation under the integral is justified by boundedness on the compact interval.

## Verification
Run `python verify.py` with NumPy and SciPy. The program compares the large-time boundary-amplitude expansion with **two different exact Bessel representations** for losses on either side of unity, including unity, over three starting sites; checks the coefficient's analytic derivative and its unique stationary point; and independently differentiates the exact total-absorption integral. In the completed run it passed 66 finite and analytic-identity checks. These diagnostics are finite and do not establish the time-uniform theorem; the proof above supplies the latter.

## Relationship to prior work
Riberi (arXiv:2605.08056, first posted 2026-05-08) provides the exactly solvable Lindblad sink, the boundary Green function, the complete finite-time propagator, and the total eventual absorption integral. Those results are premises, not new claims. The present result extracts the explicit late-absorption **mass** coefficient, the sharp conditional-moment threshold and logarithmic constant, and the unique loss maximizing this mass; it also identifies opposite local responses of late mass and overall success at the sink crossover. Friedman–Kessler–Barkai (2017) proved oscillatory cubic detection-probability decay for **stroboscopically projective measurements on the full line**, using a measurement-interval renewal equation. Didi–Barkai (2021) give a different exponent for position-measurement-induced walks. Neither is asserted to have invented the exponent in this physical setting, and the universal cubic exponent alone is not claimed as a new insight. The distinction is the autonomous, continuously coupled Lindblad sink and its explicit parameter-dependent coefficient.

## Limitations
The unconditional extended-time random variable has an atom at infinity, so all positive unconditional moments diverge for that trivial reason; every moment assertion above is expressly conditional on eventual absorption or truncated over absorbed trajectories. The oscillatory instantaneous density has no single nonoscillatory pointwise \(t^3F_m(t)\) limit; only its integrated tail has the stated scalar coefficient. The coefficient is for fixed positive loss; limits \(\eta\to0\), \(\eta\to\infty\) or \(m\to\infty\) cannot be interchanged with \(t\to\infty\) without separate uniform estimates. No broadband, multidimensional, multiple-sink, or general-graph extension is asserted. Literature-wide priority and independent validation have not been established.

## References
1. F. Riberi, *Boundary-localized non-Hermitian modes in an absorbing quantum walk*, arXiv:2605.08056 (initial public submission 2026-05-08; the full later HTML version was inspected), especially the resolvent, Bessel propagators, and Appendix D.
2. H. Friedman, D. A. Kessler and E. Barkai, *Quantum walks: the first detected passage time problem*, arXiv:1611.05676; Phys. Rev. E 95, 032141 (2017), Sections I and VI.
3. A. Didi and E. Barkai, *Measurement induced quantum walks*, arXiv:2108.13047 (2021), including the infinite-line first-passage comparison.
