# Stage-resampled second-order Runge–Kutta descent uniquely selects Heun

## Finding

Let \(H\in\mathbb R^{d\times d}\) be symmetric positive definite, \(d\ge1\), and let \(F(x)=\tfrac12 x^{\mathsf T}Hx\). Suppose each stochastic gradient evaluation returns \(YHx\), where \(Y\ge0\), \(\mathbb EY=1\) and \(\mathbb EY^2=a<\infty\). Use independent, identically distributed draws at both stages and across iterations. For \(h>0\) and \(b\in\mathbb R\setminus\{0\}\), consider the two-stage explicit Runge–Kutta tableau of deterministic order two:
\[
k_1=Y_1Hx,\qquad k_2=Y_2H\left(x-\frac{h}{2b}k_1\right),\qquad
x^+=x-h[(1-b)k_1+bk_2].
\]
Define
\[
C_{a,b}=1+a-2(a-1)b(1-b),\qquad Q_b(a,z)=1-2z+C_{a,b}z^2-az^3+\frac{a^2z^4}{4}.
\]
In an **orthonormal** eigenbasis \(Hu_j=\lambda_j u_j\), write a deterministic \(x_0=\sum_j c_ju_j\). Then for every \(n\ge0\),
\[
\mathbb E\|x_n\|^2=\sum_j c_j^2 Q_b(a,h\lambda_j)^n.
\]
If instead the \(u_j\) are orthogonal but not normalized, each summand is multiplied by \(\|u_j\|^2\). For every deterministic \(x\),
\[
\mathbb E\|x^+_b\|^2-\mathbb E\|x^+_{1/2}\|^2
=2(a-1)(b-\tfrac12)^2 h^2\|Hx\|^2.
\]
Consequently, if \(a>1\) Heun (\(b=1/2\)) uniquely minimizes the expected squared error for every nonzero deterministic initial state, positive step size and positive integer horizon. For \(a=1\), all the tableaux have the same deterministic amplification.

Let \(z_b(a)\) be the unique positive root of \(a^2z^3-4az^2+4C_{a,b}z-8=0\). Mean-square convergence is exponential for all initial states if and only if \(0<h<z_b(a)/\lambda_{\max}(H)\). At equality the expected squared norm is constant for any initial state in the top eigenspace; above equality it diverges exponentially for any nonzero such state. The midpoint method (\(b=1\)) has \(z_1(a)=2/a\), the threshold for one-gradient stochastic Euler. Heun's root \(z_*(a)\) solves
\[
a^2z^3-4az^2+(2a+6)z-8=0.
\]
It satisfies \(2/a<z_*(a)<4/a\) for \(a>1\); the relative threshold \(a z_*(a)/2\) strictly increases from \(1\) to the limit \(2\) as \(a\) increases from \(1\) to infinity. In fact \(z_*(a)=4/a-12/a^2+O(a^{-3})\).

Reusing the same multiplier gives every tableau the scalar amplification \(1-zY+z^2Y^2/2\), which for any \(z>0\) has finite second moment if and only if \(\mathbb EY^4<\infty\). Independent-stage sampling needs only \(\mathbb EY^2<\infty\). In particular, for \(Y=2V/3\) with \(\Pr(V>t)=t^{-3}\) for \(t\ge1\), \(H=1\) and \(h=1/4\), independently sampled Heun contracts the expected squared norm by \(355/576\) per step, while a reused multiplier gives infinite expected squared norm in one step from any nonzero initial state.

## Assumptions and scope

The deterministic order conditions are \(b_1+b_2=1\) and \(b_2a_{21}=1/2\). Thus the stated family exhausts the standard explicit two-stage order-two tableaux and allows negative coefficients. Within each stage, one scalar multiplies all coordinates. The result does not cover matrix-valued, additive or state-dependent noise or nonquadratic objectives. It concerns deterministic tableau order and mean-square stability, not stochastic order, almost-sure rates or efficiency at a fixed number of gradient evaluations.

## Proof

