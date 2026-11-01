# Global analytic phase-gauge conjugacy and a sharp Hurwitz obstruction in a periodic polynomial flow

## Finding
For every \(\mu>0\) and every two real values \(e_1,e_2\), the quintic polynomial vector fields \(F_{\mu,e_1}\) and \(F_{\mu,e_2}\) defined below are **globally real-analytically, volume-preservingly and time-preservingly conjugate**. An explicit coordinate change is the height-dependent rotation
\[
H_{e_1-e_2}(x+iy,z)=(e^{i(e_1-e_2)z}(x+iy),z).
\]
Hence the apparent angular parameter does not change any orbit dynamics, periods, basin membership, or Floquet multipliers.

Nevertheless, in the exact same polynomial family, pointwise Jacobian Hurwitzness depends essentially on that parameter. For **every** \(\mu>0\), the companion field \(F_{\mu,0}\) has a non-Hurwitz Jacobian at \(p=(1,0,-1/10)\). If a member \(F_{\mu,e}\) is globally Jacobian-Hurwitz, it must satisfy
\[
0<\mu<\frac{21}{166},\qquad
 e>\frac{250\mu}{7}+\frac{830\mu}{21-166\mu}.
\]
The inequalities are the **exact necessary and sufficient** conditions for the Jacobian at this single point \(p\) to be Hurwitz (not sufficient for global Hurwitzness). The cited 2026 paper proves a nonempty region of globally Hurwitz members, so its construction yields polynomial vector fields with periodic orbits which are analytically conjugate to non-Hurwitz polynomial fields.

Wherever the larger circular orbit is attracting, the entire basin has the explicit asymptotic-phase function
\[
\Psi_e(x,y,z)=\operatorname{Arg}(x+iy)+e\left(z+\frac25\right)\pmod{2\pi}.
\]
Its isochrons are precisely the level sets of \(\Psi_e\) within that basin. This formula is global on the basin, not merely a local linearization around the orbit.

## Assumptions and scope
Let \(\mu>0\), \(e\in\mathbb R\), \(R=x^2+y^2\), and define
\[
Q(R,z)=(R-5)\left(\frac{20}{21}-R\right)-\frac{400}{21}z^2,\qquad S(R,z)=z+\frac{R}{10}.
\]
The exact polynomial system is
\[
\begin{aligned}
\dot x&=\mu xQ(R,z)-[1+eS(R,z)]y,\\
\dot y&=\mu yQ(R,z)+[1+eS(R,z)]x,\\
\dot z&=-S(R,z).
\end{aligned}
\]
The source introduces this family and proves that a nonempty open set of positive parameters makes its entire Jacobian Hurwitz and produces two nonconstant period-\(2\pi\) circular orbits (one saddle, one attracting). That existence theorem is treated as established prior work, **not** proved anew here; the analytic conjugacy and pointwise obstruction below are independent algebraic deductions.

Conjugacy holds for all \(\mu>0\) and real \(e\), without requiring Hurwitzness or a limit-cycle stability assumption. The isochron assertion is conditional only on the outer circular orbit being attracting; this holds in the source's parameter region. All forward trajectories exist for all nonnegative times.

## Proof
**1. Exact angular coboundary and global conjugacy.** Write \(w=x+iy\). The system becomes
\[
\dot w=[\mu Q(R,z)+i(1+eS(R,z))]w,\qquad \dot z=-S(R,z).
\]
Set \(W=e^{iez}w\). Direct differentiation, with no division by \(w\), gives
\[
\dot W=e^{iez}\left[\dot w+ie\dot z\,w\right]
       =[\mu Q(R,z)+i]W.
\]
Because \(|W|^2=|w|^2=R\), this and \(\dot z=-S\) are **exactly** the equations for \(F_{\mu,0}\). The map \(H_e:(w,z)\mapsto(e^{iez}w,z)\) has global real-analytic inverse \(H_{-e}\), including on the entire axis \(w=0\), and \(\det DH_e\equiv1\). Thus \(DH_e F_{\mu,e}=F_{\mu,0}\circ H_e\) identically. Composing such maps gives the stated \(H_{e_1-e_2}\) conjugacy, preserving physical time and all corresponding maximal solution intervals. The standard conjugacy of linearized return maps gives identical Floquet multipliers.

**2. Forward completeness.** The planar radial variables satisfy
\[
\dot R=2\mu RQ(R,z),\qquad \dot z=-z-\frac{R}{10}.
\]
For \(R\ge5\), \(Q(R,z)\le0\), so \(0\le R(t)\le\max\{R(0),5\}\) for forward solutions. Variation of constants bounds \(|z(t)|\le e^{-t}|z(0)|+\max\{R(0),5\}/10\). Hence no finite-time forward escape occurs.

