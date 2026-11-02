# Power-law contact retention induces a sharp endemic bistability transition and critical slowing

## Finding
For \(\tau,\xi,\omega>0\) and real \(q\geq1\), define
\[
\dot y=y[\tau(1-y)z-1],\qquad
\dot z=\xi\{1-[1+\omega(1-y)^q]z\},\qquad (y,z)\in[0,1]^2.
\]
This is the adaptive well-mixed susceptible–infected–susceptible (aNIMFA) system with constant link creation and power-law link breaking. Set \(\tau_0=1+\omega\) and \(q_c=1+\omega^{-1}\). Its only disease-free equilibrium is \(E_0=(0,(1+\omega)^{-1})\), with invasion threshold \(\tau_0\).

**Complete endemic classification.** If \(1\le q\le q_c\), then there is no endemic equilibrium for \(\tau\le\tau_0\), and exactly one for \(\tau>\tau_0\), a hyperbolic sink. If \(q>q_c\), put
\[
s_f=[\omega(q-1)]^{-1/q},\qquad
\tau_f=\frac q{q-1}[\omega(q-1)]^{1/q}<\tau_0.
\]
For \(\tau<\tau_f\) there is no endemic equilibrium; at equality there is exactly one, a nondegenerate saddle-node; for \(\tau_f<\tau<\tau_0\), there are two: the smaller-prevalence equilibrium is a saddle and the larger-prevalence equilibrium a hyperbolic sink. In that open interval \(E_0\) is also a hyperbolic sink, establishing local bistability. At \(\tau=\tau_0\), the higher-prevalence sink remains while \(E_0\) is nonhyperbolic; for \(\tau>\tau_0\) only the higher-prevalence endemic sink remains, and \(E_0\) is unstable. All equilibrium counts refer to the biologically feasible square.

**Critical extinction and exponent switch.** At exactly \(\tau=\tau_0\), for every \(y(0)>0\), \(z(0)\in[0,1]\), and \(q\le q_c\), trajectories converge to \(E_0\), but their leading prevalence obeys
\[
\lim_{t\to\infty}t y(t)=\frac{1+\omega}{1-\omega(q-1)}\quad(1\le q<q_c),
\qquad
\lim_{t\to\infty}t y(t)^2=\omega\quad(q=q_c).
\]
The second law is \(y(t)\sim\sqrt{\omega/t}\), not \(t^{-1}\), and its amplitude does not involve the link-adjustment speed \(\xi\).

## Assumptions and scope
The prevalence \(y\) and link density \(z\) are normalized to \([0,1]\). Infection is bilinear at effective rate \(\tau>0\); recovery is the unit time scale. Contact creation has constant rate \(\xi>0\); contact destruction has rate \(\xi\omega(1-y)^q\) per existing link. The power-law response is mathematically admissible and decreases with prevalence, representing contact persistence or awareness-induced avoidance fatigue rather than the usual increasing isolation response. Only deterministic homogeneous mean-field dynamics are claimed. All quantified results hold for **every** real \(q\ge1\), positive \(\xi,\omega,\tau\), and indicated initial conditions; no limit \(\xi\to\infty\) is assumed.

## Proof
**1. Forward invariance and disease-free stability.** At \(y=0\), \(\dot y=0\); at \(y=1\), \(\dot y=-1\); at \(z=0\), \(\dot z=\xi\); at \(z=1\), \(\dot z=-\xi\omega(1-y)^q\le0\). Thus the square is forward invariant and all solutions exist globally. Along \(y=0\), \(z\) relaxes to \((1+\omega)^{-1}\). The two eigenvalues at \(E_0\) are \(\tau/(1+\omega)-1\) and \(-\xi(1+\omega)\); hence the disease-free state is a hyperbolic sink below \(\tau_0\) and unstable above it.

**2. Exact root parameterization.** At a positive equilibrium write \(s=1-y\in(0,1)\). The contact equation forces \(z=1/(1+\omega s^q)\), and the prevalence equation forces
\[
\tau=T(s):=s^{-1}+\omega s^{q-1}.
\]
Conversely every root of this equation in \((0,1)\) gives an endemic equilibrium. Differentiation yields
\[
T'(s)=\frac{\omega(q-1)s^q-1}{s^2},\qquad
T''(s_f)=\frac q{s_f^3}>0
\]
when the critical point exists. Since \(T(s)\to\infty\) as \(s\downarrow0\) and \(T(1)=\tau_0\), the stated count follows by monotonicity for \(q\le q_c\), and by a unique strict minimum \(s_f\in(0,1)\) for \(q>q_c\). The fold value is \(T(s_f)=\tau_f\), which is strictly below \(T(1)\).

**3. Linear type and genuine fold.** At an endemic equilibrium, the full planar Jacobian has
\[
J=\begin{pmatrix}
-y/s & y(1+\omega s^q)\\
\xi\omega q s^{q-1}/(1+\omega s^q)&-\xi(1+\omega s^q)
\end{pmatrix},
\]
so
\[
\operatorname{tr}J=-y/s-\xi(1+\omega s^q)<0,\qquad
\det J=\frac{\xi y}{s}[1-\omega(q-1)s^q].
\]
Thus the small-\(s\) (large-\(y\)) branch has positive determinant and is a hyperbolic sink; the large-\(s\) branch has negative determinant and is a saddle. At \(s_f\), the determinant vanishes, but the other eigenvalue is strictly negative. The equilibrium curve has a nonzero quadratic turning coefficient \(T''(s_f)>0\), and the scalar equilibrium relation is regular in the varying parameter \(\tau\) because \(\partial_\tau[\tau-T(s)]=1\). Elimination of the strictly stable contact direction yields a nondegenerate planar saddle-node.