For an eigenvalue \(\lambda\), let \(z=h\lambda\). The scalar update factor is \(R_b=1-z[(1-b)Y_1+bY_2]+z^2Y_1Y_2/2\). Put \(\eta_i=Y_i-1\); the terms \(1,\eta_1,\eta_2,\eta_1\eta_2\) are mutually orthogonal in \(L^2\) by independence. Their coefficients in the expansion of \(R_b\) are \(1-z+z^2/2\), \(z^2/2-z(1-b)\), \(z^2/2-zb\), \(z^2/2\). Their squared norms are \(1,a-1,a-1,(a-1)^2\). Squaring and summing gives \(Q_b\) above; the only weight-dependent increment over Heun is \(2(a-1)z^2(b-1/2)^2\). Each iteration acts diagonally in the eigenbasis and iteration draws are independent, so squared coefficients have expectations \(c_j^2Q_b(a,h\lambda_j)^n\). Parseval's identity in the orthonormal basis proves the norm formula; for an unnormalized orthogonal basis one uses the squared basis lengths. Summing the one-step gaps gives the stated identity. The strict order of nonnegative \(Q_b\) persists under positive integer powers and at least one coefficient is nonzero when \(x_0\ne0\). At \(a=1\) the multiplier equals one almost surely.

For \(z>0\), \(Q_b-1\) has the sign of \(H_{a,b}(z)=a^2z^3-4az^2+4C_{a,b}z-8\), since \(Q_b-1=zH_{a,b}/4\). We have \(C_{a,b}\ge(a+3)/2\ge2\). The derivative of \(H_{a,b}\) is bounded below by \(4C_{a,b}-16/3>0\) on the real line. The cubic starts at \(-8\) and grows to infinity, so the stable interval is exactly \(0<z<z_b(a)\). The top eigenspace gives necessity and the boundary and divergence statements. The midpoint cubic factors as \((az-2)(az^2-2z+4)\), with positive quadratic factor; Euler's moment factor is \(1-2z+az^2\).

For Heun the cubic has values \(-4+4/a\) and \(24/a\) at \(2/a\) and \(4/a\). Equivalently \(r=a z_*(a)\) solves \(2r-8+f(r)/a=0\), where \(f(r)=r(r^2-4r+6)\). Both \(f(r)\) and \(f'(r)\) are positive for \(r>0\), so implicit differentiation shows \(r'(a)>0\). Here \(r(1)=2\) and \(r\to4\) by boundedness and the equation. The same equation gives \(r-4=O(a^{-1})\); inserting this estimate into \(f(r)\) yields \(r=4-12/a+O(a^{-2})\).

With reuse, the square of \(1-zY+z^2Y^2/2\) is asymptotic to \(z^4Y^4/4\) for large \(Y\), proving the moment criterion. The Pareto example has \(\mathbb EV=3/2\), \(\mathbb EV^2=3\) and infinite fourth moment. Substitution of \(a=4/3\) and \(z=1/4\) gives \(355/576\) for Heun.

## Verification

The accompanying `verify_rk2.py` is unchanged. Its standard-library checks compare direct enumeration with the moment law for finite rational examples and test selected numerical stability frontiers. The proofs above, not the finite checks, establish the general law, boundary and heavy-tail claims.

## Relationship to prior work

Classical Runge–Kutta order conditions are not new. Stillfjord–Williamson analyze a stabilized Runge–Kutta descent method reusing the same batch across stages; Mulayoff–Michaeli analyze exact mean-square stability for ordinary minibatch SGD. Bochacik et al. give a mean-square stability calculation for a two-stage method with random stage times, not independent stochastic-gradient multipliers. Saito analyzes Heun for a Stratonovich stochastic differential equation. The distinct claims here concern the exact mean-square law, optimization over the tableau weight under independent scalar gradient multipliers, its stability frontier, and the contrast with stage reuse. These comparisons do not establish historical priority. The stability gain is per step; Euler uses one gradient evaluation and Heun uses two.

## References

1. T. Stillfjord and M. Williamson, *SRKCD: A stabilized Runge–Kutta method for stochastic optimization*, [arXiv:2201.12782](https://arxiv.org/abs/2201.12782).
2. R. Mulayoff and T. Michaeli, *Exact Mean Square Linear Stability Analysis for SGD*, [arXiv:2306.07850](https://arxiv.org/abs/2306.07850).
3. T. Bochacik et al., *Randomized Runge–Kutta method—stability and convergence under inexact information*, [arXiv:2006.12131](https://arxiv.org/abs/2006.12131).
4. Y. Saito, *Mean-square and Asymptotic Stability of the Stochastic Heun Method*, [DOI:10.11540/jsiamt.21.1_125](https://doi.org/10.11540/jsiamt.21.1_125).
