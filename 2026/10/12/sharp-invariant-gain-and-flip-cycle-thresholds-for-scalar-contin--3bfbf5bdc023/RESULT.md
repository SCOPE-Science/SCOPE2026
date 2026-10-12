# Sharp invariant-gain and flip-cycle thresholds for scalar continuous-time LQR gradient descent

## Finding

For scalar continuous-time linear-quadratic regulation (LQR), fixed-step direct policy-gradient descent has three distinct and *sharp* transition parameters: strict preservation of stabilizing gains, loss of attraction of the optimal gain, and loss of attraction of the unique positive two-cycle.

With the normalization in the next section, the parameter is \(t=\eta/(2\sqrt{1+a^2})\), where \(\eta\) is the gradient-descent step size. The update maps **every** stabilizing gain to another stabilizing gain if and only if
\[
0<t<\frac{3\sqrt 3}{2}.
\]
The optimal controller is a hyperbolically attracting fixed point for \(0<t<1\) and is repelling for \(t>1\). A distinct positive two-cycle exists uniquely for every \(t>1\). It is hyperbolically attracting precisely when
\[
1<t<t_*,\qquad t_*=\sqrt{\frac{2p_*^3}{p_*+1}},\qquad p_*=\frac{\sqrt{113}-1}{8},
\]
where \(t_*\approx1.25819035934\). Consequently, throughout \(1<t<t_*\) a fixed learning rate can preserve *all* stabilizing gains yet make the optimal gain repelling and an open neighborhood of a nonoptimal two-cycle attracting. The statements are about the exact deterministic update; no global attraction to this cycle is asserted.

## Assumptions and scope

Fix any real \(a\), and consider the scalar plant \(\dot x=a x+u\) with stationary state feedback \(u=-kx\), initial condition \(x(0)=1\), and continuous-time cost \(\int_0^\infty(x(s)^2+u(s)^2)\,ds\). Its feedback gain is stabilizing exactly when \(k>a\). For such gains,
\[
J(k)=\frac{1+k^2}{2(k-a)},\qquad
J'(k)=\frac12\left(1-\frac{1+a^2}{(k-a)^2}\right),\qquad
J''(k)=\frac{1+a^2}{(k-a)^3}>0.
\]
Thus the objective is strictly convex on its stabilizing domain and has the unique minimizer \(k_*=a+r\), where \(r=\sqrt{1+a^2}\). Its optimal cost is \(J(k_*)=a+r\).

