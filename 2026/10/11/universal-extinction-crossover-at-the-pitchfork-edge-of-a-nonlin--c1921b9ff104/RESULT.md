# Universal extinction crossover at the pitchfork edge of a nonlinear SIRS model

## Finding

In the deterministic Zhang--Li SIRS system with the incidence function defined below, the disease-free bifurcation threshold has **two distinct algebraic extinction regimes** and an exact, initial-condition-independent crossover on its pitchfork edge. All times are the original physical time, not the rescaled time used in the motivating article.

Put \(N_0=b/d\), \(\lambda=d+\gamma\), \(\rho=d+\nu\), and \(a=\gamma/\rho\). Keep \(b,d,\gamma,\nu,\alpha>0\) and \(k_1=\lambda/N_0\) fixed. Define \(k_2^*=k_1(1+a)/N_0\) and vary the positive parameter
\[
k_2(\varepsilon)=k_2^*-\frac{\varepsilon}{N_0},\qquad 0\le\varepsilon<k_1(1+a).
\]
Let
\[
C_0=\lambda\alpha+k_2^*(1+a)>0.
\]
For every initial condition \((S_0,I_0,R_0)\) with strictly positive coordinates and \(S_0+I_0+R_0=N_0\), the solution tends to \((N_0,0,0)\). The following limits hold for each fixed \(\varepsilon\):
\[
\lim_{t\to\infty}tI_\varepsilon(t)=\frac1\varepsilon \quad(\varepsilon>0),\qquad
\lim_{t\to\infty}tI_0(t)^2=\frac1{2C_0}.
\]
In either case, \(R_\varepsilon(t)/I_\varepsilon(t)\to a\). Furthermore, keeping the initial state fixed while \(\varepsilon\downarrow0\), define
\[
Y_\varepsilon(\tau)=\frac{C_0}{\varepsilon}
 I_\varepsilon\!\left(\frac{C_0\tau}{\varepsilon^2}\right),\qquad\tau>0.
\]
Then \(Y_\varepsilon\to Y\) uniformly on every compact subinterval of \((0,\infty)\), where \(Y(\tau)>0\) is the **unique** solution of
\[
\boxed{\ \frac1{Y(\tau)}-\log\!\left(1+\frac1{Y(\tau)}\right)=\tau.\ }
\]
The boundary behavior is \(Y(\tau)\sim (2\tau)^{-1/2}\) as \(\tau\downarrow0\), and \(Y(\tau)\sim\tau^{-1}\) as \(\tau\to\infty\). Thus a single universal function interpolates between cubic and quadratic extinction dynamics on the time scale \(C_0/\varepsilon^2\).

## Assumptions and scope

The system is
\[
\begin{aligned}
\dot S&=b-dS-\frac{(k_1I+k_2I^2)S}{1+\alpha I^2}+\nu R,\\
\dot I&=\frac{(k_1I+k_2I^2)S}{1+\alpha I^2}-(d+\gamma)I,\\
\dot R&=\gamma I-(d+\nu)R.
\end{aligned}
\]
All parameters are strictly positive, with \(k_1=\lambda/N_0\) and \(k_2=k_2(\varepsilon)>0\). The initial state lies in the **interior** of the fixed-total-population simplex \(S+I+R=N_0\); for the singular crossover it is fixed independently of \(\varepsilon\). In particular, the theorem makes no assertion for \(I_0=0\), negative \(\varepsilon\), time-varying parameters, stochastic populations, or totals initially different from \(N_0\). The source article identifies \(\varepsilon=0\) as the pitchfork edge of the \(\mathcal R_0=1\) disease-free bifurcation.

## Proof

**1. Exact planar reduction.** Summation gives \(\dot N=b-dN\), so the simplex is invariant, positively invariant along its faces, and compact. Write \(S=N_0-I-R\), \(w=R-aI\), and
\[
C_\varepsilon=\lambda\alpha+k_2(\varepsilon)(1+a)
=C_0-\frac{1+a}{N_0}\varepsilon.
\]
A direct common-denominator expansion using \(k_1N_0=\lambda\) yields the **exact**, not truncated, equations
\[
\begin{aligned}
\dot I&=-D_\varepsilon(I)-B_\varepsilon(I)w,\\
\dot w&=-[\rho-aB_\varepsilon(I)]w+aD_\varepsilon(I),\\
D_\varepsilon(I)&=\frac{I^2(\varepsilon+C_\varepsilon I)}{1+\alpha I^2},\qquad
B_\varepsilon(I)=\frac{I[k_1+k_2(\varepsilon)I]}{1+\alpha I^2}.
\end{aligned}
\]
For \(I>0\), both \(D_\varepsilon(I)>0\) and \(B_\varepsilon(I)>0\).

