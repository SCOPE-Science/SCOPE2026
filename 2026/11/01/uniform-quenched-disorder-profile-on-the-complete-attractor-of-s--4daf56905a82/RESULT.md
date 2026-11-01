# Uniform quenched-disorder profile on the complete attractor of strongly coupled Chialvo maps

## Finding
For a globally coupled Chialvo network with positive, nonidentical quenched inputs, **all bounded complete trajectories**, regardless of whether the common motion is periodic, quasiperiodic, or chaotic, have the same leading transverse spatial profile as the coupling tends to one. More precisely, with \(q=1-\varepsilon\), the centered voltages satisfy
\[
\sup_{t\in\mathbb Z}\|\mathbf x_t-\overline{x}_t\mathbf 1-q(\mathbf k-\overline{k}\mathbf 1)\|_2
\le \frac{q^2L}{1-qL}\|\mathbf k-\overline{k}\mathbf1\|_2,
\]
and the centered recovery variables satisfy
\[
\sup_{t\in\mathbb Z}\|\mathbf y_t-\overline{y}_t\mathbf 1+
\frac{bq}{1-a}(\mathbf k-\overline{k}\mathbf1)\|_2
\le \frac{bq^2L}{(1-a)(1-qL)}\|\mathbf k-\overline{k}\mathbf1\|_2.
\]
Both estimates are uniform in network size, time, the particular bounded complete trajectory, and the distribution of quenched inputs within the prescribed interval. The constants and assumptions are made explicit below. In particular, the squared spatial standard deviation of the voltages is \(q^2\operatorname{Var}(\mathbf k)(1+O(q))\) uniformly on the entire attractor; the leading coefficient is exactly one.

## Assumptions and scope
Choose an integer \(N\ge2\), \(0\le a<1\), \(b>0\), \(c\in\mathbb R\), and \(0<k_{\min}\le k_i\le k_{\max}<\infty\). For \(0\le q\le1\), put \(\varepsilon=1-q\) and \(F(x,y)=x^2 e^{y-x}\). The discrete-time, all-to-all mean-field network is
\[
\begin{split}
 x_i(t+1)&=q[F(x_i(t),y_i(t))+k_i]+
 (1-q)\frac1N\sum_{j=1}^N[F(x_j(t),y_j(t))+k_j],\\
 y_i(t+1)&=a y_i(t)-b x_i(t)+c,
\end{split}
\qquad (i=1,\ldots,N).
\]
Write \(\overline x=N^{-1}\sum_i x_i\), similarly for \(\overline y,\overline k\), and \(\boldsymbol\kappa=\mathbf k-\overline k\mathbf1\). Set
\[
Y=\frac{c}{1-a},\qquad
L_x=2(\sqrt2-1)e^{Y+\sqrt2-2},\quad
L_y=4e^{Y-2},\quad
L=L_x+\frac b{1-a}L_y.
\]
The result requires \(qL<1\); at \(q=0\) all bounded complete trajectories are exactly synchronized in both variables. A **bounded complete trajectory** is a sequence of states indexed by every integer, uniformly bounded as \(t\to\pm\infty\), satisfying both recurrences for every integer. No unique orbit, transverse Lyapunov exponent, or hyperbolicity assumption is imposed.

## Proof
**(1) Dissipativity and nonempty attractor.** Each voltage update is a convex combination of \(F(x,y)+k_i\), and \(F\ge0\), so every forward orbit has \(x_i(t)\ge k_{\min}\) from its first iterate onward. For nonnegative voltage, \(x^2e^{-x}\le4e^{-2}\). The scalar inequality \(y_i(t+1)\le ay_i(t)+c\) implies eventual uniform upper bounds \(y_i\le Y+\delta\) for any \(\delta>0\). Then \(x_i\le X_\delta:=k_{\max}+4e^{Y+\delta-2}\) on all sufficiently late iterates. Finally \(y_i(t+1)\ge a y_i(t)+c-bX_\delta\) gives eventual lower bounds. The closed box
\[
K_\delta=[k_{\min},X_\delta]^N\times
\left[\frac{c-bX_\delta}{1-a}-\delta,\ Y+\delta\right]^N
\]
is forward invariant: on its faces, the voltage image lies between \(k_{\min}\) and \(X_\delta\); the recovery image lies strictly inside or on the displayed bounds. It absorbs bounded initial sets (allowing a slightly larger \(\delta\) if needed). The nested nonempty compact sets \(F_q^n(K_\delta)\) have a nonempty compact intersection \(\mathcal A_q\); continuous finite-dimensional dynamics provides a bounded complete prehistory through each of its points. Thus the theorem is nonvacuous for every permissible parameter choice.

**(2) Uniform bounds on complete trajectories.** On any bounded bilateral orbit \(x_i(t)\ge k_{\min}\) for every integer, by applying the voltage recurrence at its predecessor. Iterating the recovery inequality from time \(t-n\) and letting \(n\to\infty\) gives \(y_i(t)\le Y\). Consequently \(x_i(t)\le k_{\max}+4e^{Y-2}\). In particular \(F\) is uniformly Lipschitz on the relevant half-strip. Indeed,
\[
\sup_{x\ge0}e^{-x}|2x-x^2|
=2(\sqrt2-1)e^{\sqrt2-2},\qquad
\sup_{x\ge0}x^2e^{-x}=4e^{-2}.
\]
As \(\partial_xF=(2x-x^2)e^{y-x}\) and \(\partial_yF=x^2e^{y-x}\), the constants \(L_x,L_y\) bound the respective derivatives whenever \(x\ge0\) and \(y\le Y\).

