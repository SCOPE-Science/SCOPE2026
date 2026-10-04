# Critical square-root law for the Pareto mean-threshold infimum
## Finding
Let \(X_{a,\theta}\) have the Pareto type-I distribution with scale \(a>0\), shape \(\theta>1\), and tail
\[
\Pr\{X_{a,\theta}>x\}=\left(\frac{a}{x}\right)^\theta,\qquad x\ge a.
\]
Its expectation is \(\mathbb E X_{a,\theta}=\theta a/(\theta-1)\). For \(\kappa>1\), set
\[
g_\kappa(\theta)=\Pr\{X_{a,\theta}\le \kappa\,\mathbb E X_{a,\theta}\},\qquad
m(\kappa)=\min_{\theta>1}g_\kappa(\theta).
\]
The scale \(a\) cancels. Let \(W_{-1}\) denote the lower real branch of the Lambert \(W\)-function and put
\[
w_\kappa=W_{-1}\!\left(-\frac{1}{e\kappa}\right).
\]
Then the minimizer is unique and has the closed form
\[
\theta_\kappa=\frac{w_\kappa}{w_\kappa+1},
\qquad
m(\kappa)=1+\frac{1}{e\kappa w_\kappa}.
\]
Equivalently, with \(y_\kappa=-w_\kappa>1\),
\[
y_\kappa-\log y_\kappa=1+\log\kappa,
\qquad
\theta_\kappa=\frac{y_\kappa}{y_\kappa-1},
\qquad
m(\kappa)=1-e^{-y_\kappa}.
\]

Write \(q=\sqrt{2\log\kappa}\). As \(\kappa\downarrow1\),
\[
\theta_\kappa=\frac1q+\frac23+\frac{q}{12}-\frac{2q^2}{135}+O(q^3),
\]
while
\[
m(\kappa)=1-e^{-1}+e^{-1}q-\frac{e^{-1}}6q^2-\frac{5e^{-1}}{36}q^3+O(q^4).
\]
Hence the optimizer diverges on the exact scale \((2\log\kappa)^{-1/2}\), while the minimum has a square-root onset above the boundary value \(1-e^{-1}\). At the opposite endpoint, if \(L=\log\kappa\), then as \(\kappa\to\infty\),
\[
\theta_\kappa=1+\frac{1}{L+\log L+o(1)},
\qquad
1-m(\kappa)\sim\frac{1}{e\kappa L}.
\]

## Assumptions and scope
The statement concerns the ordinary Pareto type-I family with \(a>0\), \(\theta>1\), and fixed \(\kappa>1\). The condition \(\theta>1\) is exactly the finite-mean regime. No discreteness, numerical truncation, or asymptotic assumption is used in the exact optimizer formula. The expansions describe only the indicated endpoint limits. The boundary case \(\kappa=1\) has infimum \(1-e^{-1}\), approached only as \(\theta\to\infty\); the result quantifies how the unique interior minimizer for \(\kappa>1\) emerges from that boundary.

## Proof
Direct substitution of the mean gives
\[
g_\kappa(\theta)
=1-\left(\frac{\theta-1}{\kappa\theta}\right)^\theta.
\]
Set \(x=1-1/\theta\in(0,1)\), so that \(\theta=1/(1-x)\), and define
\[
h_\kappa(x)=\frac{\log(x/\kappa)}{x-1}.
\]
Then \(g_\kappa(\theta)=1-e^{-h_\kappa(x)}\), so minimizing \(g_\kappa\) is equivalent to minimizing \(h_\kappa\). Its derivative is
\[
h_\kappa'(x)=\frac{\varphi_\kappa(x)}{(x-1)^2},
\qquad
\varphi_\kappa(x)=1-\frac1x-\log\frac{x}{\kappa}.
\]
Moreover,
\[
\varphi_\kappa'(x)=\frac{1-x}{x^2}>0
\]
for \(0<x<1\), while \(\varphi_\kappa(x)\to-\infty\) as \(x\downarrow0\) and \(\varphi_\kappa(1^-)=\log\kappa>0\). Thus there is a unique critical point, it is the unique global minimum, and it agrees with the implicit optimizer established in Proposition 3.1 of Li--Hu--Zhou.

