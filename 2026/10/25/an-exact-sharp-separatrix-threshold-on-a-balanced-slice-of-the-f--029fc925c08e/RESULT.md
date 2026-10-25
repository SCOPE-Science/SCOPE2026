# An exact sharp separatrix threshold on a balanced slice of the four-oscillator Sakaguchi ring

## Finding
Consider four identical nearest-neighbor phase oscillators indexed modulo four,
\[
\dot\theta_j=\sin(\theta_{j-1}-\theta_j+\alpha)+\sin(\theta_{j+1}-\theta_j+\alpha),\qquad 0<\alpha<\pi/2.
\]
For each \(0<\rho<1\), prescribe the balanced initial phases
\[
(\theta_0,\theta_1,\theta_2,\theta_3)=(w,\pi/2+w,-w,\pi/2-w),\qquad w=\arcsin\rho.
\]
Define the explicit critical amplitude
\[
\rho_c(\alpha)=\bigl(\cos\alpha\,e^{\alpha\tan\alpha}\bigr)^{-1/2}\in(0,1).
\]
Then the relative-phase evolution has an **exact trichotomy**:

1. For \(0<\rho<\rho_c(\alpha)\), all pairwise phase differences converge to zero; the oscillators asymptotically synchronize.
2. For \(\rho=\rho_c(\alpha)\), the trajectory converges to a saddle equilibrium in relative coordinates, precisely
\[
(\delta,u,v)=\left(\pi/2-\alpha,\ \pi/2,\ \arcsin(e^{-\alpha\tan\alpha})\right).
\]
3. For \(\rho_c(\alpha)<\rho<1\), the relative phase follows a nonconstant periodic orbit. Its physical relative-phase period is given by the convergent improper integral in the proof below.

**Prior coverage:** Burylko–Mielke–Wolfrum–Yanchuk (2018) already establish a qualitative periodic-orbit foliation and adjacent dissipative domains for a gauge-equivalent skew-coupled four-ring. The present finding is the **sharp analytic separatrix intersection with this natural one-parameter balanced initial-value slice**, with the explicit saddle and period quadrature; neither qualitative coexistence nor orbital neutrality is presented as newly discovered.

## Assumptions and scope
All phases are real lifts modulo \(2\pi\); the common-phase rotation is quotiented out. Set
\[
\theta=(A+u,B+v,A-u,B-v),\qquad \delta=B-A.
\]
Along the initial data, \(\delta(0)=\pi/2\) and \(u(0)=v(0)=\arcsin\rho\). The invariant chart is \(0<\delta<\pi\), and the initial branch has \(0<u,v<\pi/2\). Phase parameters are restricted to \(0<\alpha<\pi/2\), and the endpoint initial amplitudes \(\rho=0,1\) are deliberately excluded.

## Proof
**1. Exact reduction.** Directly summing and subtracting the four oscillator equations gives
\[
\begin{aligned}
\dot\delta&=-4\cos\alpha\,\sin\delta\,\cos u\cos v,\\
\dot u&=-2\sin u\cos v\cos(\delta+\alpha),\\
\dot v&=-2\sin v\cos u\cos(\delta-\alpha).
\end{aligned}
\]
The identities remain valid through the turning points where \(\cos u\) or \(\cos v\) vanishes. On \(0<\delta<\pi\), differentiation verifies two exact constants of motion,
\[
J_u=\frac{\sin u}{\sqrt{\sin\delta}}
\exp\!\left(\frac{\tan\alpha}{2}(\delta-\pi/2)\right),\qquad
J_v=\frac{\sin v}{\sqrt{\sin\delta}}
\exp\!\left(-\frac{\tan\alpha}{2}(\delta-\pi/2)\right).
\]
Indeed, wherever \(\dot\delta\ne0\),
\[
\frac{d\log|\sin u|}{d\delta}=\frac12(\cot\delta-\tan\alpha),\qquad
\frac{d\log|\sin v|}{d\delta}=\frac12(\cot\delta+\tan\alpha),
\]
and continuity extends conservation across turning points. The initial data yield \(J_u=J_v=\rho\).

**2. Envelopes.** Put \(a=\tan\alpha\). Along the balanced level,
\[
\sin^2u=U_\rho(\delta):=\rho^2\sin\delta\,e^{-a(\delta-\pi/2)},\qquad
\sin^2v=V_\rho(\delta):=\rho^2\sin\delta\,e^{a(\delta-\pi/2)}.
\]
Both functions vanish at \(\delta=0,\pi\), and \(V_\rho(\delta)=U_\rho(\pi-\delta)\). Their respective unique maxima occur at \(\delta_u=\pi/2-\alpha\) and \(\delta_v=\pi/2+\alpha\), with the common maximum
\[
\max_{0<\delta<\pi} U_\rho(\delta)=\max_{0<\delta<\pi}V_\rho(\delta)
=\rho^2\cos\alpha\,e^{\alpha\tan\alpha}.
\]
Because \(\log(\cos\alpha)+\alpha\tan\alpha>0\) for \(0<\alpha<\pi/2\) (its derivative is \(\alpha\sec^2\alpha>0\), and its limit at zero is zero), the critical \(\rho_c\) is strictly between zero and one.

**3. Below the threshold.** If \(\rho<\rho_c\), both envelopes are strictly below one for every \(0<\delta<\pi\). The cosines, positive initially, cannot change sign. Hence \(\dot\delta<0\). The monotone limit of \(\delta\) cannot lie in \((0,\pi/2]\), since there both cosines remain bounded away from zero and the derivative would remain strictly negative. Therefore \(\delta\downarrow0\). Both envelopes tend to zero; because \(u,v\) remain on their initial branches \((0,\pi/2)\), also \(u,v\to0\). This is synchronization modulo common rotation.

