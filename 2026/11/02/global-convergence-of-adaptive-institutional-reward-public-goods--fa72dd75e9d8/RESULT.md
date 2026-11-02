# Global convergence of adaptive institutional-reward public-goods games at all feedback speeds

## Finding

**Theorem.** Consider the following replicator–feedback system, for an integer \(N\geq 2\):
\[
\varepsilon\dot x=x(1-x)[-\kappa+\delta a S_N(x)],\qquad
\dot a=(a-\alpha)(\beta-a)[u-(u+1)x],
\qquad S_N(x)=\sum_{j=0}^{N-1}(1-x)^j.
\]
Let \(c>0\), \(1<r<N\), \(\kappa=c(1-r/N)>0\), \(\delta>0\), \(u>0\), \(0<\alpha<\beta\), and let the timescale \(\varepsilon>0\) be arbitrary, not necessarily small. Set
\[
x_*={u\over u+1},\qquad a_*={\kappa\over\delta S_N(x_*)}.
\]
If \(\alpha<a_*<\beta\), then every solution with \((x(0),a(0))\in(0,1)\times(\alpha,\beta)\) exists for all forward time, stays a positive distance from each boundary along its individual orbit, and converges to the **unique interior equilibrium** \((x_*,a_*)\). In particular, no nonconstant periodic orbit or other nontrivial recurrent orbit lies in the open state rectangle.

A strict, explicitly coercive Lyapunov function proving this assertion is
\[
V(x,a)=(u+1)D(x_*\Vert x)+{\delta S_N(x_*)\over\varepsilon}D(p_*\Vert p),
\quad p={a-\alpha\over\beta-\alpha},\quad p_*={a_*-\alpha\over\beta-\alpha},
\]
where \(D(s\Vert t)=s\log(s/t)+(1-s)\log[(1-s)/(1-t)]\) is the Bernoulli relative entropy. Its exact derivative is
\[
\dot V={\delta a\over\varepsilon}[u-(u+1)x][S_N(x_*)-S_N(x)]\leq 0,
\]
with equality only when \(x=x_*\) in the open rectangle.