**2. Global attraction.** At an equilibrium \(R=aI\), equivalently \(w=0\). The first exact equation then excludes every positive-infection equilibrium. The remaining equilibrium in the simplex is \((I,R)=(0,0)\). A hypothetical nonconstant periodic orbit contained in the interior of the convex simplex would enclose an equilibrium by the planar index theorem, which is impossible. At the disease-free point the eigenvalues of the reduced planar system are \(0\) and \(-\rho\). The one-dimensional center graph \(w=h_\varepsilon(I)\) has the small-parameter jet \(h_\varepsilon(I)=(a\varepsilon/\rho)I^2+O(\varepsilon I^3+I^3)\), uniformly as \((I,\varepsilon)\to(0,0)\), and therefore
\[
\dot I\big|_{w=h_\varepsilon(I)}=-\varepsilon I^2-C_0I^3+O(\varepsilon I^3+I^4).
\]
The negative coefficient for \(I>0\) gives a uniform one-sided attracting neighborhood for sufficiently small nonnegative \(\varepsilon\); for any other fixed allowable \(\varepsilon\) the leading term \(-\varepsilon I^2\) gives the same conclusion. The transverse direction is exponentially stable. By Poincare--Bendixson, an interior orbit in the compact simplex must have this equilibrium in its omega-limit set; once it enters the local attracting neighborhood it converges there. This proves global extinction. Equivalently one may invoke the source's disease-free global-stability theorem after observing the absence of endemic equilibria; no new priority is claimed for global attraction alone.

**3. Quantitative fast-variable estimate.** Near the disease-free point choose \(T\) sufficiently large that the trajectory remains in a small neighborhood, \(\rho-aB_\varepsilon(I)\ge3\rho/4\), and \(|\dot I/I|\le\eta\) with \(0<\eta<\rho/8\). Then \(I(s)\le I(t)e^{\eta(t-s)}\) for \(T\le s\le t\). Variation of constants in the exact \(w\) equation implies, with constants locally uniform as \(\varepsilon\downarrow0\),
\[
|w(t)|\le |w(T)|e^{-3\rho(t-T)/4}
 +K\,[\varepsilon I(t)^2+I(t)^3].
\]
Indeed the forcing is \(aD_\varepsilon(I)\), and the exponential kernel is integrable even after multiplying by the backward growth factor \(e^{3\eta(t-s)}\). Since \(I(t)\ge I(T)e^{-\eta(t-T)}\), the exponentially decaying term is asymptotically negligible compared to every fixed positive power of \(I(t)\). Substitution into \(\dot I=-D-Bw\) yields
\[
\dot I=-I^2(\varepsilon+C_0I)
 +O\!\left(I^3(\varepsilon+I)\right)
 +O\!\left(Ie^{-3\rho(t-T)/4}\right)
\]
for small nonnegative \(\varepsilon\); when \(\varepsilon\) is fixed away from zero the leading quadratic estimate follows directly from the same exact equations. Thus \(-\dot I/I^2\to\varepsilon\) for fixed \(\varepsilon>0\), and \(-\dot I/I^3\to C_0\) at \(\varepsilon=0\). Integration of the derivatives of \(I^{-1}\) and \(I^{-2}\), respectively, gives the stated time-weighted limits. The estimate also gives \(w/I\to0\), hence \(R/I\to a\).

**4. Uniform crossover, including the entrance from infinite scaled amplitude.** Fix a positive initial state. Let \(\delta>0\) be arbitrarily small. The proven attraction at \(\varepsilon=0\), continuous dependence over finite time, and uniform one-sided local stability provide a finite \(T_\delta\) such that for all sufficiently small \(\varepsilon\ge0\), the solution at every \(t\ge T_\delta\) stays within distance \(\delta\) of the disease-free point; moreover \(I_\varepsilon(T_\delta)\to I_0(T_\delta)>0\). The preceding estimate and the uniform bound \(|\dot I/I|<\eta<\rho/8\) apply after \(T_\delta\).

