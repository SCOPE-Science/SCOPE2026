# Sharp field-area pumping envelope and its fractional-power cusp

## Finding
For every temperature \(T>0\), gap ratio \(\rho>0\), and finite Euclidean control-area budget \(A>0\), the geometric heat transferred by the equal-coupling two-bath qubit pump has a unique area-optimal region, up to planar null sets. Its boundary is an explicit curvature superlevel contour. The complete optimum is given parametrically below; in particular,
\[
\mathcal H_\rho(A)=\frac{\operatorname{sech}^2\rho}{T}A-
\frac{3^{5/3}}{5\,2^{1/3}}\operatorname{sech}^2\rho
\left(\frac{\tanh\rho}{\rho}\right)^{2/3}
\frac{A^{5/3}}{T^{7/3}}+o(A^{5/3})
\quad(A\downarrow0).
\]
The sharp deficit from the available gap-restricted Landauer flux has a stretched-exponential large-area law:
\[
T\bigl[\log2-\rho\tanh\rho+\log\cosh\rho\bigr]-\mathcal H_\rho(A)
\sim\sqrt{\pi A}\exp\!\left(-\frac{4\sqrt A}{\sqrt\pi\,T}\right)
\quad(A\to\infty).
\]
The leading large-area law is independent of the fixed positive spectral-gap cutoff.

## Assumptions and scope
Take the equal-reservoir-temperature, equal-reservoir-coupling single-qubit adiabatic response of Caselli--Manuel--Arrachea--Cornaglia. Let \((B_x,B_z)\) range over the first control quadrant with \(B_x,B_z\ge0\), \(B=\sqrt{B_x^2+B_z^2}\ge T\rho>0\). The authors' geometric curvature in this quadrant is
\[
\mathcal F_L(B_x,B_z)=-\frac1T\sin(2\theta)\operatorname{sech}^2(B/T),
\quad B_x=B\sin\theta,\quad B_z=B\cos\theta,\quad0\le\theta\le\frac\pi2.
\]
For a bounded Jordan domain \(E\) in this admissible field region, with piecewise continuously differentiable boundary and *ordinary Euclidean* area \(|E|=A\), choose circulation orientation so that the absolute geometric flux is
\(\mathcal H(E)=\int_E|\mathcal F_L|\,dB_x\,dB_z\).
This is a quasistatic *geometric-flux* optimization only: it is not an optimization of finite-speed heat, dissipation, efficiency, circuit depth, or cycle duration. Boundary arcs at \(B=T\rho\) are allowed. The positive gap avoids any degeneracy at the origin.

Define \(q\in(0,\operatorname{sech}^2\rho)\),
\[
\theta_-(q)=\frac12\arcsin(q\cosh^2\rho),\quad
\theta_+(q)=\frac\pi2-\theta_-(q),\quad
R_q(\theta)=\operatorname{arcosh}\sqrt{\frac{\sin2\theta}{q}},
\quad G(r)=r\tanh r-\log\cosh r.
\]
The unique optimal region (up to null sets) consists of
\[
E_q=\{(B_x,B_z):\ \theta_-<\theta<\theta_+,\ 
\rho<B/T<R_q(\theta)\}.
\]
For every \(A>0\), its uniquely determined parameter \(q=q(A)\) solves
\[
A=\frac{T^2}{2}\int_{\theta_-}^{\theta_+}\bigl[R_q(\theta)^2-\rho^2\bigr]d\theta.
\]
The attained optimum and its exact marginal value are
\[
\mathcal H_\rho(A)=T\int_{\theta_-}^{\theta_+}\sin2\theta\,[G(R_q(\theta))-G(\rho)]d\theta,
\qquad \mathcal H_\rho'(A)=\frac{q(A)}{T}.
\]
Thus \(\mathcal H_\rho\) is strictly increasing and strictly concave on \((0,\infty)\). Equalities and uniqueness concern regions and their oriented boundary loops, not parametrizations or traversal speeds.

