# A single global existence threshold and finite-time terminal blow-up for a trigonometric Abel cycle

## Finding
Consider the forcing-periodic Abel family
\[
 x'=\sin t\,x^2+(a+\cos 2t)x^3,\qquad -1<a<0.
\]
There is a unique threshold \(a_*\in(-1,0)\) for which a strictly positive \(2\pi\)-periodic solution exists **if and only if** \(a\in(a_*,0)\). It is then unique and has Floquet multiplier strictly greater than one. Its profile strictly decreases pointwise with \(a\), and
\[
 \lim_{a\uparrow0}\frac{x_a(0)}{2\sqrt{-a}}=1.
\]
As \(a\downarrow a_*\), the periodic initial conditions increase to a finite strictly positive number \(r_*\). The solution at \(a_*\) started from \(r_*\) blows up to \(+\infty\) before or at one forcing period, and the maxima of the periodic profiles diverge. Thus the positive cycle terminates by a finite-time singularity, not a finite-amplitude fold.

## Assumptions and scope
The independent variable is real time \(t\), with forcing period \(T=2\pi\). Solutions are classical maximal solutions and strictly positive on their intervals of existence. The assertion concerns only the open parameter interval \(-1<a<0\), not arbitrary parameters, initial conditions, negative periodic solutions, or arbitrary Abel coefficients. The constant \(a_*\) is defined by the rigorous parameter classification proved below, not by a certified numerical approximation. The same model from the source literature supplies a sharp uniqueness-and-instability criterion; the global parameter continuation, nonexistence near \(-1\), and terminal mechanism are established here.

## Proof
**1. Upper bound and orientation.** Write \(A_a(t)=a+\cos2t\), \(B(t)=\sin t\). For \(-1<a<0\), the coefficient \(A_a\) has two simple zeros in \((0,\pi)\), with positive–negative–positive signs, and the required half-period symmetries hold. In the coordinate \(z=1-\cos t\), the quotient \(\widehat K(z)=A_a(t(z))/B(t(z))\) satisfies
\[
 \widehat K''(z)=\frac{a+3+2a(1-z)^2}{[z(2-z)]^{5/2}}>0\quad(0<z<2),
\]
because its numerator is at least \(3+3a>0\). The half-period convexity theorem (Theorem 1 and Proposition 7 of Bravo Trinidad–Tian–Zhao [1]) therefore gives at most one positive periodic solution, which, if present, has scalar Poincaré multiplier \(\mu_a>1\).

**2. The branch is born at zero.** Let \(P_a(r)\) be the time-\(T\) map where defined and \(D_a(r)=P_a(r)-r\). The source's explicit return expansion [1, Lemma 2] is
\[
 D_a(r)=2\pi ar^3+2\pi ar^4+(6\pi^2a^2+3\pi a+\pi/2)r^5+O(r^6),
\]
uniformly for bounded \(a\) near zero and small \(r\). Putting \(a=-\epsilon\) and \(r=c\sqrt\epsilon\) gives
\[
 \epsilon^{-5/2}D_{-\epsilon}(c\sqrt\epsilon)
 \longrightarrow \pi c^3(c^2/2-2).
\]
For each fixed \(0<c_-<2<c_+\), this displacement has opposite signs at \(c_-\sqrt\epsilon\) and \(c_+\sqrt\epsilon\) when \(\epsilon\) is small. The intermediate value theorem and Step 1 furnish a unique positive periodic solution and squeeze its initial condition to \(r_{-\epsilon}/\sqrt\epsilon\to2\).

