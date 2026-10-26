# Harmonic-feedback resonance and exponential environmental escape in a two-community game

## Finding

For the two-community, three-edge-environment evolutionary game of Betz, Fu and Masuda [1], a single exact log-odds observable detects whether persistent fully interior environmental dynamics are possible. Set
\[
u_1=\frac{1}{1+\theta_1},\qquad u_2=\frac{1}{1+\theta_2},\qquad u_{12}=\frac{1}{1+\theta_{12}},\qquad
\Delta=2u_{12}-u_1-u_2,\qquad W=u_1+u_2+2u_{12}.
\]
For environmental coordinates \(n_1,n_2,n_{12}\in(0,1)\), define the usual log-odds \(\ell(n)=\log(n/(1-n))\) and
\[
H=u_1\ell(n_1)+u_2\ell(n_2)-2u_{12}\ell(n_{12}).
\]
**Exact drift:** every trajectory with initially interior environmental coordinates satisfies
\[
\boxed{H(t)=H(0)+\Delta t}\qquad(t\ge0).
\]
The drift is independent of the payoff matrices and the within-versus-between community interaction rate. For \(\Delta\ne0\), there is no equilibrium, periodic orbit, compact invariant set, or invariant probability distribution whose support remains wholly within the environmental interior.

**Signed environmental-boundary envelope:** if \(\Delta>0\), then for every \(t\ge0\),
\[
\boxed{\min\{1-n_1(t),1-n_2(t),n_{12}(t)\}
\le\frac{1}{1+\exp((H(0)+\Delta t)/W)}.}
\]
If \(\Delta<0\), then
\[
\boxed{\min\{n_1(t),n_2(t),1-n_{12}(t)\}
\le\frac{1}{1+\exp((-H(0)-\Delta t)/W)}.}
\]
Thus the distance of the environmental triple to the indicated union of three boundary faces decreases at least exponentially, with exponent \(\lvert\Delta\rvert/W\). The logistic envelope is optimal at each fixed value of \(H\), as an inequality using no information beyond that value.

**Exact resonance and attainability:** a necessary condition for any compact, fully interior recurrent dynamics is
\[
\boxed{\frac{2}{1+\theta_{12}}=
\frac{1}{1+\theta_1}+\frac{1}{1+\theta_2}.}
\]
This condition cannot be strengthened to a nonexistence assertion on the resonance surface. For every positive feedback triple satisfying it, an explicit single pair of admissible payoff matrices has a nontrivial one-parameter family of strictly interior equilibria, even if \(\theta_1\ne\theta_2\).

## Assumptions and scope

The system has cooperation fractions \(x,y\in[0,1]\), interaction rate \(0<\delta<1\), and three environment qualities \(n_1,n_2,n_{12}\in[0,1]\). Its strategy equations are the two-community replicator equations from [1], with the game payoffs \(A(n)=(1-n)A(0)+nA(1)\). The game matrices satisfy \(R_0>T_0\), \(S_0>P_0\), \(R_1<T_1\), and \(S_1<P_1\), as in [1]. Only their boundedness is needed for the drift and escape conclusions. The environmental equations, exactly as in [1, Eqs. (8)--(10)], are
\[
\begin{aligned}
\dot n_1&=n_1(1-n_1)((1+\theta_1)x-1),\\
\dot n_2&=n_2(1-n_2)((1+\theta_2)y-1),\\
\dot n_{12}&=n_{12}(1-n_{12})\left(\frac{1+\theta_{12}}2(x+y)-1\right),
\end{aligned}
\]
with \(\theta_1,\theta_2,\theta_{12}>0\). All three environments begin strictly between zero and one. The original replicator equations preserve \(x,y\in[0,1]\), and the environmental logistic factors preserve strict interiority at every finite time. This theorem concerns deterministic continuous time and the equal-sized-community mean \((x+y)/2\) used in [1].

## Proof

**1. Global well-defined log-odds.** Because \(x,y\in[0,1]\), each environmental logarithmic derivative is bounded in magnitude on every finite time interval. The scalar equations \(\dot n_i=n_i(1-n_i)g_i(t)\) imply \(\ell(n_i(t))=\ell(n_i(0))+\int_0^t g_i(s)\,ds\). Consequently an initially interior environment cannot reach its boundary in finite time; the observable \(H\) is well defined for all \(t\ge0\).

