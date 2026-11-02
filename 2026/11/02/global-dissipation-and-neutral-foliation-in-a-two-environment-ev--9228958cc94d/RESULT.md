# Global dissipation and neutral foliation in a two-environment evolutionary game

## Finding

In the symmetric equal-feedback reduction of a two-community eco-evolutionary game, the sign of one payoff determinant gives a **complete global classification on every interior invariant leaf**. For strictly positive payoff gaps as below, put
\[
\Delta=(R_0-T_0)(P_1-S_1)-(S_0-P_0)(T_1-R_1).
\]
For every strictly interior initial condition and arbitrary community-crossing weight \(0<\delta<1\) and common feedback strength \(\theta>0\):

1. If \(\Delta<0\), the trajectory converges to the **unique** interior equilibrium selected by its initial environmental log-odds difference.
2. If \(\Delta=0\), every non-equilibrium interior trajectory is a periodic orbit. This conclusion requires no mirror symmetry of the two payoff matrices.
3. If \(\Delta>0\), every non-equilibrium interior trajectory approaches the boundary of the unit cube in the sense that its distance to that boundary tends to zero. No such trajectory converges to an interior point or is periodic.

Thus the same inequality that determines local transverse stability of the interior equilibrium line has a sharp, all-initial-condition global interpretation. The equilibrium-selection formula and the complete critical foliation are explicit below.

## Assumptions and scope

Let \(x\in(0,1)\) be the common cooperative fraction in two identical communities, \(n,m\in(0,1)\) the within-community and between-community environmental states, respectively, and \(0<\delta<1\) the between-community interaction weight. The communities are initialized symmetrically and remain so. All environmental enhancement-to-degradation ratios equal a common \(\theta>0\). These are precisely the symmetry and equal-feedback assumptions behind equations (13)--(15) of Betz, Fu and Masuda.

The payoff matrix interpolates linearly between
\[
A_0=\begin{pmatrix}R_0&S_0\\T_0&P_0\end{pmatrix},\qquad
A_1=\begin{pmatrix}R_1&S_1\\T_1&P_1\end{pmatrix},
\]
with the strict source assumptions \(R_0>T_0\), \(S_0>P_0\), \(T_1>R_1\), \(P_1>S_1\). Define
\[
d_0=R_0-T_0,\quad e_0=S_0-P_0,\quad d_1=T_1-R_1,\quad e_1=P_1-S_1,
\]
so all four numbers are positive. Let
\[
A(x)=e_0(1-x)+d_0x,\qquad
B(x)=(e_0+e_1)(1-x)+(d_0+d_1)x.
\]
Then \(0<A(x)<B(x)\) on \([0,1]\), and the exact reduced differential equations are
\[
\dot x=x(1-x)\{A(x)-B(x)[(1-\delta)n+\delta m]\},
\]
\[
\dot n=n(1-n)[(1+\theta)x-1],\qquad
\dot m=m(1-m)[(1+\theta)x-1].
\]
Every solution considered starts strictly inside \((0,1)^3\) and exists for all forward time by smooth invariance of the closed cube. No claim is made about asymmetric initial populations, unequal enhancement ratios, or trajectories initialized on the boundary.

## Proof

**Invariant leaves and equilibrium selection.** Write \(\operatorname{logit}(z)=\log(z/(1-z))\). Since both environmental equations have the same logit derivative, the quantity
\[
K=\operatorname{logit}(n)-\operatorname{logit}(m)
\]
is constant along every interior trajectory. Fix its initial value. Set \(u=\operatorname{logit}(n)\), \(\sigma(v)=(1+e^{-v})^{-1}\), and
\[
E_K(u)=(1-\delta)\sigma(u)+\delta\sigma(u-K).
\]
The invariant leaf is exactly \(n=\sigma(u)\), \(m=\sigma(u-K)\), and the flow reduces to
\[
\dot x=x(1-x)[A(x)-B(x)E_K(u)],\qquad
\dot u=(1+\theta)x-1.
\]
Here \(E_K:\mathbb R\to(0,1)\) is a smooth strictly increasing bijection. Define
\[
x_*=\frac{1}{1+\theta},\qquad E_*=\frac{A(x_*)}{B(x_*)}\in(0,1).
\]
There is therefore one and only one \(u_*\in\mathbb R\) satisfying \(E_K(u_*)=E_*\), and precisely one equilibrium \((x_*,\sigma(u_*),\sigma(u_*-K))\) on this leaf. An explicit scalar selection rule avoids integrating trajectories: given \(k=e^K>0\), the equilibrium between-community environment \(m_*\) is the unique root \(t\in(0,1)\) of
\[
(1-\delta)\frac{kt}{1+(k-1)t}+\delta t=E_*;
\]
then \(n_*=km_*/[1+(k-1)m_*]\).

**Proper energy and exact sign.** On \((0,1)\times\mathbb R\), define
\[
H_K(x,u)=\int_{x_*}^{x}\frac{s-x_*}{s(1-s)B(s)}\,ds
+\frac{1}{1+\theta}\int_{u_*}^{u}[E_K(v)-E_*] \,dv.
\]
Both summands are nonnegative and vanish only at their respective starred coordinates. Both are strictly decreasing to the left of their minimizer and strictly increasing to the right; the first diverges at \(x=0,1\) and the second diverges at \(u\to\pm\infty\). Hence \(H_K\) is proper, with a unique zero at the equilibrium and compact positive level sets. Differentiating exactly gives
\[
\frac{dH_K}{dt}=(x-x_*)\left(\frac{A(x)}{B(x)}-E_*\right).
\]
Since \(A'B-AB'=d_0e_1-e_0d_1=\Delta\),
\[
\boxed{\displaystyle\frac{dH_K}{dt}=\frac{\Delta(x-x_*)^2}{B(x)B(x_*)}.}
\]
The denominator is everywhere positive, so its sign is exactly the sign of \(\Delta\), without approximation or linearization.