**3. Pointwise strict branch monotonicity.** Along any positive periodic solution, let \(q(t)=2\sin t\,x(t)+3(a+\cos2t)x(t)^2\), so \(\mu_a=\exp(\int_0^Tq)>1\). The derivative \(w(t)=\partial_a x_a(t)\) exists by the implicit function theorem, is periodic, and solves \(w'=qw+x_a^3\). For any phase \(t\), solving this periodic inhomogeneous linear equation gives
\[
 w(t)=-\frac{\displaystyle\int_t^{t+T}\exp\!\left(-\int_t^s q(v)\,dv\right)x_a(s)^3\,ds}
 {1-\mu_a^{-1}}<0.
\]
In particular, every connected branch of positive periodic solutions strictly decreases pointwise as \(a\) increases.

**4. No cycle for parameters sufficiently close to \(-1\).** Write \(a=-1+\delta\). For a positive solution,
\[
 x'=x\bigl[(x\sin t)-2(x\sin t)^2\bigr]+\delta x^3\le x/8+\delta x^3.
\]
On \([\pi/4,3\pi/4]\), when \(0\le\delta\le1/2\), one also has \(x'\le x^2-x^3/2\). Above \(x=4\) this implies \(x'\le-x^3/4\). Since the interval has length \(\pi/2\), every solution that survives it must satisfy \(x(3\pi/4)\le4\): otherwise, while above four, \((x^{-2})'\ge1/2\) would force its value past \(1/16\) before the interval ends, a contradiction; and a solution cannot cross upwards through four.

For \(w=x^{-2}\), the first displayed inequality gives \(w'\ge-w/4-2\delta\). Comparing from \(3\pi/4\) to \(T\), every global positive solution satisfies
\[
 x(T)^{-2}\ge(1/16+8\delta)e^{-5\pi/16}-8\delta.
\]
For \(0\le\delta\le10^{-3}\), the right side exceeds \(1/64\). Thus **every positive periodic solution** in this range has initial condition \(x(0)=x(T)\le8\).

Conversely, for \(0\le\delta\le10^{-4}\) and \(0<r\le8\), the same comparison starting from zero yields
\[
 x(t)^{-2}\ge(r^{-2}+8\delta)e^{-t/4}-8\delta>0
 \quad(0\le t\le T)
\]
whenever the trajectory exists. This lower bound rules out finite-time blow-up, so the return map is well defined and continuous in \((\delta,r)\) on this compact parameter–initial-data rectangle, including at the upper edge \(r=8\).

At \(\delta=0\), the cubic coefficient is \(-2\sin^2t\). A strictly positive periodic trajectory would satisfy
\[
 0=\int_0^T (1/x)'\,dt=-\int_0^T\sin t\,dt+2\int_0^T\sin^2t\,x(t)\,dt>0,
\]
a contradiction. Therefore \(D_{-1}(r)\) has no zero for \(r>0\) and is negative throughout \((0,8]\), as its leading Taylor term near zero is \(-2\pi r^3\). By uniform dependence and the uniform small-\(r\) expansion \(D_{-1+\delta}(r)=2\pi(-1+\delta)r^3+O(r^4)\), it stays strictly negative for all \(0<r\le8\) when \(\delta>0\) is sufficiently small. The universal periodic-initial-data bound just proved excludes positive cycles there. Hence there is an open interval adjacent to \(-1\) with no positive cycles.

**5. No gaps inside the existence interval.** Let \(E\subset(-1,0)\) be the set of parameters admitting a positive periodic solution. Step 1 and hyperbolicity make \(E\) open, with a unique smoothly varying positive solution on each component. Step 2 shows it contains an interval immediately below zero, while Step 4 shows it omits an interval immediately above \(-1\). Consider any component \((\ell,u)\subset E\). If \(u<0\), Step 3 bounds every entire periodic profile on a right-hand subinterval by the profile at one smaller parameter. Moreover, uniform negativity of the small-amplitude return map for parameters in a compact negative interval prevents the positive initial conditions from converging to zero. Passing to the limit as \(a\uparrow u\) thus gives a strictly positive periodic solution at \(u\), and its hyperbolicity extends the branch to parameters above \(u\), contradiction. Therefore every component of \(E\) has right endpoint zero. Disjoint open interval components cannot share that endpoint, so \(E=(a_*,0)\) for one \(-1<a_*<0\).

**6. Singular lower endpoint.** Monotonicity shows that \(r_a=x_a(0)\) increases as \(a\downarrow a_*\). Since \(a_*>-1\), choose \(\kappa,t_0>0\) so \(a+\cos2t\ge\kappa\) and \(\sin t\ge0\) whenever \(a\in[a_*,0)\), \(t\in[0,t_0]\). Then \(x'\ge\kappa x^3\) and existence to \(t_0\) implies \(r_a\le(2\kappa t_0)^{-1/2}\). Uniform negative small-\(r\) displacement near the fixed parameter \(a_*<0\) also bounds \(r_a\) away from zero. Hence \(r_a\to r_*\in(0,\infty)\).

Were the maximal solution at \((a_*,r_*)\) defined throughout \([0,T]\), continuous dependence would yield \(P_{a_*}(r_*)=r_*\). Step 1 would make this orbit hyperbolic and extend it to \(a<a_*\), contradicting Step 5. Therefore the limiting positive solution loses existence at a finite \(\tau\in(0,T]\). A polynomial scalar ODE with bounded coefficients cannot have a finite terminal time with bounded amplitude; positivity prevents an exit at zero. Thus \(x(t)\to+\infty\) as \(t\uparrow\tau\). If the maxima of the periodic profiles failed to diverge as \(a\downarrow a_*\), an equibounded subsequence would yield the forbidden periodic solution at \(a_*\). This finishes all assertions.

## Verification
The proof's global conclusions are analytic, not inferred from numerical enumeration. A standalone finite checker (`abel_threshold_checker.py`) integrates the scalar equation together with its variational equation and probes the predicted signs, example positive roots and multipliers. On the recorded parameter selection it returns `CHECKS_PASS`; no assertion of exhaustive finite checks, rigorous interval bounds, or computer certification is made.

## Relationship to prior work
Bravo Trinidad, Tian and Zhao [1] establish the general half-period-convexity upper bound and repelling multiplier for this one-parameter subclass; they obtain a small-cycle existence argument near the critical parameter. The present result uses their theorem and Lyapunov coefficients but adds the **single global existence threshold**, strict profile monotonicity, a nonexistence interval adjacent to the opposite coefficient boundary, and the singular finite-time terminal mechanism. The Abel stability paper [2] and Chebyshev criterion [3] motivate care over stronger abstract statements: neither source as inspected directly states the present one-parameter global threshold or endpoint blow-up classification. Priority is not conclusively established by finite searching.

## Limitations
The theorem gives no closed form or validated numerical enclosure for \(a_*\), does not cover \(a\notin(-1,0)\), negative or complex-valued solutions, or the detailed blow-up exponent at \(\tau\). It imports the published half-period convexity theorem and return-map expansion rather than reproving that theorem. Numerical tests supply examples only. Equivalence under more general one-parameter Abel-continuation terminology remains a literature-priority risk. Independent review has not been performed.

## References
[1] J. L. Bravo Trinidad, R. Tian, Y. Zhao, *Uniqueness of Limit Cycles for Abel Equations and Planar Systems*, arXiv:2610.19340v1 (first public 2026-10-14), https://arxiv.org/html/2610.19340v1; see Theorem 1, Proposition 7, Lemma 2 and Section 3.

[2] *Stability of singular limit cycles for Abel equations revisited*, arXiv:2302.13642, https://arxiv.org/abs/2302.13642.

[3] *A Chebyshev criterion for at most two non-zero limit cycles in Abel equations*, arXiv:2506.14091, https://arxiv.org/abs/2506.14091.
