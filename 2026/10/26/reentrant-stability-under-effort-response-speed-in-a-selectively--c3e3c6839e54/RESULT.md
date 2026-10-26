# Reentrant stability under effort-response speed in a selectively harvested predator–prey system

## Finding

Consider the selective-harvest predator–prey model from Yadav and Gakkhar [1], retaining its original dynamic-effort equation. Fix all ecological and economic parameters as below and vary only the positive responsiveness \(\rho\). There is one positive coexistence equilibrium, and **its linear stability returns after an intermediate instability window**, even though the equilibrium coordinates do not change with \(\rho\).

Specifically, its two exact stability-transition speeds are
\[
\rho_\mp=\frac{676965\mp\sqrt{189196677289}}{5034848},\qquad
\rho_-\approx0.048064520728,\quad\rho_+\approx0.220847271644.
\]
The equilibrium is locally exponentially asymptotically stable exactly for \(0<\rho<\rho_-\) and for \(\rho>\rho_+\); it is linearly unstable exactly for \(\rho_-<\rho<\rho_+\). At either critical speed one strictly negative eigenvalue coexists with a simple imaginary pair; its real part crosses transversely, first rightwards and then leftwards. This is a statement about **linear spectral crossings**, not an assertion of nondegenerate nonlinear Hopf bifurcations or the existence of periodic orbits.

## Assumptions and scope

The state variables \(x>0\), \(y>0\), and \(E>0\) respectively represent prey abundance, predator abundance, and harvesting effort. On the positive cone, the model is
\[
\begin{aligned}
\dot x&=x(1-x)-\frac{a x y}{x+y},\\
\dot y&=\frac{e x y}{x+y}-d y-\frac{q m E y}{m_1 E+m_2 y},\\
\dot E&=\rho\left(\frac{p q m y E}{m_1 E+m_2 y}-c E\right).
\end{aligned}
\]
All parameters are positive; \(m\in(0,1]\) is the harvested fraction and \(\rho>0\) is the effort-adjustment rate. The exact specialization is
\[
 a=d=\frac{21}{2},\quad e=13,\quad q=6,\quad m=\frac12,\quad m_1=m_2=p=c=1,
\]
with **only** \(\rho>0\) free. Stability means local stability of this positive equilibrium for the three-dimensional ordinary differential equation. No claim is made about global dynamics, nonlinear periodic solutions, or state behavior on the singular boundary.

## Proof

**Equilibrium.** The third equation at any strictly positive equilibrium reduces to \(3y/(E+y)=1\), hence \(E=2y\). In the second equation this gives
\[
13\frac{x}{x+y}-\frac{21}{2}-2=0,
\quad\text{so}\quad\frac{x}{x+y}=\frac{25}{26} 
\]

Thus \(y=x/25\). The first equilibrium equation gives \(1-x=a/26=21/52\), hence
\[
(x_*,y_*,E_*)=\left(\frac{31}{52},\frac{31}{1300},\frac{31}{650}\right).
\]
Each reduction was reversible on the positive cone, proving **existence and uniqueness among strictly positive equilibria** and independence from \(\rho\).

**Jacobian and cubic.** Differentiation at this equilibrium gives the exact matrix
\[
J(\rho)=\begin{pmatrix}
-281/1352&-13125/1352&0\\
1/52&29/156&-1/3\\
0&4\rho/3&-2\rho/3
\end{pmatrix}.
\]
Its characteristic polynomial is \(\det(\lambda I-J)=\lambda^3+A\lambda^2+B\lambda+C\), where
\[
A=\frac{2704\rho+89}{4056},\qquad
B=\frac{3724\rho+1201}{8112},\qquad
C=\frac{775\rho}{4056}.
\]
All three are strictly positive for all \(\rho>0\). The Routh–Hurwitz determinant is exactly
\[
H(\rho)=AB-C=\frac{10069696\rho^2-2707860\rho+106889}{32902272}.
\]
The discriminant is positive, and its two distinct positive zeros simplify to the stated \(\rho_-\) and \(\rho_+\). Since the leading quadratic coefficient is positive, \(H>0\) on \((0,\rho_-)\cup(\rho_+,\infty)\), while \(H<0\) between them. The cubic Routh–Hurwitz criterion \(A>0\), \(B>0\), \(C>0\), \(AB>C\) therefore proves strict Hurwitz stability exactly on the exterior intervals. For \(H<0\), the Routh first column has two sign changes (\(1,A,H/A,C\)), proving two right-half-plane roots. Because every real \(\lambda\ge0\) gives \(P_\rho(\lambda)>0\), these two roots form a nonreal conjugate pair. Standard smooth-ODE linearization yields the stated local exponential stability or instability away from the critical speeds.

