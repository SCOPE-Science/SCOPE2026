# A sharp Markov-persistence risk reversal for strictly contractive two-component SGD

## Finding

Consider constant-step stochastic gradient descent (SGD) on two strictly convex scalar quadratic components, sampling their gradients along a stationary symmetric two-state Markov chain. There is an explicit problem on which both *negative correlation* and sufficiently strong *positive correlation* decrease the stationary squared distance to the full-objective minimizer relative to independent sampling, but weak positive correlation increases it. The exact transition is at a lag-one correlation of \(1/6\).

Specifically, for the problem and sampler defined below, the limiting mean-square error is
\[
R(\rho):=\lim_{t\to\infty}\mathbb E\bigl[(x_t-x_*)^2\bigr]
 =\frac{10}{9}+\frac{4(1-\rho^2)}{9(6-\rho)}
 =\frac{2(2\rho^2+5\rho-32)}{9(\rho-6)}.
\]
The independent-sampling value is \(R(0)=32/27\), and the exact difference is
\[
\boxed{R(\rho)-R(0)=\frac{2\rho(1-6\rho)}{27(6-\rho)}.}
\]
For every \(-1<\rho<1\), this difference is negative precisely for \(-1<\rho<0\) or \(1/6<\rho<1\), positive precisely for \(0<\rho<1/6\), and zero precisely at \(\rho=0\) or \(\rho=1/6\).

The risk is strictly increasing up to \(\rho_*=6-\sqrt{35}\) and strictly decreasing thereafter; its unique maximum is
\[
R(\rho_*)=\frac{58-8\sqrt{35}}9.
\]
These strict reversals persist under sufficiently small perturbations of both quadratic component coefficients and the step size, as long as the component update maps remain strict contractions. The claim is an exact characterization **of this example**, not a universal criterion for all Markovian SGD problems.

## Assumptions and scope

The component objectives and their equally weighted average are
\[
f_1(x)=\frac34 x^2-x,\qquad f_2(x)=\frac38 x^2+x,
\qquad F(x)=\tfrac12(f_1(x)+f_2(x))=\frac9{16}x^2.
\]
Their curvatures are \(3/2\) and \(3/4\), and the unique minimizer of \(F\) is \(x_*=0\). Take constant gradient step \(\eta=1\). The component-gradient updates are
\[
x_{t+1}=x_t-\nabla f_{I_t}(x_t)
=\begin{cases}-x_t/2+1,&I_t=1,\\x_t/4-1,&I_t=2.\end{cases}
\]
Every individual update is a strict contraction, with Lipschitz factors \(1/2\) and \(1/4\).

The sampling chain \((I_t)\) is stationary, with transition matrix
\[
P_\rho=\frac12\begin{pmatrix}1+\rho&1-\rho\\1-\rho&1+\rho\end{pmatrix},\qquad -1<\rho<1.
\]
It is irreducible and aperiodic throughout this open interval. Its invariant law is exactly uniform, irrespective of \(\rho\), and its lag-one signed-state autocorrelation is \(\rho\). In particular \(\rho=0\) means independent uniform component draws. The chain is independent of the initial iterate. The initial iterate may be any deterministic real number or an independent square-integrable random variable. All comparisons use the same single gradient evaluation per step and the *last iterate*, not Polyak averaging.

## Proof

**Moment recursion and its unique limit.** Write \(a=(-1/2,1/4)\), \(c=(1,-1)\), and \(\pi=(1/2,1/2)^\mathsf T\). Define joint first- and second-moment columns
\[
u_i(t)=\mathbb E[x_t\mathbf 1_{\{I_t=i\}}],\qquad
v_i(t)=\mathbb E[x_t^2\mathbf 1_{\{I_t=i\}}].
\]
Stationarity of the sampler gives \(\mathbb P(I_t=i)=\pi_i\). Conditioning on the gradient state used in the update, and then transitioning to \(I_{t+1}\), gives exactly
\[
\begin{aligned}
u(t+1)&=P_\rho^\mathsf T\bigl(\operatorname{diag}(a)u(t)+\operatorname{diag}(c)\pi\bigr),\\
v(t+1)&=P_\rho^\mathsf T\bigl(\operatorname{diag}(a^2)v(t)+\operatorname{diag}(2ac)u(t)+\pi\bigr).
\end{aligned}
\]
Here \(a^2\) and \(ac\) denote componentwise products. Both affine recursions have unique globally attracting fixed points. Indeed, \(\|P_\rho^\mathsf T\operatorname{diag}(a)\|_1\le1/2\) and \(\|P_\rho^\mathsf T\operatorname{diag}(a^2)\|_1\le1/4\); first moments contract directly and second moments contract after the vanishing first-moment forcing is accounted for. This also proves existence of the displayed \(t\to\infty\) limit. The underlying iterated random affine maps contract synchronously, so an invariant joint law exists and is unique.