**4. Global extinction at the borderline.** Fix \(\tau=\tau_0\) and \(q\le q_c\). By step 2, \(E_0\) is the only equilibrium in the square. In the interior the system is cooperative: \(\partial_z\dot y=\tau y(1-y)\ge0\) and \(\partial_y\dot z=\xi\omega q(1-y)^{q-1}z\ge0\). The comparison principle therefore bounds every trajectory between those started at \((0,0)\) and \((1,1)\). The lower trajectory increases monotonically in the coordinate order as time advances, because it begins at the minimum element of the forward-invariant square and the flow is order preserving. Likewise the upper trajectory decreases monotonically, beginning at the maximum element. Both bounded coordinatewise limits are equilibria by continuity of the vector field, hence both equal \(E_0\). The squeeze proves convergence for every feasible initial state, including \(y(0)>0\).

**5. Sharp critical rates.** Write \(g(y)=[1+\omega(1-y)^q]^{-1}\); it is the instantaneous contact nullcline. Near \(E_0\), the linearization has one stable eigenvalue and one zero eigenvalue. A smooth center manifold \(z=h(y)\) has \(h(0)=g(0)\) and \(h'(0)=g'(0)=\omega q/(1+\omega)^2\), as follows from its invariance equation
\[
h'(y)\dot y=-\xi[1+\omega(1-y)^q]\,[h(y)-g(y)].
\]
For \(q<q_c\), substitution in the prevalence equation gives
\[
\dot y=-\frac{1-\omega(q-1)}{1+\omega}y^2+O(y^3).
\]
The coefficient is strictly negative, hence the standard scalar comparison for \(y^{-1}\) yields the claimed \(t^{-1}\) asymptotic. At \(q=q_c\), the quadratic coefficient vanishes; the invariance equation then implies \(h(y)-g(y)=O(y^3)\), because \(\dot y=O(y^3)\). Expanding \(T(1-y)\) at \(y=0\) gives \(T(1-y)=\tau_0+(q/2)y^2+O(y^3)\). Consequently
\[
\dot y= -\frac{q}{2(1+\omega)}y^3+O(y^4)
=-\frac1{2\omega}y^3+O(y^4).
\]
Equivalently \(d(y^{-2})/dt=\omega^{-1}+o(1)\), proving \(t y(t)^2\to\omega\). The exponentially decaying transverse stable mode does not change either leading rate. Since the boundary \(y=0\) is the strong-stable invariant manifold of \(E_0\), trajectories with \(y(0)>0\) approach on the positive center side and obey these rates. This also shows that no unverified claim of an attracting cycle or global endemic basin has entered the theorem.

## Verification
The accompanying program `verify.py` reconstructs the root-curve and Jacobian identities by exact symbolic arithmetic; checks the critical cubic drift coefficient for \(\omega=1,q=2\), the exact nonzero endemic state at \(\omega=1,q=3,\tau=2\), the bistable example \(\omega=1,q=3,\tau=39/20\), and numerically integrates the full equations to verify the approach of the scale-free critical profiles. The exact symbolic checks supplement, not replace, the argument for arbitrary parameters. No finite experiment is treated as proof of the universal quantified statements.

## Relationship to prior work
Achterberg and Sensi introduced these general adaptive SIS equations and proved existence of endemic equilibria above the invasion threshold and absence of periodic orbits for all admissible response functions; their named examples include random link activation, increasing epidemic-induced breaking, and the different adaptive-information response with multiple equilibria. The earlier Achterberg–Van Mieghem moment-closure study analyzed selected quadratic response choices, including adaptive information diffusion. The present result is a specific decreasing breaking response with **constant creation** and an arbitrary real power, and it gives a sharp response-exponent threshold, an exact disease-free/endemic bistability wedge, and a globally valid change of critical extinction exponent. Those earlier general equilibrium identities alone do not state the critical asymptotic or the bifurcation diagram of this family. Related nonlinear-epidemic critical decay laws concern different vector fields and do not imply the formulas here.

## Limitations
This is a deterministic mean-field statement, not a finite-network Markov extinction-time theorem. The decreasing breaking response may model reinforcement/fatigue/information diffusion rather than conventional behavioral prevention. Stability results for positive equilibria are local; the separatrix between the two sinks is not explicitly characterized. The positivity of the critical asymptotic coefficient is proved only on the specified surface; no uniform crossover expansion as the response exponent varies is claimed. Literature coverage is necessarily incomplete, and equivalent calculations in unpublished or unindexed works cannot be excluded. Independent external audit has not been performed.

## References
1. M. A. Achterberg and M. Sensi, *A minimal model for adaptive SIS epidemics*, arXiv:2209.01224 (first public version 2022-09-02); *Nonlinear Dynamics* **111** (2023), 12657–12670, doi:10.1007/s11071-023-08498-4.
2. M. A. Achterberg and P. Van Mieghem, *Moment closure approximations of susceptible-infected-susceptible epidemics on adaptive networks*, *Physical Review E* **106** (2022), 014308, doi:10.1103/PhysRevE.106.014308.
3. M. A. Achterberg, M. Sensi and S. Sottile, *A minimal model for multigroup adaptive SIS epidemics*, arXiv:2407.17639 (2024); multigroup comparison considered at abstract level only.
