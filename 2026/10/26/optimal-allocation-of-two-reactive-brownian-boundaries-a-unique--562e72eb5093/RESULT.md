# Optimal allocation of two reactive Brownian boundaries: a unique interior split and sharp budget laws

## Finding

A diffusing particle in a finite one-dimensional interval meets two partially absorbing endpoints. When the **sum of their Robin reactivities is prescribed**, the expected absorption time from **every** fixed starting location has a unique global minimizer at a **strictly positive reactivity on both endpoints**. The optimal fraction obeys an exact algebraic characterization, is monotone with the available budget away from the midpoint, and crosses over between two distinct universal allocation laws.

For \(S>0\), \(y\in[0,1]\), and \(t\in[0,S]\), define
\[
 F_y(S,t)=-\frac{y^2}{2}+\frac{(1+(S-t)/2)(1+ty)}{S+t(S-t)}.
\]
The **unique** minimizing \(t_*(S,y)\in(0,S)\) is the root of
\[
 (y-\tfrac12)t^2+[S(1-y)+2]t+
 \tfrac S2[(S+2)y-(S+3)]=0.
\]
Writing \(p_*=t_*/S\), the full crossover is
\[
 \lim_{S\downarrow0}p_*(S,y)=\frac34-\frac y2,\qquad
 \lim_{S\to\infty}p_*(S,y)=
 \frac{\sqrt{1-y}}{\sqrt{1-y}+\sqrt y}.
\]
The second expression uses its continuous endpoint values \(1\) at \(y=0\) and \(0\) at \(y=1\). For \(y<1/2\) the fraction strictly **increases** with \(S\), for \(y>1/2\) it strictly **decreases**, and at the midpoint it equals \(1/2\) for all budgets. There is no finite-budget corner optimum, even for a particle initially at a reactive endpoint.

The strong-budget optimized mean has the sharp asymptotic expansion
\[
 \min_{0<t<S}F_y(S,t)=\frac{y(1-y)}2+
 \frac{(\sqrt{1-y}+\sqrt y)^2}{2S}+o(S^{-1})
 \quad(S\to\infty).
\]
At \(y=0\), the remote endpoint receives \(S-t_*=\sqrt{S+4}-2\sim\sqrt S\), and the optimized dimensionless mean is asymptotically \(1/(2S)\) rather than the one-reactive-endpoint value \(1/S\).

## Assumptions and scope

Let \(L,D,\kappa>0\). A one-dimensional diffusion \(X\) with generator \(D\partial_{xx}\) lives on \([0,L]\), with partial absorption at the endpoints in the standard radiation-boundary convention. Assign Robin reactivities \(\kappa_0,\kappa_L\ge0\) subject to \(\kappa_0+\kappa_L=\kappa\). Their interior positive choices correspond to the physical setting of two active reaction channels; boundary choices are admitted only as comparison allocations. The start \(x\in[0,L]\) is deterministic. Boundary partial killing is through boundary local time, not immediate killing at initial contact.

The unique solution \(m(x)=\mathbb E_x[T]\) of the backward mean-first-passage boundary-value problem satisfies
\[
 -D m''(x)=1,\quad Dm'(0)=\kappa_0m(0),\quad
 Dm'(L)=-\kappa_Lm(L).
\]
Put \(y=x/L\), \(S=\kappa L/D\), \(t=\kappa_0 L/D\). Then \(F_y(S,t)=D m(x)/L^2\). The source date is the first public appearance of the foundational reaction–diffusion radiation-boundary reference; it is **not** asserted as a publication date for the theorem proved here.

## Proof

**Exact mean.** The rescaled boundary-value problem is \(-F''=1\), \(F'(0)=tF(0)\), \(F'(1)=-(S-t)F(1)\). Write \(F(y)=-y^2/2+Ay+B\). At the left endpoint \(A=tB\). The right condition yields
\[
 B=\frac{1+(S-t)/2}{S+t(S-t)},\qquad A=tB,
\]
which gives the displayed exact formula. The denominator is strictly positive on the entire closed allocation interval because \(S>0\).