Solving these two nonsingular \(2\times2\) linear systems yields
\[
u_1=\frac\rho3,\qquad u_2=-\frac{2\rho}3,
\]
\[
v_1=\frac{2(10\rho^2+\rho-16)}{9(\rho-6)},\qquad
v_2=-\frac{8(2\rho^2-\rho+4)}{9(\rho-6)}.
\]
Thus the stationary iterate mean is \(\mathbb E x=-\rho/3\), which is zero only for independent sampling, while \(\mathbb E x^2=v_1+v_2\) simplifies to the announced \(R(\rho)\).

**Exact ordering and critical point.** Subtracting \(R(0)=32/27\) and factoring gives
\[
R(\rho)-R(0)=\frac{2\rho(1-6\rho)}{27(6-\rho)}.
\]
The denominator is strictly positive on \((-1,1)\), so the sign classification follows without numerical approximation. Differentiation gives
\[
R'(\rho)=\frac{4(\rho^2-12\rho+1)}{9(\rho-6)^2}.
\]
The only zero of the numerator in \((-1,1)\) is \(6-\sqrt{35}\), and the derivative changes sign from positive to negative there. Substitution gives the asserted unique maximum. The endpoint values \(\lim_{\rho\to\pm1}R(\rho)=10/9\) are **limits only**: neither endpoint is admitted as an irreducible aperiodic chain.

**Robustness.** The strict risks at \(\rho=-1/2\), \(\rho=1/12\), and \(\rho=1/2\) are respectively
\[
R(-1/2)=\frac{136}{117}<\frac{32}{27},\quad
R(1/12)=\frac{2273}{1917}>\frac{32}{27},\quad
R(1/2)=\frac{116}{99}<\frac{32}{27}.
\]
The stationary moment recursions for nearby two-quadratic problems are finite-dimensional linear systems. Their coefficients and unique solutions depend continuously on component quadratic coefficients and step size wherever both component maps are strict contractions. Therefore the three strict comparisons persist simultaneously in an open neighborhood of the displayed problem. No claim that the *exact numerical threshold* persists unchanged under perturbation is made.

## Verification

The accompanying standalone \(\texttt{verify.py}\) uses symbolic rational algebra to reconstruct both stationary moment fixed points, the resulting risk, its factored independent-sampling comparison and derivative. It separately enumerates exact finite-length Markov/sample paths, comparing them against moment recursions for seven rational correlations and the first seven steps. The verifier reports \(154\) independent rational checks in addition to symbolic identities. Finite checks are corroboration; the proof of the continuum sign classification is the exact factorization above.

Reproduce using Python 3 with SymPy installed: \(\texttt{python verify.py}\). All computation is exact rational or symbolic, with no Monte Carlo error.

## Relationship to prior work

Even's *Stochastic Gradient Descent under Markovian Sampling Schemes* (2023, arXiv:2302.14428) formulates SGD with Markov-indexed component gradients and establishes general finite-time convergence guarantees and sampling complexity. Its relevant MC-SGD analysis gives bounds rather than the exact long-run two-curvature risk ordering proved here. Beznosikov and coauthors (2023, arXiv:2305.15938) study first-order optimization under Markovian noise with complexity bounds, including two-state constructions, but not this last-iterate stationary variance frontier. Kühn and Rosenow (first posted 2023, arXiv:2306.05300; subsequently revised) analyze anti-correlated *epoch-based, without-replacement* gradient noise and stationary weight fluctuations under a different noise model; their results do not yield the exact fixed two-state Markov-indexed, state-dependent-affine risk comparison above.

General linear-system moment techniques for Markov-jump autoregressions are classical. The claimed contribution is the explicit robust numerical-optimization ordering reversal and its sharp correlation threshold **for the stated example**, not invention of the moment method or of Markovian SGD. A broader existing theorem could subsume this example and remains a priority risk.

## Limitations

This is a two-component scalar quadratic counterexample with fixed step size and last-iterate squared error, not a general optimizer design guarantee, not a minimax claim over Markov kernels, and not a result about iterate averages. The stationary iterate mean is nonzero for \(\rho\ne0\), so reduced mean-square risk can be accompanied by bias. Correlation endpoints \(\rho=\pm1\) are excluded. Real arithmetic and stationary sampling are assumed; any finite-horizon benefit may differ. Publication priority beyond the inspected literature remains uncertain; no independent scientific audit has occurred.

## References

1. Mathieu Even, *Stochastic Gradient Descent under Markovian Sampling Schemes*, first posted 28 February 2023, arXiv:2302.14428. https://arxiv.org/abs/2302.14428
2. A. Beznosikov, S. Samsonov, M. Sheshukova, A. Gasnikov, A. Naumov, and E. Moulines, *First Order Methods with Markovian Noise: from Acceleration to Variational Inequalities*, first posted 25 May 2023, arXiv:2305.15938. https://arxiv.org/abs/2305.15938
3. Marcel Kühn and Bernd Rosenow, *Anti-Correlated Noise in Epoch-Based Stochastic Gradient Descent: Implications for Weight Variances in Flat Directions*, first posted 8 June 2023, arXiv:2306.05300. https://arxiv.org/abs/2306.05300
