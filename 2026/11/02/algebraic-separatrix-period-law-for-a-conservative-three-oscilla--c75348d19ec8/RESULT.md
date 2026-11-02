# Algebraic separatrix-period law for a conservative three-oscillator phase ring

## Finding

For the three-site nearest-neighbor phase ring at quadrature phase lag, the two nonzero-energy families of reduced periodic orbits have an exact physical-time period quadrature. If \(T(E)\) is the minimal reduced period on the positive energy \(E\), then

\[
\lim_{E\downarrow0} E^{1/3}T(E)
=2B\!\left(\frac13,\frac12\right)
=2^{2/3}B\!\left(\frac13,\frac13\right)
=8.4130926319527255670\ldots .
\]

The corresponding negative-energy family has the same period. In particular, the period diverges as a power \(E^{-1/3}\), rather than logarithmically as at a hyperbolic separatrix. At the opposite end of each annulus, the period tends to \(4\pi/3\). The Hamiltonian conservation law itself is known; the claim concerns the **energy-resolved period, exact prefactor, and both endpoint laws** for this specified ring.

## Assumptions and scope

Take three identical phases \(\theta_j\in\mathbb R/(2\pi\mathbb Z)\), indices modulo three, satisfying

\[
\dot\theta_j=\sin(\theta_{j-1}-\theta_j+\pi/2)
+\sin(\theta_{j+1}-\theta_j+\pi/2).
\]

There is no normalization factor multiplying this right-hand side. Work modulo the common rotation and put \(x=\theta_2-\theta_1\) and \(y=\theta_3-\theta_2\), both modulo \(2\pi\). With

\[
H(x,y)=\sin x+\sin y-\sin(x+y),\qquad H_*=\frac{3\sqrt3}{2},
\]

write \(T(E)\) for the least positive period of the **reduced** flow with \(H=E\), for \(0<E<H_*\). This is not a claim that an arbitrary lift of all three original phases is periodic without passing to common-phase equivalence. The beta function is \(B(a,b)=\int_0^1t^{a-1}(1-t)^{b-1}\,dt\).

## Proof

**1. Reduction, geometry and orbit classification.** Since \(\sin(u+\pi/2)=\cos u\), subtraction of adjacent phase equations yields

\[
\dot x=\cos y-\cos(x+y)=\partial_yH,
\qquad
\dot y=\cos(x+y)-\cos x=-\partial_xH.
\]

On \((0,2\pi)^2\), the exact factorization is

\[
H=4\sin(x/2)\sin(y/2)\sin((x+y)/2).
\]

Thus \(H>0\) precisely in the open triangle \(D_+=\{x>0,y>0,x+y<2\pi\}\), and \(H<0\) in the other open triangle \(D_-=\{x>0,y>0,x+y>2\pi\}\). The common boundary is the zero-energy separatrix formed by \(x=0\), \(y=0\), and \(x+y=2\pi\), interpreted on the torus. These three arcs are homoclinic to \((0,0)\) modulo \(2\pi\). The only equilibria on the torus are \((0,0)\), the positive center \((2\pi/3,2\pi/3)\), and the negative center \((4\pi/3,4\pi/3)\). This follows by solving \(\cos x=\cos y=\cos(x+y)\); the two centers have energies \(\pm H_*\).

Fix \(x\in(0,2\pi)\). The function \(y\mapsto H(x,y)\), restricted to \(0<y<2\pi-x\), is strictly increasing and then strictly decreasing, with maximum

\[
g(x)=2\sin(x/2)(1+\cos(x/2)).
\]

It has a unique maximum \(H_*\) at \(x=2\pi/3\). Thus, for each \(0<E<H_*\), the equation \(g(x)=E\) has exactly two roots \(x_-(E)<2\pi/3<x_+(E)\). Between these roots the level \(H=E\) consists of precisely two smooth \(y\)-graphs joined at their turning points. It is a single compact regular simple closed curve, hence a single periodic orbit. The negative-energy case is mapped to it by \((x,y,t)\mapsto(-x,-y,-t)\), so its minimal period is the same.

**2. Exact physical-time quadrature.** Define

\[
 c_E(x)=\cos(x/2)-\frac{E}{2\sin(x/2)}.
\]

The two branches satisfy \(\cos(y+x/2)=c_E(x)\), and on each
\( |\dot x|=2\sin(x/2)\sqrt{1-c_E(x)^2}\). Each branch traverses \([x_-,x_+]\) once. Consequently the *full* primitive period (not a half-period) is

\[
\boxed{\displaystyle T(E)=\int_{x_-(E)}^{x_+(E)}
\frac{dx}{\sin(x/2)\sqrt{1-c_E(x)^2}}.}
\]

The integrand has integrable inverse-square-root singularities at its two turning points.

**3. Singular asymptotic and exact prefactor.** Set \(\varepsilon=E^{1/3}\). Expansion of \(g\) at the two ends gives the *different* turning scales

\[
 x_-(E)=E/2+O(E^3),\qquad
 2\pi-x_+(E)=2\varepsilon+O(\varepsilon^3).
\]

At the left end write \(x=\varepsilon t\). For each fixed \(t>0\), the rescaled quadrature integrand converges to

\[
\varepsilon\,\frac{dx}{\sin(x/2)\sqrt{1-c_E(x)^2}}
\longrightarrow\frac{4\,dt}{\sqrt t\sqrt{t^3+8}},
\]

or, more transparently, the contribution \(\varepsilon\,d x/[\sin(x/2)\sqrt{1-c_E(x)^2}]\) tends to \(4\,dt/(\sqrt t\sqrt{t^3+8})\). At the right end write \(2\pi-x=\varepsilon t\). The allowed limiting range is \(t>2\), and the corresponding measure tends to \(4\,dt/(\sqrt t\sqrt{t^3-8})\).

