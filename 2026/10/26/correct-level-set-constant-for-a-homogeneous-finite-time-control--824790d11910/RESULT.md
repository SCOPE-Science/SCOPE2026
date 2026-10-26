# Correct level-set constant for a homogeneous finite-time control bound

## Finding

For the homogeneous optimal-control problem in Theorem 6.5 of Weng–Chitour–Mason, let \(V_\infty\) be the value function, \(K=\{x:V_\infty(x)=1\}\), and \(m=\min_{x\in K}F(x)>0\). The Lyapunov comparison rigorously gives

\[
T_{x_0}\leq\frac{d+\mu}{m\mu}V_\infty(x_0)^{\mu/(d+\mu)}.
\]

The coefficient required by this proof is the minimum of the running cost on the unit value-function level set, not its maximum. An admissible anisotropic example below shows that the two extrema need not coincide. This repairs the coefficient justified by the displayed comparison argument; it does not claim that the preprint's printed maximum-based numerical bound is false by every possible argument.

## Assumptions and scope

Consider \(\dot x=J_nx+e_nu\), where \(J_n\) is the nilpotent Jordan block with ones on the superdiagonal and \(e_n\) is the last coordinate vector, with running cost \(|u|^q/q+F(x)\). Here \(q>1\), and \(F\) is continuously differentiable, convex, and positive definite. Assume the homogeneity conditions used in Theorem 6.5 of Weng–Chitour–Mason: for positive \(d,\mu\), define the weighted dilation by \(\delta^r_\epsilon x=(\epsilon^{r_1}x_1,\ldots,\epsilon^{r_n}x_n)\), with weights \(r_i=d/q+(n-i+1)\mu\). Assume \(F(\delta^r_\epsilon x)=\epsilon^dF(x)\) and \(\mu<d(q-1)/(qn)\). Their value function is positive definite, proper, continuously differentiable, and homogeneous of degree \(d+\mu\):

\[
V_\infty(\delta^r_\epsilon x)=\epsilon^{d+\mu}V_\infty(x).
\]

Let \(T_{x_0}\) denote the first time the optimal trajectory from \(x_0\) reaches and remains at zero. The result concerns the rigorous uniform bound supplied by this Lyapunov comparison, not a claim that the source's numerical estimate has been disproved by a separate trajectory-level counterexample.

## Proof

The stationary Hamilton–Jacobi–Bellman equation in the source is

\[
\nabla V_\infty(x)^\top J_nx-\frac{q-1}{q}\left|\partial_nV_\infty(x)\right|^{q/(q-1)}+F(x)=0.
\]

The optimal feedback is \(u_\infty(x)=-\operatorname{sgn}(\partial_nV_\infty(x))|\partial_nV_\infty(x)|^{1/(q-1)}\). Along an optimal trajectory, substitution into the derivative of \(V_\infty\) yields

\[
\dot V_\infty=-F(x)-\frac1q\left|\partial_nV_\infty(x)\right|^{q/(q-1)}\leq-F(x).
\]

Because \(V_\infty\) is proper and positive definite, \(K=V_\infty^{-1}(1)\) is compact and excludes the origin. Continuity and positive definiteness of \(F\) give \(m=\min_KF>0\). For any \(x\ne0\), put \(\epsilon=V_\infty(x)^{1/(d+\mu)}\) and \(y=\delta^r_{1/\epsilon}x\). Homogeneity gives \(V_\infty(y)=1\), hence

\[
F(x)=\epsilon^dF(y)\geq mV_\infty(x)^{d/(d+\mu)}.
\]

Consequently \(\dot V_\infty\leq-mV_\infty^{d/(d+\mu)}\), and while \(V_\infty>0\),

\[
\frac{d}{dt}V_\infty^{\mu/(d+\mu)}\leq-\frac{m\mu}{d+\mu}.
\]

Integrating until the first hitting time of zero proves the claimed estimate.

The distinction between minimum and maximum is genuine under the source's assumptions. Take \(n=2\), \(q=2\), \(d=2\), \(\mu=1/5\), and

\[
F(x_1,x_2)=|x_1|^{10/7}+|x_2|^{5/3}.
\]

The weights are \(r_1=7/5\), \(r_2=6/5\); both powers exceed one, so \(F\) is continuously differentiable, convex, positive definite, and homogeneous of degree two. The condition \(\mu<d(q-1)/(qn)\) holds because \(1/5<1/2\). If \(F\) were constant on \(K\), homogeneity would force \(V_\infty=C F^{11/10}\) for some \(C>0\). At \((s,0)\), for any \(s\ne0\), this would give \(\partial_2V_\infty=0\); also \(J_2(s,0)=0\). The HJB equation would then reduce to \(F(s,0)=0\), a contradiction. Thus \(\min_KF<\max_KF\) in this admissible case, so the maximum cannot be used as the lower comparison coefficient in the displayed argument.

## Verification

The bound follows from the source's HJB equation, the stated homogeneity of \(V_\infty\) and \(F\), compactness of \(K\), and a one-line scalar differential inequality. The anisotropic example verifies that the two level-set extrema can differ under all stated assumptions. No numerical experiment or unverified computation is used. The proof establishes the minimum-based bound and the failure of the maximum-based substitution in this argument; it does not establish that the printed maximum-based time estimate is false by every possible alternative argument.

## Relationship to prior work

Weng, Chitour, and Mason, *Finite-Time Stabilization of Linear Systems via Optimal Control* (arXiv:2607.22191v1, first public on 2026-07-24), Theorem 6.5 and its proof, state the coefficient as \(\max_{V_\infty^{-1}(1)}F\) immediately before deriving the comparison inequality. Their HJB equation and homogeneity lemma supply the premises used here. The correction is to the level-set extremum required by that proof.

Bhat and Bernstein, *Finite-Time Stability of Continuous Autonomous Systems* (2000), and Kisole, Garg, and Peet, *Bounding the Settling Time of Finite-Time Stable Systems using Sum of Squares* (arXiv:2501.11255, 2025), give the general comparison principle: if \(\dot V\leq-aV^\gamma\), then \(T(x_0)\leq V(x_0)^{1-\gamma}/(a(1-\gamma))\). These general results justify the integration once a valid lower coefficient \(a\) is established; they do not turn a maximum of \(F\) on a level set into a lower bound for \(F\).

## Limitations

This finding repairs the coefficient justified by the source's displayed Lyapunov argument. It does not furnish a trajectory-level counterexample to the printed maximum-based settling-time estimate itself, and it does not exclude the possibility of a different proof for that estimate. The source is an arXiv preprint; no independent audit or external validation has been performed. The result assumes the source's hypotheses, including convexity, positive definiteness, differentiability, and weighted homogeneity.

## References

1. W. Weng, Y. Chitour, and P. Mason, “Finite-Time Stabilization of Linear Systems via Optimal Control,” arXiv:2607.22191v1, first public 2026-07-24. https://arxiv.org/abs/2607.22191
2. S. P. Bhat and D. S. Bernstein, “Finite-Time Stability of Continuous Autonomous Systems,” *SIAM Journal on Control and Optimization* 38(3) (2000), 751–766. DOI: 10.1137/S0363012997321358. https://doi.org/10.1137/S0363012997321358
3. S. Kisole, K. Garg, and M. Peet, “Bounding the Settling Time of Finite-Time Stable Systems using Sum of Squares,” arXiv:2501.11255, first public 2025-01-20. https://arxiv.org/abs/2501.11255