Put \(y=1/x>1\). The critical-point equation is
\[
y-\log y=1+\log\kappa,
\]
which is equivalent to
\[
(-y)e^{-y}=-\frac{1}{e\kappa}.
\]
The constraint \(y>1\) selects the lower real branch, so
\[
-y=W_{-1}\!\left(-\frac{1}{e\kappa}\right)=w_\kappa.
\]
Since \(\theta=1/(1-x)=y/(y-1)\), this proves the formula for \(\theta_\kappa\). At the critical point, the relation \(y-\log y=1+\log\kappa\) gives
\[
e^{-y}=\frac{1}{e\kappa y}=-\frac{1}{e\kappa w_\kappa},
\]
so \(m(\kappa)=1-e^{-y}=1+1/(e\kappa w_\kappa)\).

For the critical expansion, write \(y=1+s\), \(L=\log\kappa\), and \(q=\sqrt{2L}\). The defining equation becomes
\[
L=s-\log(1+s)
=\frac{s^2}{2}-\frac{s^3}{3}+\frac{s^4}{4}-\frac{s^5}{5}+\frac{s^6}{6}+O(s^7).
\]
Series reversion at the positive branch gives
\[
s=q+\frac{q^2}{3}+\frac{q^3}{36}-\frac{q^4}{270}+\frac{q^5}{4320}+O(q^6).
\]
Substitution into \(\theta=(1+s)/s\) and \(m=1-e^{-1-s}\) yields the displayed expansions. This is an ordinary convergent local inversion after the square-root change of variable; the finite numerical checks in the verification script are only stress tests.

For \(\kappa\to\infty\), the exact equation \(y-\log y=L+1\) implies by one iteration that
\[
y=L+\log L+1+o(1).
\]
Consequently \(\theta=1+1/(y-1)\) gives the stated shape asymptotic, and the exact identity \(1-m=1/(e\kappa y)\) gives the stated probability asymptotic.

## Verification
The accompanying `verify.py` uses only the Python standard library. It solves \(y-\log y=1+\log\kappa\) by bisection for several values of \(\kappa\), checks the stationary equation and the exact probability identities, compares the exact minimizer with neighboring shapes, and checks the predicted small-\(q\) remainder scaling. These computations are consistency checks; the proof above is analytic and does not rely on finite sampling.

## Relationship to prior work
Li, Hu, and Zhou study exactly the same Pareto mean-threshold functional. Their Proposition 3.1 proves that for \(\kappa>1\) the optimizer is unique and writes it as \(\theta_0(\kappa)=1/(1-x_0(\kappa))\), where \(x_0(\kappa)\) is the unique root of
\[
1-\frac1x-\log\frac{x}{\kappa}=0
\]
on \((0,1)\). Their paper also identifies the boundary value \(1-e^{-1}\) at \(\kappa=1\). The present finding solves that implicit root in the required real Lambert branch and then derives the nonanalytic critical law and the large-\(\kappa\) endpoint law. The inspected source text contains no Lambert-\(W\) formulation and no endpoint asymptotic for this optimizer. NIST DLMF §4.13 supplies the standard definition and branch structure of Lambert \(W\), but does not apply it to this Pareto optimization problem. Later papers in the same probability-at-the-mean program treat Gamma, negative-binomial, or other distribution families and do not imply this Pareto-specific closed form or its critical scaling.

## Limitations
The result does not strengthen the already-known existence and uniqueness statement for \(\kappa>1\); its contribution is the exact branch-resolved closed form and the endpoint scaling laws. The originality search cannot exclude an equivalent elementary transformation in poorly indexed literature under different Pareto or Lambert-\(W\) terminology. The expansion is specific to the Pareto type-I mean-threshold functional and should not be transferred to other parameterizations without re-derivation.

## References
1. C. Li, Z.-C. Hu, Q.-Q. Zhou, *A study on the Weibull and Pareto distributions motivated by Chvátal's theorem*, arXiv:2305.02114v1 (2023), especially Section 3, Proposition 3.1 and Lemma 3.2.
2. NIST Digital Library of Mathematical Functions, §4.13, *Lambert W-Function*, especially the real-branch description and branch-point/asymptotic expansions.
3. P. Sun, Z.-C. Hu, W. Sun, *The infimum values of two probability functions for the Gamma distribution*, Journal of Inequalities and Applications 2024:5 (2024), DOI 10.1186/s13660-024-03081-w.