**Critical crossing.** At either zero of \(H\), \(C=AB\) and thus
\[
P_\rho(\lambda)=(\lambda+A)(\lambda^2+B).
\]
Because \(A,B>0\), the imaginary roots \(\lambda_\pm=\pm i\sqrt B\) are simple and the third root \(-A\) is strictly negative. Differentiating \(P_\rho(\lambda(\rho))=0\) and taking real parts at a critical speed gives
\[
\frac{d}{d\rho}\Re\lambda_+(\rho)
=-\frac{H'(\rho)}{2(A(\rho)^2+B(\rho))}.
\]
The quadratic \(H\) has \(H'(\rho_-)<0<H'(\rho_+)\). Thus the imaginary pair enters the right half-plane at the first critical speed and leaves it at the second. No first-Lyapunov-coefficient computation is supplied, so no nonlinear Hopf or periodic-orbit claim follows.

**Robustness.** At the three fixed positive rates \(\rho=1/100\), \(1/10\), and \(1\), the characteristic coefficients stay positive and \(H\) has respective signs \(+,-,+\). The positive equilibrium is hyperbolic at these rates; the implicit-function theorem continues the equilibrium uniquely nearby and continuous eigenvalues preserve the three signs for all sufficiently small parameter perturbations. The two simple zeroes of the local Hurwitz determinant also persist nearby and remain transverse by the implicit-function theorem. This robustness is local in the other parameters and does not assert that no further crossings appear outside a fixed neighborhood.

## Verification

The standalone file `verification_check.py` uses exact SymPy rational arithmetic to recreate the three differential equations, verify the equilibrium by direct substitution, differentiate the Jacobian, expand the characteristic polynomial, factor \(H\), verify its two exact algebraic roots, and check the quadratic's ordering and transverse derivative signs. It requires only Python and SymPy; execute `python verification_check.py` in the directory containing that file. All proof assertions use exact arithmetic. Three rational test rates confirm the stable–unstable–stable classification but are **not** a substitute for the preceding all-rates argument.

## Relationship to prior work

Yadav and Gakkhar [1] formulate this exact harvest-effort system, obtain its characteristic cubic, and study a Hopf parameter **varying the harvested fraction \(m\)** (especially their Sections 3.4 and 4). Their general cubic stability criterion is used here as standard mathematical background; it does not state these two critical \(\rho\)-values, the unchanged equilibrium under varying \(\rho\), or the low-speed stability interval. In particular, the paper's convenient sufficient sign restriction \(m_2<\rho p m_1\) fails at every \(\rho<1\) in our specialization, including the demonstrated low-speed stable interval. Bergland and collaborators [2] also study responsive fishery effort, but in a different pollution-and-delay fishery system without this ratio-dependent harvested-predator model. The claim is an **explicit model-specific parameter phase diagram**, not a new general Routh–Hurwitz theorem.

## Limitations

The result concerns only the stated positive three-dimensional system and its fixed exact parameter family. It asserts local exponential stability and spectral changes, not global basin structure, nonlinear cycles or first Lyapunov coefficients, optimal economic decisions, or applicability to empirically estimated harvest rates. A complete survey of older effort-dynamics literature is not possible; the 2010 effort-dynamics paper by Kar and Chakraborty [3] is a residual potential overlap source without verified full-text comparison.

## References

[1] U. Yadav and S. Gakkhar, *Effort Dynamics with Selective Predator Harvesting of a Ratio-dependent Predator-Prey System* (first public 2022-03-22), arXiv:2203.11986v1, https://arxiv.org/html/2203.11986v1 .

[2] H. Bergland, P. Mishra, P. A. Pedersen, A. Ponossov, and J. Wyller, *Time delays and pollution in an open-access fishery*, Natural Resource Modeling (first published 2022-11-30), https://doi.org/10.1111/nrm.12363 .

[3] T. K. Kar and K. Chakraborty, *Effort dynamics in a prey–predator model with harvesting*, International Journal of Information and System Sciences 6(3) (2010), pp. 318–332 (bibliographic citation; full text not independently inspected).
