# A sharp horizon bifurcation for pinned damped-Jordan observation timing

## Finding

Let a two-state stable Jordan system have known damping \(a>0\) and a scalar output
\[
\dot x=\begin{pmatrix}-a&1\\0&-a\end{pmatrix}x,
\qquad y(t)=x_1(t)+\eta_t.
\]
Here the unknown initial state is \((A,B)\in\mathbb R^2\), and observation errors at distinct *measurement events* are independent, centered, Gaussian with known common variance \(\sigma^2>0\). Measurements at the same time are independent replicates. Thus the mean signal is \(e^{-at}(A+Bt)\).

Fix the two compulsory observation times \(0\) and \(T>0\), and choose one more time \(t\in[0,T]\), allowing an endpoint replicate. Write \(b=aT\) and \(u=at\). The exact determinant of the Fisher information matrix is
\[
\det G(t)=\frac{1}{\sigma^4a^2}\Phi_b(u),\qquad
\Phi_b(u)=u^2e^{-2u}+b^2e^{-2b}+(b-u)^2e^{-2(b+u)}.
\]
The complete optimal-time classification is:

1. If \(0<b\leq1\), the **only** maximizers are \(u=0\) and \(u=b\), attaining \(\Phi_b=2b^2e^{-2b}\). Thus repeating either compulsory endpoint is optimal.
2. If \(b>1\), there is a **unique** maximizer \(u_b\in(0,1)\), namely the larger of the two roots in \((0,1)\) of
\[
u(1-u)=e^{-2b}(b-u)(1+b-u).
\]
It strictly outperforms both endpoint repeats.

The transition is quantitatively sharp. With \(b=1+\varepsilon\) and \(\varepsilon\downarrow0\),
\[
b-u_b=\frac{\varepsilon}{1-e^{-2}}+O(\varepsilon^2),\qquad
\Phi_b(u_b)-2b^2e^{-2b}=\frac{e^{-2}}{1-e^{-2}}\varepsilon^2+O(\varepsilon^3).
\]
As \(b\to\infty\),
\[
u_b=1-b(b-1)e^{-2b}+O(b^4e^{-4b}),\qquad
\frac{\Phi_b(u_b)}{2b^2e^{-2b}}\sim\frac{e^{2b-2}}{2b^2}.
\]
Consequently, the best free measurement approaches one damping time \(a^{-1}\) even while the required terminal measurement recedes, and its information advantage over simply repeating an endpoint grows exponentially.

The same optimal \(t\) remains optimal for every positive integer \(m\) if \(m\) independent observations are compulsory at each endpoint and **exactly one** additional observation time remains free: the determinant is
\[
\frac{1}{\sigma^4a^2}\bigl[m^2b^2e^{-2b}+m(\Phi_b(u)-b^2e^{-2b})\bigr].
\]

## Assumptions and scope

All parameters \(a,T,\sigma\) are positive and known. The initial two state coordinates are unknown deterministic parameters, observed through the first coordinate only. The state matrix has one genuine size-two Jordan block. Exactly three independent Gaussian measurements, including the compulsory initial and terminal events, are considered in the main result. The extra measurement may coincide with either event as an independent replicate. The objective is determinant maximization of the two-by-two information matrix, not worst-direction eigenvalue or trace minimization. The equal-endpoint-replication extension fixes \(m\) at each endpoint.

## Proof

**Information formula.** The observation row for time \(s\) is \(v(s)=e^{-as}(1,s)\). Since each noise variance is \(\sigma^2\), \(G=\sigma^{-2}\sum v(s)^\mathsf Tv(s)\). The two-column Cauchy--Binet identity gives
\[
\det G=\sigma^{-4}\sum_{i<j}e^{-2a(s_i+s_j)}(s_j-s_i)^2,
\]
with the pair sum taken over *measurement events*, including independent replicates. For \((s_1,s_2,s_3)=(0,t,T)\), scaling by \(a\) gives the stated \(\Phi_b\). With \(m\) observations at both compulsory endpoints, there are \(m^2\) cross-endpoint pairs and \(m\) pairs joining the free event to each endpoint, giving the replication formula.

