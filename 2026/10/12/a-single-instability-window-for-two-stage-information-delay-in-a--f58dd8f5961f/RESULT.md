# A single instability window for two-stage information delay in a vaccination SIRM model
## Finding
Consider the information-dependent vaccination SIRM model with an exponentially distributed reporting delay, introduced by Fang, Liu, and Du. Its linear-chain formulation is
\[
\begin{aligned}
\dot S&=\Lambda-[\mu+v(M)+\beta I]S,\\
\dot I&=\beta SI-(\gamma+\mu)I,\\
\dot R&=v(M)S+\gamma I-\mu R,\\
\dot M&=aQ-bM,\\
\tau\dot Q&=I-Q,
\end{aligned}
\qquad v(M)=\sigma\left(p_0+\frac{u_0M}{1+u_2M}\right).
\]
For a positive endemic equilibrium, changing only the mean information delay \(\tau\) can produce a **single bounded window of linear instability**: stability at small delays, instability at intermediate delays, and stability again for sufficiently large finite delays. More strongly, there is an exact all-delay criterion and no admissible parameter choice can exhibit more than one such window.

Define
\[
A=\mu+v(M_*)+\beta I_*,\qquad
C=(\gamma+\mu)\beta I_*,\qquad
D=a\beta I_*S_*v'(M_*),
\]
where the subscript \(*\) denotes the unique positive endemic equilibrium. All three are strictly positive. Define the sharp feedback threshold
\[
K(\tau)=A(Ab+C+b^2)\frac{(1+b\tau)(1+A\tau+C\tau^2)}{[1+(A+b)\tau]^2}.
\]
For every finite \(\tau>0\), the equilibrium is locally asymptotically stable if and only if
\[
D<K(\tau).
\]
It has exactly two eigenvalues with positive real part when \(D>K(\tau)\). Equality gives a simple imaginary eigenvalue pair; linearization does not determine nonlinear stability there. The corresponding criterion at the reduced limit \(\tau=0\) is \(D<K(0)\).

The threshold \(K\) has exactly one positive critical point, a strict global minimum, and grows to infinity for large \(\tau\). In particular, if
\[
K_*:=\min_{\tau\geq0}K(\tau)<D<K(0),
\]
there are exactly two stability-switching delays \(\tau_-<\tau_+\): locally stable for \(0\leq\tau<\tau_-\) and \(\tau>\tau_+\), unstable with two right-half-plane eigenvalues in between.

For the explicit positive parameter set
\[
\Lambda=10,\quad\mu=\tfrac1{10},\quad\beta=1,\quad\gamma=\tfrac{99}{10},\quad p_0=\tfrac1{20},\quad\sigma=1,\quad u_0=\tfrac94,\quad u_2=2,\quad a=10,\quad b=1,
\]
the positive equilibrium is
\[
(S_*,I_*,R_*,M_*,Q_*)=(10,\tfrac1{10},\tfrac{899}{10},1,\tfrac1{10})
\]
and the mean-delay instability interval is sharply bounded by
\[
0.11326<\tau_-<0.11327,\qquad
1.96785<\tau_+<1.96786.
\]
For example, the endemic equilibrium is locally asymptotically stable at \(\tau=0\) and \(\tau=3\), but has an unstable conjugate eigenvalue pair at \(\tau=1\). This gives a positive-parameter, source-specific realization of delay-induced loss **and subsequent recovery** of endemic local stability.

## Assumptions and scope
The source parameters satisfy
\[
\Lambda,\mu,\beta,\gamma,p_0,u_0,u_2,a,b>0,\qquad0<\sigma\leq1.
\]
Assume the source's endemic-existence condition
\[
\mathcal R_0=\frac{\beta\Lambda}{(\gamma+\mu)(\mu+\sigma p_0)}>1.
\]
Consequently there is exactly one biologically feasible endemic equilibrium with \(I_*>0\). Its coordinates satisfy
\[
S_*=(\gamma+\mu)/\beta,\quad Q_*=I_*,\quad M_*=aI_*/b,\quad
R_*=[v(M_*)S_*+\gamma I_*]/\mu.
\]
The transmission, information-decay, vaccination, and demographic parameters are fixed throughout each delay sweep; only \(\tau\) changes. The endemic equilibrium itself is independent of \(\tau\).

The order-zero mean-delay case is the well-defined **reduced** system obtained by setting \(Q=I\), not the singular five-equation ODE with a missing derivative. For \(\tau>0\), the exponential convolution formulation and its augmented linear-chain ODE are equivalent for convolution-consistent histories.

All stability statements are local properties of the endemic equilibrium of the **finite-dimensional linear-chain realization**. No global convergence or existence, amplitude, or stability of nonlinear periodic orbits is asserted.

