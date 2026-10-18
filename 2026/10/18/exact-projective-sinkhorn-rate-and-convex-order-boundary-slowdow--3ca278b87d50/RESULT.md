# Exact projective Sinkhorn rate and convex-order boundary slowdown for the minimal martingale transport grid

## Finding

For \(0<a<T<1\), set \(\mu=(\delta_{-a}+\delta_a)/2\) and \(\nu=T(\delta_{-1}+\delta_1)/2+(1-T)\delta_0\). Consider alternating exact relative-entropy projections, first onto the prescribed source marginal **and** martingale conditional means, and then onto the prescribed terminal marginal. Start from any strictly positive terminal exponential weights. After each martingale half-step, the joint law belongs to a one-parameter family \(\pi_r\), where the conditional probabilities at \(X=a\), in terminal order \((-1,0,1)\), are
\[
\left(\frac{r-a}{2},\ 1-r,\ \frac{r+a}{2}\right),\qquad a<r<1,
\]
and the law at \(X=-a\) is its reflection.

Write the terminal weights as \((u_-,u_0,u_+)\), and define their projective invariant
\[
q=\frac{\sqrt{u_-u_+}}{u_0},\qquad Q_a(r)=\frac{\sqrt{r^2-a^2}}{2(1-r)}.
\]
The martingale half-step has \(q=Q_a(r)\). One subsequent terminal-marginal rescaling gives the **exact scalar full-cycle map**
\[
\boxed{\ q_{k+1}=q_k\frac{T(1-r_k)}{(1-T)r_k},\qquad r_k=Q_a^{-1}(q_k).\ }
\]
Every \(q_0>0\) converges monotonically, with no overshoot, to \(q_*=Q_a(T)\), and therefore \(r_k\to T\), the entropy-minimizing martingale plan. If \(q_0\ne q_*\), the **exact asymptotic linear rate** for \(z_k=\log q_k\) and for \(r_k\) is
\[
\boxed{\ \lambda(a,T)=\frac{a^2(1-T)}{T(T-a^2)}\in(0,1).\ }
\]
For the relative entropy of the martingale half-step plans, the exact asymptotic ratio is \(\lambda(a,T)^2\):
\[
\lim_{k\to\infty}\frac{D_{\mathrm{KL}}(\pi_{r_{k+1}}\Vert\pi_T)}{D_{\mathrm{KL}}(\pi_{r_k}\Vert\pi_T)}=\lambda(a,T)^2.
\]
Although every fixed \(a<T\) enjoys geometric convergence, as the convex-order slack \(T-a\downarrow0\) at fixed \(a\in(0,1)\),
\[
\boxed{\ 1-\lambda(a,T)=\frac{2(T-a)}{a(1-a)}+O((T-a)^2).\ }
\]
Thus the sharp local convergence factor degenerates to one linearly in the convex-order slack. The full-cycle map has no global Euclidean Lipschitz constant strictly below one on the entire log-projective line.

## Assumptions and scope

All measures have the stated finite support, with \(0<a<T<1\). The reference measure is \(\mu\otimes\nu\), and the transport cost is identically zero. Relative entropy and KL projections use natural logarithms. The source-martingale projection is the unique KL minimizer subject to \(\pi_X=\mu\) and \(\mathbb E[Y\mid X=x]=x\); the following projection enforces \(\pi_Y=\nu\). This is the exact cyclic Bregman-projection iteration; a full cycle consists of exactly these two half-steps. The iteration starts from a measure proportional to \(\mu(x)\,u_y\), where every \(u_y>0\); the overall multiplier scale and affine martingale gauge do not affect the coupling. Throughout, \(r_k\) denotes the plan **after the martingale half-step**, not the intervening terminal-scaled measure. This distinction is necessary because the terminal-scaled measure need not yet satisfy the conditional-mean constraints. No stochastic sampling or numerical approximation is part of the theorem.

Both marginals are centered, and \(\mu\preceq_{\mathrm{cx}}\nu\), with a strictly positive feasible martingale plan when \(T>a\). There is generally a continuum of feasible plans; \(\pi_T\) is the unique KL minimizer, not the unique feasible martingale plan.

## Proof

