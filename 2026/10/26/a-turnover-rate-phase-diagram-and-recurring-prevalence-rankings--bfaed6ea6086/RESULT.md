# A turnover-rate phase diagram and recurring prevalence rankings in adaptive SIS dynamics

## Finding
Fix infection strength \(\tau>1\), contact-avoidance ratio \(\omega>0\), and a common contact-turnover speed \(\kappa>0\). In the adaptive SIS model
\[
\dot y=y[-1+\tau(1-y)z],\qquad
\dot z=\kappa[1-(1+\omega y)z],\qquad (y,z)\in[0,1]^2,
\]
all values of \(\kappa\) have the **same** endemic equilibrium
\[
E=(y_*,z_*)=\left(\frac{\tau-1}{\tau+\omega},\frac{\tau+\omega}{\tau(1+\omega)}\right).
\]
Nevertheless the transient response undergoes an exact three-regime change. Define
\[
A=\frac{\tau-1}{1+\omega},\quad B=\frac{\tau(1+\omega)}{\tau+\omega},\quad
C=\frac{\omega(\tau-1)}{\tau+\omega},\quad
g=\frac\omega\tau,\quad
\kappa_0=\frac AB,
\]
and
\[
\kappa_{\pm}=\kappa_0\bigl(\sqrt{1+g}\pm\sqrt g\bigr)^2.
\]
The endemic equilibrium is a hyperbolic stable node for \(0<\kappa<\kappa_-\) and \(\kappa>\kappa_+\), a stable focus for \(\kappa_-<\kappa<\kappa_+\), and has a defective repeated negative eigenvalue at either threshold. The spectral exponential relaxation rate
\[
\rho(\kappa)=-\max\{\operatorname{Re}\lambda:\lambda\in\sigma(J_\kappa)\}
\]
attains its **unique global maximum** at \(\kappa_+\), with
\[
\rho(\kappa_+)=A\bigl(1+g+\sqrt{g(1+g)}\bigr).
\]
Within the focus interval the ratio \(\Omega/\lambda\) of angular oscillation frequency to positive exponential damping exponent is uniquely maximized at \(\kappa_0\), and its maximum is exactly \(\sqrt{\omega/\tau}\).

There is a stronger nonlinear implication about comparing policies. For every \(\kappa_b>\kappa_0\), let the two models use the same initial state \((y(0),z(0))=(y_*+\varepsilon,z_*)\), with \(\varepsilon>0\) sufficiently small, and speeds \(\kappa_0\) and \(\kappa_b\) respectively. Then their prevalence difference \(y_{\kappa_0}(t)-y_{\kappa_b}(t)\) changes sign **infinitely often as \(t\to\infty\)**. Thus the two speeds yield identical limiting endemic burden but opposite temporal prevalence rankings along arbitrarily late sequences of times. All these reversals are transient, with amplitudes tending to zero; no persistent epidemic cycle is claimed.

## Assumptions and scope
The state variables \(y,z\) are respectively infected fraction and mean contact-link density. Recovery rate is normalized to one; \(\tau>1\) is effective infection strength. In the source's notation, the functional responses are \(f_{\mathrm{br}}(y)=y\), \(f_{\mathrm{cr}}(y)=1\), with link-breaking rate \(\zeta=\omega\kappa\) and link-creation rate \(\xi=\kappa\). Hence changing \(\kappa\) preserves the ratio \(\zeta/\xi=\omega\); it is a common rate change, not a change in the steady-state balance.

The square \([0,1]^2\) is positively invariant: at \(y=0\) the vertical velocity vanishes, at \(y=1\) it points inward, at \(z=0\) it points inward, and at \(z=1\) it is nonpositive. Since \(\tau>1\), both coordinates of \(E\) lie strictly between zero and one. Consequently the indicated perturbed initial point is admissible for all sufficiently small positive \(\varepsilon\). The spectral statements concern the Jacobian at \(E\); the infinitely many sign changes concern actual nonlinear trajectories in a sufficiently small neighborhood of \(E\), with fixed \(\tau,\omega,\kappa_b\) and \(\varepsilon\) tending to zero.

## Proof
**1. Equilibrium and Jacobian.** If \(y>0\) at equilibrium, the first equation gives \(\tau(1-y)z=1\), while the second gives \(z=1/(1+\omega y)\). Elimination gives the unique positive equilibrium \(E\) displayed above, independent of \(\kappa\). Direct differentiation yields
\[
J_\kappa=
\begin{pmatrix}
-A & \displaystyle\frac{\tau(\tau-1)(1+\omega)}{(\tau+\omega)^2}\\[3pt]
-\displaystyle\frac{\kappa\omega(\tau+\omega)}{\tau(1+\omega)} & -\kappa B
\end{pmatrix}.
\]
The off-diagonal product is \(-\kappa C\), and \(AB+C=\tau-1\). Hence
\[
\operatorname{tr}J_\kappa=-(A+\kappa B),\qquad
\det J_\kappa=\kappa(\tau-1)>0,
\]
so the equilibrium is linearly asymptotically stable for every \(\kappa>0\). Its characteristic discriminant is
\[
D(\kappa)=(A-\kappa B)^2-4\kappa C.
\]