**3. Exact pointwise Hurwitz obstruction.** At the point \(p=(1,0,-1/10)\), \(Q=S=0\). Direct differentiation of the three polynomial components yields the characteristic polynomial of \(DF_{\mu,e}(p)\):
\[
\lambda^3+a_1\lambda^2+a_2\lambda+1,\quad
 a_1=1-\frac{166\mu}{21},\quad
 a_2=1+\frac e5-\frac{50\mu}{7}.
\]
A real monic cubic with constant term one is strictly Hurwitz precisely when \(a_1>0\), \(a_2>0\), and \(a_1a_2>1\). Solving these exact inequalities gives
\[
0<\mu<\frac{21}{166},\qquad
 e>\frac{250\mu}{7}+\frac{830\mu}{21-166\mu}.
\]
For \(e=0\) and \(0<\mu<21/166\), the two positive coefficients \(a_1\) and \(a_2\) are each strictly less than one, so \(a_1a_2<1\). For \(\mu\ge21/166\), \(a_1\le0\). Thus **no positive \(\mu\)** makes \(DF_{\mu,0}(p)\) Hurwitz. For the reference \(\mu=1/1000\), the exact pointwise threshold is \(e>22037/291676\); at \(e=0\), the cubic Hurwitz determinant equals \(-22037/1470000\), whereas at \(e=1/10\) it equals \(35653/7350000\). This last positive single-point check must not be mistaken for a self-contained proof of global Hurwitzness; that separate result is supplied by the cited paper.

**4. Exact isochrons.** Away from the invariant axis \(w=0\), let \(\theta=\operatorname{Arg}(w)\). Then \(\dot\theta=1+eS\) and \(\dot z=-S\), so \(\frac d{dt}(\theta+ez)=1\) modulo \(2\pi\). The outer circle is \(R=4,z=-2/5\), with \(Q=S=0\) and angular speed one. Every point in its basin has \(R(t)\to4\) and \(z(t)\to-2/5\); the invariant axis cannot belong to that basin. Consequently, for \(\Psi_e=\theta+e(z+2/5)\),
\[
\Psi_e(\Phi_t(p))=\Psi_e(p)+t\pmod{2\pi},
\]
and the trajectory is asymptotic to the uniquely phased circle
\[
(2\cos(t+\Psi_e(p)),2\sin(t+\Psi_e(p)),-2/5).
\]
Two initial points have the same asymptotic phase exactly when their \(\Psi_e\) values agree; the stated isochrons follow. Their formula is valid throughout the basin regardless of whether a global basin-boundary formula is known.

## Verification
The accompanying `verify.py` performs exact SymPy calculations: the Cartesian differential conjugacy identity, rotational radius identity, \(\det DH_e=1\), the complete characteristic polynomial at \(p\), both rational Routh–Hurwitz margins, and the two circular equilibrium conditions in the radial system. The checker passed on the packaged source. The proof of infinite-dimensional or global flow claims is analytic; no finite test is being substituted for it.

## Relationship to prior work
Castañeda and Rebollo-Perdomo (arXiv:2610.09176v1, October 6, 2026) introduced precisely this polynomial family and proved the existence of a nonempty open Hurwitz region with one saddle and one attracting circular orbit. Their radial/angular reduction already provides the elementary differential equations used here. The contribution here is **not** those circular orbits, their existence, or the general fact that a Jacobian spectrum depends on nonlinear coordinates. It is the explicit **global** volume-preserving analytic conjugacy eliminating the full angular parameter for this given polynomial family, the resulting exact whole-basin isochrons, and the sharp algebraic obstruction connecting this dynamical redundancy to pointwise Hurwitzness.

Published mathematical records on exact phase formulas for symmetric Lorenz-84 dynamics and exact angular returns for homogeneous star-node cycles concern different vector fields and do not imply an equivalence for this family. The conjugacy is immediately suggested by the source's angular equations, so an independent priority review remains appropriate.

## Limitations
The inequality above characterizes Hurwitzness **only at \(p\)**, and therefore gives a necessary, not sufficient, condition for globally Hurwitz Jacobians. The new argument does not independently reprove the source's nonempty global-Hurwitz parameter region or determine a full stable-manifold basin boundary. Isochrons are asserted only on the actual basin of the outer attracting circle; they are undefined on the invariant axis. This is an exact smooth-flow statement, not a claim of polynomial conjugacy (the explicit conjugating diffeomorphism uses sine and cosine). The source's displayed equations make the new coordinate change algebraically accessible, a genuine historical-priority risk. Independent audit has not been performed.

## References
1. Álvaro Castañeda and Salomón Rebollo-Perdomo, *A family of Hurwitz polynomial vector fields in \(\mathbb R^3\) having non-constant periodic orbits*, arXiv:2610.09176v1, first posted 2026-10-06. https://arxiv.org/abs/2610.09176
2. Published mathematical record, *Exact phase geometry and critical logarithmic spiral in symmetric Lorenz-84*, https://github.com/Resultary/2026/tree/main/2026/9/21/SCOPE-lorenz84-exact-phase-and-critical-log-spiral--187e77a447b4 (different model; comparison only).
3. Published mathematical record, *Exact angular return and physical-time Floquet rigidity for contracting homogeneous star-node cycles*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-angular-return-and-physical-time-floquet-rigidity-for-cont--7c00337eaa41 (different model; comparison only).