Use the **ordinary Euclidean gradient in the gain** with constant \(\eta>0\): \(k_{j+1}=k_j-\eta J'(k_j)\). Set
\[
y=\frac{k-a}{r},\quad t=\frac{\eta}{2r},\quad F_t(y)=y+t\left(\frac1{y^2}-1\right).
\]
Then \(y>0\) means the controller is stabilizing, \(y=1\) is optimal, the update is exactly \(y_{j+1}=F_t(y_j)\), and \(J(k)=a+\frac r2(y+y^{-1})\). A *positive prime two-cycle* is an unordered pair of distinct positive values \(u,v\) with \(F_t(u)=v\), \(F_t(v)=u\). Attraction and repulsion are hyperbolic, determined by the derivative of \(F_t^2\). All statements quantify over \(a\in\mathbb R\) and \(t>0\) with the stated restrictions; no finite-step approximation is made.

## Proof

**(1) The sharp stabilizing-gain boundary.** Differentiation gives
\[
F_t'(y)=1-\frac{2t}{y^3},\qquad F_t''(y)=\frac{6t}{y^4}>0.
\]
For \(t>0\), the map diverges to positive infinity as \(y\downarrow0\) or \(y\to\infty\). Its sole global minimum occurs at \(y_c=(2t)^{1/3}\) and equals
\[
\min_{y>0}F_t(y)=\frac32(2t)^{1/3}-t.
\]
This is positive precisely when \(t^2<27/4\), hence precisely when \(0<t<3\sqrt3/2\). At equality some stabilizing starting gain maps to the boundary \(y=0\); for larger \(t\) some positive starting gain maps outside the stabilizing set. Strict positivity yields invariance for *every* iteration by induction, but says nothing about global convergence.

**(2) Fixed-point multiplier.** The equation \(F_t(y)=y\) gives \(y^{-2}=1\), so the only positive fixed point is \(y=1\). Its derivative is \(1-2t\), with modulus less than one exactly when \(0<t<1\), and modulus greater than one whenever \(t>1\). We do not classify the nonhyperbolic case \(t=1\) here.

**(3) Classification of positive prime two-cycles.** Suppose \(0<u<v\), \(F_t(u)=v\), \(F_t(v)=u\); put \(p=uv\) and \(s=u+v\). Subtraction and addition of the two relations, respectively, give
\[
2=\frac{t s}{p^2},\qquad \frac1{u^2}+\frac1{v^2}=2.
\]
The latter identity is equivalent to \(s^2=2p(p+1)\). Since \((v-u)^2=s^2-4p=2p(p-1)>0\), necessarily \(p>1\). Using \(t=2p^2/s\) yields
\[
t^2=\frac{2p^3}{p+1},\quad
u=\frac{s-\sqrt{2p(p-1)}}2,\quad
v=\frac{s+\sqrt{2p(p-1)}}2,
\quad s=\sqrt{2p(p+1)}.
\]
The function \(p\mapsto 2p^3/(p+1)\) is strictly increasing on \((1,\infty)\), with limit \(1\) at \(p\downarrow1\) and limit infinity as \(p\to\infty\). Hence for each \(t>1\) there is exactly one \(p>1\), and for \(t\le1\) there is none. Conversely, for the prescribed \(p,u,v,t\), their sum and difference equations both hold, and therefore \(F_t(u)=v\) and \(F_t(v)=u\). The pair is positive and distinct, proving existence and uniqueness (up to exchange).

**(4) Sharp cycle-multiplier boundary.** By the derivative formula in (1), the two-step multiplier is
\[
M(p)=F_t'(u)F_t'(v)=1-\frac{2t(u^3+v^3)}{p^3}+\frac{4t^2}{p^3}
=5-8p+\frac8{p+1}.
\]
Indeed \(u^3+v^3=s^3-3ps\). The multiplier is strictly decreasing on \(p>1\), from the limit \(1\) down to \(-\infty\). It reaches \(-1\) exactly when \(4p^2+p-7=0\), namely at \(p_*=(\sqrt{113}-1)/8>1\). Thus \(-1<M(p)<1\) exactly for \(1<p<p_*\), corresponding to \(1<t<t_*\), and \(M(p)<-1\) for \(t>t_*\). At the boundary \(t=t_*\), \(M=-1\); no hyperbolic classification is assigned there.

Because \(t_*\approx1.25819<3\sqrt3/2\), every gain in the domain remains stabilizing in the whole attracting-cycle interval. Since the two-cycle has \(|M|<1\), sufficiently close noncycle gains are attracted to its two phases, while \(F_t'(1)=1-2t<-1\) makes the optimal controller repelling. In particular, stabilizing invariance and convergence to the optimum are genuinely different properties.

**(5) Exact witness.** With \(a=0\), \(r=1\), choose \(p=9/8\). Then
\[
t=\frac{27}{4\sqrt{34}},\qquad
u=\frac{3(\sqrt{34}-\sqrt2)}{16},\qquad
v=\frac{3(\sqrt{34}+\sqrt2)}{16}.
\]
Direct substitution gives \(F_t(u)=v\), \(F_t(v)=u\), and \(F_t'(u)F_t'(v)=-4/17\). Both gains are stabilizing, the pair is nonoptimal, and its two-step multiplier has modulus strictly smaller than one.

## Verification

The accompanying `verify.py` uses exact symbolic arithmetic to check the objective derivative, normalized objective, map derivative and critical minimum, existence identities for the entire symbolic two-cycle family, the explicit multiplier, the defining critical polynomial, and the radical witness with multiplier \(-4/17\). Run `python verify.py` with the version-compatible SymPy dependency in `requirements.txt`. Its success output is an algebraic consistency check, not a replacement for the monotonicity, quantifier, stability, and boundary arguments above.

## Relationship to prior work

Bu, Mesbahi, and Mesbahi (2020) formulate continuous-time LQR as feedback-gain optimization and explicitly analyze the same Euclidean policy-gradient discretization, together with gain-dependent step-size conditions that guarantee stabilization and objective decrease (especially their §3, §4.1, §8 and appendices). The present theorem does not reassert their gradient formula or convergence guarantees; it classifies instead the exact **fixed-step, scalar, beyond-descent** regimes of the update map. The possibility of a locally attracting nonoptimal two-cycle despite global gain invariance does not follow from their sufficient step-size conditions.

Mohammadi, Zare, Soltanolkotabi, and Jovanović (2022) analyze continuous-time LQR gradient descent under sufficiently small step sizes depending on an initial cost sublevel set (their Theorem 2 and §V.C). Their result entails neither the parameter-independent sharp all-gain invariance threshold for this scalar specialization nor the exact nonconvergent two-cycle interval. Fazel et al. (2018) address discrete-time LQR and small-step convergence, whose objective and gain domain differ.

Mazumdar, Ratliff, Jordan, and Sastry (2019) report nonconvergence and numerically observed cycles of *joint multi-player gradient-play* in discrete-time LQ games; this is a different nonconvex, multi-controller dynamical system. The present exact scalar cycle is not an instance of their game construction or their strict-saddle theorem.

The generic one-dimensional facts that a hyperbolic two-cycle is attracting when its multiplier has modulus below one, and that a strictly convex function has a unique stationary minimizer, are standard and are not claimed as novel. Searches for equivalent inverse-square map formulations and specialized LQR large-learning-rate analyses did not establish prior coverage, but cannot exclude unindexed results.

## Limitations

The system is scalar, autonomous, deterministic, has unit state/control costs and unit initial state, and uses an exact Euclidean gain gradient; all parameters are specified. No statement is made about stochastic or model-free policy gradients, time-varying gains, matrix systems, non-unit weights, other initial-state distributions, finite precision, noisy measurements, or numerical implementation costs. A positive two-cycle exists for \(t>1\) even if the map fails to preserve the *whole* positive domain; outside the invariant regime, not all starting gains remain stabilizing. The nonhyperbolic cases \(t=1\) and \(t=t_*\) are not classified asymptotically. The result does not classify higher-period orbits, chaotic dynamics, or the global basin of the two-cycle. Priority beyond the inspected literature is not independently certified.

## References

1. J. Bu, A. Mesbahi, and M. Mesbahi, *Policy Gradient-based Algorithms for Continuous-time Linear Quadratic Control*, arXiv:2006.09178v1 (first posted June 12, 2020), https://arxiv.org/html/2006.09178v1 .
2. H. Mohammadi, A. Zare, M. Soltanolkotabi, and M. R. Jovanović, *Convergence and Sample Complexity of Gradient Methods for the Model-Free Linear–Quadratic Regulator Problem*, IEEE Transactions on Automatic Control (2022), DOI 10.1109/TAC.2021.3087455, open author copy https://hesameddinm.github.io/papers/mohzarsoljovTAC22.pdf .
3. M. Fazel et al., *Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator*, Proceedings of ICML, PMLR 80 (2018), https://proceedings.mlr.press/v80/fazel18a/fazel18a.pdf .
4. E. Mazumdar, L. J. Ratliff, M. I. Jordan, and S. S. Sastry, *Policy-Gradient Algorithms Have No Guarantees of Convergence in Linear Quadratic Games*, arXiv:1907.03712 (2019), https://arxiv.org/pdf/1907.03712 .
5. Mathematics Subject Classification 2020, code 90C25: Convex programming, https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=90Cxx .