**2. Exact node–focus–node phase.** Divide the discriminant by \(A^2\) and put \(r=\kappa/\kappa_0\). Since \(C/(AB)=\omega/\tau=g\),
\[
\frac{D(\kappa)}{A^2}=(1-r)^2-4rg.
\]
This quadratic is negative precisely for \(r\in((\sqrt{1+g}-\sqrt g)^2,(\sqrt{1+g}+\sqrt g)^2)\), proving the claimed sharp phase interval and the ordering \(0<\kappa_-<\kappa_0<\kappa_+\). At the two endpoints, \(D=0\), and the strictly positive upper-right matrix entry precludes a scalar matrix; therefore the repeated eigenvalue has a nontrivial Jordan block. In the interior, write its two eigenvalues as \(-\lambda\pm i\Omega\), where
\[
\lambda=\tfrac12(A+\kappa B),\qquad
\Omega=\tfrac12\sqrt{4\kappa(\tau-1)-(A+\kappa B)^2}.
\]

**3. Two distinct optimal speeds.** Within the focus region,
\[
\frac{\Omega^2}{\lambda^2}
=\frac{4\kappa(\tau-1)}{(A+\kappa B)^2}-1.
\]
The positive function \(\kappa/(A+\kappa B)^2\) has derivative of the sign of \(A-\kappa B\), so its unique maximum is at \(\kappa=\kappa_0\). There \(\Omega^2/\lambda^2=(\tau-1)/(AB)-1=C/(AB)=g\), proving the frequency-to-damping formula.

The slowest linear decay rate is
\[
\rho(\kappa)=\begin{cases}
\frac12(A+\kappa B-\sqrt{D(\kappa)}),&D(\kappa)\ge0,\\
\frac12(A+\kappa B),&D(\kappa)<0.
\end{cases}
\]
In the focus interval it is strictly increasing. In either open node interval, put \(S=A+\kappa B\), \(T=\tau-1=AB+C\), and \(X=BS-2T\). Then
\[
2\rho'(\kappa)=B-\frac{X}{\sqrt{D(\kappa)}},\qquad
X^2-B^2D(\kappa)=4T C>0.
\]
On \((0,\kappa_-)\), \(X<0\), so \(\rho'>0\). On \((\kappa_+,\infty)\), \(X>0\), so \(\rho'<0\). Continuity at both endpoints proves the unique global optimizer \(\kappa_+\). Since \(\kappa_+B=A(\sqrt{1+g}+\sqrt g)^2\), substitution gives the stated exact maximal rate. At the optimum, the nontrivial Jordan block allows a prefactor proportional to \(t\) in the linearized evolution; \(\rho\) is a **spectral asymptotic exponent**, not an assertion of a pure uniform \(O(e^{-\rho t})\) bound at that defective point.

**4. A strict spectral separation.** At \(\kappa_0\), the eigenvalues are \(-A\pm i\Omega_0\) with \(\Omega_0=\sqrt{\kappa_0 C}>0\). For every \(\kappa_b>\kappa_0\), all eigenvalues of \(J_{\kappa_b}\) have real part strictly less than \(-A\). If its eigenvalues are complex, their real part is \(-(A+\kappa_bB)/2<-A\). If they are real, note that the characteristic polynomial evaluated at \(-A\) is \(\kappa_b C>0\), while their sum is \(-(A+\kappa_bB)<-2A\). Both roots must therefore lie to the left of \(-A\): if \(-A\) were between the roots their polynomial product would be negative, and if both roots were to its right their sum would exceed \(-2A\). The repeated-root case obeys the same strict inequality. Thus the linearized \(\kappa_b\) flow decays at a strictly faster exponential rate than \(e^{-At}\).

**5. Nonlinear infinitely many rank reversals.** Write the state deviation from \(E\) as \(u\). For a fixed speed \(\kappa\), the nonlinear equation has the form \(\dot u=J_\kappa u+N_\kappa(u)\), with the polynomial remainder satisfying \(N_\kappa(u)=O(\|u\|^2)\). The equilibrium is hyperbolic and attracting; standard local stability estimates imply that sufficiently small initial deviations remain small and decay exponentially.