**Derivative signs and complete maximizers.** Direct differentiation yields
\[
\frac12e^{2u}\Phi_b'(u)=u(1-u)-e^{-2b}(b-u)(1+b-u).
\]
For \(0<u<\min\{b,1\}\), define
\[
H_b(u)=\frac{u(1-u)}{(b-u)(1+b-u)}.
\]
Its derivative has the sign of
\[
2u^2-2(b+1)u+(b+1).
\]
For \(0<b<1\), the discriminant of this quadratic is \(4(b^2-1)<0\); for \(b=1\), it is a nonnegative square, vanishing only at the excluded upper endpoint. Thus \(H_b\) is strictly increasing from zero toward a value greater than \(e^{-2b}\) as \(u\) reaches its upper endpoint (infinite when \(b<1\), and one when \(b=1\)). Therefore \(\Phi_b'\) changes once from negative to positive. Its unique interior stationary point is a minimum. The endpoints have equal determinant \(\Phi_b(0)=\Phi_b(b)=2b^2e^{-2b}\), proving the first classification.

For \(b>1\), on \((0,1)\) the derivative of \(H_b\) has exactly one zero,
\[
c_b=\frac{b+1-\sqrt{b^2-1}}2\in(0,1),
\]
and \(H_b\) increases and then decreases, with zero values at both ends. Moreover
\[
H_b(1/2)=\frac1{4b^2-1}>e^{-2b},
\]
since \(e^b>2b\) for all \(b>0\). Hence the horizontal line \(e^{-2b}\) cuts \(H_b\) in exactly two points \(u_-<u_b\) in \((0,1)\). The derivative signs of \(\Phi_b\) are negative, positive and negative across these intervals. For \(1\le u\le b\), the derivative is strictly negative. Thus \(u_-\) is a strict local minimum and \(u_b\) the sole interior local maximum. Because \(\Phi_b\) strictly decreases from \(u_b\) to \(b\), and the two endpoint values are equal, \(u_b\) is the unique global maximizer.

**Sharp transitions.** Let \(F(b,u)=u(1-u)-e^{-2b}(b-u)(1+b-u)\). At \((b,u)=(1,1)\), \(F=0\) and \(\partial_uF=-1+e^{-2}\ne0\). The implicit-function theorem therefore gives the displayed first-order expansion of \(b-u_b\). A second-order Taylor expansion of \(\Phi_b\) about \(u=b\) gives the positive quadratic improvement. At large \(b\), write \(u_b=1-\delta_b\) in \(F=0\). The resulting identity
\[
(1-\delta_b)\delta_b=e^{-2b}(b-1+\delta_b)(b+\delta_b)
\]
and \(\delta_b\to0\) yield \(\delta_b=b(b-1)e^{-2b}+O(b^4e^{-4b})\). Inserting this into \(\Phi_b\) gives \(\Phi_b(u_b)=e^{-2}+O(b^2e^{-2b})\); dividing by the exact endpoint value proves the ratio asymptotic. This completes the proof.

## Verification

Run the bundled pure-Python checker with `python3 verify.py`. It tests the two-column Cauchy--Binet identity in exact rational arithmetic for 1,404 weighted three-row cases, checks the stationary-point patterns and endpoint inequalities across a range of dimensionless horizons, tests the two asymptotic expansions, and verifies invariance of the maximizer under balanced replication. The checker reports 20,714 assertions. These finite calculations are diagnostics; the derivative and implicit-function arguments above prove the results for the full continuum of parameters.

For example, at \(b=2\), the unique optimal dimensionless free time is \(u_b=0.9594688298\ldots\); the optimized information determinant is approximately \(1.4419363\) times the endpoint-repeat value.

## Relationship to prior work

Krauss, Lopez and Müller (2022) develop sampling conditions ensuring observability of discrete-time linear systems, including Jordan-form models and irregular sampling. Their rank-guarantee problem does not optimize a noisy information determinant under compulsory continuous-time endpoints. Gündüz and Torsney (2023) analyze approximate D-optimal design support for weighted linear regression, including exponential weights. Their two-support-point results allow unrestricted support and design weights and do not give the exact fixed-three-event pinned-endpoint optimization or its horizon-one transition. Dette and Neugebauer (1997) study Bayesian D-optimal design for nonlinear exponential regression; their model and optimization objective differ. The Cauchy--Binet identity and local derivative calculation are standard ingredients, not independent novelty claims. The claimed contribution is the complete pinned-observation phase diagram, its sharp transition and replication invariant.

## Limitations

This is a conditional exact-design theorem under known damping, independent homoscedastic noise, fixed mandatory endpoints, a size-two Jordan mode and a determinant criterion. The result does not optimize arbitrary numbers of freely timed measurements, colored noise, unknown damping, conditioning, or worst-direction variance. Prior general weighted-regression design theory may provide a different derivation; full historical priority across exact-design literature has not been independently established. All asymptotic statements concern the indicated limits only.

## References

- I. Krauss, V. G. Lopez and M. A. Müller, *Sample-based observability of linear discrete-time systems*, arXiv:2204.06451 (first public April 13, 2022), https://arxiv.org/abs/2204.06451.
- N. Gündüz and B. Torsney, *D-Optimal Designs for Binary and Weighted Linear Regression Models: One Design Variable*, Mathematics **11** (2023), 2075, https://doi.org/10.3390/math11092075.
- H. Dette and H.-J. Neugebauer, *Bayesian D-optimal designs for exponential regression models*, Journal of Statistical Planning and Inference **60** (1997), 331–349, https://doi.org/10.1016/S0378-3758(96)00131-0.
