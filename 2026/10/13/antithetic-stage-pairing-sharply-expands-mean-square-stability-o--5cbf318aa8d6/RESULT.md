# Antithetic stage pairing sharply expands mean-square stability of randomized RK2

## Finding
For the scalar randomized two-stage Runge–Kutta method introduced in Bochacik–Goćwin–Morkisz–Przybyłowicz (2020), complementary uniform stage parameters on consecutive steps strictly reduce every nontrivial even-step mean-square error, without changing the one-step marginal law or the almost-sure Lyapunov exponent. The exact real-negative-axis mean-square stability interval expands from \(0<x<\beta\) to \(0<x<\alpha\), with \(\beta=1.59607163798332\ldots\) and \(\alpha=1.89655306233598\ldots\). This is a statement about a specified two-step coupling, not about globally optimal couplings or general nonlinear ODE accuracy.

## Assumptions and scope
Fix \(\lambda>0\), \(h>0\), \(x=\lambda h\), and deterministic \(y_0\ne0\). For the scalar equation \(y'=-\lambda y\), the explicit randomized two-stage scheme has a step multiplier
\[
p_x(t)=1-x+x^2t,\qquad 0\le t\le1.
\]
For each integer \(j\ge0\), draw \(U_j\sim\operatorname{Uniform}[0,1]\) independently across \(j\), and use stages \(T_{2j}=U_j\), \(T_{2j+1}=1-U_j\). Every individual stage has the original uniform distribution, but consecutive stages are dependent. Compare to the original scheme with independent uniform stages at every step. Define
\[
m=1-x+\frac{x^2}{2},\quad b=x^2,\quad
Q_{\mathrm A}=m^4-\frac{b^2m^2}{6}+\frac{b^4}{80},\quad
Q_{\mathrm I}=\left(m^2+\frac{b^2}{12}\right)^2.
\]
Mean-square stability means \(\mathbb E|y_n|^2\to0\) as \(n\to\infty\) for every deterministic initial scalar. All computations use exact arithmetic and independent pairs.

## Proof
Let \(V_j=U_j-1/2\), uniform on \([-1/2,1/2]\). The two consecutive multipliers equal \(m+bV_j\) and \(m-bV_j\), so their product is \(Z_j=m^2-b^2V_j^2\). The \(Z_j\) are independent. Since \(\mathbb E V_j^2=1/12\) and \(\mathbb E V_j^4=1/80\),
\[
\mathbb E Z_j^2=m^4-\frac{b^2m^2}{6}+\frac{b^4}{80}=Q_{\mathrm A}.
\]
The first multiplier in an independent fresh pair has square mean \(F=m^2+b^2/12\). Thus, for every integer \(j\ge0\),
\[
\mathbb E|y_{2j}|^2=Q_{\mathrm A}^{j}|y_0|^2,\qquad
\mathbb E|y_{2j+1}|^2=FQ_{\mathrm A}^{j}|y_0|^2.
\]
For iid uniform stages, the corresponding factors are \(F^{2j}\) and \(F^{2j+1}\). Their even-step factor is \(Q_{\mathrm I}=F^2\), and direct subtraction yields
\[
Q_{\mathrm I}-Q_{\mathrm A}=\frac{b^2}{180}(60m^2-b^2).
\]
For every \(x>0\), \(m=(x^2-2x+2)/2>0\) and \(b/m\le4\), because \(4m-b=(x-2)^2\ge0\). Hence \(60m^2-b^2\ge44m^2>0\). Therefore \(Q_{\mathrm A}<Q_{\mathrm I}\) for all \(x>0\), with strict improvement at every integer time \(n\ge2\).

Polynomial expansion gives
\[
Q_{\mathrm A}-1=\frac{x}{30}H(x),\quad
H(x)=x^7-10x^6+50x^5-140x^4+250x^3-300x^2+240x-120.
\]
An exact rational Sturm sequence for \(H\) has sign variations \(4\) at \(0\) and \(3\) at positive infinity, counting zero entries by omission. Thus \(H\) has exactly one positive real root, and the exact sign evaluations \(H(18965/10000)<0<H(18966/10000)\) enclose it. Because \(H(0)=-120\) and its leading coefficient is positive, \(Q_{\mathrm A}<1\) precisely for \(0<x<\alpha\), where \(\alpha\) is that root (approximately \(1.89655306233598\)). At \(x=\alpha\) the mean square is constant at even steps; above it the even-step mean square diverges.

For iid stages the one-step square factor is
\[
F=\frac{x^4-3x^3+6x^2-6x+3}{3}.
\]
The source paper establishes that \(F<1\) exactly on \(0<x<\beta\), where \(\beta\approx1.59607163798332\); equivalently, \(\beta\) is the unique positive root of \(x^3-3x^2+6x-6\). Since \(\alpha>\beta\), complementary pairing creates the strict stability-recovery window \(\beta<x<\alpha\). At the rational witness \(x=9/5\), direct substitution gives \(Q_{\mathrm A}=2551507/3906250<1<Q_{\mathrm I}=935089/390625\).

Finally, \(p_x(U)\) and \(p_x(1-U)\) share the same marginal law. Since \(\mathbb E|\log|p_x(U)||<\infty\) for every \(x>0\) (any zero is isolated and logarithmically integrable), the strong law applied to independent pairs yields
\[
\lim_{j\to\infty}\frac{1}{2j}\log\left|\frac{y_{2j}}{y_0}\right|
=\frac12\mathbb E\log|p_x(U)p_x(1-U)|
=\mathbb E\log|p_x(U)|\quad\text{almost surely}.
\]
This is exactly the original iid method's per-step Lyapunov exponent. The same full-step exponent follows because the odd-step multiplicative correction has a finite logarithmic tail and contributes \(o(j)\) almost surely. This is an equality of exponents, not of all path distributions.

## Verification
Run `python verify.py` with SymPy (see `requirements.txt`) to check the full algebraic factorization, the strict-improvement identity, the exact Sturm variation count, rational root brackets, and the rational witness. Every analytic identity above is independently reconstructible without numerical sampling. Symbolic checks do not replace the displayed proof of the sign or probabilistic limits.

## Relationship to prior work
Bochacik, Goćwin, Morkisz, and Przybyłowicz, *Randomized Runge–Kutta method – Stability and convergence under inexact information* (arXiv:2006.12131v1, first public 2020-06-22), Section 5.1 and Theorem 3, derive the original independent-stage mean-square interval. Their algorithm stipulates iid uniform stage parameters (equation (16)); their scalar stability multiplier is equation (66). The present result changes the dependence between consecutive stages while retaining every marginal and quantifies the corresponding sharp stability extension. Bochacik and Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes* (arXiv:2404.19059, first public 2024-04-29), studies different implicit-stage multipliers and again uses independent uniform stages; its stability theorems do not imply this explicit paired result. Classical antithetic-variance principles motivate the construction, but they do not by themselves supply the displayed global signed-multiplier comparison, unique degree-seven transition, or unchanged logarithmic exponent.

## Limitations
Only scalar autonomous linear decay, exact arithmetic, fixed step, and independent complementary pairs are covered. No claim concerns vector nonnormal dynamics, nonlinear equations, global strong convergence rates under non-iid stages, finite precision, or optimal coupling among all copulas. Self-review is not independent verification; equivalent specialized literature outside the checked sources may exist.

## References
1. T. Bochacik, M. Goćwin, P. M. Morkisz, and P. Przybyłowicz, *Randomized Runge–Kutta method – Stability and convergence under inexact information*, arXiv:2006.12131v1 (2020), Sections 2 and 5. https://arxiv.org/abs/2006.12131
2. T. Bochacik and P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, arXiv:2404.19059 (2024), Section 3. https://arxiv.org/abs/2404.19059