For \(\varepsilon>0\) set \(z=C_0I/\varepsilon\) and \(\tau=\varepsilon^2t/C_0\). Define
\[
G(z)=z^{-1}-\log(1+z^{-1}),\qquad
G'(z)=-\frac1{z^2(1+z)}.
\]
Direct differentiation (in physical time before changing variables) gives
\[
\frac{d}{d\tau}G(z)
=-\frac{\dot I}{I^2(\varepsilon+C_0I)}.
\]
The exact equations and estimate of Step 3 show, for \(t\ge T_\delta\), that the right side equals \(1+O(\delta+\varepsilon)+E_\varepsilon(t)\), where
\[
|E_\varepsilon(t)|\le
K\frac{e^{-3\rho(t-T_\delta)/4}}{I(t)(\varepsilon+C_0I(t))}.
\]
The accumulated scaled-time error tends to zero: since \(I(t)\ge I(T_\delta)e^{-\eta(t-T_\delta)}\), its integral is \(O(\varepsilon^2/I(T_\delta)^2)\). Also \(G(C_0I(T_\delta)/\varepsilon)\to0\), and \(\varepsilon^2T_\delta/C_0\to0\). Integrating from \(T_\delta\) therefore gives, uniformly for \(\tau\) on each fixed compact positive interval,
\[
G\!\left(\frac{C_0}{\varepsilon}
I_\varepsilon\!\left(\frac{C_0\tau}{\varepsilon^2}\right)\right)
=\tau+O(\delta\tau)+o_{\varepsilon\downarrow0}(1).
\]
Letting \(\delta\downarrow0\) proves convergence to \(\tau\). The function \(G\) decreases continuously from \(+\infty\) to \(0\) on \((0,\infty)\), so inversion gives local uniform convergence to the unique \(Y=G^{-1}\). Finally \(G(z)\sim1/(2z^2)\) as \(z\to\infty\) and \(G(z)\sim1/z\) as \(z\downarrow0\), proving the two stated limiting regimes.

## Verification

The exact common-denominator identity, the source-model parameter correspondence, and the crossover derivative can be reproduced with the bundled `verify.py` using only the Python standard library. The proof relies on exact identities, planar global dynamics, variation-of-constants inequalities, and a uniform limiting argument; numerical trajectory tests are optional sanity checks and are not used as infinite-time or uniform-limit proofs. One rational witness is \(b=d=\gamma=\nu=\alpha=1\), \(k_1=2\), \(k_2^*=3\), so \(C_0=13/2\), with exact endpoint constant \(\lim_{t\to\infty}tI_0(t)^2=1/13\).

## Relationship to prior work

Zhang and Li [1], Equation (2), give precisely this SIRS model; their Theorem 3 proves disease-free global stability without an endemic equilibrium, and their Theorem 4 identifies a pitchfork at \(\mathcal R_0=1\) and \(\Lambda=\beta(1+q)\), which is equivalent to \(\varepsilon=0\) in original variables. Their local center-manifold cubic derivative establishes the qualitative degeneracy. **None of those qualitative statements alone specifies the singular, uniform-in-parameter physical-time limit for the entire positive simplex.** The result here is the sharp pair of global extinction constants together with the universal entrance-from-infinity crossover function and its time scale. Related SEIRS bifurcation literature [2] concerns a different model, and generic critical-slowing literature [3] discusses scaling in other systems rather than this explicit SIRS limit.

## Limitations

The statement is restricted to fixed total population \(N_0\), deterministic dynamics, and \(\varepsilon\ge0\) with positive infection. It neither establishes global attraction beyond this invariant simplex nor treats the backward-bifurcation side, noise, demographic discreteness, or epidemiological forecasting. The proof uses the established planar center-manifold and Poincare--Bendixson theorems, not a computer-assisted infinite-horizon certificate. The source paper's publisher PDF was not directly retrievable in the source inspection; relevant indexed original article sections, including Equations (2)--(4), Theorems 3--4, and their stated bifurcation conditions, were inspected, while the possibility of additional less readily indexed coverage is a residual priority risk.

## References

[1] Y. Zhang and C. Li, *Bifurcation of an SIRS Model with a Modified Nonlinear Incidence Rate*, Mathematics **11** (2023), 2916, published 2023-06-29. DOI: 10.3390/math11132916; https://www.mdpi.com/2227-7390/11/13/2916 . Original primary MSC2020: 34C23.

[2] M. Amin et al., *Bifurcation and Global Stability of a SEIRS Model With a Modified Nonlinear Incidence Rate*, Journal of Applied Mathematics (2024), DOI: 10.1155/jama/6253301.

[3] T. A. Byrd et al., *Critical slowing down in biochemical networks with feedback*, Physical Review E **100** (2019), 022415, DOI: 10.1103/PhysRevE.100.022415.