**1. Exact martingale projection and scalar parameter.** For fixed positive \(u_y\), the KL-minimizing conditional law on each source row \(x\in\{-a,a\}\) is
\[
p_x(y)=\frac{u_y\exp(\theta_x y)}{\sum_{v\in\{-1,0,1\}}u_v\exp(\theta_x v)},
\]
where the unique real \(\theta_x\) enforces \(\sum_y yp_x(y)=x\). Strict positivity and \(-1<x<1\) guarantee existence and uniqueness. In each row, the product-to-middle-square ratio satisfies
\[
\frac{p_x(-1)p_x(1)}{p_x(0)^2}=\frac{u_-u_+}{u_0^2}=q^2.
\]
If the row mean is \(x=a\), write its total endpoint probability as \(r\). The row entries are necessarily \(((r-a)/2,1-r,(r+a)/2)\), whence
\[
q^2=\frac{r^2-a^2}{4(1-r)^2}.
\]
The same product ratio and row mean \(x=-a\) determine the reflected conditional row, with **the same** \(r\), because \(Q_a:(a,1)\to(0,\infty)\) is bijective. Thus the martingale step gives \(\pi_r\) for arbitrary positive starting weights, without a symmetry assumption on those weights.

**2. Exact terminal rescaling.** The terminal probabilities of \(\pi_r\) are \((r/2,1-r,r/2)\). To impose the target probabilities \((T/2,1-T,T/2)\), the next terminal weight multipliers are
\[
(u_-',u_0',u_+')=\left(\frac{T}{r}u_-,\frac{1-T}{1-r}u_0,\frac{T}{r}u_+\right).
\]
Their projective ratio is \(q'=q\,T(1-r)/[(1-T)r]\), proving the recurrence. The entropy-minimizing plan is reflection-symmetric: the reference and constraints are reflection-invariant, while KL is strictly convex. A symmetric feasible plan must have \(r=T\), so \(\pi_T\) is the unique KL minimizer. It is an interior positive plan because \(0<a<T<1\).

**3. Global convergence and sharp local rate.** Put \(z=\log q\). Taking logarithms in \(Q_a(r)\) gives
\[
\frac{dz}{dr}=\frac{r-a^2}{(r^2-a^2)(1-r)},\qquad
\frac{dr}{dz}=\frac{(r^2-a^2)(1-r)}{r-a^2}.
\]
The iteration is
\[
\Phi(z)=z+\log\frac{T(1-r(z))}{(1-T)r(z)}.
\]
By differentiation,
\[
\Phi'(z)=1-\frac{r(z)^2-a^2}{r(z)(r(z)-a^2)}
=\frac{a^2(1-r(z))}{r(z)(r(z)-a^2)},\qquad 0<\Phi'(z)<1.
\]
Also \(\Phi(z)>z\) exactly when \(r(z)<T\), and \(\Phi(z)<z\) exactly when \(r(z)>T\). The map is strictly increasing and has the unique fixed point \(z_*=\log Q_a(T)\). Therefore all iterates approach this fixed point monotonically without crossing it. At the fixed point the derivative equals \(\lambda(a,T)\) as stated. The mean-value theorem gives the asymptotic error ratio in \(z\); since \(r(z)\) is continuously differentiable with positive derivative at \(z_*\), it gives the same ratio for \(r_k-T\). For \(z_0\ne z_*\), strict monotonicity precludes reaching the fixed point in a finite number of steps. Finally, \(\Phi'(z)\to1\) as \(z\to-\infty\) (equivalently \(r\downarrow a\)), ruling out a global Lipschitz constant less than one.

**4. KL decay.** Symmetry reduces the plan divergence to one conditional row:
\[
D_{\mathrm{KL}}(\pi_r\Vert\pi_T)=
\frac{r-a}{2}\log\frac{r-a}{T-a}
+\frac{r+a}{2}\log\frac{r+a}{T+a}
+(1-r)\log\frac{1-r}{1-T}.
\]
This vanishes with its first derivative at \(r=T\), while the second derivative is
\[
I_{a,T}=\frac{T}{T^2-a^2}+\frac1{1-T}>0.
\]
Consequently, \(D_{\mathrm{KL}}(\pi_r\Vert\pi_T)=I_{a,T}(r-T)^2/2+O(|r-T|^3)\). Substitution of the sharp linear rate yields the squared KL ratio. These KL statements concern the martingale half-step sequence \(\pi_{r_k}\).

**5. Sharp convex-order boundary.** Exact algebra gives
\[
1-\lambda(a,T)=\frac{T^2-a^2}{T(T-a^2)}.
\]
Expanding at \(T=a\) yields \(2(T-a)/[a(1-a)]+O((T-a)^2)\). Because this is the derivative at the fixed point, the local factor and its first boundary coefficient are exact, not merely bounds. For \(a=1/2\) and \(T=3/4\), the factor is \(1/6\) and the entropy ratio is \(1/36\).

**6. Minimal support interpretation.** With one source atom, the martingale condition fixes its mean and a single terminal projection solves the compatible target. With at most two distinct terminal atoms, row mass plus row mean uniquely determine each conditional law, so an initially feasible martingale coupling cannot possess a nontrivial family of iterates. The present two-source, three-terminal grid is therefore the smallest source/target cardinality pair admitting the type of nontrivial asymptotic martingale-projection dynamics studied here. This claim concerns cardinality, not uniqueness of the feasible coupling.

## Verification

The accompanying standalone `VERIFY.py` independently performs the row KL projection through scalar root solving, then independently normalizes terminal columns, for arbitrary strictly positive triples of starting multipliers. It compares the resulting two rows, terminal marginals, full-cycle projective recurrence, monotone trapping, analytical derivative, and asymptotic KL ratios across randomized parameter instances. Run with `python VERIFY.py` from the extracted files. A deterministic seeded run passed 15,316 checks. Computation checks only finitely many instances and is not a substitute for the preceding analytical proof.

## Relationship to prior work

Kazeykina, Ren and Wang (2026, arXiv:2609.18850) establish exponential entropy convergence of martingale Sinkhorn under general compact-support hypotheses that include a **convex terminal support** assumption. This discrete three-atom target has nonconvex support, so their theorem cannot simply be invoked for the present model. The new statement is the exact finite-grid scalar dynamics and its sharp rate, rather than a new general existence theorem. Chen, Conforti, Ren and Wang (2024, arXiv:2407.14186) analyze martingale Sinkhorn rates and numerically discuss sensitivity to convex-order separation; the precise factor and boundary coefficient proved here were not identified in their examined arguments. Eckstein and Lakhal (2025, arXiv:2502.20264) provide abstract alternating information-projection linear rates, not an exact martingale grid constant. Tang and collaborators (2025, arXiv:2508.17641) study approximate-martingale projections and a different approximation regime. De March (2018, arXiv:1812.11104) studies entropy martingale transport algorithms in broad form. These comparisons do not prove that no unindexed equivalent finite-state calculation exists.

## Limitations

The calculation assumes exactly two symmetric source locations, three symmetric terminal locations, zero cost, strictly positive terminal multipliers, and **exact** cyclic martingale and terminal KL projections. It does not imply a sharp rate for nonsymmetric grids, costs, inexact projections, more than three terminal states, or computational runtime. The terminal marginal rescaled half-steps and the martingale half-steps are different laws; the KL ratio proved above refers to the latter. The boundary limit \(T\downarrow a\) must be taken with fixed \(0<a<1\); at equality the interior-positive optimal plan ceases to be interior. Independent scholarly assessment has not been performed.

## References

1. A. Kazeykina, Z. Ren, H. Wang, *Exponential convergence of Sinkhorn algorithm for entropy martingale optimal transport*, arXiv:2609.18850, first submitted 2026-09-16. https://arxiv.org/abs/2609.18850
2. F. Chen, G. Conforti, Z. Ren, X. Wang, *Convergence of Sinkhorn's Algorithm for Entropic Martingale Optimal Transport Problem*, arXiv:2407.14186, first submitted 2024-07-19. https://arxiv.org/abs/2407.14186
3. S. Eckstein, A. Lakhal, work on linear convergence of alternating information projections, arXiv:2502.20264, 2025. https://arxiv.org/abs/2502.20264
4. Work on approximate martingale Sinkhorn by Tang and collaborators, arXiv:2508.17641, 2025. https://arxiv.org/abs/2508.17641
5. H. De March, work on entropic martingale transport and computational algorithms, arXiv:1812.11104, 2018. https://arxiv.org/abs/1812.11104