**(3) Exact centered equations.** Let \(P=I-N^{-1}\mathbf1\mathbf1^\mathsf T\), the Euclidean orthogonal projection onto the zero-mean subspace, and define \(\boldsymbol\xi_t=P\mathbf x_t\), \(\boldsymbol\eta_t=P\mathbf y_t\). Applying \(P\) cancels the all-to-all term exactly:
\[
\boldsymbol\xi_{t+1}=q\boldsymbol\kappa+qP\mathbf F_t,
\qquad
\boldsymbol\eta_{t+1}=a\boldsymbol\eta_t-b\boldsymbol\xi_t,
\]
where \(\mathbf F_t=(F(x_i(t),y_i(t)))_i\). Since \(P\) annihilates the constant vector \(F(\overline x_t,\overline y_t)\mathbf1\) and has operator norm one,
\[
\|P\mathbf F_t\|_2\le L_x\|\boldsymbol\xi_t\|_2+L_y\|\boldsymbol\eta_t\|_2.
\]
These are full nonlinear, not linearized, inequalities.

**(4) Uniform spatial imprint.** Put \(S_x=\sup_{t\in\mathbb Z}\|\boldsymbol\xi_t\|_2\) and \(S_y=\sup_{t\in\mathbb Z}\|\boldsymbol\eta_t\|_2\), both finite by bilateral boundedness. Iterating the recovery recurrence arbitrarily far into the past yields the convergent identity
\[
\boldsymbol\eta_t=-b\sum_{j=0}^{\infty}a^j\boldsymbol\xi_{t-1-j},
\quad S_y\le\frac b{1-a}S_x.
\]
Taking suprema in the centered voltage recurrence gives
\[
S_x\le q\|\boldsymbol\kappa\|_2+qLS_x,
\quad S_x\le \frac q{1-qL}\|\boldsymbol\kappa\|_2.
\]
Substituting this into \(\boldsymbol\xi_{t+1}-q\boldsymbol\kappa=qP\mathbf F_t\) yields the first theorem inequality. For the second, subtract \(-bq\boldsymbol\kappa/(1-a)\) inside the convergent recovery series and use the first bound term by term. Every step holds for each integer time and every bounded complete orbit, giving the stated quantifiers.

**(5) Spatial variance and leading coefficient.** For \(qL<1/2\), define \(d=qL/(1-qL)<1\). If \(\boldsymbol\kappa\ne0\), the triangle inequality yields
\[
(1-d)q\|\boldsymbol\kappa\|_2\le\|\boldsymbol\xi_t\|_2
\le(1+d)q\|\boldsymbol\kappa\|_2,
\]
for every complete orbit and time. Squaring and dividing by \(N\) proves the claimed uniform asymptotic spatial variance with explicit relative factor in \([(1-d)^2,(1+d)^2]\). This establishes the leading coefficient without relying on finite numerical experiments.

## Verification
The accompanying standalone script `check_chialvo.py` checks the calculus constants, the centered projection identity, positivity and invariance of an absorbing box at source parameters, and the numerical discrepancy bounds for simulated trajectories with several small values of \(q\). Analytic proof above, not the finite simulations, establishes the all-time and all-size statements. For the source's parameters \((a,b,c)=(0.89,0.18,0.28)\), the explicit sufficient range is \(q<0.0582316\ldots\), equivalently \(\varepsilon>0.9417683\ldots\). This sufficient threshold is not asserted to be sharp.

## Relationship to prior work
Velez-Rojas and Cosenza (2026) introduce exactly this quenched-heterogeneous, globally coupled Chialvo system and numerically study clustering and a chaotic Griffiths regime. Their numerical coherence observations do not state a uniform all-complete-orbits transverse profile, the universal leading coefficient, or the explicit size-independent remainder above. Lamb and Le (2026) analyze basin geometry for **two electrically and asymmetrically diffusive-coupled** Chialvo neurons, a different coupling operator with no corresponding rank-one mean-field cancellation. Other generic synchronization and near-identical-systems theory is a possible source of stronger abstract estimates; historical priority for the present specialized, quantified statement is not independently established.

## Limitations
The strong-coupling condition is sufficient and conservative; it need not hold in the Griffiths-phase parameter range studied numerically in the source. The statement concerns bounded complete trajectories and the compact attractor, not an arbitrary transient far from it. It does not assert synchronization for distinct quenched inputs (indeed the voltage spread is generally nonzero), classify longitudinal chaos, or prove existence of a chaotic Griffiths phase. The theorem assumes complete-graph mean-field averaging, strictly positive inputs, and \(0\le a<1\); sparse and random graph couplings require different analysis. The supporting finite calculations do not certify infinite-time behavior independently.

## References
1. Juan Velez-Rojas and M. G. Cosenza, *Chaotic Griffiths phase in neuron map networks*, arXiv:2610.03344v1 (2 October 2026). https://arxiv.org/html/2610.03344v1
2. Bennett Lamb and Brandon B. Le, *Final state sensitivity and fractal basin boundaries from coupled Chialvo neurons*, European Physical Journal Plus **141**, 1076 (2026), DOI:10.1140/epjp/s13360-026-08264-6.
3. S. Acharyya and R. E. Amritkar, *Synchronization of coupled nonidentical dynamical systems*, arXiv:1111.5408 (2011); relevant generic near-identity synchronization framework, consulted at abstract level.