**Strict global optimality.** Direct differentiation yields
\[
 \frac{\partial F_y}{\partial t}=
 \frac{g_{S,y}(t)}{[S+t(S-t)]^2},
\]
where
\[
 g_{S,y}(t)=(y-\tfrac12)t^2+[S(1-y)+2]t+
 \frac S2[(S+2)y-(S+3)].
\]
For \(0\le y\le1\),
\[
 g_{S,y}(0)=\frac S2[S(y-1)+2y-3]<0,
 \quad g_{S,y}(S)=\frac S2[Sy+2y+1]>0.
\]
Furthermore \(g'_{S,y}(t)=2(y-\tfrac12)t+S(1-y)+2\) is affine in \(t\), with positive values \(S(1-y)+2\) at \(0\) and \(Sy+2\) at \(S\). Hence it is positive throughout. There is exactly one zero, and the derivative of \(F\) switches from negative to positive there, proving the global and strict minimum. A numerically stable expression is obtained by setting
\[
 a=y-\tfrac12,\quad b=S(1-y)+2,\quad
 c=\tfrac S2[(S+2)y-(S+3)],\quad
 t_*=-\frac{2c}{b+\sqrt{b^2-4ac}}.
\]
This formula remains valid at \(a=0\) by continuity and the linear limit.

**Crossovers and strict budget monotonicity.** Put \(p=t/S\) and set
\[
 H_y(p)=(y-\tfrac12)p^2+(1-y)p+\frac{y-1}{2},
 \qquad K_y(p)=2p+y-\frac32.
\]
The unique optimizer obeys \(S H_y(p_*)+K_y(p_*)=0\). As \(S\downarrow0\), \(K_y(p_*)\to0\), so \(p_*\to p_0=3/4-y/2\). As \(S\to\infty\), \(H_y(p_*)\to0\). On \([0,1]\), \(H_y\) increases (its derivative is nonnegative and not identically zero) with \(H_y(0)\le0\), \(H_y(1)\ge0\) (strict inequalities for \(0<y<1\)). Its unique root solves \((1-y)(1-p)^2=yp^2\), giving the strong-budget fraction. The endpoint cases follow with the same continuous root.

For every finite \(S>0\), implicit differentiation gives
\[
 \frac{\partial p_*}{\partial S}=
 \frac{2(p_*-p_0)}{S[S H_y'(p_*)+2]}.
\]
Because the defining left side is strictly increasing in \(p\) and \(H_y(p_0)=(2y-1)^3/32\), the optimum satisfies \(p_*>p_0\) for \(y<1/2\), \(p_*<p_0\) for \(y>1/2\), and equality for \(y=1/2\). The displayed derivative establishes strict monotonicity in exactly these cases.

**Sharp strong-budget mean and endpoint behavior.** For fixed \(0<p<1\), expansion of the exact expression gives
\[
 F_y(S,pS)=\frac{y(1-y)}{2}+
 \frac1{2S}\left(\frac{1-y}{p}+\frac{y}{1-p}\right)+O(S^{-2}).
\]
The coefficient has its unique minimizer \(p=\sqrt{1-y}/(\sqrt{1-y}+\sqrt y)\) for interior \(y\), giving the expansion. At \(y=0\), the quadratic optimality equation instead solves exactly to \(t_*=S+2-\sqrt{S+4}\), so \(S-t_*=\sqrt{S+4}-2\), and substitution in the exact mean gives the same sharp leading coefficient, \(1/2\). By endpoint symmetry the conclusion holds at \(y=1\). At \(y=1/2\), symmetry gives \(t_*=S/2\). Thus the expansion holds pointwise for every fixed \(y\in[0,1]\); uniformity as \(y\) varies with \(S\) is not claimed.

## Verification

A standalone, standard-library Python checker (`checker.py`) independently solves the Robin second-order boundary-value problem with a tridiagonal finite-difference/ghost-point discretization, compares the exact mean at 50 seeded parameters, performs 50 independent function-only golden-section optimizations, and evaluates weak/strong limits and monotonicity at seven initial locations. Its completed run reported 50/50 boundary-value comparisons, 50/50 optimizations and 7/7 asymptotic/monotonicity cases passing; maximum absolute boundary-value difference was approximately \(6.1\times10^{-11}\). The global theorem is proved analytically above; finite testing does not certify a quantified continuum statement.

## Relationship to prior work

Erban and Chapman (2006 preprint; 2007 journal) establish the physical and mathematical use of reactive Robin boundaries for stochastic reaction–diffusion models. Whitehouse, Evans and Majumdar (2013) study first-passage statistics with partial absorption and stochastic resetting, optimizing/resetting a different mechanism. Nicolaou and Mulder (2023) optimize spatial reactivity for steady-state flux to a partially absorbing body in an exterior diffusion problem, not the point-source mean capture time in a bounded interval. With a bounded two-endpoint diffusion and at least one active endpoint, eventual absorption has probability one, so maximizing total capture probability/steady flux does not imply the present allocation result. These sources motivate the model and do not supply the present global unique mean-time optimum, both crossovers, or the distant-endpoint square-root law in the inspected material. Potential equivalent formulations in specialized optimization literature remain a priority risk.

## Limitations

The theorem is for one-dimensional constant-diffusivity Brownian motion, a known starting point, memoryless Robin boundary killing, and a fixed *sum of dimensioned Robin reactivities*; it is not a fixed total number of reactive molecules or a geometry-dependent surface-cost constraint. It does not treat spatially varying diffusion, switching reactivities, resetting, higher-dimensional targets, general initial distributions, or noisy observations. The two asymptotic regimes are at fixed initial position and have no claimed uniform remainder near the endpoints. Scientific priority requires independent literature verification; the present mathematical review is not an independent audit.

## References

1. R. Erban and S. J. Chapman, *Realistic boundary conditions for stochastic simulations of reaction-diffusion processes*, arXiv:physics/0611251 (first posted 2006-11-27); journal version *Reactive boundary conditions for stochastic simulations of reaction-diffusion processes*, Physical Biology 4 (2007) 16–28, DOI 10.1088/1478-3975/4/1/003.
2. J. Whitehouse, M. R. Evans and S. N. Majumdar, *Effect of Partial Absorption on Diffusion with Resetting*, arXiv:1301.2489 (2013); Physical Review E 87, 022118.
3. K. Nicolaou and B. M. Mulder, *A probabilistic algorithm for optimising the steady-state diffusional flux into a partially absorbing body*, Scientific Reports 13 (2023), DOI 10.1038/s41598-023-49566-4.