**2. Exact drift cancellation.** Taking a time derivative yields
\[
\begin{aligned}
u_1\frac d{dt}\ell(n_1)&=x-u_1,\\
u_2\frac d{dt}\ell(n_2)&=y-u_2,\\
2u_{12}\frac d{dt}\ell(n_{12})&=x+y-2u_{12}.
\end{aligned}
\]
Subtracting the third equality from the sum of the first two proves \(\dot H=2u_{12}-u_1-u_2=\Delta\), and integration proves the stated identity. No assumption on the behavior of the strategy subsystem is used.

**3. Recurrent-state obstruction.** If \(\Delta\ne0\), then \(\lvert H(t)\rvert\to\infty\). On any compact subset of \([0,1]^2\times(0,1)^3\), however, \(H\) is bounded. No forward-complete trajectory can stay in such a compact subset. An equilibrium or a periodic orbit with interior environmental coordinates would stay in one, giving a contradiction. A compact invariant set contained in this region would likewise contain a forward trajectory with bounded \(H\), also impossible. Finally, if \(\mu\) is an invariant probability measure supported on such a compact set, invariance gives \(\int \dot H\,d\mu=0\) while the exact calculation gives \(\int\dot H\,d\mu=\Delta\), a contradiction. This proof does not exclude invariant states on boundary faces.

**4. Pointwise exponential escape and its optimality from \(H\).** Define \(L_1=\ell(n_1)\), \(L_2=\ell(n_2)\), \(L_{12}=\ell(n_{12})\). If \(\Delta>0\), then
\[
H=u_1L_1+u_2L_2+2u_{12}(-L_{12})
\le W\max\{L_1,L_2,-L_{12}\}.
\]
The three distances to the faces \(n_1=1\), \(n_2=1\), and \(n_{12}=0\) are \(1/(1+e^{L_1})\), \(1/(1+e^{L_2})\), and \(1/(1+e^{-L_{12}})\), respectively. Because \(z\mapsto(1+e^z)^{-1}\) is decreasing, their minimum obeys the first envelope. If \(\Delta<0\), apply the same argument to \(-H=u_1(-L_1)+u_2(-L_2)+2u_{12}L_{12}\) and the complementary three faces. In either case the signed exponent grows as \(\lvert\Delta\rvert t/W\). For any prescribed finite \(h\), equality in the relevant envelope at \(H=h\) occurs at the environmental triple with logits \(L_1=L_2=h/W\), \(L_{12}=-h/W\). Thus the pointwise logistic bound cannot be improved using \(H\) alone.

If every environment stays in the core \([\varepsilon,1-\varepsilon]\) for \(0\le t\le T\), where \(0<\varepsilon<1/2\), write \(L_\varepsilon=\log((1-\varepsilon)/\varepsilon)\) and \(s=\operatorname{sgn}\Delta\). Then \(\lvert H(T)\rvert\le W L_\varepsilon\), so the uninterrupted residence time obeys the explicit finite bound
\[
\boxed{T\le\frac{W L_\varepsilon-sH(0)}{\lvert\Delta\rvert}.}
\]

**5. Resonance is attainable without population symmetry.** Fix any \(\theta_1,\theta_2,\theta_{12}>0\) with \(\Delta=0\) and any \(0<\delta<1\). Use the admissible games
\[
A(0)=\begin{pmatrix}3&2\\1&0\end{pmatrix},\qquad
A(1)=\begin{pmatrix}1&0\\3&2\end{pmatrix}.
\]
In either game, the cooperator-minus-defector payoff is independent of the opponent's choice and equals \(2-4n\) at environment level \(n\). Take
\[
x=u_1,\qquad y=u_2,\qquad n_{12}=q,\qquad
n_1=n_2=\frac{1/2-\delta q}{1-\delta},
\]
where \(q\) varies in a sufficiently small open interval about \(1/2\). Then all five coordinates are strictly interior. Both community payoff differences vanish, so \(\dot x=\dot y=0\). Both within-community environment equations vanish because \(x=u_1\) and \(y=u_2\), and the between-community one vanishes because \((x+y)/2=u_{12}\) at resonance. This yields a genuine one-parameter continuum of equilibria. In particular \((\theta_1,\theta_2,\theta_{12})=(1,3,5/3)\) gives the asymmetric equilibrium \((x,y,n_1,n_2,n_{12})=(1/2,1/4,1/2,1/2,1/2)\).

