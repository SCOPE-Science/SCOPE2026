# An absorbing interval and fourth-order accuracy floor for fixed-radius CARS

## Finding

Consider the published Curvature-Aware Random Search (CARS) method, with one-dimensional independent Rademacher search directions and a **fixed positive sampling radius**. Even on globally strongly convex smooth objectives, the curvature-aware proposal and all three safeguarding choices can fail to move from a *whole interval of nonoptimal points*. The failure is structural when the third derivative at the minimizer does not vanish. The interval width is of order \(r^2\), and its maximal objective gap is of order \(r^4\), with exact leading coefficients.

**General assertion.** Let \(f:\mathbb R\to\mathbb R\) be three times continuously differentiable and globally \(\mu\)-strongly convex for some \(\mu>0\). Write \(x_*\) for its unique minimizer and assume \(f'''(x_*)\ne0\). For every sufficiently small fixed \(r>0\), define the unique zero \(z_r\) of the centered-difference derivative
\[
 d_r(x)=\frac{f(x+r)-f(x-r)}{2r}.
\]
Then every point in the nondegenerate closed interval with endpoints \(x_*\) and \(z_r\) is fixed, iteration after iteration, by the exact safeguarded CARS update using radius \(r\), any positive relative-smoothness parameter \(\widehat L\), and directions independently sampled from \(\{-1,+1\}\). Its nonoptimal endpoint has asymptotics
\[
 z_r-x_*=-\frac{f'''(x_*)}{6f''(x_*)}r^2+o(r^2),
 \qquad
 f(z_r)-f(x_*)=\frac{f'''(x_*)^2}{72f''(x_*)}r^4+o(r^4).
\]
Thus the order-four objective floor is attained by an actual absorbing initialization. This is a lower-bound illustration for *fixed-radius* accuracy claims; it is not a contradiction of the target-accuracy-dependent radius prescribed by the source's convergence theorem.

**Global explicit witness.** Set
\[
 f(x)=\frac{x^2}{2}+\frac{\sin x-x}{2},
 \qquad 0<r\le1.
\]
For this analytic function the preceding conclusion holds for the **entire** stated range of radii, with \(x_*=0\). Its absorbing interval is \([0,z_r]\), where \(z_r>0\) is the unique solution
\[
 z_r=\frac12\left(1-\frac{\sin r}{r}\cos z_r\right),
 \qquad 0<z_r\le\frac{r^2}{6}.
\]
Moreover,
\[
 z_r=\frac{r^2}{12}-\frac{7r^4}{2880}+O(r^6),
 \qquad
 \max_{x\in[0,z_r]}\{f(x)-f(0)\}
 =\frac{r^4}{288}-\frac{13r^6}{51840}+O(r^8).
\]
The radius exponent \(r=O(\varepsilon^{1/4})\), sufficient in the cited CARS analysis under a Lipschitz Hessian, therefore cannot be uniformly weakened in order for all starting points in this family to be within objective accuracy \(\varepsilon\) at termination. The example establishes the **exponent**, not minimax optimality of the source's multiplicative radius constants.

## Assumptions and scope

CARS means Algorithm 1 of Kim–Cai–McKenzie–Yin, as specified in its open arXiv manuscript: for a direction \(u\in\{-1,+1\}\) at \(x\), with radius \(r>0\), compute
\[
 d_r(x;u)=\frac{f(x+ru)-f(x-ru)}{2r},\quad
 h_r(x;u)=\frac{f(x+ru)-2f(x)+f(x-ru)}{r^2},
\]
form \(y=x-[d_r(x;u)/(\widehat Lh_r(x;u))]u\), and select a point attaining the smallest objective among \(y,x,x-ru,x+ru\). The radius satisfies the algorithm's input restriction \(r\le C\) whenever a radius cap \(C\) is supplied. Set \(r_k=r\) at every iteration. Strong convexity ensures \(h_r\ge\mu>0\), so no denominator is zero. The assertion is independent of the realized sign sequence and of \(\widehat L>0\); for the explicit witness \(\widehat L=3\) is a valid global relative-smoothness constant because \(1/2\le f''\le3/2\).

The generic assertion requires \(f\in C^3(\mathbb R)\), global strong convexity, and \(f'''(x_*)\ne0\). The fixed-radius assumption is essential; neither a decreasing-radius schedule nor the target-dependent convergence guarantee from the original paper is ruled out. The general statement is asymptotic as \(r\downarrow0\); the explicit trigonometric witness is valid for every \(0<r\le1\), subject to the algorithm's radius cap if imposed.