**Global attracting regime.** For \(\Delta<0\), the nonincreasing energy confines each solution to a compact sublevel set, so its forward omega-limit set is nonempty and interior. By LaSalle's invariance principle, it lies in the largest invariant subset of \(x=x_*\). On that subset \(\dot x=0\) requires \(E_K(u)=E_*\), hence \(u=u_*\). Thus every trajectory tends to the selected equilibrium. In particular, all three original coordinates converge.

**Neutral regime.** For \(\Delta=0\), \(H_K\) is a first integral. Every positive level is a simple closed regular curve: \(H_K\) is a sum of two proper single-well one-variable functions, and its gradient vanishes only at their common minimizer. The reduced vector field does not vanish away from that point. Its motion on each compact connected regular level curve is consequently periodic, with a finite positive period. The collection of these curves fills each invariant leaf outside the equilibrium.

**Outward regime.** For \(\Delta>0\), take any non-equilibrium interior initial state, so \(H_K(0)>0\). Suppose that its nondecreasing energy stayed bounded. Properness would give a precompact trajectory with a nonempty omega-limit set. On that set the energy is constant, so the exact derivative identity forces \(x=x_*\); invariance would then force \(u=u_*\), contradicting its strictly positive energy. Thus \(H_K(t)\to+\infty\). Every fixed compact subset of the interior cube intersects the selected leaf in a set of bounded energy, so the trajectory eventually leaves every such compact subset: its distance to the boundary tends to zero. Energy monotonicity also rules out nonstationary interior cycles. This proves all three cases.

## Verification

The accompanying \(verify.py\) (Python with SymPy and SciPy) checks the rational identity \(A'B-AB'=\Delta\) symbolically, the exact factorization of \(\dot H_K\), and the reduced critical equilibrium. It then integrates three strictly admissible test configurations (\(\Delta<0\), \(=0\), \(>0\)) and verifies the conserved environmental log-odds and the monotonic/constant energy. The full script and dependency specification are packaged with this finding; run \(python verify.py\) after installing the dependencies. The analytical arguments above, not the integrations, establish statements over all forward times.

An explicit **non-mirror critical example** is
\[
A_0=\begin{pmatrix}5&3\\3&2\end{pmatrix},\qquad
A_1=\begin{pmatrix}8&4\\12&6\end{pmatrix}.
\]
It has \((d_0,e_0,d_1,e_1)=(2,1,4,2)\) and \(\Delta=0\), without the mirror-swap symmetry of the source's equation (47). All its nonstationary strictly interior orbits are periodic when feedback ratios are equal.

## Relationship to prior work

Betz, Fu and Masuda, equations (13)--(15), Section 4.2, and Appendix E, derive the interior equilibrium line and analyze transverse *local* stability under the determinant/cross-ratio condition. Their Section 6 explicitly notes neutral periodic trajectories for a special mirror-structured payoff family. The present theorem, for the same published reduced equations, adds a conserved environmental odds difference, an explicit initial-condition-dependent point-selection rule, a proper globally monotone energy, and a complete global three-way classification including critical non-mirror payoffs. Local eigenvalues and the special mirror-payoff construction do not imply these global claims.

Weitz and collaborators study evolutionary feedback using a single environmental coordinate, and the related Gong--Yao--Cao--et al. model studies a two-dimensional environment-feedback equation with mutation and limit-cycle questions. Neither incorporates this pair of distinguishable edge-environment variables or supplies their odds-difference invariant and selected-equilibrium formula. The reduction is particular to equal feedback ratios; the broader networked model can exhibit different behavior.

## Limitations

This is an analytical statement for the symmetric equal-feedback three-dimensional invariant subsystem, not for generic asymmetric five-dimensional initial conditions. Strict payoff-gap assumptions and strictly interior initial conditions are essential to the stated proof. The outward regime proves approach to the boundary, not convergence to any particular boundary equilibrium or cycle. Periodic critical trajectories are neutral (not attracting in their invariant leaf). The novelty comparison is literature-limited; it is not a proof that equivalent mathematics cannot appear elsewhere. Independent validation has not been performed.

## References

1. K. Betz, F. Fu and N. Masuda, *Evolutionary game dynamics with environmental feedback in a network with two communities*, arXiv:2404.17082 (first public version 25 April 2024), https://arxiv.org/abs/2404.17082 . Relevant: equations (13)--(15), Section 4.2, Section 6, Appendix E.
2. J. S. Weitz, C. Eksin, K. Paarporn, S. P. Brown and W. C. Ratcliff, *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*, Proceedings of the National Academy of Sciences 113 (2016), E7518--E7525, https://doi.org/10.1073/pnas.1604096113 .
3. *Limit Cycles Analysis and Control of Evolutionary Game Dynamics with Environmental Feedback*, arXiv:2205.10734 (2022), https://arxiv.org/abs/2205.10734 . Relevant: Section 2 model and Section 3, including the mutation-dependent equilibrium and Dulac analysis.