## Proof
**Curvature rearrangement and exact profile.** Put \(r=B/T\). The Euclidean area element is \(dB_x\,dB_z=T^2r\,dr\,d\theta\). The nonnegative density to optimize is \(f(r,\theta)=T^{-1}\sin2\theta\,\operatorname{sech}^2r\). For threshold \(q/T\), its strict superlevel set on \(r\ge\rho\) is exactly \(E_q\). Its area is continuous and strictly decreasing in \(q\), from infinity as \(q\downarrow0\) to zero as \(q\uparrow\operatorname{sech}^2\rho\). At each fixed angle the threshold equation has at most one radial solution; consequently every level set has zero planar area. Given any same-area competitor \(E\), subtract the common threshold \(q/T\) from the integrand on the two sides of the symmetric difference. The integral over \(E_q\setminus E\) is nonnegative and that over \(E\setminus E_q\) is nonpositive, so \(\mathcal H(E_q)\ge\mathcal H(E)\), with equality only if \(E\) and \(E_q\) agree a.e. The region \(E_q\) is itself a bounded Jordan domain bounded by an inner circular arc and one outer level curve, proving attainment in the claimed class.

Integrating \(T^2r\) and \(T r\operatorname{sech}^2r\) radially gives the displayed formulas because \(\int r\operatorname{sech}^2r\,dr=G(r)\). Differentiation with respect to the superlevel threshold, or the equal-area exchange identity, gives \(\mathcal H_\rho'(A)=q(A)/T\). Its strictly decreasing marginal value proves strict concavity.

**Small-area law.** Let \(s_0=\operatorname{sech}^2\rho\), \(q=s_0(1-\eta)\), \(u=\theta-\pi/4\), and \(v=r-\rho\ge0\). For fixed positive \(\rho\), uniformly on the shrinking optimal domain,
\[
T f/s_0=1-2\tanh\rho\,v-2u^2+O(v^2+u^4+vu^2).
\]
Hence \(|u|\le\sqrt{\eta/2}+O(\eta^{3/2})\), and the upper radial edge is
\(v=(\eta-2u^2)/(2\tanh\rho)+O(\eta^2)\). Integrating the area element \(T^2(\rho+v)\,du\,dv\) yields
\[
A=T^2\frac{\sqrt2\,\rho}{3\tanh\rho}\,\eta^{3/2}\bigl(1+O(\eta)\bigr).
\]
Integrating the deficit from the maximum density \(s_0/T\) on that domain gives
\[
\frac{s_0 A}{T}-\mathcal H_\rho(A)
=T s_0\frac{\sqrt2\,\rho}{5\tanh\rho}\,\eta^{5/2}\bigl(1+O(\eta)\bigr).
\]
Eliminating \(\eta\) gives the stated exact \(A^{5/3}\) coefficient, which is strictly positive. The fractional power comes from the angular width \(O(\eta^{1/2})\) and the radial thickness \(O(\eta)\) at a positive-gap boundary maximum, not from a generic smooth interior quadratic maximum.

**Large-area law.** Set \(L=\log(1/q)\). Away from the two endpoint angular layers, whose total contribution to the area asymptotics is vanishing,
\[
R_q(\theta)=\frac L2+\log2+\frac12\log\sin2\theta+O\!\left(\frac q{\sin2\theta}\right).
\]
The integrable angular logarithmic moments
\(\int_0^{\pi/2}\log\sin2\theta\,d\theta=-(\pi/2)\log2\) and
\(\int_0^{\pi/2}\log^2\sin2\theta\,d\theta=(\pi/2)\log^22+\pi^3/24\)
therefore give, for fixed \(\rho>0\),
\[
\frac{A(q)}{T^2}=\frac\pi{16}(L+\log2)^2
+\frac{\pi^3}{192}-\frac{\pi\rho^2}{4}+o(1).
\]
The error follows by splitting at \(\sin2\theta=q^{1/2}\), applying the displayed expansion on the interior and bounding the two endpoint layers by their vanishing lengths times quadratic logarithmic factors. Inverting the area expansion yields
\[
q(A)=2\exp\!\left(-\frac{4\sqrt A}{\sqrt\pi T}\right)\bigl(1+O(A^{-1/2})\bigr),
\]
with the implicit constant allowed to depend on fixed \(\rho,T\). The total available flux in the gap-restricted quadrant is
\[
\mathcal H_\rho(\infty)=T\int_\rho^\infty r\operatorname{sech}^2r\,dr
=T\bigl(\log2-G(\rho)\bigr).
\]
Since the optimum has derivative \(q(A)/T\), integrating the marginal value from \(A\) to infinity gives
\(\mathcal H_\rho(\infty)-\mathcal H_\rho(A)
=\int_A^\infty q(a)\,da/T\), whose elementary Laplace-tail asymptotic is the displayed \(\sqrt{\pi A}\) times stretched exponential. No assertion is made uniformly as \(\rho\) varies with \(A\).

## Verification
The standalone `verification/check_heat_envelope.py` uses only the Python standard library. It independently integrates the defining radial/angle formulas using composite Simpson quadrature, checks the flux-cap identity and monotonicity, verifies the sharp local coefficient at three positive gaps, tests the exact envelope derivative numerically, and compares the far-area deficit against its asymptotic law. All 114 finite numerical assertions passed on replay. These numerical checks are corroboration; the optimization and both infinite-limit claims follow from the analytic proof above.

## Relationship to prior work
Caselli, Manuel, Arrachea and Cornaglia (2026), arXiv:2610.09062, provide the qubit curvature and experimentally study specified finite drive contours; their Eqs. (14) and (15) establish the flux integral and discuss the unrestricted-quadrant Landauer limit \(T\log2\). They do not give a sharp envelope indexed by *ordinary enclosed Euclidean field area*, a unique fixed-area contour, or either asymptotic exponent here.

Terren Alonso, Abiuso, Perarnau-Llobet and Arrachea (2021 preprint; 2022 publication), arXiv:2109.12648, optimize a different area-to-thermodynamic-length ratio in a possibly biased qubit thermal engine. Their isoperimetric objective is not the present fixed-Euclidean-area curvature-flux envelope. Caselli, Manuel and Arrachea (2025), arXiv:2511.16591, establish general adiabatic response and a noninteracting-qubit Landauer bound, but not this finite-area tradeoff. The geometric *threshold-set* step is a standard rearrangement/bathtub argument, not claimed as new; the qubit-specific sharp tradeoff, fractional-power coefficient, and gap-insensitive stretched-exponential tail are the evaluated contributions.

## Limitations
The field-area constraint measures accessible region in control coordinates, not thermodynamic length, actuation cost, or physical cycle time. Optimizers assume arbitrary piecewise smooth loops touching the allowed positive-gap boundary and unrestricted maximum field amplitude. The geometric flux is the infinitely slow contribution to the source's full heat dynamics; at finite speed, dissipative terms may change the preferred contour. The unique maximizing region does not imply a unique time parametrization. The result does not address unequal reservoir couplings, interacting qubits, control noise, or simultaneous optimization of flux and dissipation. Literature-wide priority and independent mathematical auditing are not certified.

## References
1. G. J. Caselli, L. O. Manuel, L. Arrachea, P. S. Cornaglia, *Geometric heat pumping on a quantum processor*, arXiv:2610.09062 (first public version, 2026-10-06), particularly Eqs. (14)--(15) and Supplemental Material.
2. P. Terren Alonso, P. Abiuso, M. Perarnau-Llobet, L. Arrachea, *Geometric optimization of non-equilibrium adiabatic thermal machines and implementation in a qubit system*, arXiv:2109.12648 (2021 preprint; PRX Quantum 3, 010326, 2022), particularly Secs. V--VI.
3. G. J. Caselli, L. O. Manuel, L. Arrachea, *Lindbladian approach for many-qubit thermal machines: enhancing the performance with geometric heat pumping by interaction*, arXiv:2511.16591 (2025), particularly Secs. 2--3 and the single-qubit appendix.