## Proof

**1. A centered-difference root.** By the fundamental theorem of calculus and strong convexity,
\[
 d_r'(x)=\frac{f'(x+r)-f'(x-r)}{2r}\ge\mu.
\]
Consequently \(d_r\) is strictly increasing, tends to opposite infinities at opposite ends of the real line, and has a unique zero \(z_r\). At the true minimizer, Taylor expansion with \(f'(x_*)=0\) gives
\[
 d_r(x_*)=\frac{f'''(x_*)}{6}r^2+o(r^2).
\]
By the mean value theorem, \(z_r-x_*=-d_r(x_*)/d_r'(\xi_r)\) for some \(\xi_r\) between \(x_*\) and \(z_r\). Strong monotonicity gives \(|z_r-x_*|=O(r^2)\), while continuity yields \(d_r'(\xi_r)\to f''(x_*)\), proving the first displayed asymptotic. Taylor expansion of the objective about its minimizer proves the second, including the exact coefficient \(f'''(x_*)^2/(72f''(x_*))>0\).

**2. A trapping interval for the entire four-choice update.** For sufficiently small \(r\), the point \(z_r\) lies strictly on the side of \(x_*\) opposite the sign of \(f'''(x_*)\). On the closed interval between them, \(f'(x)\) and \(d_r(x)\) have opposite signs whenever both are nonzero. For either Rademacher sign \(u\), one has \(d_r(x;u)=u\,d_r(x)\) and \(h_r(x;u)=h_r(x;1)>0\), so the CARS candidate is the sign-independent point
\[
 y=x-\frac{d_r(x)}{\widehat Lh_r(x;1)}.
\]
In the interval interior, \(y-x\) points away from \(x_*\); strict convexity therefore implies \(f(y)>f(x)\). At \(x=x_*\), \(y\ne x_*\) and hence \(f(y)>f(x_*)\); at \(x=z_r\), \(y=z_r\).

Uniformly for \(x\) in this interval, \(|x-x_*|=O(r^2)\). Taylor's formula at \(x_*\) gives
\[
 f(x\pm r)-f(x)=\frac12 f''(x_*)r^2+o(r^2)>0.
\]
Thus neither safeguarding probe improves the incumbent. All candidates are worse or identical, so the current point is selected at every iteration. Every nonoptimal point in the interval is a permanent fixed point, for *any* sequence of sign directions and *any* \(\widehat L>0\).

**3. Fully explicit global analytic case.** For the displayed trigonometric function,
\[
 f'(x)=x+\frac{\cos x-1}{2},\quad
 f''(x)=1-\frac{\sin x}{2}\in[1/2,3/2],\quad
 f'''(0)=-1/2,
\]
and direct cancellation gives
\[
 d_r(x)=x-\frac12+\frac{\sin r}{2r}\cos x,\quad
 h_r(x)=1+\frac{\cos r-1}{r^2}\sin x\ge1/2.
\]
For \(0<r\le1\), \(d_r(0)=(\sin r/r-1)/2<0\), while \(d_r'(x)=1-(\sin r/(2r))\sin x\ge1/2\). Its unique zero obeys
\[
 0<z_r\le1-\frac{\sin r}{r}\le\frac{r^2}{6}\le\frac r6.
\]
For \(0<x\le z_r\), \(d_r(x)\le0\), so the CARS candidate does not move left and hence cannot improve the strictly increasing positive-side objective. Also, strong convexity and smoothness imply \(y^2/4\le f(y)\le3y^2/4\) for all real \(y\) (the minimum is at zero). For each \(x\in[0,z_r]\), \(|x\pm r|\ge5r/6\), whence
\[
 f(x\pm r)\ge\frac{25r^2}{144}
 >\frac{r^2}{48}\ge f(x).
\]
Therefore the entire \([0,z_r]\) is absorbing without any small-\(r\) asymptotic qualification. Substituting a power series into \(d_r(z_r)=0\) gives \(z_r=r^2/12-7r^4/2880+O(r^6)\); then substituting into \(f(z_r)\) yields the displayed fourth- and sixth-order objective coefficients. Strict increase for \(x>0\) shows \(f(z_r)\) is the attained maximum objective gap over the interval.

## Verification

The proof uses analytic inequalities valid for all admissible radii, not finite enumeration. The included self-contained \(\texttt{verify.py}\) independently reproduces the defining finite differences and guarded selection in standard double precision for multiple radii, start points and both direction signs; it is a supplementary finite-sample check, **not** a proof of the universal quantifiers. The exact series coefficients can be regenerated by Taylor expansion of \(\sin r/r\), \(\cos z_r\), and the objective; the coefficient calculation is displayed in the proof. Source Algorithm 1, its finite-difference equations, and its radius condition were checked against the publicly accessible full manuscript.

## Relationship to prior work

Kim, Cai, McKenzie and Yin introduced CARS and proved target-accuracy convergence with an upper bound on the sampling radius depending on \(\varepsilon\); with Lipschitz Hessian the paper explicitly specifies order \(\varepsilon^{1/4}\). That is a **sufficient** radius condition. The present finding supplies a structural nonoptimal absorbing set and an attained order-\(r^4\) accuracy lower bound for fixed radius. Neither one follows merely by rewriting the cited sufficient inequality. The underlying safeguard is the Stochastic Three Points (STP) method of Bergou, Gorbunov and Richtárik, which does not contain the extra finite-difference Newton candidate. STP fixed-stepsize convergence-to-tolerance results do not imply the claimed sign-reversal absorption for the full four-point CARS update.

The classical centered-difference bias \(O(r^2)\) is an ingredient, not the entire assertion: the proof verifies that **every** selectable point, including the additional curvature-aware candidate, fails on the same nonoptimal continuum, and quantifies its attained objective floor. No claim of global priority or an independent external audit is made.

## Limitations

This is a scalar, fixed-radius, deterministic-function obstruction. It does not imply failure for a radius sent to zero, the paper's target-dependent choice of \(C\), a different derivative estimator, high-dimensional direction distributions, stochastic function noise, or the CARS-CR variant. The \(r^4\) coefficient depends on the objective's local third derivative and curvature; it is not a universal minimax constant. A possibly relevant 2023 doctoral thesis on CARS and inspection strategies was identified, but its full text was not accessible through the attempted open landing page, and corresponding novelty risk remains. Unindexed specialized literature could also contain a related characterization.

## References

1. B. Kim, H. Cai, D. McKenzie, W. Yin, *Curvature-Aware Derivative-Free Optimization*, arXiv:2109.13391 (first version 2021-09-27; full-text Algorithm 1, §2.1 and proof §4.1 consulted at https://arxiv.org/html/2109.13391v2).
2. E. Bergou, E. Gorbunov, P. Richtárik, *Stochastic Three Points Method for Unconstrained Smooth Minimization*, arXiv:1902.03591 (Algorithm 1 and fixed-stepsize analysis; https://arxiv.org/html/1902.03591v3).
3. B. Kim, *Enhancing Local Derivative-Free Optimization with Curvature Information and Inspection Strategies*, 2023 doctoral dissertation, University of California eScholarship (https://escholarship.org/uc/item/8z24w59c); abstract and metadata accessible, full text not inspected.