## Verification

The accompanying `checks.py` uses only Python's standard library. It performs 180 exact-rational tests of the feedback cancellation and resonance algebra, 250 pointwise logistic-envelope and equality-attainment checks, and a full five-coordinate Runge--Kutta integration of an admissible two-community payoff system over 30 time units. The largest observed log-odds drift residual in the time integration is approximately \(3.05\times10^{-11}\). It also evaluates the fully asymmetric resonant equilibrium and returns exactly zero for all five derivatives. These are independent consistency checks; the proof above, not finite tests, establishes the infinite-time claim.

For the illustrative feedback parameters \((\theta_1,\theta_2,\theta_{12})=(3,5,8)\) used in [1, Fig. 8], the exact values are \(\Delta=-7/36\), \(W=23/36\), and \(\lvert\Delta\rvert/W=7/23\). Hence all initially environmentally interior trajectories at those parameters become exponentially close to at least one of \(n_1=0\), \(n_2=0\), or \(n_{12}=1\), whatever their interaction rate and initial cooperation fractions.

## Relationship to prior work

Betz, Fu and Masuda [1] derived the five equations, characterized equilibria in a symmetric reduction, and analyzed general five-dimensional equilibria and numerical behavior. In their symmetric reduction the absence of interior equilibria for mismatched enhancement/degradation ratios is established, but no payoff-independent affine log-odds functional, sharp environmental-face envelope, or exclusion of compact interior recurrent states in the general asymmetric five-dimensional system is stated in the inspected primary versions [1,2]. The present theorem goes beyond the equilibrium condition by excluding all compact interior recurrent dynamics for nonresonant parameter triples and quantifying how rapidly some environmental coordinate must approach a particular boundary union. The resonant example establishes realizability in a fixed admissible payoff family for arbitrary, including asymmetric, resonant feedback strengths.

Gong, Gao and Cao [3] analyze a different two-population model with one shared environmental coordinate, proving convergence and periodicity under different assumptions. Govaert, Zino and Tegling [4] analyze changing community densities rather than three independent edge-type environmental qualities. Neither inspected model has the three logistic environmental equations whose weighted differences produce the present drift. Standard log-odds differentiation is not claimed as new in itself; the specific harmonic resonance, global obstruction, optimal bound, and realization in the stated network game form the result.

## Limitations

The conclusion describes proximity to a union of environmental faces, not convergence of any individually preselected environmental coordinate or convergence of the full dynamical state. Boundary equilibria and boundary periodic behavior remain possible. The resonance condition is necessary for fully interior recurrence but is not a sufficient condition for recurrence under every payoff matrix; only existence of an interior equilibrium family for one explicit admissible payoff choice is proved. The theorem assumes equal community sizes, constant feedback parameters, and the exact logistic edge-environment dynamics. It makes no stochastic or globally attracting-cycle assertion. Originality has not undergone independent bibliographic validation.

## References

[1] K. Betz, F. Fu, and N. Masuda, *Evolutionary game dynamics with environmental feedback in a network with two communities*, arXiv:2404.17082v1, first public 25 April 2024. https://arxiv.org/html/2404.17082v1

[2] K. Betz, F. Fu, and N. Masuda, same work, arXiv:2404.17082v2, 7 June 2024; *Bulletin of Mathematical Biology* 86, 84 (2024). https://arxiv.org/html/2404.17082v2 ; https://doi.org/10.1007/s11538-024-01310-3

[3] L. Gong, J. Gao, and M. Cao, *Evolutionary Game Dynamics for Two Interacting Populations under Environmental Feedback*, arXiv:1806.03194 (2018). https://arxiv.org/abs/1806.03194

[4] A. Govaert, L. Zino, and E. Tegling, *Population games on dynamic community networks*, arXiv:2203.00371 (2022). https://arxiv.org/abs/2203.00371