There is also a **sharp node-to-focus transition** in the interior equilibrium's linearization. Define
\[
P=\delta a_*x_*(1-x_*)[-S_N'(x_*)],\qquad
Q=\delta x_*(1-x_*)S_N(x_*)(u+1)(a_*-\alpha)(\beta-a_*).
\]
These are positive and the characteristic polynomial is \(\lambda^2+(P/\varepsilon)\lambda+Q/\varepsilon\). Consequently the equilibrium is a stable node for \(0<\varepsilon<P^2/(4Q)\), a non-diagonalizable repeated-negative-eigenvalue node at equality, and a stable focus for \(\varepsilon>P^2/(4Q)\). This classification concerns local decay geometry; **global convergence holds on both sides**.

## Assumptions and scope

The evolutionary model is the homogeneous deterministic \(N\)-player public-goods game with adaptation of institutional reward strength, as formulated in Hua and Liu (2023), equation (6). The analysis assumes the same unmodified payoff and feedback equations, positive parameters, an interior equilibrium satisfying \(\alpha<a_*<\beta\), and interior initial data. The theorem does not assert attraction from invariant rectangle boundaries, and it does not apply to stochastic updates, delays, discontinuous reward control, or alternative feedback laws.

## Proof

**1. Interior equilibria and monotonicity.** The feedback equation vanishes at interior states exactly when \(u-(u+1)x=0\), hence \(x=x_*\). Then the first equation requires \(a=a_*\), which is inside the permitted interval precisely by hypothesis. Because \(N\geq2\),
\[
S_N'(x)=-\sum_{j=1}^{N-1}j(1-x)^{j-1}<0\quad (0<x<1).
\]

**2. Invariance and derivatives.** The right-hand side is smooth on the closed rectangle and tangent to its boundary; uniqueness of solutions preserves the open rectangle for every finite forward time. For any fixed \(s\in(0,1)\), differentiating the Bernoulli divergence gives \(\partial_t D(s\Vert t)=(t-s)/[t(1-t)]\). Substitution therefore yields
\[
\partial_xV=-{u-(u+1)x\over x(1-x)},\qquad
\partial_aV={\delta S_N(x_*)\over\varepsilon}\,{a-a_*\over(a-\alpha)(\beta-a)}.
\]
Using \(\kappa=\delta a_*S_N(x_*)\) and both equations gives exactly the derivative stated under **Finding**. Since \(u-(u+1)x=-(u+1)(x-x_*)\) and \(S_N\) is strictly decreasing, \(\dot V<0\) whenever \(x\ne x_*\).

**3. Compactness and global convergence.** Both coefficients in \(V\) are positive, and each binary relative entropy tends to \(+\infty\) as its variable approaches either endpoint of \((0,1)\). Thus each sublevel \(\{(x,a):V(x,a)\leq V(x(0),a(0))\}\) is a compact subset of the open rectangle. Nonincrease of \(V\) makes this sublevel forward invariant; solutions are forward complete and precompact. By LaSalle's invariance principle, every omega-limit set lies in the largest invariant subset of \(\{x=x_*\}\). But on this vertical line,
\[
\varepsilon\dot x=x_*(1-x_*)\delta S_N(x_*)(a-a_*),
\]
so the only trajectory that remains on it has \(a=a_*\). The omega-limit set is therefore the singleton equilibrium; this proves global convergence and absence of interior recurrence.

**4. Spectral crossover.** At \((x_*,a_*)\), the Jacobian is
\[
J_*=
\begin{pmatrix}
-P/\varepsilon & \delta x_*(1-x_*)S_N(x_*)/\varepsilon\\
-(u+1)(a_*-\alpha)(\beta-a_*)&0
\end{pmatrix}.
\]
It has trace \(-P/\varepsilon<0\), determinant \(Q/\varepsilon>0\), and discriminant \((P^2-4\varepsilon Q)/\varepsilon^2\). At zero discriminant the nonzero upper-right entry precludes a scalar matrix, so the repeated eigenvalue has a nontrivial Jordan block. The node/focus regimes follow exactly.

**5. Reproducible rational instance.** For \(N=5\), \(r=3\), \(c=1\), \(\delta=1/5\), \(\alpha=1/2\), \(\beta=3\), \(u=2\), one obtains
\[
x_*=2/3,\quad a_*=162/121,\quad P=232/1815,\quad Q=13601/49005,
\quad \varepsilon_{\mathrm{focus}}={4176\over283745}.
\]
The attached standalone symbolic checker reconstructs these identities exactly and checks illustrative log-odds trajectories for multiple \(\varepsilon\) values.

## Verification

Run `python verify_adaptive_reward.py` with the versions listed in `requirements.txt`. The symbolic checks reconstruct both entropy gradients and their cancellation for \(N=2,\ldots,12\), the critical characteristic-polynomial identities, and four exact timescale comparisons. Nine log-odds-coordinate numerical integrations confirm the attracting equilibrium from disparate interior initial conditions. The all-\(N\), all-\(\varepsilon\) theorem follows from the analytical argument, not from finite checks or finite-time numerics.

## Relationship to prior work

Hua and Liu (2023), equation (6), supplies the exact adaptive institutional-reward system and characterizes equilibrium existence and local Jacobian stability, while Figure 2 reports numerical trajectories converging for one parameter configuration and its text states convergence in that example. The present theorem makes this **global for every eligible parameter configuration and every positive timescale**, and provides a proper entropy certificate that excludes cycles. The explicit sharp node/focus boundary is a separate local consequence. The related adaptive-gain control papers by Zino and colleagues concern two-player matrix-game controls with different adjustment equations; they do not contain this multiplayer payoff-dependent entropy identity. Related collective-risk feedback games have different, non-monotone payoff functions and can exhibit oscillatory dynamics, so their phase diagrams do not imply this result.

## Limitations

The result requires \(\alpha<a_*<\beta\) and all relevant parameters strictly positive, and only concerns interior initial states. Invariant boundary initial states may converge elsewhere; no uniform settling-time estimate over the whole open rectangle is claimed. The node/focus distinction characterizes the linearization, not necessarily the number of peaks in any particular nonlinear trajectory. No claim of universal novelty in all unindexed literature or of independent validation is made.

## References

1. Shijia Hua and Linjie Liu, *Coevolutionary dynamics of population and institutional rewards in public goods games*, arXiv:2308.09530 (first posted 2023-08-18), especially equation (6), Section 4, and Appendix. https://arxiv.org/abs/2308.09530
2. Lorenzo Zino et al., *On Adaptive-Gain Control of Replicator Dynamics in Population Games*, arXiv:2306.14469 (2023). https://arxiv.org/abs/2306.14469
3. Lorenzo Zino et al., *Equilibrium Selection in Replicator Equations Using Adaptive-Gain Control*, arXiv:2407.09305 (2024). https://arxiv.org/abs/2407.09305
4. *Coevolutionary dynamics via adaptive feedback in collective-risk social dilemma game*, arXiv:2305.00253 (2023). https://arxiv.org/abs/2305.00253