These pointwise limits can be integrated. To justify this, first fix a small \(\delta>0\) and split the integral into \([x_-,\delta]\), \([\delta,2\pi-\delta]\), and \([2\pi-\delta,x_+]\). The middle term is uniformly bounded, hence disappears after multiplication by \(\varepsilon\). On the left, the short interval \([x_-,2x_-]\) contributes only \(O(1)\) to the unscaled period, because \(1+c_E\) vanishes simply at \(x_-\) while \(x_-\asymp E\); on the rest one can use \(1-c_E\asymp x^2+E/x\), \(1+c_E\ge c_0>0\), obtaining an integrable \(Ct^{-1/2}(1+t^3)^{-1/2}\) majorant after \(x=\varepsilon t\). On the right, writing \(u=2\pi-x\), the relation \(1+c_E\asymp(u^3-u_+^3)/u\) near the turning point \(u_+=2\pi-x_+\) gives an integrable \(C(t-t_+(E))^{-1/2}\) bound for \(t\) in a fixed neighborhood of \(t_+(E)=u_+/\varepsilon\to2\); away from that neighborhood the rescaled integrand is bounded by \(Ct^{-2}\). Dominated convergence, including the moving right endpoint, now yields

\[
\lim_{E\downarrow0}E^{1/3}T(E)
=4\int_0^\infty\frac{dt}{\sqrt{t(t^3+8)}}
+4\int_2^\infty\frac{dt}{\sqrt{t(t^3-8)}}.
\]

Substituting \(t=2u\), followed by \(z=u^3\) in the first integral and \(z=u^{-3}\) in the second, gives respectively

\[
\frac23 B\!\left(\frac16,\frac13\right),
\qquad\frac23 B\!\left(\frac13,\frac12\right).
\]

The gamma reflection identity gives \(B(1/6,1/3)=2B(1/3,1/2)\), so the total is exactly \(2B(1/3,1/2)\). Gamma duplication gives the alternative \(2^{2/3}B(1/3,1/3)\) expression.

**4. Center endpoint.** The Hessian at the positive center is

\[
D^2H=\begin{pmatrix}-\sqrt3&-\sqrt3/2\\-\sqrt3/2&-\sqrt3\end{pmatrix},
\]

whose determinant is \(9/4\). The canonical linearized frequency is \(3/2\). The continuous nonlinear period function near a nondegenerate planar Hamiltonian center therefore tends to \(2\pi/(3/2)=4\pi/3\). The negative center is related by time reversal and has the same limit.

## Verification

The standalone program `VERIFY.py` computes the exact beta-function identities at 45-digit precision and independently evaluates the full period quadrature after desingularizing both turning points. For \(E=10^{-1},10^{-2},10^{-3},10^{-4},10^{-5}\), the computed values of \(E^{1/3}T(E)\) are, respectively, approximately \(8.0434040161\), \(8.3330576842\), \(8.3958454418\), \(8.4093767950\), and \(8.4122920787\), approaching the proven constant \(8.4130926320\). The code also checks the center frequency. Numerical quadrature alone is not a proof of the asymptotic limit.

Reproduce using `python VERIFY.py` with the `mpmath` Python package.

## Relationship to prior work

Yan, Ozawa, Kori, and Sato study the same nearest-neighbor phase-ring model and expressly identify the Hamiltonian \(\pi/2\) limit; they analyze basin geometry, winding-number stabilization and large-ring transients, not the exact small-ring reduced period law. Ashwin, Bick, and Burylko established/reviewed the integrability and time-reversal organization of fully symmetric three-oscillator networks with even coupling, including the existence of periodic islands. Those facts imply no claim of novelty for integrability, the energy foliation, or the mere existence of periodic trajectories. The present quantitative result resolves the exact asymptotic period prefactor of the cubic-degenerate homoclinic boundary for this fixed natural model. The generic hyperbolic-separatrix logarithmic law and the nondegenerate-center local-period theory have different hypotheses and do not provide this coefficient.

## Limitations

The result concerns exactly three oscillators, unit neighbor coupling, exact quadrature lag, and phase-difference orbits. It makes no assertion about phase lifts closing, about nonzero dissipation, more sites, noisy dynamics, basin transients, or period monotonicity at intermediate energies. The known Hamiltonian structure is not a new contribution. The period-asymptotic originality assessment is limited to the stated inspected literature; unseen earlier specialized formulas remain a possible priority risk.

## References

1. Jin Yan, Ayumi Ozawa, Hiroshi Kori, and Yuzuru Sato, *Basin Riddling in Coupled Phase Oscillators*, arXiv:2603.02135v1, first posted 2026-03-02; revised as *Basin Metamorphosis in Coupled Phase Oscillators*, arXiv:2603.02135v2 (2026-07-09), https://arxiv.org/pdf/2603.02135 .
2. Peter Ashwin, Christian Bick, and Oleksandr Burylko, *Identical Phase Oscillator Networks: Bifurcations, Symmetry and Reversibility for Generalized Coupling*, Frontiers in Applied Mathematics and Statistics **2**, 7 (2016), https://doi.org/10.3389/fams.2016.00007 .
3. *Monotonicity of the Period Function in Planar Separable Hamiltonian Systems: An Extension of Chicone’s Criterion*, Qualitative Theory of Dynamical Systems (2026), https://doi.org/10.1007/s12346-026-01595-w . Different separable class, used for period-function comparison rather than for the proof.