At \(\kappa_0\), choose any sufficiently small \(\delta\in(0,A/2)\) and apply variation of constants. A local estimate \(\|u(t)\|\le K\varepsilon e^{-(A-\delta)t}\) makes the integral
\[
v_\varepsilon=(\varepsilon,0)+\int_0^\infty e^{-J_{\kappa_0}s}N_{\kappa_0}(u(s))\,ds
\]
convergent; moreover \(v_\varepsilon=(\varepsilon,0)+O(\varepsilon^2)\). The integral tail tends to zero after multiplication by \(e^{-J_{\kappa_0}t}\), hence
\[
u(t)=e^{J_{\kappa_0}t}\bigl(v_\varepsilon+o(1)\bigr).
\]
Because \((J_{\kappa_0}+AI)^2=-\Omega_0^2I\), the first coordinate satisfies
\[
e^{At}(y_{\kappa_0}(t)-y_*)
=\bigl(\varepsilon+O(\varepsilon^2)\bigr)\cos(\Omega_0t)
+O(\varepsilon^2)\sin(\Omega_0t)+o(1).
\]
The coefficient of the cosine is nonzero for sufficiently small positive \(\varepsilon\). By the strict spectral separation proved above and the local nonlinear stability estimate for \(\kappa_b\), one has \(e^{At}(y_{\kappa_b}(t)-y_*)\to0\), even at its Jordan point. Therefore
\[
\limsup_{t\to\infty}e^{At}[y_{\kappa_0}(t)-y_{\kappa_b}(t)]>0,
\qquad
\liminf_{t\to\infty}e^{At}[y_{\kappa_0}(t)-y_{\kappa_b}(t)]<0.
\]
Continuity of the prevalence difference now forces infinitely many sign-changing crossings. The comparison uses **the same** initial condition and the **same** endemic equilibrium, with only \(\kappa\) changed. This completes the proof.

## Verification
The standalone standard-library program `CHECK.py` recomputes the equilibrium and matrix identities in 245 exact-rational parameter cases, checks the explicit \(\tau=2\), \(\omega=1\) Jacobians and discriminant, and uses fourth-order Runge–Kutta integration solely to illustrate several alternating finite-time prevalence differences. Run `python3 CHECK.py` from the package directory. Its exact checks corroborate the calculations; the infinite-crossing assertion is proved in Step 5 and **not** inferred from finite simulation.

For the illustrative parameters \(\tau=2\), \(\omega=1\), \(\kappa_0=3/8\), \(\kappa_b=10\), the shared endemic state is \(E=(1/3,3/4)\). From \((1/3+0.01,3/4)\), numerical differences at times \(t=1,5,15,25\) have respective signs \(+,-,+,-\). The two Jacobian spectra are exactly \(-1/2\pm i\sqrt2/4\) and \((-83\pm\sqrt{5449})/12\); the second spectrum lies strictly left of \(-1/2\).

## Relationship to prior work
Achterberg and Sensi introduced this two-variable adaptive SIS model, gave the equilibrium and its Jacobian for precisely these functional responses, proved global endemic attraction, and noted spiraling in an example. Those statements **already cover** the model, the equilibrium and qualitative possibility of a focus; none is asserted here to be new. The present claim instead resolves, along the previously unclassified common-rate scaling \((\xi,\zeta)=(\kappa,\omega\kappa)\), the sharp *entire* node–focus–node interval, the two different rate optima, and the nonlinear recurring reversal of prevalence rankings between identical-equilibrium systems.

The related multigroup aNIMFA model of Achterberg, Sensi and Sottile concerns networked interacting communities, including genuine cycles in two communities, whereas the present recurrent crossings are decaying transients within one community. Earlier Markovian adaptive-SIS moment-closure work by Achterberg and Van Mieghem concerns a larger stochastic network model and its approximations; the available published summary does not establish the present fixed-ratio one-community claims. Such a related source was not accessible in full and creates a residual overlap risk. Neither ordinary local-stability theory alone nor the observation of a spiral identifies the explicit global optimum or proves a nonlinear, infinitely recurring *same-initial-condition* comparison without the strict spectral-gap argument.

## Limitations
These are exact theorems for the stated deterministic, well-mixed, single-community mean-field model with linear break response and constant creation response. The nonlinear crossing conclusion is **local in initial amplitude**; it does not claim every initial condition produces crossings. The crossing amplitude decays to zero, so there is no stable epidemic wave or limit cycle. \(\kappa_+\) optimizes a linearized **asymptotic spectral rate**, not finite-time or globally uniform speed, and it does not optimize the focus frequency-to-decay ratio. The model assumes recovery-rate normalization and does not itself prove analogous behavior for stochastic networks, different functional responses, or heterogeneous multi-community dynamics. An equivalent prior formula under different adaptive-network terminology remains possible without independent validation.

## References
1. M. A. Achterberg and M. Sensi, *A minimal model for adaptive SIS epidemics*, arXiv:2209.01224 (first public 2022-09-02); *Nonlinear Dynamics* **111** (2023), 12657–12670, DOI:10.1007/s11071-023-08498-4, especially Example 2 and its Jacobian.
2. M. A. Achterberg, M. Sensi and S. Sottile, *A minimal model for multigroup adaptive SIS epidemics*, arXiv:2407.17639 (first public 2024-07-24); *Chaos* **35** (2025), 033127, DOI:10.1063/5.0246228.
3. M. A. Achterberg and P. Van Mieghem, *Moment closure approximations of susceptible-infected-susceptible epidemics on adaptive networks*, *Physical Review E* **106** (2022), 014308, DOI:10.1103/PhysRevE.106.014308 (full text not verified accessible for this comparison).