## Proof
**Step 1: Exact characteristic polynomial.** Write \(\delta=\gamma+\mu\), \(h=\beta I_*\), and \(k=S_*v'(M_*)\). Then \(C=\delta h\) and \(D=akh\). The recovered equation is downstream from the other four and contributes the eigenvalue \(-\mu\).

In the state order \((S,I,M,Q)\), the remaining Jacobian is
\[
J_4=\begin{pmatrix}
-A&-\delta&-k&0\\
h&0&0&0\\
0&0&-b&a\\
0&1/\tau&0&-1/\tau
\end{pmatrix}.
\]
Direct determinant expansion yields, for \(\tau>0\),
\[
\tau\det(\lambda I-J_4)=P_\tau(\lambda)
=(\lambda^2+A\lambda+C)(\lambda+b)(1+\tau\lambda)+D.
\]
The full five-dimensional characteristic polynomial is \((\lambda+\mu)P_\tau(\lambda)/\tau\), which proves that no additional infected-feedback eigenmodes have been omitted.

**Step 2: Exact stability criterion.** Expanding
\[
P_\tau(\lambda)=a_4\lambda^4+a_3\lambda^3+a_2\lambda^2+a_1\lambda+a_0
\]
gives
\[
\begin{aligned}
a_4&=\tau,\\
a_3&=1+(A+b)\tau,\\
a_2&=A+b+(C+Ab)\tau,\\
a_1&=C+Ab+Cb\tau,\\
a_0&=Cb+D.
\end{aligned}
\]
All coefficients are positive. The second Hurwitz determinant is
\[
\Delta_2=a_3a_2-a_4a_1
=(A+b)+(A+b)^2\tau+A(Ab+C+b^2)\tau^2>0.
\]
The third Hurwitz determinant has the **exact factorization**
\[
\begin{aligned}
\Delta_3&=a_3a_2a_1-a_4a_1^2-a_3^2a_0\\
&=A(Ab+C+b^2)(1+b\tau)(1+A\tau+C\tau^2)
-D[1+(A+b)\tau]^2.
\end{aligned}
\]
The quartic Routh–Hurwitz criterion now gives stability precisely when \(\Delta_3>0\), equivalent to \(D<K(\tau)\). If \(\Delta_3<0\), the Routh first-column signs are \((+,+,+,-,+)\), so precisely two eigenvalues have positive real part. Since the polynomial's coefficients are positive, no positive real root exists; these two unstable eigenvalues form a conjugate non-real pair.

If \(\Delta_3=0\), set \(\Omega^2=a_1/a_3>0\). The polynomial factors as
\[
P_\tau(\lambda)
=(\lambda^2+\Omega^2)
\left(a_4\lambda^2+a_3\lambda+\frac{a_0}{\Omega^2}\right).
\]
The quadratic's coefficients are positive, so its roots have strictly negative real part. The pair \(\lambda=\pm i\Omega\) is simple, and the full Jacobian has the additional stable eigenvalue \(-\mu\). These equalities do not by themselves establish nonlinear periodic orbits or nonlinear stability at a threshold.

At \(\tau=0\), the polynomial reduces to
\[
P_0(\lambda)=\lambda^3+(A+b)\lambda^2+(C+Ab)\lambda+(Cb+D).
\]
Its cubic Routh–Hurwitz condition is exactly \(D<K(0)=A(Ab+C+b^2)\); equality yields an imaginary pair and inequality reversal yields two unstable eigenvalues.

**Step 3: Exactly one destabilizing delay scale.** Direct differentiation gives
\[
\frac{K'(\tau)}{K(\tau)}
=\frac{H(\tau)}{(1+b\tau)(1+A\tau+C\tau^2)[1+(A+b)\tau]},
\]
where
\[
H(\tau)=Cb(A+b)\tau^3+3Cb\tau^2+(2C-A^2-b^2)\tau-(A+b).
\]
The denominator is positive. Read from highest to lowest degree, the nonzero coefficient signs of \(H\) have **exactly one** sign change, regardless of the sign of its linear coefficient. Descartes' rule therefore gives at most one strictly positive root. Because \(H(0)=-(A+b)<0\) and \(H(\tau)\to+\infty\), there is exactly one positive root \(\tau_*\), and it is simple. Thus \(K\) first decreases and then increases strictly. Moreover
\[
K(\tau)\sim
\frac{A(Ab+C+b^2)bC}{(A+b)^2}\,\tau
\qquad(\tau\to\infty),
\]
so the critical point is the unique global minimum and \(K(\tau)\to\infty\).

The horizontal line at height \(D>0\) can therefore intersect \(K\) at most twice. If \(D<K_*\), the equilibrium is stable at all finite delays. If \(D=K_*\), it has a single neutral delay \(\tau_*\) and is stable elsewhere. If \(K_*<D<K(0)\), there are exactly two distinct positive crossing delays, with the stable–unstable–stable ordering stated above. If \(D=K(0)\), the reduced system is neutral, small positive delays are unstable, and one later positive crossing restores stability. If \(D>K(0)\), the reduced system and small positive delays are unstable, and again one positive crossing restores stability. Away from the minimum, the two threshold roots of \(D=K(\tau)\) are simple; the associated imaginary-pair eigenvalues cross the imaginary axis spectrally.

**Step 4: Fully positive rational example.** Use the parameters specified above. They satisfy the source's positivity conditions, and
\[
\mathcal R_0=\frac{20}{3}>1.
\]
Substitution into the five model equations verifies the stated strictly positive endemic equilibrium exactly. The vaccine rate at its information state is \(v(1)=4/5\), with derivative \(v'(1)=1/4\); hence
\[
(A,b,C,D)=(1,1,1,5/2).
\]
Therefore
\[
\Delta_3(\tau)=\tfrac12(6\tau^3-8\tau^2-8\tau+1),
\]
with signs
\[
\Delta_3(0)=\tfrac12>0,\quad
\Delta_3(1)=-\tfrac92<0,\quad
\Delta_3(3)=\tfrac{67}{2}>0.
\]
The unique-minimum theorem proves there are exactly two positive zeros. Exact rational substitution gives opposite signs at the endpoints of each of the intervals stated in the Finding. This certifies both crossing brackets without relying on floating-point root finding.

## Verification
The standalone script `verification/verify.py` symbolically rederives the Jacobian characteristic polynomial, the two Hurwitz determinant identities, the derivative-factorization identity for \(K\), and the exact rational equilibrium and classification witness. It checks the four rational sign endpoints enclosing the positive stability thresholds, as well as the signs at \(\tau=0,1,3\). Run with `python verification/verify.py`; successful execution prints `VERIFY_OK`.

Symbolic checks are independent algebraic consistency tests. The proof for **all** positive parameters is given above by exact characteristic-polynomial factorization, Routh–Hurwitz, and Descartes' rule. Finite numerical eigenvalue experiments are neither needed nor used as proof of the universal statement.

## Relationship to prior work
Fang, Liu, and Du derive the two-stage information-memory realization and study equilibria and local/global dynamics of its reduced \(\tau=0\) model. Their perturbation theorem addresses sufficiently small positive \(\tau\) and continuation of heteroclinic connections; their conclusion specifically identifies possible Hopf bifurcations as future work. They do not give the full finite-delay characteristic-polynomial classification established here.

Reentrant stability in information-dependent vaccination is **not new as a general phenomenon**. In the 2007 model of d'Onofrio, Manfredi, and Salinelli, vaccination operates at birth and the information variable follows one exponentially relaxing filter, giving a three-dimensional endemic characteristic polynomial. Their exact instability window in the inverse decay rate is a direct and important predecessor. Centrone, Perchiazzo, and Salinelli (2026) extend that **single-filter** birth-vaccination framework to incidence-based information, again obtaining delay-dependent instability windows. Kumar, Takeuchi, and Srivastava (2023) study stability switches in a different model with two discrete delays.

The present theorem is distinct: vaccination acts on the current susceptible stock, information is first convolved into \(Q\) and **then** filtered through a separate decay state \(M\), the characteristic polynomial is quartic, and the variable mean delay is independent of \(a\) and \(b\). Neither the earlier single-filter cubic conditions nor discrete-delay characteristic equations imply the exact source-specific function \(K(\tau)\), its one-minimum theorem, or the rational positive witness. The significance is a complete parameter-explicit stability map for the later two-filter model, not priority for the qualitative mechanism.

## Limitations
Only **local equilibrium stability** is classified. The two simple imaginary crossings are necessary spectral ingredients for Hopf bifurcation, but no first Lyapunov coefficient, periodic-orbit branch, or nonlinear criticality is computed; the theorem does not claim attracting cycles, sustained oscillations, global stability, or attractor selection.

At equality \(D=K(\tau)\), linearization is neutral and does not settle nonlinear asymptotic stability. At the minimum where \(D=K_*\), the stability boundary is tangent rather than a transversal switch.

The delay is an **exponential distributed mean delay** permitting the exact linear-chain realization, not a discrete delay or arbitrary kernel. All other parameters and the endemic equilibrium remain fixed during the \(\tau\) sweep. The theorem does not compare transients under changes in vaccination strength or information growth.

## References
1. J. Fang, J. Liu, and Z. Du, “Dynamics of multiple time scale SIRM model with information-dependent vaccination,” Discrete and Continuous Dynamical Systems - B 39 (2026), 272–297. DOI: 10.3934/dcdsb.2026090. Online June 11, 2026.
2. A. d'Onofrio, P. Manfredi, and E. Salinelli, “Bifurcation thresholds in an SIR model with information-dependent vaccination,” Mathematical Modelling of Natural Phenomena 2 (2007), 26–43. DOI: 10.1051/mmnp:2008009.
3. F. Centrone, A. Perchiazzo, and E. Salinelli, “Bifurcations in an SIR model with vaccinating behaviour based on lagged information depending on the incidence,” Far East Journal of Mathematical Sciences 143 (2026), 2993–3022. DOI: 10.17654/0972087126165.
4. A. Kumar, Y. Takeuchi, and P. K. Srivastava, “Stability switches, periodic oscillations and global stability in an infectious disease model with multiple time delays,” Mathematical Biosciences and Engineering 20 (2023), 11000–11032. DOI: 10.3934/mbe.2023487.