**4. At the threshold.** If \(\rho=\rho_c\), the decreasing trajectory remains in \((\delta_u,\pi/2]\) and its first accessible zero of \(\cos u\) occurs at \(\delta=\delta_u\), the double maximum \(U_{\rho_c}(\delta_u)=1\). The smooth ODE prevents arrival at that equilibrium in finite time, and monotonicity forces \(\delta\downarrow\delta_u\). Consequently \(u\uparrow\pi/2\), and
\[
\sin^2v\longrightarrow V_{\rho_c}(\delta_u)=e^{-2\alpha\tan\alpha},
\]
so \(v\to\arcsin(e^{-\alpha\tan\alpha})\). Substitution into the reduced vector field verifies the stated limiting saddle equilibrium. The saddle lies on the known separatrix surface; its precise intersection with the initial-value slice is what is quantified here.

**5. Above the threshold.** If \(\rho_c<\rho<1\), let \(\delta_-\in(\pi/2-\alpha,\pi/2)\) be the unique solution of
\[
\rho^2\sin\delta_-\,e^{-a(\delta_--\pi/2)}=1,
\]
and put \(\delta_+=\pi-\delta_-\). The portion \(\delta_-\le\delta\le\delta_+\) has both envelopes at most one. At \(\delta_-\), the variable \(u\) crosses \(\pi/2\) transversely, and at \(\delta_+\), the variable \(v\) crosses \(\pi/2\) transversely. These crossings glue four smooth sign branches for the two cosines into a compact regular level-set circle on which the reduced vector field has no zero. Every trajectory on this circle is periodic. Since each branch traverses the interval once, the exact period is
\[
T_\rho=\frac1{\cos\alpha}\int_{\delta_-}^{\delta_+}
\frac{d\delta}{\sin\delta\,
\sqrt{1-U_\rho(\delta)}\sqrt{1-V_\rho(\delta)}}.
\]
Both endpoint singularities are integrable inverse square roots because each relevant envelope crosses the value one transversely for \(\rho>\rho_c\). This proves the trichotomy and its sharp boundary. The periodicity concerns phase differences, not necessarily closure of the common-phase motion in the original four-torus.

## Verification
The supplementary file `checks.py` evaluates the reduced equations against the original four-site vector field for 400 random configurations, checks the two conserved quantities numerically, and integrates representative below-threshold, critical, and periodic trajectories. Its output is recorded in `checker_output.txt`. These are finite corroborative tests; the theorem follows from the displayed analytic derivation, monotonicity, and compact regular-level argument. For \(\alpha=0.4\), the computed threshold is approximately \(0.957486043310968\).

## Relationship to prior work
The March 2, 2026 version of Yan–Ozawa–Sato–Kori studies basin structure of the same nearest-neighbor phase-lag equation and motivates determining explicit separatrix geometry. An older, materially closer result must be acknowledged: under the site-dependent gauge shift \(\theta_j=\phi_j+j\pi/2\), the present symmetric-neighbor model becomes
\[
\dot\phi_j=\cos(\phi_{j+1}-\phi_j+\alpha)-\cos(\phi_{j-1}-\phi_j+\alpha),
\]
which is the four-site skew-neighbor model of Burylko–Mielke–Wolfrum–Yanchuk with \(g(s)=-\sin(s-(\pi/2-\alpha))\). Their Proposition 5.2 and subsequent phase-space analysis already establish families of periodic trajectories near the corresponding rotating waves, adjacent attraction regions, and a heteroclinic separatrix surface. Those general qualitative conclusions **cover** any claim that these types of domains are discovered here. Their materially inspected discussion (section 5.2, pp. 2092–2093) does not supply the present two analytic invariants at nonzero phase lag, the exact \(\rho_c\) for the balanced slice, or the stated closed-form saddle coordinates and period quadrature. Mihara–Medrano-T (2018) analyze linearized modes at twisted equilibria, rather than this global initial-value boundary. As with any priority claim, possible alternative exact separatrix parametrizations remain a residual risk.

## Limitations
The threshold is only for the specified one-dimensional balanced initial family, not a complete classification of the three-dimensional relative-phase space or all initial conditions. At equality there is a heteroclinic-type approach to an equilibrium; there is no claim of an additional periodic orbit. The period integral is an improper quadrature, not an evaluated elementary function. Common-phase drift is not classified. Independent mathematical verification and exhaustive priority assessment have not been performed.

## References
1. J. Yan, A. Ozawa, Y. Sato and H. Kori, *Basin Riddling in Coupled Phase Oscillators*, arXiv:2603.02135v1 (first publicly posted March 2, 2026); subsequent version titled *Basin Metamorphosis in Coupled Phase Oscillators*. https://arxiv.org/abs/2603.02135
2. O. Burylko, A. Mielke, M. Wolfrum and S. Yanchuk, *Coexistence of Hamiltonian-Like and Dissipative Dynamics in Rings of Coupled Phase Oscillators with Skew-Symmetric Coupling*, SIAM J. Appl. Dyn. Syst. 17 (2018), 2076–2105, especially Proposition 5.2 and pp. 2092–2093. DOI:10.1137/17M1155685. https://imath.kiev.ua/files/uploads/26/BMWY_SIAM_2018.pdf
3. A. Mihara and R. O. Medrano-T, *Exact dynamical solution of the Kuramoto–Sakaguchi Model for finite networks of identical oscillators*, arXiv:1805.01027v1 (2018). https://arxiv.org/abs/1805.01027
